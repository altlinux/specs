%define _unpackaged_files_terminate_build 1
%define oname pexpect

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 4.2.1
Release: alt1.1

%setup_python_module %oname

Summary: Pexpect is a pure Python Expect. It allows easy control of other applications

License: Python Software Foundation License
Group: Development/Python
Url: http://pexpect.sourceforge.net/

# https://github.com/pexpect/pexpect.git
Source0: https://pypi.python.org/packages/e8/13/d0b0599099d6cd23663043a2a0bb7c61e58c6ba359b2656e6fb000ef5b98/%{oname}-%{version}.tar.gz

BuildArch: noarch

Obsoletes: %oname < 0.999-alt6
Provides: %oname

%add_findreq_skiplist %python_sitelibdir/%oname/async.py

BuildPreReq: python-devel python-module-setuptools /dev/pts
BuildPreReq: python-module-pytest-cov python-module-ptyprocess
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-pytest-cov python3-module-ptyprocess
%endif

BuildPreReq: python-module-sphinx-devel

%description
Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output. Pexpect works like
Don Libes' Expect. Pexpect allows your script to spawn a child application and
control it as if a human were typing commands.

%package -n python3-module-%oname
Summary: Pexpect is a pure Python Expect. It allows easy control of other applications
Group: Development/Python3

%description -n python3-module-%oname
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
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
py.test -vv --cov pexpect --cov-config .coveragerc
%if_with python3
pushd ../python3
py.test-%_python3_version -vv --cov pexpect --cov-config .coveragerc
popd
%endif

%files
%doc LICENSE README.rst doc/_build/html examples PKG-INFO doc
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.rst doc/_build/html examples PKG-INFO doc
%python3_sitelibdir/*
%endif

%changelog
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

