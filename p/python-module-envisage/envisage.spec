%define _unpackaged_files_terminate_build 1

%def_with python3

%define oname envisage

Name:           python-module-%oname
Version:        4.7.2
Release:        alt1
Summary:        Extensible Application Framework
Group:          Development/Python
License:        BSD
URL:            https://docs.enthought.com/envisage/

BuildArch:      noarch

# https://github.com/enthought/envisage.git
Source:        %name-%version.tar

Patch1:        %oname-alt-docs.patch

BuildRequires(pre): python-module-setupdocs python-module-sphinx-devel
BuildRequires: python-devel python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

Requires: python-module-apptools

Provides: python-module-EnvisageCore = %EVR
Obsoletes: python-module-EnvisageCore < %EVR
Provides: python-module-EnvisagePlugins = %EVR
Obsoletes: python-module-EnvisagePlugins < %EVR

%add_findprov_skiplist %python_sitelibdir/%oname/plugins/*
%add_findreq_skiplist  %python_sitelibdir/%oname/plugins/*

%if_with python3
%add_findprov_skiplist %python3_sitelibdir/%oname/plugins/*
%add_findreq_skiplist  %python3_sitelibdir/%oname/plugins/*
%endif

%description
Envisage is a Python-based framework for building extensible
applications, that is, applications whose functionality can be
extended by adding "plug-ins". Envisage provides a standard mechanism
for features to be added to an application, whether by the original
developer or by someone else.

%package tests
Summary: Tests for Extensible Application Framework
Group: Development/Python
Requires: %name = %EVR

%description tests
Envisage is a Python-based framework for building extensible
applications, that is, applications whose functionality can be
extended by adding "plug-ins". Envisage provides a standard mechanism
for features to be added to an application, whether by the original
developer or by someone else.

This package contains tests for Envisage.

%if_with python3
%package -n python3-module-%oname
Summary: Extensible Application Framework
Group: Development/Python3
%add_python3_req_skip wx
%add_python3_req_skip ui.main
%add_python3_req_skip envisage.plugins.text_editor.editor.text_editor
%add_python3_req_skip envisage.workbench envisage.workbench.services
%add_python3_req_skip envisage.ui.single_project
%add_python3_req_skip envisage.single_project.services

%description -n python3-module-%oname
Envisage is a Python-based framework for building extensible
applications, that is, applications whose functionality can be
extended by adding "plug-ins". Envisage provides a standard mechanism
for features to be added to an application, whether by the original
developer or by someone else.

%package -n python3-module-%oname-tests
Summary: Tests for Extensible Application Framework
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Envisage is a Python-based framework for building extensible
applications, that is, applications whose functionality can be
extended by adding "plug-ins". Envisage provides a standard mechanism
for features to be added to an application, whether by the original
developer or by someone else.

This package contains tests for Envisage.
%endif

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

%prep
%setup
%patch1 -p1

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

export PYTHONPATH=$PWD
%generate_pickles docs/source docs/source %oname
sphinx-build -E -a -b html -c docs/source -d doctrees docs/source html

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR pickle %buildroot%python_sitelibdir/%oname/

%files
%doc image_LICENSE*.txt LICENSE.txt
%doc CHANGES.txt README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/example*
%exclude %python_sitelibdir/*/*/*/*/example*
%exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/*/tests
%python_sitelibdir/*/*/*/example*
%python_sitelibdir/*/*/*/*/example*

%files docs
%doc examples html

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc image_LICENSE*.txt LICENSE.txt
%doc CHANGES.txt README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests
%exclude %python3_sitelibdir/*/*/*/*/tests
%exclude %python3_sitelibdir/*/*/*/example*
%exclude %python3_sitelibdir/*/*/*/*/example*
%exclude %python3_sitelibdir/*/*/*/*/*/example*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests
%python3_sitelibdir/*/*/*/*/tests
%python3_sitelibdir/*/*/*/example*
%python3_sitelibdir/*/*/*/*/example*
%python3_sitelibdir/*/*/*/*/*/example*
%endif

%changelog
* Mon Jul 22 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 4.7.2-alt1
- Updated to upstream version 4.7.2.
- Built modules for python-3.

* Sun May 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20150428
- New snapshot

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20140812
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20140425
- Version 4.5.0

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20131017
- New snapshot

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130418
- Version 4.3.0

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20130108
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20120928
- Version 4.2.1

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
