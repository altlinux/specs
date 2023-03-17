%define oname flup

Name: python3-module-%oname
Version: 1.0.3
Release: alt4

Summary: Random assortment of WSGI servers
License: BSD
Group: Development/Python3
URL: https://pypi.org/project/flup

Source0: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx

%description
Random assortment of WSGI servers.

%package docs
Summary: Documentation for flup
Group: Development/Documentation
BuildArch: noarch

%description docs
Random assortment of WSGI servers.

This package contains documentation for flup.

%package pickles
Summary: Pickles for flup
Group: Development/Documentation
BuildArch: noarch

%description pickles
Random assortment of WSGI servers.

This package contains pickles for flup.

%prep
%setup -n %oname-%version

%prepare_sphinx3 docs/source

%build
%python3_build

#docs

%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

%install
%python3_install

#docs

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/

%files docs
%doc docs/build/html

%files pickles
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/pickle

%files
%doc PKG-INFO
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info
%exclude %python3_sitelibdir/%oname/pickle

%changelog
* Fri Mar 17 2023 Anton Vyatkin <toni@altlinux.org> 1.0.3-alt4
- (NMU) Build from pypi.

* Thu Jul 22 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.3-alt3.hg20120223.1.2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.3-alt2.hg20120223.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.3-alt2.hg20120223.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt2.hg20120223.1
- NMU: Use buildreq for BR.

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt2.hg20120223
- Use 'find... -exec...' instead of 'for ... $(find...'

* Sun Mar 17 2013 Aleksey Avdeev <solo@altlinux.ru> 1.0.3-alt1.hg20120223.1
- Rebuild with Python-3.3
- Fix non-identical noarch packages (python{,3}-module-flup)

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.hg20120223
- New snapshot
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt1.hg20101014.1.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.hg20101014.1
- Rebuilt with python-module-sphinx-devel

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.hg20101014
- New snapshot

* Thu Jun 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.hg20100525.1
- Added docs and pickles

* Thu Jun 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.hg20100525
- Version 1.0.3 (ALT #23628)

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.svn2016
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.5-alt0.svn2016.1
- Rebuilt with python-2.5.

* Sat Jul 01 2006 Ivan Fedorov <ns@altlinux.ru> 0.5-alt0.svn2016
- update to svn r2016

* Wed Oct 19 2005 Ivan Fedorov <ns@altlinux.ru> 0.5-alt0.svn1823
- Initial build for ALT Linux.
