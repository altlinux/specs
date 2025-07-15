%define _unpackaged_files_terminate_build 1
%define pypi_name httpx
%define mod_name %pypi_name

%def_with check

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%pyproject_runtimedeps_metadata_extra %1 \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 0.28.1
Release: alt1
Summary: A next generation HTTP client for Python
License: BSD-3-Clause
Group: Development/Python
Url: https://pypi.org/project/httpx/
Vcs: https://github.com/encode/httpx
BuildArch: noarch
Source0: %name-%version.tar
Source1: pyproject_deps.json
Patch0: %name-%version-alt.patch
# manually manage extra dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not packaged
%add_pyproject_deps_check_filter mkautodoc
%add_pyproject_deps_check_filter trio-typing
%pyproject_builddeps_metadata_extra zstd
%pyproject_builddeps_metadata_extra brotli
%pyproject_builddeps_metadata_extra cli
%pyproject_builddeps_metadata_extra http2
%pyproject_builddeps_metadata_extra socks
%pyproject_builddeps_check
%endif

%description
HTTPX is a fully featured HTTP client library for Python 3. It includes an
integrated command line client, has support for both HTTP/1.1 and HTTP/2, and
provides both sync and async APIs.

%add_python_extra cli
%add_python_extra http2
%add_python_extra socks
%add_python_extra brotli
%add_python_extra zstd

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vvra -Wignore -m 'not network'

%files
%_bindir/httpx
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jul 02 2025 Stanislav Levin <slev@altlinux.org> 0.28.1-alt1
- 0.27.0 -> 0.28.1.

* Tue Jun 04 2024 Stanislav Levin <slev@altlinux.org> 0.27.0-alt2
- Added missing runtime dependency on anyio.

* Mon May 06 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.27.0-alt1
- 0.27.0 released

* Wed Jan 24 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.26.0-alt1
- 0.26.0 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.24.0-alt1
- 0.24.0 released

* Thu Jul 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.23.0-alt2
- 0.23.0

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22.0-alt2
- drop upper bound on httpcore version

* Tue Feb 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22.0-alt1
- 0.22.0

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19.0-alt1
- 0.19.0

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.18.2-alt1
- 0.18.2

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Tue Apr 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.17.1-alt1
- new version 0.17.1 (with rpmrb script)

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.16.1-alt1
- 1.16.1

* Thu May 28 2020 Vitaly Lipatov <lav@altlinux.ru> 0.13.2-alt1
- initial build for Sisyphus
