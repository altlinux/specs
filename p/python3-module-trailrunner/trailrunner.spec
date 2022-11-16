%define _unpackaged_files_terminate_build 1
%define pypi_name trailrunner

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.1
Release: alt2

Summary: Run things on paths
License: MIT
Group: Development/Python3
# Source-git: https://github.com/omnilib/trailrunner.git
Url: https://pypi.org/project/trailrunner

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(flit_core)

# install_requires=
BuildRequires: python3(pathspec)

BuildArch: noarch

%description
trailrunner is a simple library for walking paths on the filesystem, and
executing functions for each file found. trailrunner obeys project level
.gitignore files, and runs functions on a process pool for increased
performance. trailrunner is designed for use by linting, formatting, and other
developer tools that need to find and operate on all files in project in a
predictable fashion with a minimal API.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

# don't package tests
rm -r %buildroot%python3_sitelibdir/%pypi_name/tests/

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    python -m %pypi_name.tests -v
EOF
%tox_check_pyproject

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Nov 16 2022 Michael Shigorin <mike@altlinux.org> 1.2.1-alt2
- BR: python3(pathspec) is requisite for %%build, not just %%check.

* Mon Sep 12 2022 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.1.3 -> 1.2.1.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 1.1.3-alt1
- 1.1.2 -> 1.1.3.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus.
