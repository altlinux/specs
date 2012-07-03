%define oname logilab-mtconverter

%def_without python3

Name: python-module-%oname
Version: 0.8.2
Release: alt1.hg20120315
Summary: A library to convert from a MIME type to another

Group: Development/Python
License: LGPLv2.1+
URL: http://www.logilab.org/project/logilab-mtconverter
# hg clone http://hg.logilab.org/logilab/mtconverter
Source: %name-%version.tar
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: python-devel python-module-logilab-common
BuildPreReq: python-module-distribute python-module-epydoc
BuildPreReq: graphviz
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python3-module-logilab-common python-tools-2to3
%endif

%description
A library to convert from a MIME type to another.

This package originally a backport of Zope's PortalTransforms tool with
all Zope's internal removed (e.g. most of the code).

%package docs
Summary: Documentation for logilab mtconverter
Group: Development/Documentation

%description docs
A library to convert from a MIME type to another.

This package originally a backport of Zope's PortalTransforms tool with
all Zope's internal removed (e.g. most of the code).

This package contains documentation for logilab mtconverter.

%if_with python3
%package -n python3-module-%oname
Summary: A library to convert from a MIME type to another (Python 3)
Group: Development/Python3
%add_python3_req_skip PIL

%description -n python3-module-%oname
A library to convert from a MIME type to another.

This package originally a backport of Zope's PortalTransforms tool with
all Zope's internal removed (e.g. most of the code).

%package -n python3-module-%oname-tests
Summary: Tests for logilab mtconverter (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
A library to convert from a MIME type to another.

This package originally a backport of Zope's PortalTransforms tool with
all Zope's internal removed (e.g. most of the code).

This package contains tests for logilab mtconverter.
%endif

%package tests
Summary: Tests for logilab mtconverter
Group: Development/Python
Requires: %name = %version-%release

%description tests
A library to convert from a MIME type to another.

This package originally a backport of Zope's PortalTransforms tool with
all Zope's internal removed (e.g. most of the code).

This package contains tests for logilab mtconverter.

%prep
%setup
touch test/__init__.py
%if_with python3
rm -rf ../python3
cp -a . ../python3
touch ../python3/test/__init__.py
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	if [ "$i" != "./setup.py" ]; then
		2to3 -w -n $i
	fi
done
%python3_build
popd
%endif

%make -C doc

%install
%python_install
rm -f %buildroot%python_sitelibdir/logilab/__init__.py*
%if_with python3
pushd ../python3
%python3_install
popd
rm -f %buildroot%python3_sitelibdir/logilab/__init__.py*
%endif

%files
%doc announce.txt ChangeLog README
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test

%files tests
%python_sitelibdir/*/*/test

%files docs
%doc doc/apidoc/*

%if_with python3
%files -n python3-module-%oname
%doc announce.txt ChangeLog README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test
%endif

%changelog
* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.hg20120315
- Initial build for Sisyphus

