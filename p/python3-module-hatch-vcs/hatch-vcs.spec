%define _unpackaged_files_terminate_build 1
%define pypi_name hatch-vcs
%define wheel_dir %_builddir/dist

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.0
Release: alt1

Summary: Hatch plugin for versioning with your preferred VCS
License: MIT
Group: Development/Python3
# Source-git: https://github.com/ofek/hatch-vcs.git
Url: https://pypi.org/project/hatch-vcs

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build frontend
BuildRequires: python3(build)
# build backend
BuildRequires: python3(hatchling)
# installer
BuildRequires: python3(installer)

%if_with check
# dependencies=
BuildRequires: python3(setuptools-scm)
BuildRequires: python3(hatchling)

BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

# PEP503 name
%py3_provides %pypi_name

# lazy import
%py3_requires setuptools_scm

%description
%pypi_name provides a plugin for Hatch that uses your preferred version control
system (like Git) to determine project versions.

%prep
%setup
%autopatch -p1

%build
%__python3 -m build --no-isolation --outdir %wheel_dir .

%install
%__python3 -m installer --destdir %buildroot %wheel_dir/hatch_vcs-%version-*.whl

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    {envbindir}/pytest -vra {posargs:tests}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr \
    --installpkg %wheel_dir/hatch_vcs-%version-*.whl

%files
%doc README.md
%python3_sitelibdir/hatch_vcs/
%python3_sitelibdir/hatch_vcs-%version.dist-info/

%changelog
* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus.
