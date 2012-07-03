%define version 1.0.3
%define release alt2.1
%setup_python_module recaptcha-client

Name: %packagename
Version:%version
Release: %release.1

Summary: Provides a CAPTCHA for Python using the reCAPTCHA service

License: MIT/X11
Group: Development/Python
BuildArch: noarch
Url: http://pyobject.ru/projects/pytils
Packager: Denis Klimov <zver@altlinux.org>

BuildRequires: python-module-setuptools

Source: %modulename-%version.tar


%description
Provides a CAPTCHA for Python using the reCAPTCHA service. Does not
require any imaging libraries because the CAPTCHA is served directly
from reCAPTCHA. Also allows you to securely obfuscate emails with
Mailhide.

%prep
%setup -n %modulename-%version

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt2.1.1
- Rebuild with Python-2.7

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt2.1
- Rebuilt with python 2.6

* Sun Feb 01 2009 Denis Klimov <zver@altlinux.org> 1.0.3-alt2
- more improve using setup_python_module macros
- use optimize and record options for install

* Fri Jan 30 2009 Denis Klimov <zver@altlinux.org> 1.0.3-alt1
- Initial build for ALT Linux

