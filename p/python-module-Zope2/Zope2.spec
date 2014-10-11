%define oname Zope2
Name: python-module-%oname
Version: 2.13.22
Release: alt5
Summary: Zope2 application server / web framework
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/Zope2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
# http://cvs.zope.org/*checkout*/Python-2.2.3/Lib/regsub.py?rev=1.1.1.1&cvsroot=Zope.org&sortby=author&content-type=text/plain
Source1: regsub.py

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel

%add_python_req_skip ntsecuritycon pywintypes win32api win32con win32event

%description
Zope2 is an open-source web application server.

%package tests
Summary: Tests for Zope2
Group: Development/Python
Requires: %name = %version-%release
Requires: python-module-zope.sendmail python-module-zope.viewlet
Requires: python-module-Products.PythonScripts python-module-zLOG
Requires: python-module-Products.MIMETools python-module-zope.size
Requires: python-module-zope.traversing python-module-zope.tales
Requires: python-module-zope.testbrowser python-module-zope.tal
Requires: python-module-zope.site python-module-zope.ptresource
Requires: python-module-zope.processlifetime python-module-ZODB3
Requires: python-module-zope.pagetemplate
Requires: python-module-zope.lifecycleevent
Requires: python-module-zope.contentprovider
Requires: python-module-zope.container python-module-zope.annotation
Requires: python-module-zope.browserresource
Requires: python-module-zope.browserpage
Requires: python-module-zope.browsermenu python-module-mechanize
Requires: python-module-initgroups python-module-Missing
Requires: python-module-zope.filerepresentation
Requires: python-module-zope.dottedname
Requires: python-module-Products.MailHost
Requires: python-module-Products.StandardCacheManagers
Requires: python-module-Products.ZCTextIndex
Requires: python-module-Products.ZCatalog
Requires: python-module-Products.ExternalMethod
Requires: python-module-Products.BTreeFolder2
Requires: python-module-Products.OFSP

%add_python_req_skip http_date

%description tests
Zope2 is an open-source web application server.

This package contains tests for Zope2.

%package pickles
Summary: Pickles for Zope2
Group: Development/Python

%description pickles
Zope2 is an open-source web application server.

This package contains pickles for Zope2.

%package docs
Summary: Documentation for Zope2
Group: Development/Documentation
BuildArch: noarch

%description docs
Zope2 is an open-source web application server.

This package contains documentation for Zope2.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build

pushd doc
export PYTHONPATH=$PWD/../build/lib
%make pickle
%make html
popd

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

touch %buildroot%python_sitelibdir/Shared/__init__.py
touch %buildroot%python_sitelibdir/Products/__init__.py
touch %buildroot%python_sitelibdir/Testing/__init__.py

install -p -m644 %SOURCE1 %buildroot%python_sitelibdir

cp -fR doc/.build/pickle %buildroot%python_sitelibdir/%oname/

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%files
%doc *.txt
%_bindir/*
%exclude %_bindir/zpasswd
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/*test*
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/tests
%exclude %python_sitelibdir/*/Test*
%exclude %python_sitelibdir/Test*
%exclude %python_sitelibdir/*/*/examples
%exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/*test*
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/tests
%python_sitelibdir/*/Test*
%python_sitelibdir/Test*
%python_sitelibdir/*/*/examples

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc doc/.build/html/*

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.22-alt5
- Added more testing requirements

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.22-alt4
- Added testing requirements

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.22-alt3
- Excluded .pth file

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.22-alt2
- Set as archdep

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.22-alt1
- Version 2.13.22

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.21-alt1
- Version 2.13.21

* Fri Apr 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.19-alt2
- Applied repocop patch
- Moved examples into tests subpackage

* Thu Apr 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.19-alt1
- Version 2.13.19

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.7-alt2.1
- Rebuild with Python-2.7

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.7-alt2
- Moved all tests into tests package

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.7-alt1
- Initial build for Sisyphus

