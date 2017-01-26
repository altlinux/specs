%def_enable check
%def_with python3

%define oname logilab-common
Name: python-module-%oname
Version: 1.0.2
Release: alt2.hg20150708

Summary: Useful miscellaneous modules used by Logilab projects
License: LGPLv2.1+
Group: Development/Python

Url: http://www.logilab.org/project/logilab-common
Packager: Python Development Team <python@packages.altlinux.org>

# Do not install /usr/bin/pytest from there
# and use it instead of ours quietly;
# an explicit "Requires: pytest" is needed.
Conflicts: python-module-pytest = 3.0.5-alt1

BuildArch: noarch

# hg clone http://hg.logilab.org/review/logilab/common/
Source: %name-%version.tar

%py_requires mx.DateTime
%add_python_req_skip mercurial sphinx

%setup_python_module %oname

%{?!_without_check:%{?!_disable_check:BuildRequires: /proc %py_dependencies mx.DateTime unittest2}}
#BuildPreReq: python-module-six python-module-pytz
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-module-six python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base xz
BuildRequires: python-module-egenix-mx-base python-module-pytz python-module-unittest2 python3-module-pytz python3-module-setuptools python3-module-six rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
#BuildPreReq: python3-module-six python3-module-pytz
%endif

%description
logilab-common is a collection of low-level Python packages and modules,
designed to ease:
  * handling command line options and configuration files
  * writing interactive command line tools
  * manipulation files and character strings
  * interfacing to OmniORB (removed by packager)
  * generating of SQL queries
  * running unit tests
  * manipulating tree structures
  * accessing RDBMS (currently postgreSQL, mysql and sqlite)
  * generating text and HTML reports
  * logging

%if_with python3
%package -n python3-module-%oname
Summary: Useful miscellaneous modules used by Logilab projects (Python 3)
Group: Development/Python3
# Do not install /usr/bin/pytest3 from there
# and use it instead of ours quietly;
# an explicit "Requires: pytest3" is needed.
Conflicts: python-module-pytest = 3.0.5-alt1
%add_python3_req_skip kerberos mercurial sphinx
%add_python3_req_skip six.moves
%py3_requires six

%description -n python3-module-%oname
logilab-common is a collection of low-level Python packages and modules,
designed to ease:
  * handling command line options and configuration files
  * writing interactive command line tools
  * manipulation files and character strings
  * interfacing to OmniORB (removed by packager)
  * generating of SQL queries
  * running unit tests
  * manipulating tree structures
  * accessing RDBMS (currently postgreSQL, mysql and sqlite)
  * generating text and HTML reports
  * logging
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . -T ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
cp setup.py -T setup.py.back
find -type f -name '*.py' -exec sed -i 's|unittest2|unittest|g' -- '{}' +
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
mv -f setup.py.back -T setup.py
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
install -p -m644 logilab/__init__.py \
	-t %buildroot%python3_sitelibdir/logilab/
install -pD -m644 doc/pytest.1 -T %buildroot%_man1dir/pytest3_logilab-common.1
popd
mv %buildroot%_bindir/pytest -T %buildroot%_bindir/pytest3_logilab-common
%endif

%python_install
install -p -m644 logilab/__init__.py \
	-t %buildroot%python_sitelibdir/logilab/
install -pD -m644 doc/pytest.1 -T %buildroot%_man1dir/pytest_logilab-common.1
mv %buildroot%_bindir/pytest -T %buildroot%_bindir/pytest_logilab-common

%check
PYTHONPATH=%buildroot%python_sitelibdir \
    %buildroot%_bindir/pytest_logilab-common \
    -t test \
    -s test_4
%if_with python3
pushd ../python3
PYTHONPATH=%buildroot%python3_sitelibdir \
    %buildroot%_bindir/pytest3_logilab-common \
    -t test \
    -s test_4
popd
%endif

%global _unpackaged_files_terminate_build 1
%files
%_bindir/pytest_logilab-common
%python_sitelibdir/logilab/
%python_sitelibdir/*.egg-info
%python_sitelibdir/*.pth
%_man1dir/pytest_*
%doc ChangeLog README

%if_with python3
%files -n python3-module-%oname
%_bindir/pytest3_logilab-common
%python3_sitelibdir/logilab/
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*.pth
%_man1dir/pytest3_*
%doc ChangeLog README
%endif

%changelog
* Thu Jan 26 2017 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt2.hg20150708
- Rename /usr/bin/pytest{,3} to avoid collision with pytest{,3}-3.0.5
  (ALT#33028).
- Package *.pth files for modifying the Python path for the
  namespace pkg.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.hg20150708.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1.hg20150708.1
- NMU: Use buildreq for BR.

* Thu Aug 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.hg20150708
- Version 1.0.2

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.63.2-alt1.hg20141130
- Version 0.63.2

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.63.0-alt1.hg20141105
- Version 0.63.0

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.62.0-alt1.hg20140716
- Version 0.62.0

* Wed Mar 19 2014 Timur Aitov <timonbl4@altlinux.org> 0.61.0-alt1.hg20140211
- Version 0.61.0

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.59.0-alt2.hg20130215
- Use 'find... -exec...' instead of 'for ... $(find...'

* Thu Feb 28 2013 Aleksey Avdeev <solo@altlinux.ru> 0.59.0-alt1.hg20130215
- Version 0.59.0

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.58.0-alt2.hg20120417
- Added module for Python 3

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.58.0-alt1.hg20120417
- Version 0.58.0

* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.57.1-alt1
- Version 0.57.1

* Sun Oct 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.52.0-alt1.1
- Rebuild with Python-2.7

* Tue Sep 28 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.52.0-alt1
- 0.52.0
- skip test_knownValues_is_standard_module_4 test because
  logilab.common.modutils.is_standard_module is fundamentally broken on
  our x86_64 (see #24144)

* Mon Sep 13 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.51.1-alt1
- 0.51.1

* Sat Aug 28 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.51.0-alt1
- 0.51.0
- run tests

* Sun Jun 13 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.50.3-alt1
- 0.50.3

* Fri May 14 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.50.1-alt2
- build from hg

* Mon May 03 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.50.1-alt1
- 0.50.1

* Fri Mar 19 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.49.0-alt1
- 0.49.0

* Fri Feb 26 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.48.0-alt1
- 0.48.0

* Fri Dec 18 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.45.2-alt1
- 0.45.2

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.45.0-alt1.1
- Rebuilt with python 2.6

* Fri Sep 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.45.0-alt1
- 0.45.0

* Thu Aug 20 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.44.0-alt1
- 0.44.0

* Thu Mar 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.39.0-alt1
- 0.39.0

* Fri Mar 06 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.38.1-alt1
- 0.38.1

* Sun Feb 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.38.0-alt2
- use %%python_{build,install}

* Wed Jan 28 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.38.0-alt1
- 0.38.0

* Sat Dec 13 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.37.0-alt1
- 0.37.0

* Sat Nov 15 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.36.1-alt1
- 0.36.1

* Sun Nov 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.36.0-alt1
- 0.36.0

* Sun Oct 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.35.2-alt1
- 0.35.2
- spec cleanup
- package logilab/__init__.py, fixing imports and automatic dependency
  search (closes: #17532)
- don't package tests

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.21.0-alt1.1
- Rebuilt with python-2.5.

* Wed Dec 6 2006 Andrey Khavryuchenko <akhavr@altlinux.org> 0.21.0-alt1
- Initial build for ALT Linux
