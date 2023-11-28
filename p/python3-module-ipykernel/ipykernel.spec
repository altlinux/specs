%define _unpackaged_files_terminate_build 1

%define oname ipykernel

%ifnarch ppc64le
%def_with check
%else
%def_without check
%endif

Name: python3-module-%oname
Version: 6.27.1
Release: alt1

Summary: IPython Kernel for Jupyter
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/ipykernel/
VCS: https://github.com/ipython/ipykernel.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-jupyter_client
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-comm
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-ipython
BuildRequires: python3-module-flaky
BuildRequires: python3-module-nest-asyncio
BuildRequires: python3-module-psutil
BuildRequires: python3-module-zmq
BuildRequires: python3-module-traitlets
BuildRequires: python3-module-tornado
BuildRequires: /proc
BuildRequires: /dev/pts
BuildRequires: python3-module-ipyparallel
BuildRequires: xvfb-run
BuildRequires: python3-module-trio
%endif

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
sed -i 's/--color=yes//' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

# ipykernel.tests.utils need by python3-module-numba
cp -r tests/ %buildroot%python3_sitelibdir/%oname/

%check
# Cause pytest error.
rm -rf examples/
%pyproject_run -- xvfb-run pytest -v -W ignore::DeprecationWarning -k 'not test_tk_loop'

%files
%doc README.*
%_datadir/jupyter
%python3_sitelibdir/ipykernel_launcher.py
%python3_sitelibdir/__pycache__/ipykernel_launcher.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Tue Nov 28 2023 Anton Vyatkin <toni@altlinux.org> 6.27.1-alt1
- New version 6.27.1.

* Wed Oct 25 2023 Anton Vyatkin <toni@altlinux.org> 6.26.0-alt1
- New version 6.26.0.

* Wed Sep 06 2023 Anton Vyatkin <toni@altlinux.org> 6.25.2-alt1
- New version 6.25.2.

* Wed Aug 23 2023 Anton Vyatkin <toni@altlinux.org> 6.25.1-alt1.1
- Fix FTBFS.

* Tue Aug 08 2023 Anton Vyatkin <toni@altlinux.org> 6.25.1-alt1
- New version 6.25.1.

* Wed Jul 26 2023 Anton Vyatkin <toni@altlinux.org> 6.25.0-alt1
- New version 6.25.0.

* Tue Jul 04 2023 Anton Vyatkin <toni@altlinux.org> 6.24.0-alt1
- New version 6.24.0.

* Sat Jun 24 2023 Anton Vyatkin <toni@altlinux.org> 6.23.3-alt1
- New version 6.23.3.

* Fri Jun 16 2023 Anton Vyatkin <toni@altlinux.org> 6.23.2-alt1
- New version 6.23.2.

* Fri Jun 09 2023 Anton Vyatkin <toni@altlinux.org> 6.23.1-alt1
- New version 6.23.1.

* Fri Mar 10 2023 Anton Vyatkin <toni@altlinux.org> 6.21.3-alt1
- New version 6.21.3.

* Fri Mar 10 2023 Anton Vyatkin <toni@altlinux.org> 6.21.2-alt1
- new version 6.21.2

* Thu Oct 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.0-alt2
- Updated build dependencies.

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

