%define oname windmill

%def_without python3

Name: python-module-%oname
Version: 1.7
Release: alt1.pre.git20130327
Summary: Web testing tool designed to let you painlessly automate and debug your web application
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/windmill/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/windmill/windmill.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
Windmill is an Open Source AJAX Web UI Testing framework.

Windmill implements cross browser testing, in-browser recording and
playback, and functionality for fast accurate debugging and test
environment integration.

%package -n python3-module-%oname
Summary: Web testing tool designed to let you painlessly automate and debug your web application
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Windmill is an Open Source AJAX Web UI Testing framework.

Windmill implements cross browser testing, in-browser recording and
playback, and functionality for fast accurate debugging and test
environment integration.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

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
	mv $i $i.py3
done
popd
%endif

%python_install

pushd windmill2
cp -fR *.py *.html docs tests \
	%buildroot%python_sitelibdir/windmill2/
cp -fR browser/extension \
	%buildroot%python_sitelibdir/windmill2/browser/
cp -fR castile/js \
	%buildroot%python_sitelibdir/windmill2/castile/
popd
%if_with python3
pushd ../python3
pushd windmill2
cp -fR *.py *.html docs tests \
	%buildroot%python3_sitelibdir/windmill2/
cp -fR browser/extension \
	%buildroot%python3_sitelibdir/windmill2/browser/
cp -fR castile/js \
	%buildroot%python3_sitelibdir/windmill2/castile/
popd
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt tutorial
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt tutorial
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.pre.git20130327
- Initial build for Sisyphus

