%define _unpackaged_files_terminate_build 1
%define pypi_name stdlibs

%def_with check

Name: python3-module-%pypi_name
Version: 2022.2.2
Release: alt1

Summary: List of packages in the stdlib
License: MIT
Group: Development/Python3
# Source-git: https://github.com/jreese/stdlibs.git
Url: https://pypi.org/project/stdlibs

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(flit.sdist)

%if_with check
BuildRequires: python3(tox)
%endif

BuildArch: noarch

%description
Simple list of top-level packages in Python's stdlib.

Note: If you only need the live module names on 3.10+, just use
sys.stdlib_module_names. This is not exactly a backport, but a static list of
those for most useful Python versions.

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
    python -m stdlibs.tests -v
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
* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 2022.2.2-alt1
- Initial build for Sisyphus.
