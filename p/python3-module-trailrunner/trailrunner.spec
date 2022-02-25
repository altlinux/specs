%define _unpackaged_files_terminate_build 1
%define pypi_name trailrunner

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.2
Release: alt1

Summary: Run things on paths
License: MIT
Group: Development/Python3
# Source-git: https://github.com/omnilib/trailrunner.git
Url: https://pypi.org/project/trailrunner

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(flit.sdist)

%if_with check
# install_requires=
BuildRequires: python3(pathspec)

BuildRequires: python3(tox)
%endif

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
# flit build backend
# generate setup.py for legacy builder
%__python3 - <<-'EOF'
from pathlib import Path
from flit.sdist import SdistBuilder


with open("setup.py", "wb") as f:
    sd_builder = SdistBuilder.from_ini_path(Path("pyproject.toml"))
    f.write(sd_builder.make_setup_py())
EOF
%python3_build

%install
%python3_install

# don't package tests
rm -r %buildroot%python3_sitelibdir/%pypi_name/tests/

%check
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    python -m %pypi_name.tests -v
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version-py%_python3_version.egg-info/

%changelog
* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus.
