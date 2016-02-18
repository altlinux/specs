%define oname moto

%def_with python3
# slow:
%def_disable check

Name: python-module-%oname
Version: 0.4.10
Release: alt1.git20150808.1
Summary: A library that allows your python tests to easily mock out the boto library
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/moto/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/spulec/moto.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-jinja2 python-module-boto
#BuildPreReq: python-module-dicttoxml python-module-flask
#BuildPreReq: python-module-httpretty python-module-requests
#BuildPreReq: python-module-xmltodict python-module-six
#BuildPreReq: python-module-werkzeug python-module-nose
#BuildPreReq: python-module-mock python-module-sure
#BuildPreReq: python-module-coverage python-module-freezegun
#BuildPreReq: python-modules-xml python-modules-email
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-jinja2 python3-module-boto
#BuildPreReq: python3-module-dicttoxml python3-module-flask
#BuildPreReq: python3-module-httpretty python3-module-requests
#BuildPreReq: python3-module-xmltodict python3-module-six
#BuildPreReq: python3-module-werkzeug python3-module-nose
#BuildPreReq: python3-module-mock python3-module-sure
#BuildPreReq: python3-module-coverage python3-module-freezegun
%endif

%py_provides %oname
%py_requires jinja2 boto dicttoxml flask httpretty requests xmltodict
%py_requires six werkzeug xml bisect

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-jinja2 python-module-pyasn1 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-jinja2 python3-module-ndg-httpsclient python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools python3-module-yieldfrom.http.client
BuildRequires: python-module-chardet python-module-coverage python-module-dicttoxml python-module-ecdsa python-module-ndg-httpsclient python-module-nose python-module-ntlm python-module-pbr python-module-pycrypto python-module-pytest python-module-unittest2 python-module-yaml python3-module-chardet python3-module-coverage python3-module-dicttoxml python3-module-ecdsa python3-module-html5lib python3-module-mimeparse python3-module-nose python3-module-pbr python3-module-pycrypto python3-module-pytest python3-module-unittest2 python3-module-urllib3 python3-module-yaml python3-module-yieldfrom.urllib3 rpm-build-python3

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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.10-alt1.git20150808.1
- NMU: Use buildreq for BR.

* Sun Aug 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.10-alt1.git20150808
- Version 0.4.10

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.7-alt1.git20150722
- Version 0.4.7

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150222
- Version 0.4.1

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git201500203
- Version 0.4.0

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.9-alt1.git20150117
- Initial build for Sisyphus

