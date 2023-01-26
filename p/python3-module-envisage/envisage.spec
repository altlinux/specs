%define _unpackaged_files_terminate_build 1

%define oname envisage

Name: python3-module-envisage
Version: 6.1.0
Release: alt2

Summary: Extensible Application Framework

License: BSD
Group: Development/Python3
Url: https://docs.enthought.com/envisage/

BuildArch: noarch

# Source-url: %__pypi_url %oname
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

Patch1: %oname-alt-docs.patch
Patch2: envisage-6.1.0-alt-fix-mistake-in-menu-group-specification.patch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%add_findprov_skiplist %python3_sitelibdir/%oname/plugins/*
%add_findreq_skiplist  %python3_sitelibdir/%oname/plugins/*

%add_findprov_skiplist %python3_sitelibdir/%oname/examples/*
%add_findreq_skiplist  %python3_sitelibdir/%oname/examples/*

%add_python3_req_skip wx
%add_python3_req_skip ui.main
%add_python3_req_skip envisage.plugins.text_editor.editor.text_editor
%add_python3_req_skip envisage.workbench envisage.workbench.services
%add_python3_req_skip envisage.ui.single_project
%add_python3_req_skip envisage.single_project.services

%description
Envisage is a Python-based framework for building extensible
applications, that is, applications whose functionality can be
extended by adding "plug-ins". Envisage provides a standard mechanism
for features to be added to an application, whether by the original
developer or by someone else.

%package tests
Summary: Tests for Extensible Application Framework
Group: Development/Python3
Requires: %name = %EVR

%description tests
Envisage is a Python-based framework for building extensible
applications, that is, applications whose functionality can be
extended by adding "plug-ins". Envisage provides a standard mechanism
for features to be added to an application, whether by the original
developer or by someone else.

This package contains tests for Envisage.

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

%prep
%setup
#patch1 -p1
%patch2 -p1

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%doc image_LICENSE*.txt LICENSE.txt
%doc CHANGES.rst README.rst
%python3_sitelibdir/*

%changelog
* Mon Jan 23 2023 Anton Vyatkin <toni@altlinux.org> 6.1.0-alt2
- added patch for fix mistake in menu group specification

* Sat Aug 27 2022 Vitaly Lipatov <lav@altlinux.ru> 6.1.0-alt1
- new version 6.1.0 (with rpmrb script)

* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 6.0.1-alt1
- new version 6.0.1 (with rpmrb script)

* Fri Jul 30 2021 Ivan A. Melnikov <iv@altlinux.org> 5.0.0-alt2
- skip examples in findreq and findprov

* Wed Apr 21 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt1
- new version
- switch to build from tarball

* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 4.7.2-alt2
- NMU: disable build python2 module

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
