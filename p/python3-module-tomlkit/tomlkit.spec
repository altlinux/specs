%define _unpackaged_files_terminate_build 1
%define oname tomlkit

%def_with check

Name: python3-module-%oname
Version: 0.9.1
Release: alt1

Summary: Style preserving TOML library
License: MIT
Group: Development/Python3
# Source-git: https://github.com/sdispater/tomlkit.git
Url: https://pypi.org/project/tomlkit

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(poetry-core)

%if_with check
BuildRequires: golang-github-burntsushi-toml-test
BuildRequires: python3(yaml)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%description
TOML Kit is a 1.0.0-compliant TOML library. It includes a parser that preserves
all comments, indentations, whitespace and internal element ordering, and makes
them accessible and editable via an intuitive API. You can also create new TOML
documents from scratch using the provided helpers.

%prep
%setup
%autopatch -p1

%build
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
# make use of system's toml-test
rm -r tests/toml-test
ln -s %_datadir/toml-test tests/
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false

%files
%doc README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Mon Feb 07 2022 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1
- 0.9.0 -> 0.9.1.

* Thu Feb 03 2022 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.
