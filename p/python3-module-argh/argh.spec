%define _unpackaged_files_terminate_build 1

%define pypi_name argh
%define mod_name %pypi_name
%def_with check

Name: python3-module-%pypi_name
Version: 0.31.3
Release: alt1
Summary: Plain Python functions as CLI commands without boilerplate
License: LGPLv3
Group: Development/Python3
Url: https://pypi.org/project/argh/
Vcs: https://github.com/neithere/argh
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
Building a command-line interface? Found yourself uttering "argh!" while
struggling with the API of argparse? Don't like the complexity but need the
power?

Argh builds on the power of argparse (which comes with Python) and makes it
really easy to use. It eliminates the complex API and lets you "dispatch"
ordinary Python functions as CLI commands.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 15 2024 Stanislav Levin <slev@altlinux.org> 0.31.3-alt1
- 0.31.2 -> 0.31.3.

* Thu Jun 20 2024 Stanislav Levin <slev@altlinux.org> 0.31.2-alt1
- 0.26.2 -> 0.31.2.

* Sun Jan 28 2024 Grigory Ustinov <grenka@altlinux.org> 0.26.2-alt3
- Moved on modern pyproject macros.

* Mon Nov 29 2021 Stanislav Levin <slev@altlinux.org> 0.26.2-alt2
- Fixed FTBFS.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 0.26.2-alt1
- 0.26.1 -> 0.26.2.
- Stopped Python2 package build.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.26.1-alt1.git20141030.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.26.1-alt1.git20141030.2
- Fixed build spec with pytest3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.26.1-alt1.git20141030.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.26.1-alt1.git20141030.1
- NMU: Use buildreq for BR.

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.26.1-alt1.git20141030
- Initial build for Sisyphus

