%define sname oslo.i18n

%def_with python3

Name: python-module-%sname
Version: 3.5.0
Release: alt1
Summary: OpenStack i18n library
Group: Development/Python
License: ASL 2.0
Url: https://github.com/openstack/%sname
Source: %name-%version.tar

Provides: python-module-oslo-i18n = %EVR

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-d2to1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-sphinx >= 1.1.2
BuildRequires: python-module-oslosphinx >= 2.5.0
BuildRequires: python-module-fixtures
BuildRequires: python-module-oslo.config >= 3.7.0
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-sphinx >= 1.1.2
BuildRequires: python3-module-oslosphinx >= 2.5.0
BuildRequires: python3-module-fixtures
%endif

BuildArch: noarch

%description
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application
or library.

%if_with python3
%package -n python3-module-%sname
Summary:    OpenStack common configuration library
Group: Development/Python3
Provides: python3-module-oslo-i18n = %EVR

%description -n python3-module-%sname
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application
or library.
%endif


%package doc
Summary: Documentation for OpenStack i18n library
Group: Development/Documentation
Provides: python-module-oslo-i18n-doc = %EVR

%description doc
Documentation for the oslo.i18n library.

%prep
%setup

# Remove bundled egg-info
rm -rf %sname.egg-info

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


# generate html docs
python setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}


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
%doc AUTHORS ChangeLog CONTRIBUTING.rst HACKING.rst LICENSE PKG-INFO README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%files doc
%doc doc/build/html

%changelog
* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 3.5.0-alt1
- 3.5.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- Initial release
