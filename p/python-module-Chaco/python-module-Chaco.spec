%define oname Chaco
Name: python-module-%oname
Version: 4.1.1
Release: alt1.git20120508
Summary: Interactive 2-Dimensional Plotting

Group: Development/Python
License: BSD and GPLv2
URL: http://code.enthought.com/projects/chaco/
# https://github.com/enthought/chaco.git
Source: %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-devel, python-module-setuptools
#BuildPreReq: libnumpy-devel python-module-traits python-module-Enable
BuildPreReq: libnumpy-devel
BuildPreReq: python-module-sphinx python-module-Pygments

%description
Chaco is a Python plotting application toolkit that facilitates writing
plotting applications at all levels of complexity, from simple scripts with
hard-coded data to large plotting programs with complex data interrelationships
and a multitude of interactive tools. While Chaco generates attractive static
plots for publication and presentation, it also works well for interactive data
visualization and exploration.

%package doc
Summary: Documentation for Chaco (Interactive 2-Dimensional Plotting)
Group: Development/Documentation
BuildArch: noarch

%description doc
Chaco is a Python plotting application toolkit that facilitates writing
plotting applications at all levels of complexity, from simple scripts with
hard-coded data to large plotting programs with complex data interrelationships
and a multitude of interactive tools. While Chaco generates attractive static
plots for publication and presentation, it also works well for interactive data
visualization and exploration.

This package contains documentation for Chaco.

%prep
%setup

%build
%python_build_debug

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir:$PWD/docs/source/sphinxext
sphinx-build -E -a -b html -c docs/source -d doctrees docs/source html

%files
%doc *.txt
%python_sitelibdir/*

%files doc
%doc docs/*.txt docs/*.pdf docs/*.tgz docs/chaco* docs/scipy_tutorial
%doc examples html

%changelog
* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120508
- New snapshot

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.1-alt1.git20120119.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120119
- Version 4.1.1

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.git20111107
- Version 4.1.0

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt1.svn20110127.2
- Rebuild with Python-2.7

* Mon Oct 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20110127.1
- Rebuilt with updated NumPy

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20110127
- Version 3.4.1

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20101120.2
- Rebuilt with NumPy 2.0.0-alt2.git20110405.4

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20101120.1
- Rebuilt for debuginfo

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20101120
- Version 3.3.3

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.2-alt1.svn20100706
- Version 3.3.2

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20091001.1
- Rebuilt with python 2.6

* Wed Oct 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20091001
- Initial build for Sisyphus

