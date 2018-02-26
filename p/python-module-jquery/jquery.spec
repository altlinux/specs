%define oname jquery
Name: python-module-%oname
Version: 1.2.3
Release: alt1.1
Summary: Jquery javascript library for TurboGears
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/jquery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-TurboGears2 python-module-markdown

%description
jquery is a jquery javascript library wrapper and ajax helper for happy
TurboGears web designers.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.3-alt1.1
- Rebuild with Python-2.7

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1
- Initial build for Sisyphus

