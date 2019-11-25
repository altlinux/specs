%define oname facebook_utils

Name: python3-module-%oname
Version: 0.50.5
Release: alt1

Summary: Simple utilites for facebook integration
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/facebook_utils/
# https://github.com/jvanasco/facebook_utils.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
A collection of utilities for integrating user accounts with
Facebook.com.

Right now this handles oauth and graph operations.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt *.md
%python3_sitelibdir/*


%changelog
* Mon Nov 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.50.5-alt1
- version updated to 0.50.5
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.20.3-alt1.git20140717.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.20.3-alt1.git20140717.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20.3-alt1.git20140717
- Initial build for Sisyphus

