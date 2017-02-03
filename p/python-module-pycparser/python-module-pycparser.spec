%define modulename pycparser
%def_with python3

Name: python-module-pycparser
Version: 2.14
Release: alt1.1.1

Summary: C parser in Python

Group: Development/Python
License: BSD
Url: http://pypi.python.org/pypi/%modulename/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/p/%modulename/%modulename-%version.tar

%setup_python_module %modulename

BuildArch: noarch

# Automatically added by buildreq on Mon Apr 08 2013
# optimized out: python-base python-devel python-module-distribute python-module-peak python-module-zope python-modules python-modules-compiler python-modules-email
BuildRequires: python-module-paste
%{?!_with_bootstrap:BuildRequires: python-module-mwlib}
%if_with python3
BuildRequires(pre): rpm-build-python3
%endif

%description
pycparser is a complete parser of the C language, written in pure Python
using the PLY parsing library.
It parses C code into an AST and can serve as a front-end for C compilers or analysis tools.

%if_with python3
%package -n python3-module-%modulename
Summary: C parser in Python
Group: Development/Python3

%description -n python3-module-%modulename
pycparser is a complete parser of the C language, written in pure Python
using the PLY parsing library.
It parses C code into an AST and can serve as a front-end for C compilers or analysis tools.
%endif

%prep
%setup -n %modulename-%version

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

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

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/%modulename-%version-*.egg-info

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version-*.egg-info
%endif

%changelog
* Fri Feb 03 2017 Michael Shigorin <mike@altlinux.org> 2.14-alt1.1.1
- BOOTSTRAP: avoid python-module-mwlib -> gevent -> greenlet (!e2k)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.14-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14-alt1
- Version 2.14

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12-alt1
- Version 2.12

* Tue Jul 29 2014 Vladimir Didenko <cow@altlinux.org> 2.10-alt1
- 2.10
- add python3 version

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 2.09.1-alt1
- initial build for ALT Linux Sisyphus
