%define pypi_name castellan
%def_with python3

Name: python-module-%pypi_name
Version: 0.4.0
Release: alt1
Summary: Generic Key Manager interface for OpenStack
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/%pypi_name

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-cryptography >= 1.0
BuildRequires: python-module-oslo.config >= 3.7.0
BuildRequires: python-module-oslo.context >= 0.2.0
BuildRequires: python-module-oslo.log >= 1.14.0
BuildRequires: python-module-oslo.policy >= 0.5.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.5.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-cryptography >= 1.0
BuildRequires: python3-module-oslo.config >= 3.7.0
BuildRequires: python3-module-oslo.context >= 0.2.0
BuildRequires: python3-module-oslo.log >= 1.14.0
BuildRequires: python3-module-oslo.policy >= 0.5.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.5.0
%endif

%description
Generic Key Manager interface for OpenStack

%package -n python3-module-%pypi_name
Summary: Generic Key Manager interface for OpenStack
Group: Development/Python3

%description -n python3-module-%pypi_name
Generic Key Manager interface for OpenStack


%package doc
Summary: Documentation for Generic Key Manager interface for OpenStack
Group: Development/Documentation

%description doc
Documentation for Generic Key Manager interface for OpenStack

%prep
%setup
# Remove bundled egg-info
rm -rf %pypi_name.egg-info

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

# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif
# Delete tests

rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%endif

%files doc
%doc  doc/build/html

%changelog
* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1.1
- NMU: Use buildreq for BR.

* Fri Oct 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1
- Initial build for Sisyphus

