%define _unpackaged_files_terminate_build 1
%define pypi_name ini2toml

%def_with check

Name: python3-module-%pypi_name
Version: 0.10
Release: alt1

Summary: Automatically conversion of .ini/.cfg files to TOML equivalents
License: MPL-2.0
Group: Development/Python3
# Source-git: https://github.com/abravalheri/ini2toml.git
Url: https://pypi.org/project/ini2toml

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
# install_requires=
BuildRequires: python3(packaging)

# extras
BuildRequires: python3(configupdater)
BuildRequires: python3(tomlkit)
BuildRequires: python3(tomli-w)
BuildRequires: python3(validate-pyproject)
BuildRequires: python3(pyproject-fmt)

BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

# try-except import
%py3_requires packaging

# manually manage extra dependencies
%filter_from_requires /python3(tomlkit\(\..*\)\?)/d
%filter_from_requires /python3(tomli_w\(\..*\)\?)/d
%filter_from_requires /python3(configupdater\(\..*\)\?)/d

%description
The original purpose of this project is to help migrating setup.cfg files to
PEP621, but by extension it can also be used to convert any compatible .ini/.cfg
file to TOML.

%package lite
Summary: %summary
Group: Development/Python3
Requires: %name
%py3_requires tomli-w

%description lite
Extra 'lite' for %pypi_name.

%package full
Summary: %summary
Group: Development/Python3
Requires: %name
%py3_requires configupdater
%py3_requires tomlkit

%description full
Extra 'full' for %pypi_name.

%prep
%setup
%autopatch -p1

# if build from git source tree
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM. These files will be packaged unless filtered by MANIFEST.in.
git init
git config user.email author@example.com
git config user.name author
git add .
git commit -m 'release'
git tag '%version'

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false --develop

%files
%doc README.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version-py%_python3_version.egg-info/

%files lite

%files full

%changelog
* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 0.10-alt1
- Initial build for Sisyphus.
