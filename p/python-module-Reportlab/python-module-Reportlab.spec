%define rname reportlab
Name: python-module-Reportlab
Version: 2.5
Release: alt3.1.1
License: BSD license (see LICENSE.txt for details)
Summary: The Reportlab Toolkit
Group: Development/Python
Packager: Alexey Morsov <swi@altlinux.ru>
Url: http://www.reportlab.org

Source: %name-%version.tar

BuildRequires: rpm-build-python >= 0.8
BuildRequires: python-devel python-module-sphinx-devel

%add_python_req_skip rlextra

%description
The ReportLab Toolkit.
An Open Source Python library for generating PDFs and graphics.

%package tests
Summary: Tests for Reportlab Toolkit
Group: Development/Python
Requires: %name = %version-%release

%description tests
The ReportLab Toolkit.
An Open Source Python library for generating PDFs and graphics.

This package contains tests for Reportlab Toolkit.

%package docs
Summary: Documentation for Reportlab Toolkit
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description docs
The ReportLab Toolkit.
An Open Source Python library for generating PDFs and graphics.

This package contains documentation for Reportlab Toolkit.

%prep
%setup
%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug

%make -C docs html

%install
%add_optflags -fno-strict-aliasing
%python_build_install --optimize=2 \
	--record=INSTALLED_FILES

cp -fR tests %buildroot%python_sitelibdir/%rname/

%files -f INSTALLED_FILES
%doc *.txt
%python_sitelibdir/%rname
%exclude %python_sitelibdir/%rname/tests

%files tests
%python_sitelibdir/%rname/tests

%files docs
%doc docs/build/html docs/userguide demos

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5-alt3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5-alt3.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt3
- Rebuilt with python-module-sphinx-devel

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt2
- Rebuilt for debuginfo

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1
- Version 2.5
- Added tests

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.4-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for python-module-Reportlab
  * postclean-05-filetriggers for spec file

* Sat Jan 23 2010 Alexey Morsov <swi@altlinux.ru> 2.4-alt1
- new version

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1.1
- Rebuilt with python 2.6

* Wed Feb 25 2009 Alexey Morsov <swi@altlinux.ru> 2.3-alt1
- new version
- clean spec

* Wed Nov 26 2008 Alexey Morsov <swi@altlinux.ru> 2.2-alt1
- new version

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 2.1-alt2.1
- Rebuilt with python-2.5.

* Tue Jan 22 2008 Grigory Batalov <bga@altlinux.ru> 2.1-alt2
- Remove python version from BuildRequires and Requires.

* Fri Jun 15 2007 Alexey Morsov <swi@altlinux.ru> 2.1-alt1
- version 2.1
- add python_sitelibdir  to files

* Thu Jan 18 2007 Alexey Morsov <swi@altlinux.ru> 2.0-alt1
- New version: full support for unicode, python 2.4 or higher
is required.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.20-alt2.1
- Rebuilt using rpm-build-python-0.29-alt4.

* Sat Apr 09 2005 Andrey Orlov <cray@altlinux.ru> 1.20-alt2
- Font rina.ttf excluded due to  license restrictions
- Documentation files added
- License text added

* Wed Jan 12 2005 Andrey Orlov <cray@altlinux.ru> 1.20-alt1
- New Version

* Mon May 17 2004 Andrey Orlov <cray@altlinux.ru> 1.19-alt5
- Changed for sisyphus

* Mon May 10 2004 Andrey Orlov <cray@altlinux.ru> 1.19-alt4.d
- Rebuild

* Thu Apr 22 2004 Andrey Orlov <cray@altlinux.ru> 1.19-alt3.d
- Rebuild with new rpm/python macros

* Tue Apr 13 2004 Andrey Orlov <cray@altlinux.ru> 1.19-alt2.d
- Rebuild with new rpm/python macros

* Thu Mar 25 2004 Andrey Orlov <cray@altlinux.ru> 1.19-alt1.d
- Initial release

