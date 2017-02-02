%define oname libacl

%def_with python3

Name: python-module-%oname
Version: 0.5.3
Release: alt1

Summary: POSIX.1e ACLs for python
License: LGPLv2.1+
Group: Development/Python

URL: http://pylibacl.sourceforge.net/

#Source-url: https://pypi.io/packages/source/p/pylibacl/pylibacl-%version.tar.gz
# Source-git: https://github.com/iustin/pylibacl.git
Source: %name-%version.tar
Patch: libacl-0.5.2-alt-doc.patch

#BuildPreReq: libacl-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: libacl-devel python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-devel python3-module-setuptools rpm-build-python3 time

%description
python-libacl is a C extension module for Python which implements
POSIX ACLs manipulation. It is a wrapper on top of the systems's
acl C library - see acl(5).

%package -n python3-module-%oname
Summary: POSIX.1e ACLs for python
Group: Development/Python3

%description -n python3-module-%oname
python-libacl is a C extension module for Python which implements
POSIX ACLs manipulation. It is a wrapper on top of the systems's
acl C library - see acl(5).

%prep
%setup
%patch -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
%make doc

%files
%python_sitelibdir/*
%doc NEWS README doc/html

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%doc NEWS README doc/html
%endif

%changelog
* Thu Feb 02 2017 Vitaly Lipatov <lav@altlinux.ru> 0.5.3-alt1
- new version 0.5.3 (with rpmrb script)

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.2-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1.1
- NMU: Use buildreq for BR.

* Thu Aug 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Version 0.5.2
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt3.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt3
- Rebuilt for debuginfo

* Thu Aug 26 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.5.0-alt2
- fix buildreqs

* Sun Jul 11 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.5.0-alt1
- 0.5.0
- spec fixes

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.1
- Rebuilt with python 2.6

* Sat Apr 05 2008 Mikhail Pokidko <pma@altlinux.org> 0.2.1-alt1
- Initial ALT build

