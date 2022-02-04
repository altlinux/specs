%define _unpackaged_files_terminate_build 1
%define pypi_name poetry-core

%def_without bootstrap
%def_with check

%if_with bootstrap
# poetry bundles several packages some of which require poetry to be built
%def_with vendored
%else
%def_without vendored
%endif

%if_with vendored
%define build_req_filter() %(for mod in %{*}; do echo -n "/python3(${mod}\\(\\..*\\)\\?)/d;"; done; )
%else
%define build_vendor_buildreq() %(for mod in %{*}; do echo -n "python3(${mod}) "; done; )
%endif

Name: python3-module-%pypi_name
Version: 1.0.7
Release: alt2

Summary: Poetry Core
License: MIT
Group: Development/Python3
# Source-git: https://github.com/python-poetry/poetry-core.git
Url: https://pypi.org/project/poetry-core

Source0: %name-%version.tar
Source1: vendored_pkg.list
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_without vendored
# unvendored packages
BuildRequires: %build_vendor_buildreq %(echo `cat %{SOURCE1}`)
%endif

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)

BuildRequires: /usr/bin/git
BuildRequires: python3(pep517)
%endif

BuildArch: noarch

# PEP503 name
%py3_provides %pypi_name

%if_with vendored
# drop deps on system packages which were bundled
%filter_from_requires %build_req_filter %(echo `cat %{SOURCE1}`)

%add_findreq_skiplist %python3_sitelibdir/poetry/core/_vendor/*
%add_findprov_skiplist %python3_sitelibdir/poetry/core/_vendor/*
%endif

%description
A PEP 517 build backend implementation developed for Poetry. This project is
intended to be a light weight, fully compliant, self-contained package allowing
PEP 517 compatible build frontends to build Poetry managed projects.

%prep
%setup
%autopatch -p1

%build
# check if actual bundled modules list is synced to expected one
set -o pipefail
PYTHONPATH="$(pwd)" %__python3 - <<-'EOF' | sort -u > actual.pkg.list
import pkgutil
for mod in pkgutil.iter_modules(["./poetry/core/_vendor"]):
    if not mod.name.startswith("_"):
        print(mod.name)
EOF
cat %SOURCE1 | sort -u > expected.pkg.list
diff -y expected.pkg.list actual.pkg.list

%if_without vendored
# unbundle packages
rm -r poetry/core/_vendor/*
%endif

# current working directory will be prepended to sys.path
# generate legacy setup.py, PEP517 builds are not currently supported
%__python3 - <<-'EOF'
from pathlib import Path

from poetry.core.factory import Factory
from poetry.core.masonry.builders.sdist import SdistBuilder


poetry = Factory().create_poetry(Path(".").resolve(), with_dev=False)
builder = SdistBuilder(poetry)

setup = builder.build_setup()

with open("setup.py", "wb") as f:
    f.write(setup)
EOF

%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    {envbindir}/pytest {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false

%files
%doc README.md
%python3_sitelibdir/poetry/
%python3_sitelibdir/poetry_core-%version-py%_python3_version.egg-info/

%changelog
* Fri Feb 04 2022 Stanislav Levin <slev@altlinux.org> 1.0.7-alt2
- Built without vendored distributions

* Fri Jan 28 2022 Stanislav Levin <slev@altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus.

