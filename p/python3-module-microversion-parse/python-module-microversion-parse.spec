%define pypi_name microversion-parse
%define fname microversion_parse

Name: python3-module-%pypi_name
Version: 0.2.1
Release: alt2
Summary: A simple parser for OpenStack microversion headers
Group: Development/Python3
License: Apache-2.0
Url: https://github.com/openstack/%pypi_name
Source: https://tarballs.openstack.org/%pypi_name/%fname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-webob >= 1.2.3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 0.1.1

%description
A simple parser for OpenStack microversion headers.

%package doc
Summary: Documentation for OpenStack %pypi_name library
Group: Development/Documentation

%description doc
Documentation for OpenStack %pypi_name library

%prep
%setup -n %fname-%version
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%build
%python3_build

python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python3_install

# Delete tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%python3_sitelibdir/*

%files doc
%doc README.rst doc/build/html

%changelog
* Tue Jul 28 2020 Grigory Ustinov <grenka@altlinux.org> 0.2.1-alt2
- Drop python2 support.

* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 0.2.1-alt1
- 0.2.1

* Fri Oct 21 2016 Alexey Shabalin <shaba@altlinux.ru> 0.1.4-alt1
- Initial packaging
