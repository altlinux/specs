%define _unpackaged_files_terminate_build 1
%define oname ipyparallel

%def_without check
%def_with bootstrap

Name: python3-module-%oname
Version: 8.6.1
Release: alt2
Summary: Interactive Parallel Computing with IPython
License: BSD-3-Clause
Group: Development/Python3
Url: https://ipyparallel.readthedocs.io/
Vcs: https://github.com/ipython/ipyparallel.git
BuildArch: noarch
Source: %name-%version.tar

Requires: python3-module-tqdm

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-entrypoints
BuildRequires: python3-module-psutil
BuildRequires: python3-module-ipykernel
BuildRequires: python3-module-ipython
BuildRequires: python3-module-ipython-tests
BuildRequires: python3-module-testpath
BuildRequires: python3-module-tornado
BuildRequires: python3-module-ipykernel
BuildRequires: python3-module-zmq
BuildRequires: python3-module-tqdm
BuildRequires: python3-module-decorator
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-jupyter_client
BuildRequires: python3-module-numpy-testing
BuildRequires: /proc
%endif

%if_with bootstrap
%add_python3_req_skip IPython
%add_python3_req_skip IPython.core
%add_python3_req_skip IPython.core.application
%add_python3_req_skip IPython.core.error
%add_python3_req_skip IPython.core.magic
%add_python3_req_skip IPython.core.profiledir
%add_python3_req_skip IPython.display
%add_python3_req_skip IPython.paths
%add_python3_req_skip IPython.utils.capture
%add_python3_req_skip IPython.utils.coloransi
%add_python3_req_skip IPython.utils.path
%add_python3_req_skip IPython.utils.text
%add_python3_req_skip ipykernel
%add_python3_req_skip ipykernel.comm
%add_python3_req_skip ipykernel.ipkernel
%add_python3_req_skip ipykernel.jsonutil
%add_python3_req_skip ipykernel.kernelapp
%add_python3_req_skip ipykernel.zmqshell
%add_python3_req_skip notebook.services.config
%endif

%description
Use multiple instances of IPython in parallel, interactively.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Use multiple instances of IPython in parallel, interactively.

This package contains tests for %oname.

%prep
%setup

%build
export IPP_DISABLE_JS=1
%pyproject_build

%install
%pyproject_install

# fix installation directory
mv %buildroot%_prefix%_sysconfdir %buildroot%_sysconfdir

%check
export TMPDIR=/tmp
%pyproject_run_pytest -v --color=no

%files
%doc *.md
%_bindir/*
%_sysconfdir/jupyter
%_datadir/jupyter
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Wed Oct 18 2023 Anton Vyatkin <toni@altlinux.org> 8.6.1-alt2
- Build with bootstrap.

* Mon Jun 12 2023 Anton Vyatkin <toni@altlinux.org> 8.6.1-alt1
- New version 8.6.1.

* Thu Apr 27 2023 Anton Vyatkin <toni@altlinux.org> 6.3.0-alt4
- Fix BuildRequires

* Thu Jun 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.3.0-alt3
- Updated build dependencies.

* Fri Oct 23 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.3.0-alt2
- Updated build dependencies.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.3.0-alt1
- Updated to upstream version 6.3.0.
- Dropped python-2 support.

* Fri May 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.1.0-alt3
- rebuild with all requires

* Fri May 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.1.0-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.dev.git20150819.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.1.0-alt1.dev.git20150819.1
- NMU: Use buildreq for BR.

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.dev.git20150819
- Initial build for Sisyphus

