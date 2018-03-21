Name: kodi-addon-inputstream-adaptive
Version: 17.5
Release: alt1.1

Summary: Adaptive stream addon for Kodi
License: GPL
Group: Video
Url: https://github.com/peak3d/inputstream.adaptive/

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel libkodiplatform-devel >= 17.0
BuildRequires: libexpat-devel

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
%_libdir/kodi/addons/*
%_datadir/kodi/addons/*

%changelog
* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 17.5-alt1.1
- NMU: added URL

* Sat Nov 11 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.5-alt1
- 2.0.19

* Mon Feb 06 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.0-alt1
- initial
