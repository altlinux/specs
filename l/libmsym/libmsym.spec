%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    python
%define        nomen msym

Name:          lib%nomen
Version:       0.2.4
Release:       alt0.1
Summary:       Molecular point group symmetry lib
License:       MIT
Group:         System/Libraries
Url:           https://github.com/mcodev31/libmsym
Vcs:           https://github.com/mcodev31/libmsym.git

Source:        %{name}-%{version}.tar
BuildRequires(pre): rpm-build-python3
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: pkgconfig(python3)
BuildRequires: python3(setuptools)

%description
libmsym is a C library dealing with point group symmetry in molecules.


%package       devel
Summary:       Development package for %{name}
Group:         Development/C++
Provides:      %nomen-devel = %EVR

%description   devel
Header files for development with %{name}.


%if_enabled    python
%package       -n python3-module-%name
Summary:       Python 3 bindings for %{name}
Group:         Development/Python
BuildArch:     noarch

%description   -n python3-module-%name
Python 3 bindings for %{name}.
%endif


%prep
%setup -q


%build
%cmake \
   -DBUILD_SHARED_LIBS:BOOL=ON \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo \
   -DINSTALL_LIB_DIR=%{_libdir} \
   -DINSTALL_CMAKE_DIR=%{_libdir}/cmake/%{name} \
   -DMSYM_BUILD_EXAMPLES=ON \
   -DMSYM_BUILD_PYTHON=ON \
   -DPYTHON=%{__python3} \
   -DMSYM_PYTHON_INSTALL_OPTS=--root="%{buildroot}"
%cmake_build

%install
%cmake_install


%files
%doc README.md
%_libdir/%name.so.*

%files         devel
%doc README.md
%_includedir/%name
%_libdir/%name.so
%_cmakedir/%name

%if_enabled    python
%files         -n python3-module-%name
%doc bindings/python/README.md
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%name-*-py%{__python3_version}.egg-info
%endif


%changelog
* Wed Jul 23 2025 Pavel Skrylev <majioa@altlinux.org> 0.2.4-alt0.1
- ^ 0.2.3 -> 0.2.4pre
- * rebased to upstream

* Tue Feb 06 2024 Grigory Ustinov <grenka@altlinux.org> 0.2.3-alt2_7.1
- NMU: fixed build

* Sun Apr 10 2022 Igor Vlasenko <viy@altlinux.org> 0.2.3-alt2_7
- update by mgaimport

* Thu Mar 25 2021 Igor Vlasenko <viy@altlinux.org> 0.2.3-alt2_5
- update by mgaimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_4
- fixed build

* Mon Jan 13 2020 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_3
- fixed build

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_3
- new version

