%define oname deliverance

Name: python-module-%oname
Version: 0.6.1
Release: alt3

Summary: Deliverance transforms HTML to theme pages
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/Deliverance
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3


%description
Deliverance does transformations of HTML to 'theme' pages, similar in
function to XSLT but using a simpler XML-based language to express the
transformation.

%package -n python3-module-%oname
Summary: Deliverance transforms HTML to theme pages
Group: Development/Python3

%description -n python3-module-%oname
Deliverance does transformations of HTML to 'theme' pages, similar in
function to XSLT but using a simpler XML-based language to express the
transformation.

%package -n python3-module-%oname-tests
Summary: Tests for Deliverance
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Deliverance does transformations of HTML to 'theme' pages, similar in
function to XSLT but using a simpler XML-based language to express the
transformation.

This package contains tests for Deliverance.

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

cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|rfc822|rfc822py3|' '{}' +
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%python_install

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%files
%_bindir/*

%exclude %_bindir/*.py3

%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/*/*/*/*/test

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/*/*/*/*/test

%files -n python3-module-%oname
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/*/*/*/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/*/*/*/*/test


%changelog
* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt3
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added module for Python 3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Version 0.6.1

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

