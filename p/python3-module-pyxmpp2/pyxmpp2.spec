%define oname pyxmpp2

Name: python3-module-%oname
Version: 2.0.1
Release: alt1

Summary: The new and shiny XMPP implementation for Python
License: LGPLv2.1
Group: Development/Python3
Url: https://github.com/Jajcus/pyxmpp2
BuildArch: noarch

# https://github.com/Jajcus/pyxmpp2.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
The new and shiny XMPP implementation for Python.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
The new and shiny XMPP implementation for Python.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc README COPYING TODO doc/*.txt examples/
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files tests
%python3_sitelibdir/*/test


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.1-alt1
- Version updated to 2.0.1
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt2.git20130922.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.git20130922.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20130922
- Enabled requirement on python3-module-libxml2

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20130922
- Initial build for Sisyphus

