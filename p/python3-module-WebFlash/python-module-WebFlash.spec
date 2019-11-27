%define oname WebFlash

Name: python3-module-%oname
Version: 0.1a9
Release: alt2

Summary: WebFlash is a library to display "flash" messages in python web applications
License: MIT
Group: Development/Python3
Url: http://python-rum.org/wiki/WebFlash
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

Source: http://pypi.python.org/packages/source/W/WebFlash/%oname-%version.tar


%description
WebFlash is a library to display "flash" messages in python web
applications. These messages are usually used to provide feedback to
the user (eg: you changes have been saved, your credit card number has
been stolen, ...). One important characteristic they must provide is the
ability to survive a redirect (ie: display the message in a page after
being redirected from a form submission).

%prep
%setup -n %oname-%version

sed -i 's|from urllib|&.parse|' webflash/__init__.py

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/webflash/__pycache__/
%python3_sitelibdir/webflash/*


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1a9-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1a9-alt1.2.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1a9-alt1.2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1a9-alt1.2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1a9-alt1.1
- Rebuild with Python-2.7

* Tue Oct 05 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1a9-alt1
- initial build for ALT Linux Sisyphus

