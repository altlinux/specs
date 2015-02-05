%define mname kids
%define oname %mname.data

%def_with python3

Name: python-module-%oname
Version: 0.0.3
Release: alt1.git20150205
Summary: Kids data manipulation helpers
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kids.data/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/0k/kids.data.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests git
BuildPreReq: python-module-d2to1 python-module-nose
BuildPreReq: python-module-distance python-module-kids.cache
BuildPreReq: python-module-kids.txt python-module-sact.epoch
BuildPreReq: python-module-pytz python-module-zope.component
BuildPreReq: python-module-zope.interface python-module-dateutil
BuildPreReq: python-module-zope.event python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-d2to1 python3-module-nose
BuildPreReq: python3-module-distance python3-module-kids.cache
BuildPreReq: python3-module-kids.txt python3-module-sact.epoch
BuildPreReq: python3-module-pytz python3-module-zope.component
BuildPreReq: python3-module-zope.interface python3-module-dateutil
BuildPreReq: python3-module-zope.event python3-module-six
%endif

%py_provides %oname
%py_requires %mname distance kids.cache kids.txt sact.epoch pytz six
%py_requires zope.component zope.interface dateutil zope.event

%description
kids.data is a Python library providing helpers to manage data.

It's part of 'Kids' (for Keep It Dead Simple) library.

%package -n python3-module-%oname
Summary: Kids data manipulation helpers
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname distance kids.cache kids.txt sact.epoch pytz six
%py3_requires zope.component zope.interface dateutil zope.event

%description -n python3-module-%oname
kids.data is a Python library providing helpers to manage data.

It's part of 'Kids' (for Keep It Dead Simple) library.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version -m "%version"

%if_with python3
cp -fR . ../python3
%endif

%build
./autogen.sh
%python_build_debug

%if_with python3
pushd ../python3
./autogen.sh
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.rst
%python_sitelibdir/%mname/data
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/data
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20150205
- Initial build for Sisyphus

