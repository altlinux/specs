%define shortname comps
%define major 0
%define libname lib%shortname%major
%define libname_devel lib%shortname-devel

%def_enable docs

Name: libcomps
Version: 0.1.23
Release: alt1

Summary: Comps XML file manipulation library

Group: System/Libraries
License: GPLv2+
Url: https://github.com/rpm-software-management/libcomps
Vcs: https://github.com/rpm-software-management/libcomps

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-macros-cmake
BuildRequires: /usr/bin/dot gcc-c++ pkgconfig(liblzma) python3(setuptools)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(check)
BuildRequires: pkgconfig(expat)
BuildRequires: ccmake cmake ctest

%description
Libcomps is library for structure-like manipulation with content of
comps XML files. Supports read/write XML file, structure(s) modification.

%package -n %libname
Summary: Libraries for %name
Group: System/Libraries
#https://bugzilla.altlinux.org/show_bug.cgi?id=51577#c2
Provides: libcomps = %EVR
Obsoletes: libcomps < %EVR

%description -n %libname
Libraries for %name.

%package -n %libname_devel
Summary: Development files for libcomps library
Group: Development/C
Provides: %name-devel = %version-%release
Requires: %libname = %version-%release

%description -n %libname_devel
Development files for %name.

%if_enabled docs
%package doc
Summary: Documentation files for libcomps library
Group: Development/C
BuildArch: noarch
BuildRequires: doxygen

%description doc
Documentation files for libcomps library.

%package -n python-module-libcomps-doc
Summary: Documentation files for python bindings libcomps library
Group: Development/Python
Requires: python3-module-libcomps = %version-%release
BuildArch: noarch
BuildRequires: python3-module-sphinx python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3-module-sphinx_rtd_theme

%description -n python-module-libcomps-doc
Documentation files for python bindings libcomps library.
%endif

%package -n python3-module-libcomps
Summary: Python 3 bindings for libcomps library
%{?python_provide:%python_provide python3-libcomps}
Group: Development/Python
BuildRequires: python3-devel
Requires: %libname = %version-%release

%description -n python3-module-libcomps
Python3 bindings for libcomps library.

%prep
%setup

# Fix build with sphinx 1.8.3
sed -i -e 's,sphinx.ext.pngmath,sphinx.ext.imgmath,' libcomps/src/python/docs/doc-sources/conf.py.in

%build
%cmake %{?_enable_%{docs}:-DSPHINX_EXECUTABLE="%_bindir/sphinx-build-3"} ./libcomps/
%cmake_build

%if_enabled docs
make docs -C %_arch-alt-linux
sphinx-build-3  %name/src/python/docs/doc-sources html
%endif

%check
%ctest

%install
%cmake_install

%files -n %libname
%doc README.md
%doc --no-dereference COPYING
%_libdir/libcomps.so.%major

%files -n %libname_devel
%_includedir/*
%_libdir/libcomps.so
%_libdir/pkgconfig/%name.pc

%if_enabled docs
%files doc
%doc %_arch-alt-linux/docs/libcomps-doc/html

%files -n python-module-libcomps-doc
%doc  html
%endif

%files -n python3-module-libcomps
%python3_sitelibdir/%name/

%changelog
* Fri Sep 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.23-alt1
- 0.1.22 -> 0.1.23

* Sat Aug 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.22-alt1
- 0.1.21 -> 0.1.22

* Fri Jul 18 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.21-alt2
- spec cleanup

* Thu Jul 17 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.21-alt1
- NMU:
  + 0.1.18 -> 0.1.21
  + fixed FTBFS
  + added obsoletes and changed provides

* Fri Mar 22 2024 Igor Vlasenko <viy@altlinux.org> 0.1.18-alt1_4
- update by mgaimport

* Sun Apr 10 2022 Igor Vlasenko <viy@altlinux.org> 0.1.18-alt1_3
- update by mgaimport

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 0.1.18-alt1_1
- new version

* Mon Jun 21 2021 Igor Vlasenko <viy@altlinux.org> 0.1.17-alt1_1
- new version

* Thu Mar 25 2021 Igor Vlasenko <viy@altlinux.org> 0.1.15-alt1_3
- update by mgaimport

* Tue Sep 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.1.15-alt1_2
- update by mgaimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.1.14-alt1_2
- new version

* Thu Apr 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.11-alt1_1
- update by mgaimport

* Tue Jan 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.9-alt1_1
- update by mgaimport

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.8-alt1_3.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt1_3
- new version

