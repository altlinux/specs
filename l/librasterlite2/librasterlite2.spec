%global pre beta1

# This package requires libspatialite 4.2 and solves the tasks librasterlite
# and gaiagraphics solved in the past. It is not a drop-in replacement for either.
Name:          librasterlite2
Version:       1.1.0
Release:       alt1.1
Summary:       Stores and retrieves huge raster coverages using a SpatiaLite DBMS
License:       MPLv1.1 or GPLv2+ or LGPLv2+
Group: System/Libraries
URL:           https://www.gaia-gis.it/fossil/librasterlite2
Source0:       http://www.gaia-gis.it/gaia-sins/%{name}-sources/%{name}-%{version}%{?pre:-%pre}.tar.gz

BuildRequires: gcc
BuildRequires: libcairo-devel
BuildRequires: libCharLS-devel
BuildRequires: libgif-devel
BuildRequires: libcurl-devel
BuildRequires: libgeotiff-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libspatialite-devel
BuildRequires: libwebp-devel
BuildRequires: libxml2-devel
BuildRequires: libzstd-devel
BuildRequires: liblz4-devel
BuildRequires: libminizip-devel
BuildRequires: libopenjpeg2.0-devel
BuildRequires: libproj-devel
BuildRequires: libsqlite3-devel libpixman-devel
#BuildRequires: libxz-devel
BuildRequires: zlib-devel liblzma-devel xz
BuildRequires: make

%description
librasterlite2 is a library that stores and retrieves huge raster coverages
using a SpatiaLite DBMS.


%package devel
Summary:  Development libraries and headers for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Group: System/Libraries

%description devel
This package contains libraries and header files for
developing applications that use %{name}.


%package tools
Summary:  Tools for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
License:  GPLv3+
Group: System/Libraries

%description tools
The %{name}-tools package contains l2tool and rwmslite.
rl2tool is a CLI tool to create and manage rasterlite2 coverages.
wmslite is a simple WMS server (Web Map Service) based on librasterlite2.


%prep
%setup -n %{name}-%{version}%{?pre:-%pre}


%build
%configure --disable-static
%make_build


%install
#make_install
%makeinstall_std

# Delete undesired libtool archives
rm -f %{buildroot}/%{_libdir}/%{name}.la
rm -f %{buildroot}/%{_libdir}/mod_rasterlite2.la

# Delete soname symlink for the sqlite extension
#rm -f %{buildroot}/%{_libdir}/mod_rasterlite2.so.*




%files
%doc AUTHORS
%{_libdir}/%{name}.so.*
# The symlink must be present to allow loading the extension
# https://groups.google.com/forum/#!topic/spatialite-users/zkGP-gPByXk
%{_libdir}/mod_rasterlite2.so*

%files devel
%doc examples/*.c
%{_includedir}/rasterlite2
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/rasterlite2.pc

%files tools
%{_bindir}/rl2sniff
%{_bindir}/rl2tool
%{_bindir}/wmslite


%changelog
* Thu Feb 23 2023 Ivan A. Melnikov <iv@altlinux.org> 1.1.0-alt1.1
- NMU: drop libgaiagraphics from BR to fix FTBS

* Thu Jan 06 2022 Ilya Mashkin <oddity@altlinux.ru> 1.1.0-alt1
- Build for Sisyphus

* Sun Mar 07 2021 Sandro Mani <manisandro@gmail.com> - 1.1.0-0.4.beta1
- Rebuild (proj)

* Wed Feb 10 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-0.3.beta1
- Rebuild for new minizip

* Fri Nov 13 2020 Sandro Mani <manisandro@gmail.com> - 1.1.0-0.1.beta1
- Update to 1.1.0-beta1

* Tue Apr 14 2020 Sandro Mani <manisandro@gmail.com> - 1.1.0-0.1.beta0
- Update to 1.1.0-beta0

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 1.0.0-3.rc0.10
- Rebuild (giflib)

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 1.0.0-3.rc0.5
- Rebuild (libwebp)

* Mon Dec 28 2015 Volker Froehlich <volker27@gmx.at> - 1.0.0-3.rc0.3
- rebuilt

* Mon Dec 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-3.rc0.2
- Rebuilt for libwebp soname bump

* Wed Mar 11 2015 Devrim Gündüz <devrim@gunduz.org> - 1.0.0-3.rc0
- Rebuild for Proj 4.9.1

* Mon Aug 25 2014 Devrim Gündüz <devrim@gunduz.org> - 1.0.0-2.rc0
- Rebuilt for libgeotiff
- Add dependency for proj-devel

* Fri Aug  8 2014 Volker Fröhlich <volker27@gmx.at> - 1.0.0-1.rc0
- Remove pkgconfig requirement on the devel sub-package
- Delete soname symlink for the sqlite extension

* Wed Jun 11 2014 Volker Fröhlich <volker27@gmx.at> - 1.0.0-0.rc0
- Initial package for Fedora
