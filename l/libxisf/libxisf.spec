%global libname libXISF

Name:           libxisf
Version:        0.2.13
Release:        alt1
Summary:        Library to load and write XISF format
License:        GPL-3.0-or-later
Packager:       Ilya Mashkin <oddity@altlinux.ru>
URL:            https://gitea.nouspiro.space/nou/libXISF
Source0:        %{url}/archive/%name-%version.tar.gz
Group: System/Libraries
BuildRequires:  cmake >= 3.14
BuildRequires:  gcc ctest
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(zlib)
ExcludeArch:    i586

%description
LibXISF is C++ library to load and save images in XISF format that
is native format PixInsight astronomical image processing program.
It implements XISF 1.0 specifications.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Group: System/Libraries

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -n libxisf

# remove bundled libraries
for d in "lz4" "pugixml" "zlib"
do
  rm -rf $d
done


%build
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DUSE_BUNDLED_LIBS=OFF
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%doc README.md LICENSE
%{_libdir}/%{libname}.so.0
%{_libdir}/%{libname}.so.%{version}


%files devel
%{_includedir}/%{libname}_global.h
%{_includedir}/libxisf.h
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/libxisf.pc


%changelog
* Sat Dec 06 2025 Ilya Mashkin <oddity@altlinux.ru> 0.2.13-alt1
- Build for Sisyphus

* Wed Feb 12 2025 Mattia Verga <mattia.verga@proton.me> - 0.2.13-2
- Disable i686 builds

* Wed Feb 12 2025 Mattia Verga <mattia.verga@proton.me> - 0.2.13-1
- Update to 0.2.13

* Mon Jun 03 2024 Mattia Verga <mattia.verga@proton.me> - 0.2.12-1
- Update to 0.2.12

* Fri Aug 18 2023 Mattia Verga <mattia.verga@proton.me> - 0.2.9-1
- Update to 0.2.9 (fedora#2231736)
- Enable zstd support

* Sat Jun 17 2023 Mattia Verga <mattia.verga@proton.me> - 0.2.8-1
- Update to 0.2.8

* Fri Jun 02 2023 Mattia Verga <mattia.verga@proton.me> - 0.2.6-1
- Update to 0.2.6 (fedora#2211840)

* Mon May 29 2023 Adam Williamson <awilliam@redhat.com> - 0.2.5-2
- Backport patches from upstream to fix pkgconfig file

* Sun May 28 2023 Mattia Verga <mattia.verga@proton.me> - 0.2.5-1
- Update to 0.2.5 (fedora#2208667)
- Added pkgconfig file

* Sat Apr 15 2023 Mattia Verga <mattia.verga@proton.me> - 0.2.3-1
- Update to 0.2.3 (fedora#2186985)

* Mon Mar 20 2023 Mattia Verga <mattia.verga@proton.me> - 0.2.1-1
- Initial import (fedora#2177855)
