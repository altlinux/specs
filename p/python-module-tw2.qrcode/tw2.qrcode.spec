%define mname tw2
%define oname %mname.qrcode

%def_with python3

Name: python-module-%oname
Version: 2.0.2
Release: alt1.git20120306
Summary: QRCode Widget
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.qrcode/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gregjurman/tw2.qrcode.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mako python-module-tw2.core-tests
BuildPreReq: python-module-tw2.jquery python-module-nose
BuildPreReq: python-module-BeautifulSoup python-module-genshi
BuildPreReq: python-module-FormEncode python-module-strainer
BuildPreReq: python-module-webtest
BuildPreReq: python-modules-multiprocessing python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mako python3-module-tw2.core-tests
BuildPreReq: python3-module-tw2.jquery python3-module-nose
BuildPreReq: python3-module-BeautifulSoup python3-module-genshi
BuildPreReq: python3-module-FormEncode python3-module-strainer
BuildPreReq: python3-module-webtest
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname mako tw2.core tw2.jquery

%description
Client-side QR Code Widget.

%package -n python3-module-%oname
Summary: QRCode Widget
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname mako tw2.core tw2.jquery

%description -n python3-module-%oname
Client-side QR Code Widget.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc docs/*.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc docs/*.rst
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.git20120306
- Initial build for Sisyphus

