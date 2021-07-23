%define _unpackaged_files_terminate_build 1
%define oname pycmd

Name: python3-module-%oname
Version: 1.2
Release: alt3

Summary: Command line tools for helping with Python development
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pycmd/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# pycmd was separated from pylib at that point
Conflicts: py < 1.4.0
BuildArch: noarch

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
Collection of command line tools for dealing with python files
(locating, counting LOCs, cleaning up pyc files ...)

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	%oname/*.py

%build
%python3_build

%install
%python3_install

%files
%doc CHANGELOG LICENSE *.txt
%_bindir/py.cleanup
%_bindir/py.convert_unittest
%_bindir/py.countloc
%_bindir/py.lookup
%_bindir/py.svnwcrevert
%_bindir/py.which
%python3_sitelibdir/pycmd/
%python3_sitelibdir/pycmd-*.egg-info/

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.2-alt3
- Drop python2 support.

* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 1.2-alt2
- Add Requires on python py.

* Fri Apr 13 2018 Stanislav Levin <slev@altlinux.org> 1.2-alt1
- 1.1 -> 1.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.hg20140627.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1-alt1.hg20140627.1
- NMU: Use buildreq for BR.

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.hg20140627
- Version 1.1
- Added module for Python 3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.a2dev1-alt1.hg20130918
- New snapshot

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.a2dev1-alt1.hg20121007
- Version 1.0.a2dev1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.hg20101129.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20101129
- New snapshot

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20101108.1
- Added explicit conflict with py

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20101108
- Initial build for Sisyphus

