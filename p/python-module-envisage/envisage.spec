%define oname envisage
Name:           python-module-%oname
Version:        4.1.1
Release:        alt1.git20120320
Summary:        Extensible Application Framework

Group:          Development/Python
License:        BSD
URL:            http://code.enthought.com/projects/envisage/
# https://github.com/enthought/envisage.git
Source:        %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildArch:      noarch
BuildRequires:  python-module-setuptools, python-devel
BuildPreReq: python-module-setupdocs python-module-sphinx-devel
Requires:       python-module-apptools
Provides: python-module-EnvisageCore = %version-%release
Obsoletes: python-module-EnvisageCore < %version-%release
Provides: python-module-EnvisagePlugins = %version-%release
Obsoletes: python-module-EnvisagePlugins < %version-%release

%description
Envisage is a Python-based framework for building extensible
applications, that is, applications whose functionality can be
extended by adding "plug-ins". Envisage provides a standard mechanism
for features to be added to an application, whether by the original
developer or by someone else.

%package docs
Summary: Documentation for Extensible Application Framework
Group: Development/Documentation
BuildArch: noarch

%description docs
Envisage is a Python-based framework for building extensible
applications, that is, applications whose functionality can be
extended by adding "plug-ins". Envisage provides a standard mechanism
for features to be added to an application, whether by the original
developer or by someone else.

This package contains development documentation for Envisage.

%package pickles
Summary: Pickles for Extensible Application Framework
Group: Development/Python

%description pickles
Envisage is a Python-based framework for building extensible
applications, that is, applications whose functionality can be
extended by adding "plug-ins". Envisage provides a standard mechanism
for features to be added to an application, whether by the original
developer or by someone else.

This package contains pickles for Envisage.

%package tests
Summary: Tests for Extensible Application Framework
Group: Development/Python
Requires: %name = %version-%release

%description tests
Envisage is a Python-based framework for building extensible
applications, that is, applications whose functionality can be
extended by adding "plug-ins". Envisage provides a standard mechanism
for features to be added to an application, whether by the original
developer or by someone else.

This package contains tests for Envisage.

%prep
%setup

%prepare_sphinx .

%build
%python_build

%generate_pickles docs/source docs/source %oname
sphinx-build -E -a -b html -c docs/source -d doctrees docs/source html

%install
%python_install

cp -fR pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/tests
%exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/*/tests

%files docs
%doc examples html

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle

%changelog
* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120320
- New snapshot

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120109
- Version 4.1.1

* Mon Nov 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20111110
- Version 4.0.1

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20110127
- Version 3.2.1

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.4-alt1.svn20101102.1
- Rebuilt with python-module-sphinx-devel

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.4-alt1.svn20101102
- Version 3.1.4

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1.svn20100720
- New snapshot

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1.svn20100225
- Version 3.1.3
- Exctracted docs into separate package
- Added tests and pickles packages

* Mon Jan 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1.svn20090721.2
- Rebuilt with new NumPy

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1.svn20090721.1
- Rebuilt with python 2.6

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1.svn20090721
- Version 3.1.2

* Fri Oct 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt2.1
- Fixed versions of requirements

* Fri Oct 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt2
- Fixed build with python 2.6

* Thu Oct 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus (thnx Valery Pipin)

* Fri Jun 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-1
- Updated

* Sat May 02 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.1-2
- Added examples directory to %%doc, Added python-configobj &
- python-AppTools in Requires field.

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.1-1
- Initial package
