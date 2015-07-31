%define oname hitchsmtp

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1.git20150622
Summary: Mock SMTP server that logs incoming messages to stdout for easy parsing and testing
License: AGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/hitchsmtp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hitchtest/hitchsmtp.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests /proc
BuildPreReq: python-module-hitch python-module-hitchserve
BuildPreReq: python-module-hitchenvironment python-module-hitchtest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-hitch python3-module-hitchserve
BuildPreReq: python3-module-hitchenvironment python3-module-hitchtest
%endif

%py_provides %oname
%py_requires hitch hitchserve

%description
Mock SMTP server that logs all incoming messages to stdout as JSON for
easy parsing by HitchServe.

HitchSMTP contains a service definition for use with Hitch, but can also
be used alone.

%if_with python3
%package -n python3-module-%oname
Summary: Mock SMTP server that logs incoming messages to stdout for easy parsing and testing
Group: Development/Python3
%py3_provides %oname
%py3_requires hitch hitchserve

%description -n python3-module-%oname
Mock SMTP server that logs all incoming messages to stdout as JSON for
easy parsing by HitchServe.

HitchSMTP contains a service definition for use with Hitch, but can also
be used alone.
%endif

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

%check
python setup.py test -v
%if_with python3
py.test -vv tests/*.py
pushd ../python3
python3 setup.py test -v
py.test-%_python3_version -vv tests/*.py
popd
%endif

%files
%doc *.rst tests
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst tests
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150622
- Initial build for Sisyphus

