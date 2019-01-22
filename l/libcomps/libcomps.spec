# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3 rpm-macros-mageia-compat
BuildRequires: gcc-c++ python-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define shortname comps
%define major 0
%define libname lib%{shortname}%{major}
%define libname_devel lib%{shortname}-devel

Name:           libcomps
Version:        0.1.9
Release:        alt1_1
Summary:        Comps XML file manipulation library

Group:          System/Libraries
License:        GPLv2+
URL:            https://github.com/rpm-software-management/libcomps
Source0:        https://github.com/rpm-software-management/libcomps/archive/%{name}-%{version}.tar.gz

# Patches from upstream
Patch1:         0001-Fix-Missing-braces.patch

# Fixes zlib linking, from:
# https://github.com/rpm-software-management/libcomps/pull/28
Patch0:         libcomps-0001-Add-zlib-as-an-explicit-dependency.patch
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(expat)
BuildRequires:  ccmake cmake ctest


# prevent provides from nonstandard paths:
%define __provides_exclude_from ^(%{python_sitelibdir}/.*\\.so\\|%{python3_sitelibdir}/.*\\.so)$
Source44: import.info

%description
Libcomps is library for structure-like manipulation with content of
comps XML files. Supports read/write XML file, structure(s) modification.

%package -n %{libname}
Summary:        Libraries for %{name}
Group:          System/Libraries

%description -n %{libname}
Libraries for %{name}

%package -n %{libname_devel}
Summary:        Development files for libcomps library
Group:          Development/C
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n %{libname_devel}
Development files for %{name}.

%package doc
Summary:        Documentation files for libcomps library
Group:          Development/C
BuildArch:      noarch
BuildRequires:  doxygen

%description doc
Documentation files for libcomps library

%package -n python-module-libcomps-doc
Summary:        Documentation files for python bindings libcomps library
Group:          Development/Python
Requires:       python-module-libcomps = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  python-module-sphinx
BuildRequires:  python-module-sphinx_rtd_theme

%description -n python-module-libcomps-doc
Documentation files for python bindings libcomps library

%package -n python-module-libcomps
Summary:        Python 2 bindings for libcomps library
Group:          Development/Python
BuildRequires:  pkgconfig(python)
Provides:       python-%{name} = %{version}-%{release}
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n python-module-libcomps
Python2 bindings for libcomps library

%package -n python3-module-libcomps
Summary:        Python 3 bindings for libcomps library
Group:          Development/Python
BuildRequires:  python3-devel
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n python3-module-libcomps
Python3 bindings for libcomps library


%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
%patch1 -p1

rm -rf py3
mkdir py3

# Fix build with sphinx 1.8.3
sed -i -e 's,sphinx.ext.pngmath,sphinx.ext.imgmath,' libcomps/src/python/docs/doc-sources/conf.py.in

%build
%{mageia_cmake} -DPYTHON_DESIRED:STRING=2 ../libcomps/
%make_build
make docs
make pydocs

# Py3 build
pushd ../py3
%{mageia_cmake} -DPYTHON_DESIRED:STRING=3 ../../libcomps/
%make_build
popd


%check
pushd ./build
make test
popd

# Py3 check
pushd ./py3/build
make pytest
popd


%install
pushd ./build
%makeinstall_std
popd

# Py3 install
pushd ./py3/build
%makeinstall_std
popd


%files -n %{libname}
%{_libdir}/libcomps.so.%{major}.*
%doc README.md COPYING

%files -n %{libname_devel}
%{_libdir}/libcomps.so
%{_includedir}/*

%files doc
%doc build/docs/libcomps-doc/html

%files -n python-module-libcomps-doc
%doc build/src/python/docs/html

%files -n python-module-libcomps
%{python_sitelibdir}/libcomps

%files -n python3-module-libcomps
%{python3_sitelibdir}/libcomps


%changelog
* Tue Jan 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.9-alt1_1
- update by mgaimport

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.8-alt1_3.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt1_3
- new version

