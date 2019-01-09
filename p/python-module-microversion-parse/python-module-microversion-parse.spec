%define pypi_name microversion-parse
%define fname microversion_parse

Name: python-module-%pypi_name
Version: 0.2.1
Release: alt1
Summary: A simple parser for OpenStack microversion headers
Group: Development/Python
License: ASL 2.0
Url: https://github.com/openstack/%pypi_name
Source: https://tarballs.openstack.org/%pypi_name/%fname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-webob >= 1.2.3
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 0.1.1

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-webob >= 1.2.3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-reno >= 0.1.1

%description
A simple parser for OpenStack microversion headers.

%package doc
Summary: Documentation for OpenStack %pypi_name library
Group: Development/Documentation

%description doc
Documentation for OpenStack %pypi_name library

%package -n python3-module-%pypi_name
Summary: A simple parser for OpenStack microversion headers
Group: Development/Python3

%description -n python3-module-%pypi_name
A simple parser for OpenStack microversion headers.

%prep
%setup -n %fname-%version
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python_install

pushd ../python3
%python3_install
popd

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%python_sitelibdir/*

%files doc
%doc README.rst doc/build/html

%files -n python3-module-%pypi_name
%python3_sitelibdir/*

%changelog
* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 0.2.1-alt1
- 0.2.1

* Fri Oct 21 2016 Alexey Shabalin <shaba@altlinux.ru> 0.1.4-alt1
- Initial packaging
