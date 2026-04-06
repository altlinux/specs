%define _unpackaged_files_terminate_build 1
%define pypi_name deptry

%def_with check

Name: python3-module-%pypi_name
Version: 0.25.1
Release: alt1

Summary: A command line utility to check for unused, missing and transitive dependencies in a Python project
License: MIT
Group: Development/Tools
Url: https://pypi.org/project/deptry/
Vcs: https://github.com/fpgmaas/deptry

Source0: %name-%version.tar
Source1: vendor.tar
Source2: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_check
%pyproject_builddeps_metadata
%endif

%description
%summary.

%prep
%setup -a1
mkdir -p .cargo
cat << EOF >> .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/astral-sh/ruff?tag=0.15.6#e4c7f35"]
git = "https://github.com/astral-sh/ruff"
tag = "0.15.6"
rev = "e4c7f35"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[profile.release]
strip = false

EOF

sed -i 's/version = "[0-9]\+\.[0-9]\+\.[0-9]\+"/version = "%version"/' pyproject.toml

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest ./tests -m "not xdist_group" --deselect \
    "tests/functional/cli/test_cli.py::test_cli_config_does_not_supress_output"

%files
%_bindir/%pypi_name
%doc LICENSE README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Mar 30 2026 Timofei Fedotov <sovtouch@altlinux.org> 0.25.1-alt1
- Updated to 0.25.1.

* Wed Nov 26 2025 Timofei Fedotov <sovtouch@altlinux.org> 0.24.0-alt1
- Initial build for ALT Sisyphus.
