%define oname repoze.who.plugins.sa

Name:           python3-module-%oname
Version:        1.0.1
Release:        alt3

Summary:        The repoze.who SQLAlchemy plugin

License:        BSD-derived
Group:          Development/Python3
URL:            http://pypi.python.org/pypi/repoze.who.plugins.sa/

# Source-url: %__pypi_url %oname
Source:         %oname-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%py3_requires repoze.who SQLAlchemy
%py3_provides repoze.who.plugins.sa
#BuildRequires: python3-module-setuptools rpm-build-python3

%description
This plugin provides one repoze.who authenticator and one metadata
provider which works with SQLAlchemy or Elixir-based models.

%package docs
Summary: Documentation for repoze.who.plugins.sa
Group: Development/Documentation
BuildArch: noarch

%description docs
This plugin provides one repoze.who authenticator and one metadata
provider which works with SQLAlchemy or Elixir-based models.

This package contains documentation for repoze.who.plugins.sa.

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

#install -d %buildroot%python_sitelibdir/%oname
#cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt PKG-INFO
%python3_sitelibdir/%{oname}*
%exclude %python3_sitelibdir/*.pth
%python3_sitelibdir/repoze/who/plugins/*

#files tests
#doc tests

#files docs
#doc docs/build/latex/*.pdf
#doc docs/build/html

%changelog
* Wed Jun 16 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt3
- build python3 module separately

* Fri Feb 09 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt2.1.1.1.1
- (NMU) Fix Provides of python3 module

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt2.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt2.1
- NMU: Use buildreq for BR.

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Added module for Python 3

* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Version 1.0.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt4.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Set as archdep package

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Version 1.0

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.rc2.1
- Rebuilt with python-module-sphinx-devel

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.rc2
- Initial build for Sisyphus

