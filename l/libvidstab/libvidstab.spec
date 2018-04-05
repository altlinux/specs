Name: libvidstab
Version: 1.1.0
Release: alt1%ubt

Summary: Video stabilization library
License: GPL
Group: Video
Url: http://public.hronopik.de/vid.stab/

Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-ubt
BuildRequires: cmake gcc-c++ libgomp-devel

%description
Vidstab is a video stabilization library which can be plugged-in with Ffmpeg and Transcode.

%package devel
Summary: Development files for Vidstab framework
License: GPL
Group: Development/C
%description devel
Development files for Vidstab framework.

%prep
%setup

%build
%cmake
pushd BUILD
%make_build
popd

%install
pushd BUILD
%make DESTDIR=%buildroot install
popd

%files
%_libdir/libvidstab.so.*

%files devel
%_includedir/vid.stab/
%_libdir/libvidstab.so
%_pkgconfigdir/vidstab.pc

%changelog
* Thu Apr 05 2018 Oleg Solovyov <mcpain@altlinux.org> 1.1.0-alt1%ubt
- initial build for ALT

