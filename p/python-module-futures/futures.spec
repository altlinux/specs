%define _unpackaged_files_terminate_build 1
%define oname futures
Name: python-module-%oname
Version: 3.0.5
Release: alt1
Summary: Backport of the concurrent.futures package from Python 3.2
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/futures
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/55/db/97c1ca37edab586a1ae03d6892b6633d8eaa23b23ac40c7e5bbc55423c78/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
Backport of the concurrent.futures package from Python 3.2.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%files
%doc CHANGES docs/*.rst
%python_sitelibdir/*

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.5-alt1
- automated PyPI update

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1
- Version 3.0.3

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1
- Version 2.2.0

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.6-alt1
- Version 2.1.6

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.5-alt1
- Version 2.1.5

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4-alt1
- Version 2.1.4

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.3-alt1
- Initial build for Sisyphus

