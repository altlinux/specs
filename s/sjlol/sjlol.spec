Name: sjlol
Version: 1.1
Release: alt2.1.1
License: GPL
Packager: Pavlov Konstantin <thresh@altlinux.ru>
Group: Development/Python
Summary: LOLCODE Interpreter written in Python
Source0: %name-%version.tar.bz2
Url: http://lolcode.com/implementations/sjlol
BuildArch: noarch

BuildRequires: python-modules-compiler python-modules-encodings

%description
LOLCODE Interpreter written in Python.

%prep
%setup -q

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%python_sitelibdir

install sjlol.py %buildroot%_bindir/sjlol
install sjlol_*.py %buildroot%python_sitelibdir

%files
%_bindir/%name
%python_sitelibdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1.1
- Rebuild with Python-2.7

* Thu Nov 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2.1
- Rebuilt with python 2.6

* Mon Apr 20 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.1-alt2
- Make sisyphus_check less unhappy: place python files inside
  %%python_sitelibdir.

* Wed Jun 13 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.1-alt1
- Initial build for Sisyphus.

