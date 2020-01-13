%define _unpackaged_files_terminate_build 1

%define oname mockup

Name: python3-module-%oname
Version: 3.1.1
Release: alt1

Summary: A collection of client side patterns for faster and easier web development
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/mockup/
BuildArch: noarch

# https://github.com/plone/mockup.git
Source0: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python3


%description
Plone Mockup is an ongoing effort to modernize Plone's javascript
story.

The Goals of Mockup:

1. Standardize configuration of patterns implemented in js to use HTML
   data attributes, so they can be developed without running a backend
   server.
2. Use modern AMD approach to declaring dependencies on other js libs.
3. Full unit testing of js

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Plone Mockup is an ongoing effort to modernize Plone's javascript
story.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Mon Jan 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.1.1-alt1
- Version updated to 3.1.1
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.1.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.6-alt1
- automated PyPI update

* Mon Jul 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.6-alt1.git20150726
- Version 2.0.6

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20150213
- Initial build for Sisyphus

