%def_with python3

%define pypi_name futurist

Name: python-module-%pypi_name
Version: 0.5.0
Release: alt1
Summary: Useful additions to futures, from the future
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/futurist
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-futures >= 3.0
BuildRequires: python-module-monotonic >= 0.3
BuildRequires: python-module-contextlib2 >= 0.4.0
BuildRequires: python-module-six >= 1.9.0

#Requires: python-module-six >= 1.9.0
Requires: python-module-monotonic
Requires: python-module-futures >= 3.0
Requires: python-module-contextlib2 >= 0.4.0

%description
Code from the future, delivered to you in the now.

%package doc
Summary: Documentation for futurist library
Group: Development/Documentation

%description doc
Documentation for futurist library.

%if_with python3
%package -n python3-module-%pypi_name
Summary: Useful additions to futures, from the future
Group: Development/Python3

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-monotonic
BuildRequires: python3-module-contextlib2
BuildRequires: python3-module-six

#Requires: python3-module-six >= 1.9.0
Requires: python3-module-monotonic
Requires: python3-module-contextlib2 >= 0.4.0

%description -n python3-module-%pypi_name
Code from the future, delivered to you in the now.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo


%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst
%python_sitelibdir/%pypi_name
%python_sitelibdir/*.egg-info

%files doc
%doc doc/build/html

%if_with python3
%files -n python3-module-%pypi_name
%doc README.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- Initial package.
