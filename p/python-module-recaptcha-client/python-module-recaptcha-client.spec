%define version 1.0.6
%define release alt1
%setup_python_module recaptcha-client

%def_with python3

Name: %packagename
Version:%version
Release: alt1.1

Summary: Provides a CAPTCHA for Python using the reCAPTCHA service

License: MIT/X11
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/recaptcha-client

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

Source: %modulename-%version.tar

%py_requires Crypto

%description
Provides a CAPTCHA for Python using the reCAPTCHA service. Does not
require any imaging libraries because the CAPTCHA is served directly
from reCAPTCHA. Also allows you to securely obfuscate emails with
Mailhide.

%package -n python3-module-%modulename
Summary: Provides a CAPTCHA for Python using the reCAPTCHA service
Group: Development/Python3
%py3_requires Crypto

%description -n python3-module-%modulename
Provides a CAPTCHA for Python using the reCAPTCHA service. Does not
require any imaging libraries because the CAPTCHA is served directly
from reCAPTCHA. Also allows you to securely obfuscate emails with
Mailhide.

%prep
%setup -n %modulename-%version

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1
- Version 1.0.6
- Added module for Python 3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt2.1.1
- Rebuild with Python-2.7

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt2.1
- Rebuilt with python 2.6

* Sun Feb 01 2009 Denis Klimov <zver@altlinux.org> 1.0.3-alt2
- more improve using setup_python_module macros
- use optimize and record options for install

* Fri Jan 30 2009 Denis Klimov <zver@altlinux.org> 1.0.3-alt1
- Initial build for ALT Linux

