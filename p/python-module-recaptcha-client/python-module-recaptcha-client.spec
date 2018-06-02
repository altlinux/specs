%def_with python3

Name: python-module-recaptcha-client
Version: 2.0.1
Release: alt1

Summary: Python module for working with Google's reCAPTCHA v1 and v2

License: MIT/X11
Group: Development/Python
BuildArch: noarch
Url: https://github.com/redhat-infosec/python-recaptcha

%setup_python_module recaptcha-client

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

# Source-url: https://github.com/redhat-infosec/python-recaptcha/archive/v%version.tar.gz
Source: %name-%version.tar

%py_requires Crypto

%description
Provides a CAPTCHA for Python using the reCAPTCHA service. Does not
require any imaging libraries because the CAPTCHA is served directly
from reCAPTCHA. Also allows you to securely obfuscate emails with
Mailhide.

This Python module brings in Google's reCAPTCHA v1 and v2 support.
Although v1 is being deactivated starting from the 31st of March 2018
it's kept around for backwards compatibility and it's still marked as the default library option.

%package -n python3-module-%modulename
Summary: Provides a CAPTCHA for Python using the reCAPTCHA service
Group: Development/Python3
%py3_requires Crypto

%description -n python3-module-%modulename
Provides a CAPTCHA for Python using the reCAPTCHA service. Does not
require any imaging libraries because the CAPTCHA is served directly
from reCAPTCHA. Also allows you to securely obfuscate emails with
Mailhide.

This Python module brings in Google's reCAPTCHA v1 and v2 support.
Although v1 is being deactivated starting from the 31st of March 2018
it's kept around for backwards compatibility and it's still marked as the default library option.

%prep
%setup

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/*
%endif

%changelog
* Sat Jun 02 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- upstream got forked into https://github.com/redhat-infosec/python-recaptcha
- build new version, cleanup spec
- reCAPTCHA v2 support landed

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.6-alt1.2
- (NMU) rebuild with python3.6

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

