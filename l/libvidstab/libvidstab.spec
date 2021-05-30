Name: libvidstab
Version: 1.1.0
Release: alt2.1

Summary: Video stabilization library
License: GPL
Group: Video
Url: http://public.hronopik.de/vid.stab/

Source: %name-%version.tar.gz

BuildRequires: cmake gcc-c++ libgomp-devel

%description
Vidstab is a video stabilization library which can be plugged-in with Ffmpeg and Transcode.

%package devel
Summary: Development files for Vidstab framework
License: GPL
Group: Development/C
Requires: libgomp-devel
%description devel
Development files for Vidstab framework.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_libdir/libvidstab.so.*

%files devel
%_includedir/vid.stab/
%_libdir/libvidstab.so
%_pkgconfigdir/vidstab.pc

%changelog
* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 1.1.0-alt2.1
- NMU: spec: adapted to new cmake macros.

* Wed Nov 21 2018 Oleg Solovyov <mcpain@altlinux.org> 1.1.0-alt2
- rebuilt with libgomp8

* Thu Apr 05 2018 Oleg Solovyov <mcpain@altlinux.org> 1.1.0-alt1%ubt
- initial build for ALT

