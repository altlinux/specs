%define oname futures
Name: python-module-%oname
Version: 2.1.4
Release: alt1
Summary: Backport of the concurrent.futures package from Python 3.2
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/futures
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
Backport of the concurrent.futures package from Python 3.2.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
#doc CHANGES docs/*.rst
%python_sitelibdir/*

%changelog
* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4-alt1
- Version 2.1.4

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.3-alt1
- Initial build for Sisyphus

