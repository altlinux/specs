%define oname moto

%def_with python3
# slow:
%def_disable check

Name: python-module-%oname
Version: 0.4.0
Release: alt1.git201500203
Summary: A library that allows your python tests to easily mock out the boto library
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/moto/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/spulec/moto.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-jinja2 python-module-boto
BuildPreReq: python-module-dicttoxml python-module-flask
BuildPreReq: python-module-httpretty python-module-requests
BuildPreReq: python-module-xmltodict python-module-six
BuildPreReq: python-module-werkzeug python-module-nose
BuildPreReq: python-module-mock python-module-sure
BuildPreReq: python-module-coverage python-module-freezegun
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-jinja2 python3-module-boto
BuildPreReq: python3-module-dicttoxml python3-module-flask
BuildPreReq: python3-module-httpretty python3-module-requests
BuildPreReq: python3-module-xmltodict python3-module-six
BuildPreReq: python3-module-werkzeug python3-module-nose
BuildPreReq: python3-module-mock python3-module-sure
BuildPreReq: python3-module-coverage python3-module-freezegun
%endif

%py_provides %oname
%py_requires jinja2 boto dicttoxml flask httpretty requests xmltodict
%py_requires six werkzeug

%description
Moto is a library that allows your python tests to easily mock out the
boto library.

%package -n python3-module-%oname
Summary: A library that allows your python tests to easily mock out the boto library
Group: Development/Python3
%py3_provides %oname
%py3_requires jinja2 boto dicttoxml flask httpretty requests xmltodict
%py3_requires six werkzeug

%description -n python3-module-%oname
Moto is a library that allows your python tests to easily mock out the
boto library.

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
python setup.py test
%make test
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3|' Makefile
%make test
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git201500203
- Version 0.4.0

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.9-alt1.git20150117
- Initial build for Sisyphus

