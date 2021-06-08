%define _unpackaged_files_terminate_build 1
%define oname releases

Name: python3-module-%oname
Version: 1.4.0
Release: alt2
Summary: A Sphinx extension for changelog manipulation
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/releases/

# https://github.com/bitprophet/releases.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
Releases is a Sphinx extension designed to help you keep a source
control friendly, merge friendly changelog file & turn it into useful,
human readable HTML output.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info

%changelog
* Tue Jun 08 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt2
- Drop python2 support.

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.0-alt1
- Updated to upstream version 1.4.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.git20150323.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20150323
- Version 0.7.0

* Mon Aug 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added module for Python 3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

