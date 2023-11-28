%define _unpackaged_files_terminate_build 1
%define pypi_name py-cpuinfo
%define mod_name cpuinfo

Name: python3-module-%mod_name
Version: 9.0.0
Release: alt2
Summary: Get CPU info with pure Python
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/py-cpuinfo
Vcs: https://github.com/workhorsy/py-cpuinfo
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch3500: 0001-Add-support-for-LoongArch.patch
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
Conflicts: python-module-%mod_name <= 3.3.0-alt2
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work without any
extra programs or libraries, beyond what your OS provides. It does not require
any compilation(C/C++, assembly, et cetera) to use. It works with Python 3.

%prep
%setup
%patch3500 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python3 test_suite.py

%files
%doc README.md
%_bindir/cpuinfo
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Aug 13 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 9.0.0-alt2
- Added LoongArch support.

* Tue May 02 2023 Stanislav Levin <slev@altlinux.org> 9.0.0-alt1
- 8.0.0 -> 9.0.0.

* Tue Oct 26 2021 Ivan A. Melnikov <iv@altlinux.org> 8.0.0-alt1
- 8.0.0
- backport RISC-V support from upstream

* Thu Jan 28 2021 Ivan A. Melnikov <iv@altlinux.org> 7.0.0-alt2
- MIPS support (https://github.com/workhorsy/py-cpuinfo/pull/160)

* Wed Aug 12 2020 Ivan A. Melnikov <iv@altlinux.org> 7.0.0-alt1
- 7.0.0

* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.3.0-alt3
- Version in conflict on py2 module added.

* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.3.0-alt2
- Build for python3 disabled.

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.0-alt1
- Initial build for ALT.
