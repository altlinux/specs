%define oname WebFlash
Name: python-module-%oname
Version: 0.1a9
Release: alt1.1

Summary: WebFlash is a library to display "flash" messages in python web applications

License: MIT
Group: Development/Python
Url: http://python-rum.org/wiki/WebFlash

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: python-module-setuptools

%setup_python_module webflash

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

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/%{oname}*.egg-info

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1a9-alt1.1
- Rebuild with Python-2.7

* Tue Oct 05 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1a9-alt1
- initial build for ALT Linux Sisyphus

