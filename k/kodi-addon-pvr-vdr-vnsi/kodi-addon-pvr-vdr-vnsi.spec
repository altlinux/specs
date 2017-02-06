Name: kodi-addon-pvr-vdr-vnsi
Version: 17.0
Release: alt1

Summary: PVR VDR addon for Kodi
License: GPL
Group: Video

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel libkodiplatform-devel >= 17.0
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
%_libdir/kodi/addons/pvr.vdr.vnsi
%_datadir/kodi/addons/pvr.vdr.vnsi

%changelog
* Mon Feb 06 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.0-alt1
- updated for Krypton

* Wed Feb 24 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 16.0-alt1
- updated for Jarvis

* Wed Jul 29 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 15.0-alt1
- initial
