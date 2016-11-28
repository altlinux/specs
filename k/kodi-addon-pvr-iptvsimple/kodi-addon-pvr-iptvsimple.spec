Name: kodi-addon-pvr-iptvsimple
Version: 16.0
Release: alt1

Summary: IPTVSimple addon for Kodi
License: GPL
Group: Video

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel libkodiplatform-devel zlib-devel
%ifarch %ix86 x86_64
BuildRequires:libGL-devel
%endif
%ifarch armh
BuildRequires: libGLES-devel
%endif

%description
%summary

%prep
%setup

%build
cmake . -DCMAKE_INSTALL_PREFIX=%prefix -DCMAKE_INSTALL_LIBDIR=%_libdir/kodi
%make_build

%install
%makeinstall_std

%files
%_libdir/kodi/addons/pvr.iptvsimple
%_datadir/kodi/addons/pvr.iptvsimple

%changelog
* Mon Nov 28 2016 Anton Farygin <rider@altlinux.ru> 16.0-alt1
- initial build for ALT


