%define _unpackaged_files_terminate_build 1
%define oname crank

Name: python3-module-%oname
Version: 0.8.1
Release: alt1
Summary: Generalization of dispatch mechanism for use across frameworks
License: MIT
Group: Development/Python3
Url: http://pypi.python.org/pypi/crank

Source0: https://pypi.python.org/packages/59/9b/5df0c3319f0c4de5a8fc428243487750bbd9e96646b5aa435494e724a1c5/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
Generalization of dispatch mechanism for use across frameworks.

%prep
%setup -n %{oname}-%{version}

%build
%python3_build

%install
%python3_install

%files
%doc PKG-INFO
%python3_sitelibdir/*

%changelog
* Mon May 23 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt1
- Build new version.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt2
- Drop python2 support.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Version 0.7.1
- Added module for Python 3

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus

