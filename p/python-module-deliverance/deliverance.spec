%define oname deliverance
Name: python-module-%oname
Version: 0.6
Release: alt2
Summary: Deliverance transforms HTML to theme pages
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/Deliverance
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
Deliverance does transformations of HTML to 'theme' pages, similar in
function to XSLT but using a simpler XML-based language to express the
transformation.

%package tests
Summary: Tests for Deliverance
Group: Development/Python
Requires: %name = %version-%release

%description tests
Deliverance does transformations of HTML to 'theme' pages, similar in
function to XSLT but using a simpler XML-based language to express the
transformation.

This package contains tests for Deliverance.

%prep
%setup

%build
%python_build

%install
%python_install

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%files
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/*/*/*/*/test

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/*/*/*/*/test

%changelog
* Sun Dec 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2
- Extracted test into separate package

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Version 0.6

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2
- Applied patch from Repocop

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus

