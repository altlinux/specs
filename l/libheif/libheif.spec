Name: libheif
Version: 1.17.5
Release: alt1
Summary: HEIF file format decoder and encoder
License: LGPLv3
Group: System/Libraries
Url: https://github.com/strukturag/libheif
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: cmake gcc-c++ libde265-devel libjpeg-devel libpng-devel libx265-devel libgdk-pixbuf-devel libaom-devel
#BuildRequires: libdav1d-devel
#%ifnarch %e2k
#BuildRequires: librav1e-devel
#%endif

%description
HEIF is a new image file format employing HEVC (h.265) image coding for the
best compression ratios currently possible.

%package devel
Group: Development/C
Summary:  Development libraries for %name

%description devel
Development libraries for %name

%prep
%setup -q
%patch -p1
%ifarch %e2k
sed -i 's/-Werror/-Wno-error/g' configure.ac CMakeLists.txt
%endif

%build
%cmake

%cmake_build

%install
%cmake_install

%files
%_bindir/*
%_libdir/%name.so.*
%_libdir/%name
%_libdir/gdk-pixbuf-2.0/2.10.0/loaders/*.so*
%_datadir/thumbnailers/heif.thumbnailer
%_man1dir/*.1*

%files devel
%_includedir/%name
%_libdir/%name.so
%_libdir/cmake/%name
%_pkgconfigdir/%name.pc

%changelog
* Mon Nov 27 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.17.5-alt1
- 1.17.5

* Thu Nov 09 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.17.3-alt1
- 1.17.3

* Thu Oct 19 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.17.1-alt1
- 1.17.1

* Thu Aug 31 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.15.2-alt1.1
- Fixed build for Elbrus

* Mon Mar 06 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.15.1-alt1
- 1.15.1

* Thu Feb 09 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.14.2-alt1
- 1.14.2

* Fri Nov 18 2022 Valery Inozemtsev <shrek@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Tue Apr 27 2021 Anton Farygin <rider@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Thu Sep 24 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Mon Aug 31 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Mon Jun 08 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Wed Feb 12 2020 Anton Farygin <rider@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Fri Dec 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Thu Nov 14 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Wed Mar 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Fri Aug 31 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt1.S1
- 1.3.2

* Tue Jun 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1.S1
- rebuild with libva 2.1.0

* Wed Jun 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- initial release
