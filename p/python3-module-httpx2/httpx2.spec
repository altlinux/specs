%define _unpackaged_files_terminate_build 1
%define pypi_name httpx2
%define module_name httpx2
%define src_dir src/%pypi_name
%define tests_dir ../../tests/%pypi_name
%def_with check

%define _add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%pyproject_runtimedeps_metadata_extra %1 \
%%description -n %%name+%1 \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 2.9.1
Release: alt1

Summary: A next generation HTTP client for Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/httpx2/
Vcs: https://github.com/pydantic/httpx2
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
Requires: python3-module-httpcore2 = %version

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter 'trio-typing$'
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra cli
%pyproject_builddeps_metadata_extra http2
%pyproject_builddeps_metadata_extra socks
%pyproject_builddeps_metadata_extra ws
%pyproject_builddeps_metadata_extra zstd
%pyproject_builddeps_check
%endif

%_add_python_extra brotli
%_add_python_extra cli
%_add_python_extra http2
%_add_python_extra socks
%_add_python_extra ws
%_add_python_extra zstd

%description
HTTPX2 is a fully featured HTTP client library for Python. It
includes an integrated command line client, has support for both
HTTP/1.1 and HTTP/2, and provides both sync and async APIs.

%prep
%setup
%autopatch -p1
cd %src_dir
sed -i '/^fallback-version/s/= ".*"/= "%version"/' pyproject.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
cd -
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
cd %src_dir
%pyproject_build
cd -

%install
cd %src_dir
%pyproject_install
cd -

%check
cd %src_dir
%pyproject_run_pytest %tests_dir \
    --ignore=%tests_dir/models/test_whatwg.py \
    -m 'not network'
cd -

%files
%doc README.md LICENSE.md
%_bindir/%pypi_name
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jul 28 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.9.1-alt1
- Updated to 2.9.1.

* Fri Jul 24 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.7.0-alt1
- Updated to 2.7.0.

* Fri Jul 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.5.0-alt1
- Updated to 2.5.0.
- Split package: moved httpcore2 to a separate source package.

* Thu Jun 11 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.4.0-alt1
- Updated to 2.4.0.

* Wed Jun 10 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.3.0-alt1
- Initial build for ALT Sisyphus.
