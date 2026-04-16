%define _unpackaged_files_terminate_build 1
%define pypi_name xonsh-rd-parser
%def_with check

Name: python3-module-%pypi_name
Version: 1.7.0
Release: alt1

Summary: A Rust based, recursive descent parser for Xonsh
License: MIT
Group: Development/Python3
Url: https://github.com/jnoortheen/xonsh-rd-parser
Vcs: https://github.com/jnoortheen/xonsh-rd-parser.git

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: %name-%version-vendor.tar
Patch0: 0001-Fix-build-without-nightly-rust-features.patch
# https://github.com/jnoortheen/xonsh-rd-parser/issues/29
Patch1: xonsh-rd-parser-1.6.0-tests-drop-excessive-dependency-on-pytest-subtests.patch
%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

BuildRequires(pre): rpm-build-pyproject
BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: python3-dev

%if_with check
%pyproject_builddeps_metadata
# pytest-memray is only used in manual benchmarks (poe bench), not in the test suite.
%add_pyproject_deps_check_filter 'pytest-memray$'
# xonsh depends on xonsh-rd-parser, avoid circular build dependency.
%add_pyproject_deps_check_filter 'xonsh$'
%pyproject_builddeps_check
%endif

%description
Core parsing engine for xonsh (cross-platform shell).  Implements predictive
recursive descent parsing to handle xonshs unique combination of Python and
shell syntax.  Generates optimized AST for command execution.

%prep
%setup -a2
%autopatch -p1

mkdir -pv .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/astral-sh/ruff.git?tag=0.12.8"]
git = "https://github.com/astral-sh/ruff.git"
tag = "0.12.8"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

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
%pyproject_run_pytest

%files
%python3_sitelibdir/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Apr 16 2026 Ajrat Makhmutov <rauty@altlinux.org> 1.7.0-alt1
- New version.
- Drop excessive dependency on pytest-memray from build requires.

* Wed Feb 25 2026 Stanislav Levin <slev@altlinux.org> 1.6.0-alt2
- NMU: fixed FTBFS (pytest 9).

* Fri Jun 27 2025 Ivan Khanas <xeno@altlinux.org> 1.6.0-alt1
- First build for ALT.
