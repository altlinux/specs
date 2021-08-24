%define _unpackaged_files_terminate_build 1

%define oname ipykernel

Name: python3-module-%oname
Version: 6.2.0
Release: alt1
Summary: IPython Kernel for Jupyter
License: BSD-3-Clause
Group: Development/Python3
Url: https://ipython.readthedocs.io/en/stable/

BuildArch: noarch

# https://github.com/ipython/ipykernel.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
BuildRequires: python3(IPython)
BuildRequires: python3(IPython.testing.tests)
BuildRequires: python3(flaky)
BuildRequires: python3(numpy.testing)

%add_python3_req_skip gtk

%description
This package provides the IPython kernel for Jupyter.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package provides the IPython kernel for Jupyter.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
rm -fR build
PYTHONPATH=$(pwd) py.test3 -vv

%files
%doc *.md examples
%_datadir/jupyter
%python3_sitelibdir/ipykernel_launcher.py
%python3_sitelibdir/__pycache__/ipykernel_launcher.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/*/tests

%files tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/*/tests

%changelog
* Tue Aug 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.0-alt1
- Updated to upstream version 6.2.0.

* Thu Jun 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.3.4-alt2
- Updated build dependencies.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.3.4-alt1
- Updated to upstream version 5.3.4.
- Dropped python-2 support.

* Wed Jan 30 2019 Stanislav Levin <slev@altlinux.org> 4.6.1-alt4
- Fixed testing (applied upstream patches for support for tornado5,
  closes: #35981).

* Fri May 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.6.1-alt3.1
- rebuild with all requires

* Fri May 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.6.1-alt3
- rebuild with python3.6

* Wed Nov 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.6.1-alt1
- Updated to upstream version 4.6.1.

* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.3-alt3
- Fixed build

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.3-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.3-alt2.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt2
- Enabled check

* Fri Aug 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Initial build for Sisyphus

