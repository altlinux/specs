%define version 0.9.6
%define release alt1.1
%setup_python_module kid

Name: %packagename
Version:%version
Release: %release.1

Summary: Template language for XML

License: MIT/X11
Group: Development/Python
BuildArch: noarch
Url: http://www.kid-templating.org/
Packager: Denis Klimov <zver@altlinux.org>

Source: %modulename-%version.tar

BuildRequires: python-module-setuptools

%description
Kid is a simple template language for XML based vocabularies written
in Python. It was spawned as a result of a kinky love triangle between
XSLT, TAL, and PHP. We believe many of the best features of these
languages live on in Kid with much of the limitations and complexity
stamped out (see WhatsBorrowed and WhatsDifferent). For more info on
current and planned features and licensing information, see AboutKid.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename
%python_sitelibdir/%modulename-*.egg-info
%_bindir/kid
%_bindir/kidc

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.6-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt1.1
- Rebuilt with python 2.6

* Sun Mar 29 2009 Denis Klimov <zver@altlinux.org> 0.9.6-alt1
- Initial build for ALT Linux

