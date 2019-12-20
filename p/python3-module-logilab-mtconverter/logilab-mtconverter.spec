%define oname logilab-mtconverter

Name: python3-module-%oname
Version: 0.9.0
Release: alt1
Summary: A library to convert from a MIME type to another

Group: Development/Python3
License: LGPLv2.1+
URL: http://www.logilab.org/project/logilab-mtconverter
BuildArch: noarch

# hg clone http://hg.logilab.org/logilab/mtconverter
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: graphviz python3-module-logilab-common

%add_python3_req_skip PIL


%description
A library to convert from a MIME type to another.

This package originally a backport of Zope's PortalTransforms tool with
all Zope's internal removed (e.g. most of the code).

%package tests
Summary: Tests for logilab mtconverter
Group: Development/Python3
Requires: %name = %version-%release

%description tests
A library to convert from a MIME type to another.

This package originally a backport of Zope's PortalTransforms tool with
all Zope's internal removed (e.g. most of the code).

This package contains tests for logilab mtconverter.

%prep
%setup
touch test/__init__.py

%build
%python3_build

%install
%python3_install

rm -f %buildroot%python3_sitelibdir/logilab/__init__.py*

mv test/ %buildroot%python3_sitelibdir/logilab/mtconverter/

%files
%doc ChangeLog COPYING README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/logilab/mtconverter/test

%files tests
%python3_sitelibdir/logilab/mtconverter/test


%changelog
* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.0-alt1
- Version updated to 0.9.0
- build for python2 disabled

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

