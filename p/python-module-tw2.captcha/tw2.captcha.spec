%define mname tw2
%define oname %mname.captcha

%def_with python3

Name: python-module-%oname
Version: 0.0.4
Release: alt1.git20120520
Summary: tw2 captchas with lots of plugins
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.captcha/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.captcha.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core python-module-pycrypto
BuildPreReq: python-module-Pillow python-module-kitchen
BuildPreReq: python-module-tw2.forms python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core python3-module-pycrypto
BuildPreReq: python3-module-Pillow python3-module-kitchen
BuildPreReq: python3-module-tw2.forms python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname tw2.core Crypto PIL kitchen tw2.forms

%description
tw2.captcha is a toscawidgets2 (tw2) captcha plugin.

%package -n python3-module-%oname
Summary: tw2 captchas with lots of plugins
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core Crypto PIL kitchen tw2.forms

%description -n python3-module-%oname
tw2.captcha is a toscawidgets2 (tw2) captcha plugin.

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
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/%mname/captcha
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/captcha
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20120520
- Initial build for Sisyphus

