%define oname logilab-mtconverter

Name: python-module-%oname
Version: 0.8.4
Release: alt3
Summary: A library to convert from a MIME type to another

Group: Development/Python
License: LGPLv2.1+
URL: http://www.logilab.org/project/logilab-mtconverter
# hg clone http://hg.logilab.org/logilab/mtconverter
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: fontconfig fonts-bitmap-misc libwayland-client libwayland-server python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-docutils python-module-egenix-mx-base python-module-genshi python-module-jinja2 python-module-kerberos python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-setuptools
BuildRequires: graphviz python-module-epydoc python-module-html5lib time
BuildPreReq: python-module-logilab-common python3-module-logilab-common


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

rm -rf ../python3
cp -a . ../python3
touch ../python3/test/__init__.py

%build
%python_build

pushd ../python3
for i in $(find ./ -name '*.py'); do
	if [ "$i" != "./setup.py" ]; then
		2to3 -w -n $i
	fi
done
%python3_build
popd

%make -C doc

%install
%python_install
rm -f %buildroot%python_sitelibdir/logilab/__init__.py*

pushd ../python3
%python3_install
popd
rm -f %buildroot%python3_sitelibdir/logilab/__init__.py*

%files
%doc announce.txt ChangeLog README
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test

%files tests
%python_sitelibdir/*/*/test

%files docs
%doc doc/apidoc/*

%files -n python3-module-%oname
%doc announce.txt ChangeLog README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test


%changelog
* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.8.4-alt3
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.4-alt2.hg20130321.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.4-alt2.hg20130321.1
- NMU: Use buildreq for BR.

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt2.hg20130321
- Added module for Python 3

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1.hg20130321
- Version 0.8.4

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.hg20120315
- Initial build for Sisyphus

