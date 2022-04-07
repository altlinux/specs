%define _unpackaged_files_terminate_build 1
%define pypi_name pyproject-fmt
%define wheel_dir %_builddir/dist

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.3
Release: alt1

Summary: Format pyproject.toml file
License: MIT
Group: Development/Python3
# Source-git: https://github.com/tox-dev/pyproject-fmt.git
Url: https://pypi.org/project/pyproject-fmt

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build frontend
BuildRequires: python3(build)
# build backend
BuildRequires: python3(hatchling)
BuildRequires: python3(hatch-vcs)
# wheel installer
BuildRequires: python3(installer)

%if_with check
# dependencies=
BuildRequires: python3(packaging)
BuildRequires: python3(tomlkit)

BuildRequires: python3(pytest)
BuildRequires: python3(pytest-mock)
BuildRequires: python3(tox)
%endif

BuildArch: noarch

# PEP503 name
%py3_provides %pypi_name

%description
%summary.

%prep
%setup
%autopatch -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%__python3 -m build --no-isolation --outdir %wheel_dir .

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%__python3 -m installer --destdir %buildroot %wheel_dir/pyproject_fmt-%version-*.whl

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    # some imports rely on cwd in sys.path
    python -m pytest -vra {posargs:tests}
EOF
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr \
    --installpkg %wheel_dir/pyproject_fmt-%version-*.whl

%files
%doc README.md
%_bindir/%pypi_name
%python3_sitelibdir/pyproject_fmt/
%python3_sitelibdir/pyproject_fmt-%version.dist-info/

%changelog
* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus.
