%define oname Chaco

Name: python3-module-%oname
Version: 5.0.0
Release: alt1

Summary: Interactive 2-Dimensional Plotting
License: BSD and GPLv2
Group: Development/Python3
URL: http://code.enthought.com/projects/chaco/

# https://github.com/enthought/chaco.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-sphinx python3-module-Pygments
BuildRequires: python3-module-traits
BuildRequires: python3-module-Cython
BuildRequires: xvfb-run


%description
Chaco is a Python plotting application toolkit that facilitates writing
plotting applications at all levels of complexity, from simple scripts with
hard-coded data to large plotting programs with complex data interrelationships
and a multitude of interactive tools. While Chaco generates attractive static
plots for publication and presentation, it also works well for interactive data
visualization and exploration.

%package tests
Summary: Tests for Chaco (Interactive 2-Dimensional Plotting)
Group: Development/Python3
Requires: %name = %EVR

%description tests
Chaco is a Python plotting application toolkit that facilitates writing
plotting applications at all levels of complexity, from simple scripts with
hard-coded data to large plotting programs with complex data interrelationships
and a multitude of interactive tools. While Chaco generates attractive static
plots for publication and presentation, it also works well for interactive data
visualization and exploration.

This package contains tests for Chaco.

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

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install
%python3_prune
rm -rfv %buildroot%python3_sitelibdir/chaco/tests_with_backend/

export PYTHONPATH=%buildroot%python3_sitelibdir:$PWD/docs/source/sphinxext
xvfb-run sphinx-build-3 -E -a -b html -c docs/source -d doctrees docs/source html

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/example*
%if 0
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%files doc
%doc docs/*.txt docs/*.pdf
%doc examples html


%changelog
* Mon Oct 31 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Build new version.

* Thu Jun 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.8.0.0.91.git22972069-alt2
- Fixed build with new traits.

* Mon Feb 08 2021 Grigory Ustinov <grenka@altlinux.org> 4.8.0.0.91.git22972069-alt1
- Build from last commit for python3.9.

* Tue Dec 01 2020 Vitaly Lipatov <lav@altlinux.ru> 4.8.0-alt3
- NMU: drop tests packing

* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.8.0-alt2
- Fixed build with numpy.

* Wed Dec 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.8.0-alt1
- porting on python3

* Mon May 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.dev.git20150427
- New snapshot

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.dev.git20141105
- Version 4.6.0-dev

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20141029
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20140415
- Version 4.5.0

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20131020
- New snapshot

* Mon Jun 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20130422
- Rebuilt with updated NumPy

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130422
- Version 4.3.0

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20130128
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20120925
- Version 4.2.1

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

