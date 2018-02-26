Name: python-module-CodeTools
Version: 4.0.1
Release: alt1.git20120221
Summary: Code Analysis and Execution Tools

Group:          Development/Python
License: BSD and GPLv2
URL: http://enthought.com/
# https://github.com/enthought/codetools.git
Source: CodeTools-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildArch:      noarch
BuildRequires:  python-devel, python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-Pygments

%description
The CodeTools project includes packages that simplify meta-programming
and help the programmer separate data from code in Python. This library
contains classes that allow defining simple snippets, or "blocks", of
Python code, analyze variable dependencies in the code block, and use
these dependencies to construct or restrict an execution graph. These
(restricted) code blocks can then be executed in any namespace. However,
this project also provides a Traits-event-enhanced namespace, called a
"context", which can be used in place of a vanilla namespace to allow
actions to be performed whenever variables are assigned or retrieved
from the namespace. This project is used as the foundation for the
BlockCanvas project.

%package tests
Summary: Tests for CodeTools
Group: Development/Python
Requires: %name = %version-%release

%description tests
The CodeTools project includes packages that simplify meta-programming
and help the programmer separate data from code in Python. This library
contains classes that allow defining simple snippets, or "blocks", of
Python code, analyze variable dependencies in the code block, and use
these dependencies to construct or restrict an execution graph. These
(restricted) code blocks can then be executed in any namespace. However,
this project also provides a Traits-event-enhanced namespace, called a
"context", which can be used in place of a vanilla namespace to allow
actions to be performed whenever variables are assigned or retrieved
from the namespace. This project is used as the foundation for the
BlockCanvas project.

This package contains tests for CodeTools.

%prep
%setup

%prepare_sphinx .
ln -s ../../objects.inv docs/source/

%build
%python_build

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
sphinx-build -E -a -b html -c docs/source -d doctrees docs/source html

%files
%doc *.txt examples html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%changelog
* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20120221
- New snapshot

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20110622
- Version 4.0.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.1-alt1.svn20110127.1
- Rebuild with Python-2.7

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20110127
- Version 3.2.1

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1.svn20101117.1
- Rebuilt with python-module-sphinx-devel

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1.svn20101117
- Version 3.1.3

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1.svn20100627.1
- Extracted tests into separate package

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1.svn20100627
- Version 3.1.2

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.svn20090812.1
- Rebuilt with python 2.6

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.svn20090812
- Initial build for Sisyphus

