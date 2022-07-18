%define oname repoze.sphinx.autointerface

Name: python3-module-%oname
Version: 1.0.0
Release: alt1

Summary: Auto-generate Sphinx API docs from Zope interfaces (Python 3)

License: BSD
Group: Development/Python3
Url: https://github.com/repoze/repoze.sphinx.autointerface

#Source0-url: %__pypi_url %oname
# See https://github.com/repoze/repoze.sphinx.autointerface/pull/17/commits
# Source0-url: https://github.com/stevepiercy/repoze.sphinx.autointerface/archive/refs/heads/sphinx-40-compat.zip
Source0: %oname-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%py3_requires zope.interface sphinx jinja2.tests
Requires: python3-module-repoze.sphinx = %EVR

%description
This package defines an extension for the `Sphinx` documentation system.
The extension allows generation of API documentation by introspection of
`zope.interface` instances in code.


%package -n python3-module-repoze.sphinx
Summary: Core package for repoze.sphinx (Python 3)
Group: Development/Python3
%py3_provides repoze.sphinx
%py3_requires repoze

%description -n python3-module-repoze.sphinx
Core package for repoze.sphinx.


%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

touch %buildroot%python3_sitelibdir/repoze/sphinx/__init__.py

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/repoze/sphinx/__init__.*

%files -n python3-module-repoze.sphinx
%python3_sitelibdir/repoze/sphinx/__init__.*

%changelog
* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version 1.0.0 (with rpmrb script)

* Tue May 18 2021 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt3.0
- use sphinx 4.0 PR

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt2.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt2.1
- NMU: Use buildreq for BR.

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7.1-alt1
- Version 0.7.1

* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20120215
- New snapshot
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt1.git20110322.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20110322.1
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20110322
- Initial build for Sisyphus
