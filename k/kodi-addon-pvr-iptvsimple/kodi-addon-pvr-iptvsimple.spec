Name: kodi-addon-pvr-iptvsimple
Version: 17.0
Release: alt2

Summary: IPTVSimple addon for Kodi
License: GPL
Group: Video
Url: https://github.com/kodi-pvr/pvr.iptvsimple/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
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
* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 17.0-alt2
- NMU: added URL

* Mon Feb 06 2017 Anton Farygin <rider@altlinux.ru> 17.0-alt1%ubt
- new version

* Mon Nov 28 2016 Anton Farygin <rider@altlinux.ru> 16.0-alt1
- initial build for ALT
