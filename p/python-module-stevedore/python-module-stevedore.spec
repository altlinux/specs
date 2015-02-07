%define oname stevedore

%def_with python3

Name:           python-module-%oname
Version:        1.1.0
Release:        alt2
Summary:        Manage dynamic plugins for Python applications

Group:		Development/Python
License:        ASL 2.0
URL:            https://github.com/dreamhost/stevedore
Source0:        %{name}-%{version}.tar
Patch: stevedore-alt-requirements.patch
Patch1: stevedore-alt-docs.patch
BuildArch:      noarch

BuildRequires:  python-devel python-module-argparse
BuildRequires:  python-module-setuptools-tests
BuildRequires:  python-module-pbr python-module-six
BuildRequires:  python-module-Pillow python-module-oslotest
BuildRequires:  python-module-discover python-module-testrepository
BuildRequires:  python-module-coverage python-module-mock
BuildRequires:  python-module-mox3 python-module-mimeparse
BuildRequires:  python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel python3-module-argparse
BuildRequires:  python3-module-setuptools-tests
BuildRequires:  python3-module-pbr python3-module-six
BuildRequires:  python3-module-Pillow python3-module-oslotest
BuildRequires:  python3-module-discover python3-module-testrepository
BuildRequires:  python3-module-coverage python3-module-mock
BuildRequires:  python3-module-mox3 python3-module-mimeparse
BuildRequires:  python3-module-sphinx
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
%setup
%patch -p2
%patch1 -p2

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
rm -fR build
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc README.rst LICENSE
%python_sitelibdir/%oname
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Avoid requirement on pbr in egg-info

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0
- Added module for Python 3
- Added docs
- Moved tests into separate package

* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 0.14-alt1
- First build for ALT (based on Fedora 0.14-1.fc21.src)

