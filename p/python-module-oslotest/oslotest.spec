%define oname oslotest

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.10.0
Release: alt1.1
Summary: OpenStack test framework
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/oslotest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/openstack/oslotest.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools git-core
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-fixtures >= 3.0.0
BuildRequires: python-module-subunit >= 0.0.18
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-testrepository >= 0.0.18
BuildRequires: python-module-testscenarios >= 0.4
BuildRequires: python-module-testtools >= 1.4.0
BuildRequires: python-module-mock >= 2.0 python-module-mox3 >= 0.7.0
BuildRequires: python-module-hacking python-module-coverage
BuildRequires: python-module-mimeparse python-module-mccabe
BuildRequires: python-module-flake8 pyflakes
BuildRequires: python-module-sphinx-devel python-module-oslosphinx
BuildRequires: python-module-requests
BuildRequires: python-module-os-client-config >= 1.13.1
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-oslo.config >= 3.14.0
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-fixtures python3-module-subunit
BuildRequires: python3-module-six python3-module-testrepository
BuildRequires: python3-module-testscenarios python3-module-testtools
BuildRequires: python3-module-mock python3-module-mox3
BuildRequires: python3-module-hacking python3-module-coverage
BuildRequires: python3-module-mimeparse python3-module-mccabe
BuildRequires: python3-module-flake8 python3-pyflakes
BuildRequires: python3-module-sphinx python3-module-oslosphinx
BuildRequires: python3-module-requests
BuildRequires: python3-module-os-client-config
BuildRequires: python3-module-debtcollector >= 1.2.0
%endif

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
%setup
# let RPM handle deps
rm -rf {test-,}requirements.txt

git init-db
git config user.email "real at altlinux.org"
git config user.name "REAL"
git add . -A
git commit -a -m "commit"
git tag %version

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	sed -i 's|python|python3|g' $i
	sed -i 's|python33|python3|g' $i
	sed -i 's|tox|tox.py3|g' $i
	mv $i $i.py3
done
popd
mv %buildroot%python3_sitelibdir/%oname-*-py%_python3_version.egg-info \
	%buildroot%python3_sitelibdir/%oname-py%_python3_version.egg-info
%endif

%python_install
mv %buildroot%python_sitelibdir/%oname-*-py%_python_version.egg-info \
	%buildroot%python_sitelibdir/%oname-py%_python_version.egg-info

export PYTHONPATH=$PWD
pushd doc
sphinx-build -b pickle -d build/doctrees source build/pickle
sphinx-build -b html -d build/doctrees source build/html
popd

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
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

