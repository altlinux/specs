%define _unpackaged_files_terminate_build 1
%define pypi_name installer
%define wheel_dir %_builddir/dist

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.1
Release: alt1

Summary: A library for installing Python wheels
License: MIT
Group: Development/Python3
# Source-git: https://github.com/pypa/installer.git
Url: https://pypi.org/project/installer

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build frontend
BuildRequires: python3(build)
# build backend
BuildRequires: python3(flit_core)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%description
%pypi_name is a low-level library for installing a Python package from a
wheel distribution. It provides basic functionality and abstractions for
handling wheels and installing packages from wheels.

- Logic for "unpacking" a wheel (i.e. installation).
- Abstractions for various parts of the unpacking process.
- Extensible simple implementations of the abstractions.
- Platform-independent Python script wrapper generation.

%prep
%setup
%autopatch -p1

# don't ship `exe`s
find -type f -name '*.exe' -delete

%build
%__python3 -m build --no-isolation --outdir %wheel_dir .

%install
# install installer using installer
PYTHONPATH=src %__python3 -m installer \
    --destdir %buildroot \
    %wheel_dir/%pypi_name-%version-*.whl

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    {envbindir}/pytest -vra {posargs:tests}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr \
    --installpkg %wheel_dir/%pypi_name-%version-*.whl

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus.
