Name: python-module-pexpect
Version: 3.0
Release: alt1

%setup_python_module pexpect

Summary: Pexpect is a pure Python Expect. It allows easy control of other applications

License: Python Software Foundation License
Group: Development/Python
Url: http://pexpect.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pexpect.sourceforge.net/%modulename-%version.tar.gz

BuildArchitectures: noarch

Obsoletes: pexpect < 0.999-alt6
Provides: pexpect

# Automatically added by buildreq on Mon Dec 29 2008
BuildRequires: python-devel

BuildPreReq: python-module-sphinx-devel

%description
Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output. Pexpect works like
Don Libes' Expect. Pexpect allows your script to spawn a child application and
control it as if a human were typing commands.

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
%setup -n %modulename-%version

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build

%make -C doc pickle
%make -C doc html

%install
%python_install

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/pexpect/

%files
%doc DEVELOPERS LICENSE README.rst doc/_build/html examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%changelog
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

