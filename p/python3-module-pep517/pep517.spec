%define _unpackaged_files_terminate_build 1
%define oname pep517

%def_with check

Name: python3-module-%oname
Version: 0.12.0
Release: alt1

Summary: API to call PEP 517 hooks for building Python packages

Group: Development/Python3
License: MIT
Url: https://github.com/pypa/pep517

BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(flit)

%if_with check
# install_requires:
BuildRequires: python3(tomli)

# tests
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
%endif

%py3_requires tomli

%description
PEP 517 specifies a standard API for systems which build Python packages.

%prep
%setup
%autopatch -p1

%build
# setup.py-less projects
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

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
export NO_INTERNET=YES
export TOX_TESTENV_PASSENV='NO_INTERNET'
tox.py3 --sitepackages --no-deps --console-scripts -vvr -s false

%files
%doc README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Tue Jan 11 2022 Stanislav Levin <slev@altlinux.org> 0.12.0-alt1
- 0.10.0 -> 0.12.0.

* Thu Apr 22 2021 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt2
- initial build for ALT Sisyphus

* Tue Apr 20 2021 Pablo Soldatoff <soldatoff@etersoft.ru> 0.10.0-alt1
- new version (0.10.0) with rpmgs script



