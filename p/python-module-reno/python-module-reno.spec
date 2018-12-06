%define pypi_name reno
%def_with python3
%def_without doc

Name: python-module-%pypi_name
Version: 2.11.2
Release: alt1
Summary: Release Notes manager
Group: Development/Python

License: ASL 2.0
Url: http://www.openstack.org/
Source: %pypi_name-%version.tar.gz
BuildArch: noarch

Requires: git-core

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.4
BuildRequires: python-module-sphinx
BuildRequires: python-module-openstackdocstheme
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-yaml >= 3.10.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-oslotest
BuildRequires: python-module-nose
BuildRequires: git-core

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.4
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-yaml >= 3.10.0
BuildRequires: python3-module-oslotest
BuildRequires: python3-module-nose
%endif

%description
Reno is a release notes manager for storing
release notes in a gitnrepository and then building documentation from them.

Managing release notes for a complex project over a long period
of time with many releases can be time consuming and error prone. Reno
helps automate the hard parts.

%if_with python3
%package -n python3-module-%pypi_name
Summary: Release Notes manager
Group: Development/Python3
Requires: git-core

%description -n python3-module-%pypi_name
Reno is a release notes manager for storing
release notes in a gitnrepository and then building documentation from them.

Managing release notes for a complex project over a long period
of time with many releases can be time consuming and error prone. Reno
helps automate the hard parts.
%endif

%package doc
Summary: reno documentation
Group: Development/Documentation

%description doc
Documentation for reno

%package tests
Summary: Tests for %pypi_name
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %pypi_name.

%package -n python3-module-%pypi_name-tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: python3-module-%pypi_name = %EVR

%description -n python3-module-%pypi_name-tests
This package contains tests for %pypi_name.

%prep
%setup -n %pypi_name-%version

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

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

%if_with doc
# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo
%endif

%install
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/%pypi_name %buildroot%_bindir/%pypi_name.py3
popd
%endif
%python_install

%files
%doc README.rst
%_bindir/%pypi_name
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%pypi_name
%doc README.rst
%_bindir/%pypi_name.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%pypi_name-tests
%python3_sitelibdir/*/tests
%endif

%files tests
%python_sitelibdir/*/tests

%if_with doc
%files doc
%doc doc/build/html
%endif

%changelog
* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 2.11.2-alt1
- 2.11.2

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.2-alt1
- 1.6.2
- add git to requires

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Dec 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial Package
