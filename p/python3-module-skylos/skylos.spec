%define _unpackaged_files_terminate_build 1
%define pypi_name skylos
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 5.5.0
Release: alt1

Summary: Local-first PR scanner: dead code, security, secrets, quality, AI-code issues
License: Apache-2.0
Group: Development/Python3
Url: https://duriantaco.github.io/skylos
VCS: https://github.com/duriantaco/skylos

ExclusiveArch: %go_arches
# tree-sitter-language-pack is not built for i586
ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: pyproject_deps.json
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires(pre): rpm-build-golang
%pyproject_builddeps_build
%pyproject_runtimedeps_metadata

%if_with check
BuildRequires: git-core
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra test
%endif

AutoReq: yes, nopython3

%description
Skylos is an open-source static analysis CLI for Python, TypeScript,
JavaScript, Java, Go, Kotlin, PHP, Rust, Dart, C#, C++, Shell,
and deployment config. It runs locally by default and can
also be used as a CI/CD PR gate.

%package -n skylos-go
Summary: Go analysis engine for skylos
Group: Development/Other
Requires: %name = %EVR

%description -n skylos-go
Skylos is an open-source static analysis CLI for Python, TypeScript,
JavaScript, Java, Go, Kotlin, PHP, Rust, Dart, C#, C++, Shell,
and deployment config. It runs locally by default and can
also be used as a CI/CD PR gate.

This package contains the native engine used for Go code analysis.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build
export GOPROXY=off
export CGO_ENABLED=0
export GOCACHE=%_builddir/.gocache
cd %mod_name/engines/go
%gobuild -o skylos-go ./cmd/skylos-go

%install
%pyproject_install --platlib
install -Dpm0755 %mod_name/engines/go/skylos-go %buildroot%_bindir/skylos-go

%check
export SKYLOS_GO_BIN=$PWD/%mod_name/engines/go/skylos-go
# the tests expect a short temp dir and a git work tree
export TMPDIR=/tmp
git init -q
git add -A
# Run basic functionality tests; the full suite also checks analysis accuracy.
%pyproject_run_pytest -vra \
    test/test_cli.py \
    test/test_security_trace_integration.py \
    test/test_cleanup_cmd.py \
    test/test_done_gate.py \
    test/test_github_annotations.py \
    test/test_gitlab_report.py \
    test/test_git_context.py \
    test/test_agent_integration.py \
    test/test_sarif_exporter.py \
    test/test_ui_paths.py \
    test/test_integration.py \
    test/test_go_runner.py

%files
%doc README.md LICENSE docs
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{mod_name}_mcp/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n skylos-go
%doc LICENSE
%_bindir/skylos-go

%changelog
* Wed Nov 11 2026 Dmitry Mihalchenko <tascad@altlinux.org> 5.5.0-alt1
- Initial build for ALT Sisyphus.
