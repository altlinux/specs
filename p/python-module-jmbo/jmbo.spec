%define oname jmbo

%def_with python3

Name: python-module-%oname
Version: 1.1.3
Release: alt1.git20141112
Summary: The Jmbo base product introduces a content type and various tools required to build Jmbo products
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jmbo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/jmbo.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires atlas tastypie celery

%description
Jmbo is a CMS built on Django enabling you to rapidly build multilingual
web and mobi sites with the minimum amount of code and customization.

The Jmbo base product introduces abstract models and concepts that are
used in Jmbo products.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Jmbo is a CMS built on Django enabling you to rapidly build multilingual
web and mobi sites with the minimum amount of code and customization.

The Jmbo base product introduces abstract models and concepts that are
used in Jmbo products.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: The Jmbo base product introduces a content type and various tools required to build Jmbo products
Group: Development/Python3
%py3_requires atlas tastypie celery

%description -n python3-module-%oname
Jmbo is a CMS built on Django enabling you to rapidly build multilingual
web and mobi sites with the minimum amount of code and customization.

The Jmbo base product introduces abstract models and concepts that are
used in Jmbo products.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Jmbo is a CMS built on Django enabling you to rapidly build multilingual
web and mobi sites with the minimum amount of code and customization.

The Jmbo base product introduces abstract models and concepts that are
used in Jmbo products.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests.*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/*/*/testmodel*

%files tests
%python_sitelibdir/*/*/tests.*
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/*/*/testmodel*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/*/*/testmodel*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/*/*/testmodel*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20141112
- Version 1.1.3

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2.git20140903
- Applied python-module-jmbo-1.1.1-alt1.git20140903.diff

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20140903
- Initial build for Sisyphus

