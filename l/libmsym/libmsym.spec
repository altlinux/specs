# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3 rpm-macros-mageia-compat
BuildRequires: gcc-c++ python3-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major     0.2
%define libname   libmsym%{major}
%define develname libmsym-devel

Name:           libmsym
Version:        0.2.3
Release:        alt2_3
Summary:        Molecular point group symmetry lib
License:        MIT
Group:          System/Libraries
Url:            https://github.com/mcodev31/libmsym
Source0:        https://github.com/mcodev31/libmsym/archive/v%{version}-paper/%{name}-%{version}.tar.gz
Patch0:         libmsym-0.2.3-fix-version.patch
BuildRequires:  ccmake cmake ctest
BuildRequires:  pkgconfig(python3)
Source44: import.info

%description
libmsym is a C library dealing with point group symmetry in molecules.

#----------------------------------------------------

%package -n     %{libname}
Summary:        Molecular point group symmetry lib
Group:          System/Libraries

%description -n %{libname}
libmsym is a C library dealing with point group symmetry in molecules.

#----------------------------------------------------

%package -n     %{develname}
Summary:        Development package for %{name}
Group:          Development/C++
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       msym-devel = %{version}-%{release}

%description -n %{develname}
Header files for development with %{name}.

#----------------------------------------------------

%package -n python3-module-libmsym
Summary:        Python 3 bindings for %{name}
Group:          Development/Python
BuildArch:      noarch

%description -n python3-module-libmsym
Python 3 bindings for %{name}.

#----------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-paper
%patch0 -p1


%build
%{mageia_cmake} \
        -DINSTALL_LIB_DIR=%{_libdir} \
        -DINSTALL_CMAKE_DIR=%{_libdir}/cmake/%{name} \
        -DMSYM_BUILD_PYTHON=ON \
        -DPYTHON=%{__python3} \
        -DMSYM_PYTHON_INSTALL_OPTS=--root="%{buildroot}"
%make_build

%install
%makeinstall_std -C build

%files -n %{libname}
%doc README.md
%doc --no-dereference LICENSE
%{_libdir}/libmsym.so.%{major}*

%files -n %{develname}
%doc README.md
%{_includedir}/%{name}/
%{_libdir}/libmsym.so
%{_libdir}/cmake/%{name}/

%files -n python3-module-libmsym
%doc bindings/python/README.md
%{python3_sitelibdir_noarch}/%{name}/
%{python3_sitelibdir_noarch}/%{name}-%{version}-py%{__python3_version}.egg-info


%changelog
* Mon Jan 13 2020 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_3
- fixed build

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_3
- new version

