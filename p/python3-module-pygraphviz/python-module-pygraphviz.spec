%define module_name pygraphviz

Name: python3-module-%module_name
Version: 1.10
Release: alt1

Summary: Python wrapper for the Graphviz Agraph data structure

License: BSD
Group: Development/Python3
Url: https://pygraphviz.github.io/

Packager: Denis Klimov <zver@altlinux.org>

# https://github.com/pygraphviz/pygraphviz.git
Source: %module_name-%version.tar

BuildRequires: libgraphviz-devel

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute

%description
Python wrapper for the Graphviz Agraph data structure.
It can be used to create and draw networks and graphs with Graphviz.

%prep
%setup -n %module_name-%version

%build
%add_optflags -I%_includedir/graphviz

%python3_build_debug

%install
%python3_install
%python3_prune
%__subst "s|from pygraphviz.tests.test import run as test||" %buildroot%python3_sitelibdir/pygraphviz/__init__.py

%files
%doc %_docdir/*
%python3_sitelibdir/pygraphviz/
%python3_sitelibdir/pygraphviz-*.egg-info

%changelog
* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt1
- new version 1.10 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt1
- new version 1.9 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- new version 1.7 (with rpmrb script)

* Sun Nov 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt5
- build python3 module (don't pack tests, fix tests depends)

* Thu Jul 11 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.5-alt3
- Fix ln options to change symlink

* Mon Feb 04 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.5-alt2
- Cleanup spec

* Wed Dec 26 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.5-alt1
- update to 1.5

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt2.git20140720.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt2.git20140720.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 1.3-alt2.git20140720
- Fix graphviz.i

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20140720
- Version 1.3

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.svn20120328
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.2-alt1.svn20120328.1
- Rebuild with Python-3.3

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20120328
- Version 1.2
- Extracted tests into separate package
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.99.1-alt1.3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.99.1-alt1.3.1
- Rebuild with Python-2.7

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 0.99.1-alt1.3
- NMU: rebuilt with current graphviz

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.1-alt1.2
- Rebuilt for debuginfo

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.1-alt1.1
- Rebuilt with python 2.6

* Thu Jan 22 2009 Denis Klimov <zver@altlinux.org> 0.99.1-alt1
- Initial build for ALT Linux

