Name: python3-module-recaptcha-client
Version: 2.0.1
Release: alt2

Summary: Python module for working with Google's reCAPTCHA v1 and v2

License: MIT/X11
Group: Development/Python3
BuildArch: noarch
Url: https://github.com/redhat-infosec/python-recaptcha

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-tools-2to3

# Source-url: https://github.com/redhat-infosec/python-recaptcha/archive/v%version.tar.gz
Source: %name-%version.tar

%py3_requires Crypto

%description
Provides a CAPTCHA for Python using the reCAPTCHA service. Does not
require any imaging libraries because the CAPTCHA is served directly
from reCAPTCHA. Also allows you to securely obfuscate emails with
Mailhide.

This Python module brings in Google's reCAPTCHA v1 and v2 support.
Although v1 is being deactivated starting from the 31st of March 2018
it's kept around for backwards compatibility and it's still marked as the default library option.

%prep
%setup
find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Thu May 27 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt2
- Drop python2 support.

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

