%define _unpackaged_files_terminate_build 1

%define oname jupyter_client

%def_with check

Name: python3-module-%oname
Version: 8.6.1
Release: alt2
Summary: Jupyter protocol implementation and client libraries
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/jupyter-client/
Vcs: https://github.com/jupyter/jupyter_client/

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-ipykernel
BuildRequires: python3-module-ipython
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-jupyter
BuildRequires: python3-module-pytest-timeout
BuildRequires: openssh-clients
BuildRequires: iproute2
BuildRequires: python3-module-flaky
BuildRequires: python3-module-pexpect
%endif

%py3_provides %oname

# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %oname} = %EVR

%description
jupyter_client contains the reference implementation of the Jupyter protocol.
It also provides client and kernel management APIs for working with kernels.

It also provides the jupyter kernelspec entrypoint for installing
kernelspecs for use with Jupyter frontends.

%prep
%setup
sed -i '/--color=yes/d' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
sed -i '/localinterfaces._load_ips_ifconfig/d' tests/test_localinterfaces.py
%pyproject_run_pytest -v -k 'not test_input_request' \
		      --force-flaky --max-runs=3 --no-success-flaky-report

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info


%changelog
* Tue May 21 2024 Anton Zhukharev <ancieg@altlinux.org> 8.6.1-alt2
- Mapped PyPI name to distro's one.

* Wed Mar 13 2024 Anton Vyatkin <toni@altlinux.org> 8.6.1-alt1
- New version 8.6.1.

* Tue Mar 12 2024 Anton Vyatkin <toni@altlinux.org> 8.6.0-alt2
- Fixed FTBFS.

* Tue Nov 07 2023 Anton Vyatkin <toni@altlinux.org> 8.6.0-alt1
- New version 8.6.0.

* Wed Oct 25 2023 Anton Vyatkin <toni@altlinux.org> 8.5.0-alt1
- New version 8.5.0.

* Thu Oct 12 2023 Anton Vyatkin <toni@altlinux.org> 8.4.0-alt1
- New version 8.4.0.

* Fri Sep 29 2023 Anton Vyatkin <toni@altlinux.org> 8.3.1-alt2
- Fix FTBFS (use flaky for parallel kernel test).

* Wed Aug 30 2023 Anton Vyatkin <toni@altlinux.org> 8.3.1-alt1
- New version 8.3.1.

* Mon Jun 26 2023 Anton Vyatkin <toni@altlinux.org> 8.3.0-alt1
- New version 8.3.0 (Closes: #44225).

* Fri Jun 02 2023 Anton Vyatkin <toni@altlinux.org> 8.2.0-alt1
- New version 8.2.0.

* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 7.3.4-alt1
- Automatically updated to 7.3.4.

* Thu Oct 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 7.0.6-alt1
- Updated to upstream version 7.0.6.

* Thu Aug 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.0-alt1
- Updated to upstream version 6.2.0.

* Thu Jun 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.7-alt3
- Updated build dependencies.

* Fri Oct 23 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.7-alt2
- Updated build dependencies.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.7-alt1
- Updated to upstream version 6.1.7.
- Disabled build for python-2.

* Wed Jan 30 2019 Stanislav Levin <slev@altlinux.org> 5.1.0-alt2
- Applied upstream patches for Tornado5 support.

* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.0-alt1
- Updated to upstream release 5.1.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt2.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Enabled check

* Fri Aug 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus

