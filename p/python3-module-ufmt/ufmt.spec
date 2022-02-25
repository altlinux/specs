%define _unpackaged_files_terminate_build 1
%define pypi_name ufmt

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.2
Release: alt1

Summary: Safe, atomic formatting with black and usort
License: MIT
Group: Development/Python3
# Source-git: https://github.com/omnilib/ufmt.git
Url: https://pypi.org/project/ufmt

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(flit.sdist)

%if_with check
# install_requires=
BuildRequires: python3(black)
BuildRequires: python3(moreorless)
BuildRequires: python3(tomlkit)
BuildRequires: python3(trailrunner)
BuildRequires: python3(usort)

BuildRequires: python3(tox)
%endif

BuildArch: noarch

%description
%pypi_name is a safe, atomic code formatter for Python built on top of black and
usort. %pypi_name formats files in-memory, first with usort and then with black,
before writing any changes back to disk. This enables a combined, atomic step
in CI/CD workflows for checking or formatting files, without any with conflict
or intermediate changes between the import sorter and the code formatter.

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

# don't ship tests
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
tox.py3 --sitepackages -vvr

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version-py%_python3_version.egg-info/

%files -n %pypi_name
%_bindir/%pypi_name

%changelog
* Fri Feb 25 2022 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1
- 1.3.1 -> 1.3.2.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
