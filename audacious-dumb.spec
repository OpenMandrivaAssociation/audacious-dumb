%define name audacious-dumb
%define version 0.56
%define release %mkrel 2

Summary: MOD player plugin for Audacious based on DUMB
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.netswarm.net/misc/%name-%version.tar.gz
License: GPL
Group: Sound
Url: http://www.netswarm.net/
BuildRequires: dumb-devel
BuildRequires: libaudacious-devel >= 5:1.4.0-0.beta1.3mdv2008.1
Requires: audacious >= 5:1.4.0-0.beta1.3mdv2008.1
Provides: beep-media-player-dumb
Obsoletes: beep-media-player-dumb

%description
This is a plugin for Audacious that can play IT/XM/S3M/MOD files.

%prep
%setup -q
%build
%make CC="gcc -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_libdir/audacious/Input
cp *.so %buildroot%_libdir/audacious/Input/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README*
%_libdir/audacious/Input/*.so


