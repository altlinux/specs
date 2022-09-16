%define _unpackaged_files_terminate_build 1
%define pypi_name usort

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.5
Release: alt1

Summary: A small, safe import sorter
License: MIT
Group: Development/Python3
# Source-git: https://github.com/facebook/usort.git
Url: https://pypi.org/project/usort

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
# install_requires=
BuildRequires: python3(attr)
BuildRequires: python3(click)
BuildRequires: python3(libcst)
BuildRequires: python3(moreorless)
BuildRequires: python3(stdlibs)
BuildRequires: python3(toml)
BuildRequires: python3(trailrunner)
%endif

BuildArch: noarch

# python.req wrongly guess stdlibs is usort's module
%py3_requires stdlibs

%description
usort is a safe, minimal import sorter. Its primary goal is to make no
"dangerous" changes to code. This is achieved by detecting distinct "blocks" of
imports that are the most likely to be safely interchangeable, and only
reordering imports within these blocks without altering formatting. Code style
is left as an exercise for linters and formatters.

%package -n %pypi_name
Summary: Executable for %pypi_name
Group: Development/Python3
Requires: %name

%description -n %pypi_name
%summary

%prep
%setup
%autopatch -p1

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    python -m usort.tests -v
EOF
%tox_check_pyproject

%files
%doc README.md
%python3_sitelibdir/usort/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n %pypi_name
%_bindir/%pypi_name

%changelog
* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 1.0.5-alt1
- 1.0.2 -> 1.0.5.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1
- 1.0.1 -> 1.0.2.

* Thu Feb 10 2022 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
