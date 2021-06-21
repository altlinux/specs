Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3 rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: python-devel rpm-build-python
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define __cmake_in_source_build 1

Name:           libcomps
Version:        0.1.17
Release:        alt1_1
Summary:        Comps XML file manipulation library

License:        GPLv2+
URL:            https://github.com/rpm-software-management/libcomps
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  ctest cmake
BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  libcheck-devel
BuildRequires:  libexpat-devel
BuildRequires:  zlib-devel
Source44: import.info

%description
Libcomps is library for structure-like manipulation with content of
comps XML files. Supports read/write XML file, structure(s) modification.

%package devel
Group: Development/C
Summary:        Development files for libcomps library
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for libcomps library.

%package doc
Group: Development/C
Summary:        Documentation files for libcomps library
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  doxygen

%description doc
Documentation files for libcomps library.

%package -n python-module-libcomps-doc
Group: Development/Python
Summary:        Documentation files for python bindings libcomps library
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  python3-module-sphinx python3-module-sphinx-sphinx-build-symlink


%description -n python-module-libcomps-doc
Documentation files for python bindings libcomps library.

%package -n python3-module-libcomps
Group: Development/Python
Summary:        Python 3 bindings for libcomps library
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{name}}
Requires:       %{name} = %{version}-%{release}
Obsoletes:      platform-python-%{name} < %{version}-%{release}

%description -n python3-module-libcomps
Python3 bindings for libcomps library.

%prep
%setup -q -n %{name}-%{version}


mkdir build-py3
mkdir build-doc

%build
pushd build-py3
  %{fedora_v2_cmake} ../libcomps/
  %make_build
popd

pushd build-doc
  %{fedora_v2_cmake} ../libcomps/
%make_build docs
%make_build pydocs
popd

%install
pushd build-py3
  %makeinstall_std
popd

%check
pushd build-py3
  make test
  make pytest
popd

%files
%doc --no-dereference COPYING
%doc README.md
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/

%files doc
%doc build-doc/docs/libcomps-doc/html

%files -n python-module-libcomps-doc
%doc build-doc/src/python/docs/html

%files -n python3-module-libcomps
%{python3_sitelibdir}/%{name}/
#%{python3_sitelibdir}/%{name}-%{version}-py%{__python3_version}.egg-info

%changelog
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

