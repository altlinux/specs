%define oname stevedore

%def_with python3

Name: python-module-%oname
Version: 1.20.1
Release: alt1.1
Summary: Manage dynamic plugins for Python applications
Group: Development/Python
License: ASL 2.0
URL: http://docs.openstack.org/developer/stevedore/
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx

BuildRequires: python-devel python-module-argparse
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8 python-module-six >= 1.9
BuildRequires: python-module-argparse
BuildRequires: python-module-Pillow python-module-oslotest
BuildRequires: python-module-discover python-module-testrepository
BuildRequires: python-module-coverage python-module-mock
BuildRequires: python-module-mox3 python-module-mimeparse
BuildRequires: python-module-sphinx-devel
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-argparse
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8 python3-module-six >= 1.9
BuildRequires: python3-module-argparse
BuildRequires: python3-module-Pillow python3-module-oslotest
BuildRequires: python3-module-discover python3-module-testrepository
BuildRequires: python3-module-coverage python3-module-mock
BuildRequires: python3-module-mox3 python3-module-mimeparse
%endif

%py_provides %oname

%description
Manage dynamic plugins for Python applications

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Manage dynamic plugins for Python applications

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Manage dynamic plugins for Python applications

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Manage dynamic plugins for Python applications

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Manage dynamic plugins for Python applications
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Manage dynamic plugins for Python applications

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Manage dynamic plugins for Python applications

This package contains tests for %oname.

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD
%make -C doc pickle
%make -C doc html

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

#%check
#python setup.py test
#rm -fR build
#export PYTHONPATH=$PWD
#py.test
#%if_with python3
#pushd ../python3
#python3 setup.py test
#rm -fR build
#export PYTHONPATH=$PWD
#py.test-%_python3_version
#popd
#%endif

%files
%doc README.rst LICENSE
%python_sitelibdir/%oname
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/example

%files tests
%python_sitelibdir/%oname/tests
%python_sitelibdir/%oname/example

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/example

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/example
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.20.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 1.20.1-alt1
- 1.20.1

* Fri Apr 28 2017 Alexey Shabalin <shaba@altlinux.ru> 1.20.0-alt1
- 1.20.0

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1.17.1-alt1
- 1.17.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Thu Mar 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Avoid requirement on pbr in egg-info

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0
- Added module for Python 3
- Added docs
- Moved tests into separate package

* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 0.14-alt1
- First build for ALT (based on Fedora 0.14-1.fc21.src)

