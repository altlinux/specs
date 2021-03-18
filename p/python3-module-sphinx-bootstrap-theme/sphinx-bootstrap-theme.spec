%define _unpackaged_files_terminate_build 1
%define oname sphinx-bootstrap-theme

Name: python3-module-%oname
Version: 0.6.0
Release: alt3
Summary: Sphinx Bootstrap Theme
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/sphinx-bootstrap-theme/
BuildArch: noarch

# https://github.com/ryan-roemer/sphinx-bootstrap-theme.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_requires sphinx

%description
This Sphinx theme integrates the Twitter Bootstrap CSS / JavaScript
framework with various layout options, hierarchical menu navigation, and
mobile-friendly responsive design. It is configurable, extensible and
can use any number of different Bootswatch CSS themes.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE.txt *.rst
%python3_sitelibdir/*

%changelog
* Thu Mar 18 2021 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt3
- Drop python2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2.qa1
- NMU: applied repocop patch

* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.0-alt2
- Updated runtime dependencies for python-3.

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.0-alt1
- Updated to upstream version 0.6.0.
- Enabled build for python3.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.13-alt1
- automated PyPI update

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1
- VErsion 0.4.3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

