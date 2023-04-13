%define _unpackaged_files_terminate_build 1

%define oname ipython_genutils

Name: python3-module-%oname
Version: 0.2.0
Release: alt2
Summary: Vestigial utilities from IPython
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/ipython_genutils/

BuildArch: noarch

# https://github.com/ipython/ipython_genutils.git
Source: %name-%version.tar
Patch: remove-nose.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%description
Vestigial utilities from IPython.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Vestigial utilities from IPython.

This package contains tests for %oname.

%prep
%setup
%patch -p1

%build
%python3_build_debug

%install
%python3_install

%check
export LC_ALL=en_US.UTF-8
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3

%files
%doc COPYING.md
%doc README.md CONTRIBUTING.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info
%exclude %python3_sitelibdir/%oname/test*

%files tests
%python3_sitelibdir/%oname/test*

%changelog
* Thu Apr 13 2023 Anton Vyatkin <toni@altlinux.org> 0.2.0-alt2
- Fix BuildRequires

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt1
- Updated to upstream version 0.2.0.
- Disabled build for python-2.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

