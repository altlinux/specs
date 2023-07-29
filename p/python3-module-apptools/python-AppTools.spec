%define _unpackaged_files_terminate_build 1

# wait for python module importlib_resources
# https://bugzilla.altlinux.org/39327
%def_without check

%define oname apptools

Name:           python3-module-%oname
Version:        5.2.1
Release:        alt1

Summary:        Enthough Tool Suite Application Tools

License:        BSD and LGPLv2+
Group:          Development/Python3
URL:            https://docs.enthought.com/apptools/

# Source-url: https://github.com/enthought/apptools/archive/refs/tags/%version.tar.gz
Source:         %name-%version.tar
Source1:        README.fedora.python-AppTools

# Users of Python 3.9 and beyond should use the standard library module
Patch1: apptools-5.1.0-python3.9-compat.patch

BuildArch:      noarch

#if_with check
BuildRequires: xvfb-run unzip

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3 >= 3.8
#BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(tables)
#BuildRequires: python3-module-setupdocs python3-module-sphinx-devel
# for 2to3
BuildRequires: python3-tools
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-traits-tests
BuildRequires: python3-module-pyface
BuildRequires: python3-module-numpy-testing
BuildRequires: python3(tables.tests)
BuildRequires: python3(pandas)
%endif

%add_python3_req_skip traits.protocols.api
%add_python3_req_skip new wx
%add_python3_req_skip codetools.contexts.api

%description
The AppTools project includes a set of packages that Enthought has
found useful in creating a number of applications. They implement
functionality that is commonly needed by many applications

    * enthought.appscripting: Framework for scripting applications.

    * enthought.help: Provides a plugin for displaying documents and
      examples and running demos in Envisage Workbench applications.

    * enthought.io: Provides an abstraction for files and folders in a
      file system.

    * enthought.naming: Manages naming contexts, supporting non-string
      data types and scoped preferences

    * enthought.permissions: Supports limiting access to parts of an
      application unless the user is appropriately authorised (not
      full-blown security).

and many more.

%package tests
Summary: Tests for AppTools
Group: Development/Python3
Requires: %name = %EVR
%add_python3_req_skip apptools.template.impl.base_data_context_adapter
%add_python3_req_skip blockcanvas.app.utils
%add_python3_req_skip chaco.api
%add_python3_req_skip chaco.scatter_markers
%add_python3_req_skip chaco.tools.api
%add_python3_req_skip enable.wx_backend.api
%add_python3_req_skip etsdevtools.developer.features.api
%add_python3_req_skip etsdevtools.developer.helper.themes
%add_python3_req_skip traitsui.wx.themed_slider_editor
%add_python3_req_skip traitsui.wx.themed_text_editor

%description tests
The AppTools project includes a set of packages that Enthought has
found useful in creating a number of applications.

This package contains tests for AppTools.

%package docs
Summary: Documentation for AppTools
Group: Development/Documentation
BuildArch: noarch

%description docs
The AppTools project includes a set of packages that Enthought has
found useful in creating a number of applications.

This package contains documentation for AppTools.

%prep
%setup
#patch1 -p2

%if_with doc
%prepare_sphinx3 docs/source
%endif

%build
%python3_build

#sphinx-build -E -a -b html -c docs/source -d doctrees docs/source html

%install
install -p -m644 %SOURCE1 README.fedora
%python3_install
%python3_prune

%check
#  Note: if the cwd is somewhere under /tmp, that confuses test_file_path.py
xvfb-run py.test3

%files
%doc image_LICENSE*.txt LICENSE.txt
%doc README.fedora README.rst
%python3_sitelibdir/*
%if 0
%exclude %python3_sitelibdir/%oname/*/test*
%exclude %python3_sitelibdir/%oname/*/*/test*
%exclude %python3_sitelibdir/%oname/*/*/example*
%exclude %python3_sitelibdir/%oname/*/*/*/example*
%exclude %python3_sitelibdir/%oname/*/*/*/*/example*

%files tests
%python3_sitelibdir/%oname/*/test*
%python3_sitelibdir/%oname/*/*/test*
%python3_sitelibdir/%oname/*/*/example*
%python3_sitelibdir/%oname/*/*/*/example*
%python3_sitelibdir/%oname/*/*/*/*/example*
%endif

%if_with doc
%files docs
%doc examples html
%endif


%changelog
* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 5.2.1-alt1
- new version 5.2.1 (with rpmrb script)

* Wed Jun 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.0-alt2
- Fixed runtime dependencies.

* Sun Apr 18 2021 Vitaly Lipatov <lav@altlinux.ru> 5.1.0-alt1
- new version 5.1.0 (with rpmrb script)
- build from tarball
- disable tests (wait for python module importlib_resources)

* Sat Nov 21 2020 Vitaly Lipatov <lav@altlinux.ru> 4.5.0-alt1
- new version 4.5.0 (with rpmrb script)

* Sat Nov 21 2020 Vitaly Lipatov <lav@altlinux.ru> 4.4.0-alt6
- build as python3 module, don't pack tests

* Sat Feb 01 2020 Vitaly Lipatov <lav@altlinux.ru> 4.4.0-alt5
- build with python2 modules disabled

* Mon Jul 22 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt4
- Built modules for python-3.

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 4.4.0-alt3
- Added missing dep on `numpy.testing`.

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt2
- Updated to upstream release version 4.4.0.

* Sun May 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.0-alt1.git20150430
- Version 4.4.0

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20150211
- Version 4.3.0

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt2.git20140919
- New snapshot

* Thu May 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt2.git20140408
- Moved tests into tests subpackage

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20140408
- Version 4.2.1

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1.git20130328
- Version 4.2.0

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20121012
- Version 4.1.1

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.git20120329
- New snapshot

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.git20111221
- Version 4.0.2

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20111110
- Version 4.0.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.2-alt1.svn20110127.1
- Rebuild with Python-2.7

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.2-alt1.svn20110127
- Version 3.4.2

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20101102.1
- Rebuilt with python-module-sphinx-devel

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20101102
- Version 3.4.1

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20100706
- Version 3.3.3

* Fri Mar 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.2-alt1.svn20100225
- Version 3.3.2
- Extracted docs into separate package
- Added pickles package

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20090928.1
- Rebuilt with python 2.6

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20090928
- Version 3.3.1

* Fri Oct 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt2
- Fixed versions of requirements

* Thu Oct 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus (thnx Valery Pipin)

* Fri Jun 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.2.0-1
- Updated

* Thu Jun 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-4
- Added README.fedora

* Fri Apr 24 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-3
- Removed AppTools.egg-info directory

* Fri Mar 06 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-2
- Included examples in %%doc, added python-TraitsGUI & python-EnthoughtBase
- as Requires. Added html folder.

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-1
- Initial package
