%define _unpackaged_files_terminate_build 1
%define oname zope.filerepresentation

%def_with check

Name: python3-module-%oname
Version: 6.0
Release: alt1

Summary: File-system Representation Interfaces
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.filerepresentation/
VCS: https://github.com/zopefoundation/zope.filerepresentation

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-zope.schema
BuildRequires: python3-module-zope.testrunner
%endif

%description
File-system representation interfaces.

The interfaces defined here are used for file-system and
file-system-like representations of objects, such as file-system
synchronization, FTP, PUT, and WebDAV.

%prep
%setup

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%check
%tox_check

%files
%doc *.txt *.rst
%python3_sitelibdir/zope/filerepresentation/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zope/filerepresentation/tests.py
%exclude %python3_sitelibdir/zope/filerepresentation/__pycache__/tests.*

%changelog
* Mon Mar 20 2023 Anton Vyatkin <toni@altlinux.org> 6.0-alt1
- New version 6.0.

* Wed Mar 30 2022 Stanislav Levin <slev@altlinux.org> 5.0.0-alt1
- 4.2.0 -> 5.0.0.

* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.2.0-alt1
- version updated to 4.2.0
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1.dev0.git20150228.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150228.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150228.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150228
- Version 4.1.1.dev0
- Enabled check

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

