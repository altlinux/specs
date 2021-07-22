%define _unpackaged_files_terminate_build 1
%define oname pyyaml-env-tag

%def_with check

Name: python3-module-%oname
Version: 0.1
Release: alt1

Summary: Custom YAML tag for referencing environment variables in YAML files

License: MIT
Group: Development/Python3
# Source-git: https://github.com/waylan/pyyaml-env-tag.git
Url: https://pypi.org/project/pyyaml_env_tag/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires:
BuildRequires: python3(yaml)

BuildRequires: python3(flit)
BuildRequires: python3(tox)
%endif

BuildArch: noarch

# PyPI name(dash, underscore)
%py3_provides %oname

%description
A custom YAML tag for referencing environment variables in YAML files.

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
    python test_yaml_env_tag.py
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%doc README.md
%python3_sitelibdir/yaml_env_tag.py
%python3_sitelibdir/__pycache__/yaml_env_tag.cpython*
%python3_sitelibdir/pyyaml_env_tag-%version-py%_python3_version.egg-info/

%changelog
* Tue Jul 20 2021 Stanislav Levin <slev@altlinux.org> 0.1-alt1
- Initial build.
