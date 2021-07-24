%define _unpackaged_files_terminate_build 1
%define oname yamlloader

%def_with check

Name: python3-module-%oname
Version: 1.1.0
Release: alt1

Summary: Ordered YAML loader and dumper for PyYAML
License: MIT
Group: Development/Python3
# Source-git: https://github.com/Phynix/yamlloader.git
Url: https://pypi.org/project/yamlloader

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires:
BuildRequires: python3(yaml)

BuildRequires: python3(pytest)
BuildRequires: python3(hypothesis)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%description
This module provides loaders and dumpers for PyYAML. Currently, an OrderedDict
loader/dumper is implemented, allowing to keep items order when loading resp.
dumping a file from/to an OrderedDict (Python 3.7+: Also regular dicts are
supported and are the default items to be loaded to. As of Python 3.7
preservation of insertion order is a language feature of regular dicts.).

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
commands =
    pytest -vra
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false

%files
%doc README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Fri Jul 23 2021 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
