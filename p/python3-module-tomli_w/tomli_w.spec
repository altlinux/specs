%define _unpackaged_files_terminate_build 1
%define oname tomli_w

%def_with check

Name: python3-module-%oname
Version: 1.0.0
Release: alt1

Summary: A lil' TOML writer
License: MIT
Group: Development/Python3
# Source-git: https://github.com/hukkin/tomli-w.git
Url: https://pypi.org/project/tomli_w

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# PEP517 build backend
BuildRequires: python3(flit)

%if_with check
BuildRequires: python3(tomli)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

# PyPI name(dash, underscore)
%py3_provides tomli-w
Provides: python3-module-tomli-w = %EVR

%description
Tomli-W is a Python library for writing TOML. It is a write-only counterpart to
Tomli, which is a read-only TOML parser. Tomli-W is fully compatible with TOML
v1.0.0.

%prep
%setup
%autopatch -p1

%build
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

%check
# pyproject.toml already has configuration for tox, but it requires
# patching. It is simpler to override with own config.
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    pytest {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 -c tox.ini --sitepackages --console-scripts -vvr

%files
%doc README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Wed Jan 26 2022 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- 0.4.0 -> 1.0.0.

* Thu Oct 21 2021 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- 0.3.0 -> 0.4.0.

* Mon Oct 18 2021 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus.
