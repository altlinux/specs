%define oname WebFlash

%def_with python3

Name: python-module-%oname
Version: 0.1a9
Release: alt1.2.1

Summary: WebFlash is a library to display "flash" messages in python web applications

License: MIT
Group: Development/Python
Url: http://python-rum.org/wiki/WebFlash

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%setup_python_module webflash

Source: http://pypi.python.org/packages/source/W/WebFlash/%oname-%version.tar

%description
WebFlash is a library to display "flash" messages in python web
applications. These messages are usually used to provide feedback to
the user (eg: you changes have been saved, your credit card number has
been stolen, ...). One important characteristic they must provide is the
ability to survive a redirect (ie: display the message in a page after
being redirected from a form submission).

%package -n python3-module-%oname
Summary: WebFlash is a library to display "flash" messages in python web applications
Group: Development/Python3

%description -n python3-module-%oname
WebFlash is a library to display "flash" messages in python web
applications. These messages are usually used to provide feedback to
the user (eg: you changes have been saved, your credit card number has
been stolen, ...). One important characteristic they must provide is the
ability to survive a redirect (ie: display the message in a page after
being redirected from a form submission).

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
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
%python_sitelibdir/%modulename/
%python_sitelibdir/%{oname}*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{oname}*.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1a9-alt1.2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1a9-alt1.2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1a9-alt1.1
- Rebuild with Python-2.7

* Tue Oct 05 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1a9-alt1
- initial build for ALT Linux Sisyphus

