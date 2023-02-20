%define _unpackaged_files_terminate_build 1
%def_disable check

%define oname networkx

Name:           python3-module-%oname
Epoch:          2
Version:        2.8.8
Release:        alt1
Summary:        Creates and Manipulates Graphs and Networks
Group:          Development/Python3
License:        BSD-3-Clause
URL:            http://networkx.github.io

BuildArch:      noarch

# https://github.com/networkx/networkx.git
Source:         %name-%version.tar

Patch1:         %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-decorator >= 4.3.0
BuildRequires: python3-module-yaml >= 5.3
BuildRequires: python3-module-lxml >= 4.5
BuildRequires: python3-module-gdal >= 1.10.0
%if_enabled check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-pandas-tests
%endif

Requires: %name-drawing = %EVR

%description
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%package core
Summary: Creates and Manipulates Graphs and Networks (Python 3)
Group: Development/Python3
Requires: python3-module-decorator
Requires: python3-module-yaml
%add_python3_req_skip tests
%add_python3_req_skip networkx.tests.test

%description core
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%package drawing
Summary: Creates and Manipulates Graphs and Networks (Python 3)
Group: Development/Python3
Requires: %name-core = %EVR
Requires: python3-module-pygraphviz >= 1.5
Requires: python3-module-pygraphviz < 2.0
Requires: python3-module-pydot >= 1.4.1
Requires: python3-module-matplotlib >= 3.2

%description drawing
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

This package provides support for graph visualizations.

%package tests
Summary: Tests for NetworkX (Python 3)
Group: Development/Python3
Requires: %name = %EVR

%description tests
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

This package contains tests for NetworkX.

%prep
%setup
%patch1 -p1

find -type f -name '*.py' -exec sed -i \
	's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +

%build
%python3_build

%install
%python3_install

rm -rf %buildroot%_defaultdocdir

%check
py.test3 --durations=10 --pyargs networkx

%files

%files core
%doc LICENSE.txt
%doc README.rst CODE_OF_CONDUCT.rst CONTRIBUTING.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info
%exclude %python3_sitelibdir/%oname/drawing
%exclude %python3_sitelibdir/%oname/readwrite/nx_shp.py
%exclude %python3_sitelibdir/%oname/readwrite/__pycache__/nx_shp.*
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/conftest.py
%exclude %python3_sitelibdir/%oname/__pycache__/conftest.*
%exclude %python3_sitelibdir/%oname/testing
%exclude %python3_sitelibdir/%oname/*/tests
%exclude %python3_sitelibdir/%oname/*/*/tests

%files drawing
%python3_sitelibdir/%oname/drawing
%python3_sitelibdir/%oname/readwrite/nx_shp.py
%python3_sitelibdir/%oname/readwrite/__pycache__/nx_shp.*
%exclude %python3_sitelibdir/%oname/drawing/tests

%files tests
%python3_sitelibdir/%oname/conftest.py
%python3_sitelibdir/%oname/__pycache__/conftest.*
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/testing
%python3_sitelibdir/%oname/*/tests
%python3_sitelibdir/%oname/*/*/tests

%changelog
* Sat Dec 03 2022 Anton Farygin <rider@altlinux.ru> 2:2.8.8-alt1
- 2.6.3 -> 2.8.8

* Tue Feb 15 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 2:2.6.3-alt1
- Updated to upstream version 2.6.3.

* Tue Aug 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2:2.6.2-alt1
- Updated to upstream version 2.6.2.

* Tue Jul 13 2021 Vitaly Lipatov <lav@altlinux.ru> 2:2.5.1-alt2
- make scipy and numpy optional
- update requires
- drop pytest require from core package

* Tue Jun 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2:2.5.1-alt1
- Updated to upstream version 2.5.1.
- Fixed license.
- Cleaned up spec.

* Mon Jan 18 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2:2.5-alt1
- Updated to upstream version 2.5.
- Removed dependency from python3-module-networkx-core
  to python3-module-networkx-drawing (Closes: 39559).

* Mon Aug 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2:2.4-alt1
- Updated to upstream version 2.4.
- Disabled build for python-2.

* Thu Jun 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2:2.2-alt3
- Fixed dependencies of core modules.

* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2:2.2-alt2
- drop panda buildrequire

* Mon Dec 24 2018 Alexey Shabalin <shaba@altlinux.org> 2:2.2-alt1
- 2.2

* Wed Oct 26 2016 Alexey Shabalin <shaba@altlinux.ru> 2:1.11-alt2
- update recuires pydot -> pydotplus

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1:1.11-alt1
- 1.11

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.10-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:1.10-alt2.1
- NMU: Use buildreq for BR.

* Wed Nov 11 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.10-alt2
- fixed import optional modules

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.10-alt1
- 1.10

* Mon Oct 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.9.1-alt1
- downgrade to 1.9.1 release

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20150205
- New snapshot

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20140713
- Version 2.0

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1.git20131127
- New snapshot

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1.git20130915
- Version 1.9

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt3.git20130303
- Use 'find... -exec...' instead of 'for ... $(find...'

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt2.git20130303
- New snapshot

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.8-alt1.hg20120708.1
- Rebuild with Python-3.3

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1.hg20120708
- Version 1.8
- Added module for Python 3
- Disabled docs

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.hg20111126
- Version 1.7

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt2.svn20100829
- Enabled docs (except pdf)

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4-alt1.svn20100829.2.1
- Rebuild with Python-2.7

* Mon Apr 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.svn20100829.2
- Fixed build

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.svn20100829.1
- Rebuilt with python-module-sphinx-devel

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.svn20100829
- Version 1.4

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20100505
- Version 1.2

* Sun Mar 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.svn20100306.1
- Added docs and pickles packages

* Sun Mar 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.svn20100306
- Version 1.1
- Exatracted tests into separate package

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20091004.1
- Rebuilt with python 2.6

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20091004
- Initial build for Sisyphus

* Tue Mar 24 2009 Conrad Meyer <konrad@tylerc.org> - 0.99-3
- Replace __python macros with direct python invocations.
- Disable checks for now.
- Replace a define with global.

* Thu Mar 12 2009 Conrad Meyer <konrad@tylerc.org> - 0.99-2
- License is really LGPLv2+.
- Include license as documentation.
- Add a check section to run tests.

* Sat Dec 13 2008 Conrad Meyer <konrad@tylerc.org> - 0.99-1
- Initial package.
