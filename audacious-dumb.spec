%define name audacious-dumb
%define version 0.80
%define release %mkrel 1
%define audepoch 5
%define audver 3.1

Summary: MOD player plugin for Audacious based on DUMB
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.netswarm.net/misc/%name-%version.tar.gz
License: GPLv2+
Group: Sound
Url: http://www.netswarm.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: dumb-devel
BuildRequires: libaudacious-devel >= %audepoch:%audver
Requires: audacious >= %audepoch:%audver
Provides: beep-media-player-dumb
Obsoletes: beep-media-player-dumb

%description
This is a plugin for Audacious that can play IT/XM/S3M/MOD files.

%prep
%setup -q
%build
%make CC="gcc -fPIC" AUDMINVER=%audver

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


