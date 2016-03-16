%define oname rfc822py3
Name: python3-module-%oname
Version: 20110416
Release: alt1.1.1
Summary: A port of the Python 2.x rfc822 library to Python3
License: Python
Group: Development/Python3
Url: https://github.com/MarkNenadov/rfc822py3
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/MarkNenadov/rfc822py3.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
rfc822py3 - A port of the Python 2.x rfc822 module into Python.

%prep
%setup

%install
install -d %buildroot%python3_sitelibdir
install -p -m644 *.py %buildroot%python3_sitelibdir

%files
%doc *.txt
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 20110416-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 20110416-alt1.1
- Rebuild with Python-3.3

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110416-alt1
- Initial build for Sisyphus

