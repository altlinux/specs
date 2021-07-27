%define oname TAP

Name: python3-module-%oname
Version: 0.001
Release: alt2.git20110216
Summary: Test Anything Protocol
License: MIT/X11
Group: Development/Python3
Url: http://testanything.org/

# git://git.codesimply.com/PyTAP.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
TAP, the Test Anything Protocol, is a simple text-based interface
between testing modules in a test harness.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc examples
%python3_sitelibdir/*

%changelog
* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 0.001-alt2.git20110216
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.001-alt1.git20110216.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.001-alt1.git20110216.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.001-alt1.git20110216
- Initial build for Sisyphus

