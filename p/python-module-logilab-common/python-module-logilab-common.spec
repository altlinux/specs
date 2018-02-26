%def_enable check
%def_with python3

%define oname logilab-common
Name: python-module-%oname
Version: 0.58.0
Release: alt2.hg20120417

Summary: Useful miscellaneous modules used by Logilab projects
License: LGPLv2.1+
Group: Development/Python

BuildArch: noarch

Url: http://www.logilab.org/project/logilab-common
Source: %name-%version.tar

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%py_requires mx.DateTime
%add_python_req_skip mercurial sphinx

%setup_python_module %oname

%{?!_without_check:%{?!_disable_check:BuildRequires: /proc %py_dependencies mx.DateTime unittest2}}
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
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
%add_python3_req_skip kerberos mercurial sphinx

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
cp -a . ../python3
%endif

%build
rm corbautils.py
%python_build
%if_with python3
pushd ../python3
rm corbautils.py
for i in $(find ./ -name '*.py'); do
	sed -i 's|unittest2|unittest|g' $i
	if [ "$i" != "./setup.py" ]; then
		2to3 -w -n $i
	fi
done
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
rm -rf %buildroot%python3_sitelibdir/logilab/common/test
mv %buildroot%_bindir/pytest %buildroot%_bindir/pytest3
%endif

%python_install
install -pD -m644 doc/pytest.1 %buildroot%_man1dir/pytest.1
rm -rf %buildroot%python_sitelibdir/logilab/common/test

%check
touch build/lib/logilab/__init__.py
PYTHONPATH=$(pwd)/build/lib/ \
    $(pwd)/build/scripts-%_python_version/pytest \
    -t test \
    -s test_knownValues_is_standard_module_4
rm -f build/lib/logilab/__init__.py

%files
%_bindir/pytest
%python_sitelibdir/logilab/
%python_sitelibdir/*.egg-info
%_man1dir/*
%doc ChangeLog README

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README
%_bindir/pytest3
%python3_sitelibdir/logilab/
%python3_sitelibdir/*.egg-info
%endif

%changelog
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
