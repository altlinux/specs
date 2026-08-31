%define _unpackaged_files_terminate_build 1
%define pypi_name ormsgpack
%define mod_name ormsgpack

%def_with check

Name: python3-module-%pypi_name
Version: 1.12.2
Release: alt1

Summary: Fast, correct Python msgpack library supporting dataclasses, datetimes, and numpy
License: Apache-2.0 OR MIT
Group: Development/Python3
Url: https://pypi.org/project/ormsgpack/
Vcs: https://github.com/ormsgpack/ormsgpack

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %pyproject_deps_config_name
Source3: config.toml
Patch0: %name-%version-alt.patch

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
ormsgpack is a fast MessagePack serialization library for Python derived from
orjson, with native support for various Python types.

%prep
%setup -a1
%autopatch -p1
install -vD %SOURCE3 .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# do not check datetime due to too old pendulum:
# https://bugzilla.altlinux.org/58620
%pyproject_run -- pytest -vra -k 'not test_datetime'

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Aug 31 2026 Anton Zhukharev <ancieg@altlinux.org> 1.12.2-alt1
- Packaged for ALT Sisyphus.
