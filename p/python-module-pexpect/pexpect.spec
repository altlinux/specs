%define _unpackaged_files_terminate_build 1
%define oname pexpect

%def_with check

Name: python-module-%oname
Version: 4.4
Release: alt1%ubt

Summary: Pexpect is a pure Python Expect. It allows easy control of other applications
License: Python Software Foundation License
Group: Development/Python
# Source-git: https://github.com/pexpect/pexpect.git
Url: https://pypi.python.org/pypi/pexpect

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-objects.inv
BuildRequires: python-module-setuptools
BuildRequires: python-module-ptyprocess
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-ptyprocess

%if_with check
BuildRequires: /dev/pts
BuildRequires: man-db
BuildRequires: openssl
BuildRequires: python-module-pytest
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch
Obsoletes: %oname < 0.999-alt6
Provides: %oname

%add_findreq_skiplist %python_sitelibdir/%oname/_async.py

%description
Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output. Pexpect works like
Don Libes' Expect. Pexpect allows your script to spawn a child application and
control it as if a human were typing commands.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Pexpect is a pure Python Expect. It allows easy control of other applications
Group: Development/Python3

%description -n python3-module-%oname
Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output. Pexpect works like
Don Libes' Expect. Pexpect allows your script to spawn a child application and
control it as if a human were typing commands.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package pickles
Summary: Pickles for Pexpect
Group: Development/Python

%description pickles
Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output. Pexpect works like
Don Libes' Expect. Pexpect allows your script to spawn a child application and
control it as if a human were typing commands.

This package contains pickles for Pexpect.

%prep
%setup
%patch0 -p1

rm -rf ../python3
cp -a . ../python3

pushd ../python3
# change shebang python -> python3
find -type f -name '*.py' | \
	xargs sed -i '1s|#!/usr/bin/env python|#!/usr/bin/env python3|'
xargs sed -i '1s|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	tests/fakessh/ssh

# fix print functions and other for python3
find tests -type f -name '*.py' -exec 2to3 -f print -f imports -w -n '{}' +

# change python -> python3 calls
find tests -type f -name '*.py' | \
	xargs sed -i 's/\(.*pexpect.spawn(\x27python\)\(\(\x27\| \)\)/\13\2/'
sed -i 's|self.runfunc(\x27python exit1.py\x27|self.runfunc(\x27python3 exit1.py\x27|' \
	tests/test_run.py
popd

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
cp -fR tests %buildroot%python_sitelibdir/%oname/

pushd ../python3
%python3_install
cp -fR tests %buildroot%python3_sitelibdir/%oname/
popd

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL="en_US.UTF-8"

py.test -v

pushd ../python3
py.test3 -v
popd

%files
%doc LICENSE *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files docs
%doc doc/_build/html
%doc examples

%files pickles
%python_sitelibdir/*/pickle

%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%changelog
* Wed Mar 21 2018 Stanislav Levin <slev@altlinux.org> 4.4-alt1%ubt
- 4.2.1 -> 4.4.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0-alt1.dev.git20150811.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.dev.git20150811
- Version 4.0.dev

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt1
- Version 3.3
- Added module for Python 3

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Version 3.0

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1.1
- Rebuilt with python 2.6

* Mon Dec 29 2008 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt1
- new version 2.3 (with rpmrb script)
- cleanup spec

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.999-alt8.1
- Rebuilt with python-2.5.

* Wed Apr 20 2005 Andrey Orlov <cray@altlinux.ru> 0.999-alt8
- Documentation and examples added

* Sat Jul 03 2004 Andrey Orlov <cray@altlinux.ru> 0.999-alt7
- Provide pexpect clause added

* Thu May 20 2004 Andrey Orlov <cray@altlinux.ru> 0.999-alt6
- Previous packages are obsoleted

* Tue May 18 2004 Andrey Orlov <cray@altlinux.ru> 0.999-alt5
- Conditional operators excluded from spec

* Mon May 10 2004 Andrey Orlov <cray@altlinux.ru> 0.999-alt4.d
- Rebuild

* Thu Apr 22 2004 Andrey Orlov <cray@altlinux.ru> 0.999-alt3.d
- BuildNoArch clause added

* Tue Apr 13 2004 Andrey Orlov <cray@altlinux.ru> 0.999-alt2.d
- Rebuild with new rpm/python macros
- Fix description field omited before

* Mon Mar 29 2004 Andrey Orlov <cray@altlinux.ru> 0.999-alt1.d
- Initial release

