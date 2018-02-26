%define oname enthought

%def_disable docs

Name:           python-module-EnthoughtBase
Version:        3.1.1
Release:        alt1.svn20110127.1
Summary:        Core packages for the Enthought Tool Suite

Group:          Development/Python
License:        BSD and/or LGPLv2+
URL:            http://pypi.python.org/pypi/EnthoughtBase/%version
# https://svn.enthought.com/svn/enthought/EnthoughtBase
Source:        EnthoughtBase-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
%py_provides %oname
%setup_python_module %oname

BuildArch:      noarch
BuildRequires: python-module-setuptools, python-devel
BuildPreReq: python-module-setupdocs python-module-sphinx-devel
BuildRequires: unzip

%description
The EnthoughtBase project includes a few core packages that are used
by many other projects in the Enthought Tool Suite:

    * enthought.etsconfig: Supports configuring settings that need to
      be shared across multiple projects or programs on the same
      system.

    * enthought.logger: Provides convenience functions for creating
      logging handlers.

    * enthought.util: Provides miscellaneous utility functions.

%if_enabled docs
%package docs
Summary: Documentation for core packages for the Enthought Tool Suite
Group: Development/Documentation
BuildArch: noarch

%description docs
The EnthoughtBase project includes a few core packages that are used
by many other projects in the Enthought Tool Suite.

This package contains documentation for EnthoughtBase.

%package pickles
Summary: Pickles for core packages for the Enthought Tool Suite
Group: Development/Python

%description pickles
The EnthoughtBase project includes a few core packages that are used
by many other projects in the Enthought Tool Suite.

This package contains pickles for EnthoughtBase.
%endif

%prep
%setup -n EnthoughtBase-%version

%if_enabled docs
%prepare_sphinx .
%endif

%build
%python_build

%install
%python_install -O1
 
#sed -i 's|\.dev||' \
#	%buildroot%python_sitelibdir/EnthoughtBase-%version-*info/requires.txt

install -p -m644 enthought/logger/plugin/preferences.ini \
	%buildroot%python_sitelibdir/enthought/logger/plugin
%if_enabled docs
%generate_pickles docs/source docs/source EnthoughtBase
sphinx-build -E -a -b html -c docs/source -d doctrees docs/source html
cp -fR pickle %buildroot%python_sitelibdir/EnthoughtBase
%endif

%files
%doc *.txt docs/*.txt
%python_sitelibdir/*
%if_enabled docs
%exclude %python_sitelibdir/EnthoughtBase/pickle
%endif

%if_enabled docs
%files docs
%doc examples html

%files pickles
%dir %python_sitelibdir/EnthoughtBase
%python_sitelibdir/EnthoughtBase/pickle
%endif

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.1-alt1.svn20110127.1
- Rebuild with Python-2.7

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.svn20110127
- Version 3.1.1

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.7-alt1.svn20101102.1
- Rebuilt with python-module-sphinx-devel

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.7-alt1.svn20101102
- Version 3.0.7

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.6-alt1.svn20100719
- Version 3.0.6

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.5-alt1.svn20100225
- Version 3.0.5
- Extracted docs into separate package
- Added pickles package

* Fri Jan 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt1.svn20090811.3
- Rebuild without python-module-Numeric

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt1.svn20090811.2
- Rebuilt with python 2.6

* Sat Oct 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt1.svn20090811.1
- Added preferences for logger plugin

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt1.svn20090811
- Version 3.0.4

* Fri Oct 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt2
- Fixed versions of requirements

* Thu Oct 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1
- Initial build for Sisyphus (thnx Valery Pipin)

* Fri Jun 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.2-1
- Updated

* Thu Jun 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.1-3
- Added README.fedora

* Tue Mar 17 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.1-2
- Included html & examples, fixed license, and removed egg folder

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.1-1
- Initial package
