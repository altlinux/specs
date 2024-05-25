%define oname libacl

Name: python3-module-%oname
Version: 0.7.0
Release: alt1

Summary: POSIX.1e ACLs for python
License: LGPLv2.1+
Group: Development/Python3

URL: https://pypi.org/project/pylibacl
VCS: https://github.com/iustin/pylibacl

Source: %name-%version.tar
Patch: libacl-0.5.2-alt-doc.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: libacl-devel
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-recommonmark

%description
python-libacl is a C extension module for Python which implements
POSIX ACLs manipulation. It is a wrapper on top of the systems's
acl C library - see acl(5).

%prep
%setup
%patch -p1

# Fix shebang
sed -i "s/\(env python\)/\13/" setup.py

%prepare_sphinx3 .
ln -s ../objects.inv doc/

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make SPHINXBUILD="sphinx-build-3" doc

%files
%doc *.md doc/html
%python3_sitelibdir/posix1e.cpython-*.so
%python3_sitelibdir/pylibacl-%version.dist-info

%changelog
* Sat May 25 2024 Grigory Ustinov <grenka@altlinux.org> 0.7.0-alt1
- Automatically updated to 0.7.0.

* Mon Dec 12 2022 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt1
- Build new version.

* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 0.5.3-alt2
- Drop python2 support.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.3-alt1.1
- (NMU) Rebuilt with python-3.6.4.

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

