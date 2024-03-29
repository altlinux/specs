
%define sover 19
Name: jsoncpp%sover
Version: 1.8.4
Release: alt6
%define rname jsoncpp
%define libname lib%rname%sover

Group: System/Libraries
Summary: JSON library implemented in C++
Url: https://github.com/open-source-parsers/jsoncpp/
License: MIT

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Jun 11 2015 (-bi)
# optimized out: cmake-modules elfutils fontconfig fonts-bitmap-misc libstdc++-devel libwayland-client libwayland-server pkg-config python-base python-modules python3 python3-base ruby ruby-stdlibs
#BuildRequires: cmake doxygen fonts-bitmap-terminus fonts-otf-stix fonts-ttf-dejavu fonts-ttf-google-droid-kufi fonts-ttf-google-droid-sans fonts-ttf-google-droid-serif fonts-type1-urw gcc-c++ graphviz libdb4-devel python-module-google python-modules-compiler rpm-build-python3 rpm-build-ruby
BuildRequires: cmake doxygen gcc-c++ graphviz kde-common-devel
BuildRequires: rpm-build-python3

%description
%name is an implementation of a JSON (http://json.org) reader and writer in
C++. JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It is easy for humans to read and write. It is easy for machines to parse and
generate.

%package -n %libname
Summary: JSON library implemented in C++
Group: System/Libraries
%description -n %libname
%name is an implementation of a JSON (http://json.org) reader and writer in
C++. JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It is easy for humans to read and write. It is easy for machines to parse and
generate.

%package devel
Summary: Development headers and library for %name
Group: Development/C++
Conflicts: libjson-devel < 0.12
%description devel
This package contains the development headers and library for %name.

%package doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch
%description doc
This package contains the documentation for %name

%prep
%setup -n %rname-%version

%build
%Kbuild \
  -DJSONCPP_WITH_CMAKE_PACKAGE=ON \
  -DJSONCPP_WITH_PKGCONFIG_SUPPORT=ON \
  -DJSONCPP_WITH_TESTS=OFF \
  -DBUILD_STATIC_LIBS=OFF \
  -DBUILD_SHARED_LIBS=ON \
  #

%install
%Kinstall
# cleanup
rm -rf %buildroot/%_includedir
rm -rf %buildroot/%_libdir/cmake
rm -rf %buildroot/%_pkgconfigdir
rm -rf %buildroot/%_libdir/lib*.so

%files -n %libname
%doc AUTHORS LICENSE
%_libdir/lib%rname.so.%sover
%_libdir/lib%rname.so.*

%if 0
%files devel
%doc dist/doxygen/jsoncpp-api-html-*
%_libdir/lib%rname.so
%_includedir/json/
%_libdir/pkgconfig/%rname.pc
%_libdir/cmake/%rname/
%endif

#%files doc
#%_docdir/%name/

%changelog
* Thu Sep 30 2021 Sergey V Turchin <zerg@altlinux.org> 1.8.4-alt6
- build compat package

* Sat Dec 28 2019 Sergey V Turchin <zerg@altlinux.org> 1.8.4-alt5
- build with python3

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt4
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt3
- NMU: remove ubt from release

* Fri Feb 16 2018 Sergey V Turchin <zerg@altlinux.org> 1.8.4-alt2
- fix package specfile

* Tue Feb 06 2018 Sergey V Turchin <zerg@altlinux.org> 1.8.4-alt1
- new version

* Tue Apr 05 2016 Sergey V Turchin <zerg@altlinux.org> 1.7.2-alt1
- new version

* Tue Jun 16 2015 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt2
- add conflict with old json-c devel package (ALT#31072)

* Thu Jun 11 2015 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt1
- new version

* Thu Jun 04 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.0-alt0.1.1
- rebuild with c++11 ABI

* Tue Feb 04 2014 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt0.0.M70P.2
- built for M70P

* Mon Feb 03 2014 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt0.1
- initial build
