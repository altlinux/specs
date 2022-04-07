%define _unpackaged_files_terminate_build 1
%define pypi_name usort

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.2
Release: alt1

Summary: A small, safe import sorter
License: MIT
Group: Development/Python3
# Source-git: https://github.com/facebookexperimental/usort.git
Url: https://pypi.org/project/usort

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(tox)
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

%build
# https://github.com/pypa/setuptools_scm/#environment-variables
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    python -m usort.tests -v
EOF
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version-py%_python3_version.egg-info/

%files -n %pypi_name
%_bindir/%pypi_name

%changelog
* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1
- 1.0.1 -> 1.0.2.

* Thu Feb 10 2022 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
