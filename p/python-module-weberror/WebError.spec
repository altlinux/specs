%define oname weberror
Name: python-module-%oname
Version: 0.10.3
Release: alt1.1
Summary: Web Error handling and exception catching
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/WebError
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

Source: WebError-%version.tar.gz

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-setuptools

%description
Web Error handling and exception catching.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc CHANGELOG LICENSE
%python_sitelibdir/*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10.3-alt1.1
- Rebuild with Python-2.7

* Fri Nov 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3-alt1
- Version 0.10.3

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1
- Version 0.10.2

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt2
- Rebuilt with python 2.6

* Tue Sep 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1
- Initial build for Sisyphus

