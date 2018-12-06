%define oname oslotest

%def_disable check

Name: python-module-%oname
Version: 3.6.0
Release: alt1
Summary: OpenStack test framework
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/oslotest/
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools git-core
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-fixtures >= 3.0.0
BuildRequires: python-module-subunit >= 1.0.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-testrepository >= 0.0.18
BuildRequires: python-module-testscenarios >= 0.4
BuildRequires: python-module-testtools >= 2.2.0
BuildRequires: python-module-mock >= 2.0 python-module-mox3 >= 0.20.0
BuildRequires: python-module-hacking python-module-coverage
BuildRequires: python-module-mimeparse python-module-mccabe
BuildRequires: python-module-flake8 pyflakes
BuildRequires: python-module-sphinx-devel
BuildRequires: python-module-requests
BuildRequires: python-module-os-client-config >= 1.28.0
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-oslo.config >= 5.2.0


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-fixtures python3-module-subunit
BuildRequires: python3-module-six python3-module-testrepository
BuildRequires: python3-module-testscenarios python3-module-testtools
BuildRequires: python3-module-mock python3-module-mox3
BuildRequires: python3-module-hacking python3-module-coverage
BuildRequires: python3-module-mimeparse python3-module-mccabe
BuildRequires: python3-module-flake8 python3-pyflakes
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-requests
BuildRequires: python3-module-os-client-config
BuildRequires: python3-module-debtcollector
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-reno
BuildRequires: python3-module-oslo.config


%py_provides %oname


%description
OpenStack test framework and test fixtures.

%package -n python3-module-%oname
Summary: OpenStack test framework
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
OpenStack test framework and test fixtures.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
OpenStack test framework and test fixtures.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
OpenStack test framework and test fixtures.

This package contains documentation for %oname.

%prep
%setup -n %oname-%version
rm -rf {test-,}requirements.txt

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

#python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
#rm -fr doc/build/html/.buildinfo

%install

pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	sed -i 's|python|python3|g' $i
	sed -i 's|python33|python3|g' $i
	sed -i 's|tox|tox.py3|g' $i
	mv $i python3-$i
done
popd

%python_install

%check
python setup.py test
py.test

pushd ../python3
python3 setup.py test
py.test-%_python3_version
popd

%files
%doc *.rst
%_bindir/*
%exclude %_bindir/python3-*
%python_sitelibdir/*
#%exclude %python_sitelibdir/*/pickle

#%files pickles
#%python_sitelibdir/*/pickle

#%files docs
#%doc doc/build/html/*

%files -n python3-module-%oname
%doc *.rst
%_bindir/python3-*
%python3_sitelibdir/*

%changelog
* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 3.6.0-alt1
- 3.6.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.11.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Fri May 15 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20141105
- Initial build for Sisyphus

