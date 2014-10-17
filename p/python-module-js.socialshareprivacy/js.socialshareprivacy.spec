%define oname js.socialshareprivacy

%def_with python3

Name: python-module-%oname
Version: 1.5
Release: alt1.git20140212
Summary: Fanstatic packaging of jquery.socialshareprivacy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.socialshareprivacy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zerobuzz/js.socialshareprivacy.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-js.jquery python-module-hgtools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-js.jquery python3-module-hgtools
%endif

%py_provides %oname
%py_requires js.jquery fanstatic

%description
This library packages the jquery plugin jquery.socialshareprivacy for
fanstatic. The Library allows you to integrate facebook, twitter and
google+ in a privacy friendly way.

%package -n python3-module-%oname
Summary: Fanstatic packaging of jquery.socialshareprivacy
Group: Development/Python3
%py3_provides %oname
%py3_requires js.jquery fanstatic

%description -n python3-module-%oname
This library packages the jquery plugin jquery.socialshareprivacy for
fanstatic. The Library allows you to integrate facebook, twitter and
google+ in a privacy friendly way.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
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

cp -fR js/socialshareprivacy/resources \
	%buildroot%python_sitelibdir/js/socialshareprivacy/
%if_with python3
pushd ../python3
cp -fR js/socialshareprivacy/resources \
	%buildroot%python3_sitelibdir/js/socialshareprivacy/
popd
%endif

%check
python setup.py test
python -c \
	"from js.socialshareprivacy import socialshareprivacy; socialshareprivacy.need()"
%if_with python3
pushd ../python3
python3 setup.py test
python3 -c \
	"from js.socialshareprivacy import socialshareprivacy; socialshareprivacy.need()"
popd
%endif

%files
%doc *.txt
%python_sitelibdir/js/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20140212
- Initial build for Sisyphus

