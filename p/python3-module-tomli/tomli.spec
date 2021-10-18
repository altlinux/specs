%define _unpackaged_files_terminate_build 1
%define oname tomli

%def_with check

Name: python3-module-%oname
Version: 1.2.1
Release: alt1

Summary: A lil' TOML parser
License: MIT
Group: Development/Python3
# Source-git: https://github.com/hukkin/tomli.git
Url: https://pypi.org/project/tomli

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(dateutil)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%description
Tomli is a Python library for parsing TOML. Tomli is fully compatible with TOML
v1.0.0.

%prep
%setup
%autopatch -p1

%build
# tomli no longer provides setup.py, rpm-build-python3 cannot build
# setup.py-less projects. The following converter can be used to generate
# setup.py if the build backend is flit.

# from pathlib import Path
# from flit.sdist import SdistBuilder
#
# with open("setup.py", "wb") as f:
#     sd_builder = SdistBuilder.from_ini_path(Path("pyproject.toml"))
#     f.write(sd_builder.make_setup_py())
%python3_build

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --no-deps --console-scripts -vvr -s false

%files
%doc README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Wed Sep 29 2021 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.1.0 -> 1.2.1.

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- NMU: drop BR: python3-module-flit (publishing tool)

* Mon Jul 26 2021 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.

