%define oname pyxattr
%define fname python-module-%oname
%define descr \
This is the pyxattr module, a Python extension module which gives access \
to the extended attributes for filesystem objects available in some \
operating systems.

Name: %fname-docs
Version: 0.5.3
Release: alt4

%if "-docs"==""
Summary: A python module for accessing filesystem Extended Attributes
Group: Development/Python
%else
Summary: Documentation for %oname
Group: Development/Documentation
%endif

License: LGPLv2.1
Url: http://pyxattr.sourceforge.net/
# https://github.com/iustin/pyxattr.git
Source: %name-%version.tar

BuildPreReq: libattr-devel python-module-sphinx-devel python-devel
BuildRequires(pre): rpm-build-python

%if "-docs"!=""
Conflicts: %fname < %EVR
Conflicts: %fname > %EVR
%endif

%description
%descr
%if "-docs"!=""

This package contains documentation for %oname.
%endif

%prep
%setup
%if "-docs"!=""
%prepare_sphinx .
ln -s ../objects.inv doc/
%endif

%build
%if "-docs"==""
%python_build
%else
export PYTHONPATH=%buildroot%python_sitelibdir
%make doc
%endif

%install
%python_install

%if "-docs"==""

%files
%python_sitelibdir/*
%doc NEWS README

%else

%files
%doc doc/*
%python_sitelibdir/*.egg-info*

%endif

%changelog
* Tue Apr 10 2018 Grigory Ustinov <grenka@altlinux.org> 0.5.3-alt4
- Tranfer package to subst-packaging system.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.3-alt3.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.3-alt3.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Feb 25 2016 Denis Medvedev <nbr@altlinux.org> 0.5.3-alt3
- removed ENOATTR from code.

* Thu Feb 25 2016 Denis Medvedev <nbr@altlinux.org> 0.5.3-alt2
- Fix includes. Bug in includes.

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1
- Version 0.5.3
- Added module for Python 3

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Version 0.5.2

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt1.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt1.1.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.1
- Rebuilt for debuginfo

* Sun Jul 11 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.5.0-alt1
- 0.5.0
- spec fixes

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt2
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 0.2.1-alt1.1
- Rebuilt with python-2.5.

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux Sisyphus
