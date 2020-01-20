%define oname imsvdex

Name: python3-module-%oname
Version: 2.0
Release: alt3

Summary: Read/write vocabularies in IMS Vocabulary Definition Exchange format
License: D-FSL - German Free Software License
Group: Development/Python3
Url: https://pypi.python.org/pypi/imsvdex/
BuildArch: noarch

# http://svn.plone.org/svn/collective/imsvdex/trunk/
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-lxml python-tools-2to3

%py3_provides %oname


%description
API to access and modify XML files in the IMS Vocabulary Definition
Exchange format.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
API to access and modify XML files in the IMS Vocabulary Definition
Exchange format.

This package contains tests for %oname.

%prep
%setup
%patch0 -p1

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Mon Jan 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.0-alt3
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0-alt2.dev0.svn20140527.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2.dev0.svn20140527
- Fixed build

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.dev0.svn20140527
- Initial build for Sisyphus

