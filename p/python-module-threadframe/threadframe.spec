%define oname threadframe
Name: python-module-%oname
Version: 0.2
Release: alt1.1.1
Summary: Advanced thread debugging extension
License: Python
Group: Development/Python
Url: http://pypi.python.org/pypi/threadframe/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%description
Obtaining tracebacks on other threads than the current thread.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.1
- Rebuild with Python-2.7

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

