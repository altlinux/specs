%define _unpackaged_files_terminate_build 1
%define rname reportlab
%define oname Reportlab

%def_with python3

Name: python-module-%oname
Version: 3.3.0
Release: alt1
License: BSD license (see LICENSE.txt for details)
Summary: The Reportlab Toolkit
Group: Development/Python
Packager: Alexey Morsov <swi@altlinux.ru>
Url: http://www.reportlab.org

Source0: https://pypi.python.org/packages/b8/17/7c5342dfbc9dc856173309270006e34c3bfad59934f0faa1dcc117ac93f1/reportlab-%{version}.tar.gz

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-devel rpm-build-python3 time

#BuildRequires: rpm-build-python >= 0.8
#BuildRequires: python-devel python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
%endif

%add_python_req_skip rlextra

%description
The ReportLab Toolkit.
An Open Source Python library for generating PDFs and graphics.

%package -n python3-module-%oname
Summary: The Reportlab Toolkit
Group: Development/Python3
%add_python3_req_skip rlextra __main__

%description -n python3-module-%oname
The ReportLab Toolkit.
An Open Source Python library for generating PDFs and graphics.

%package -n python3-module-%oname-tests
Summary: Tests for Reportlab Toolkit
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
The ReportLab Toolkit.
An Open Source Python library for generating PDFs and graphics.

This package contains tests for Reportlab Toolkit.

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
%setup -q -n reportlab-%{version}

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%make -C docs html

%install
%add_optflags -fno-strict-aliasing
%python_build_install --optimize=2 \
	--record=INSTALLED_FILES

cp -fR tests %buildroot%python_sitelibdir/%rname/

%if_with python3
pushd ../python3
%python3_install
cp -fR tests %buildroot%python3_sitelibdir/%rname/
popd
%endif

%files -f INSTALLED_FILES
%doc *.txt
%python_sitelibdir/%rname
%exclude %python_sitelibdir/%rname/tests

%files tests
%python_sitelibdir/%rname/tests

%files docs
%doc docs/build/html docs/userguide demos

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%rname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%rname/tests
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 3.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Added module for Python 3

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1
- Version 2.7

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

