%define _unpackaged_files_terminate_build 1
%define oname toml

%def_with check

Name: python-module-%oname
Version: 0.10.0
Release: alt1

Summary: A Python library for parsing and creating TOML.
License: MIT
Group: Development/Python
# Source-git: https://github.com/uiri/toml.git
Url: https://pypi.org/project/toml/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python-module-tox
BuildRequires: python-module-pytest-cov
BuildRequires: golang-github-BurntSushi-toml-test
BuildRequires: pytest
BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest-cov
BuildRequires: pytest3
%endif

BuildArch: noarch

%description
TOML aims to be a minimal configuration file format that's easy to read due to
obvious semantics. TOML is designed to map unambiguously to a hash table. TOML
should be easy to parse into data structures in a wide variety of languages.
This package loads toml file into python dictionary and dump dictionary into
toml file.

%package -n python3-module-%oname
Summary: A Python3 library for parsing and creating TOML.
Group: Development/Python3

%description -n python3-module-%oname
TOML aims to be a minimal configuration file format that's easy to read due to
obvious semantics. TOML is designed to map unambiguously to a hash table. TOML
should be easy to parse into data structures in a wide variety of languages.
This package loads toml file into python dictionary and dump dictionary into
toml file.

%prep
%setup
rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
%python3_install
popd

%python_install

%check
export PIP_INDEX_URL=http://host.invalid./
ln -s %_datadir/toml-test toml-test

# copy nessecary exec deps
tox --sitepackages -e py%{python_version_nodots python} --notest
cp -f %_bindir/pytest .tox/py%{python_version_nodots python}/bin/

tox --sitepackages -e py%{python_version_nodots python} -v -- -v

pushd ../python3
ln -s %_datadir/toml-test toml-test
# copy nessecary exec deps
tox.py3 --sitepackages -e py%{python_version_nodots python3} --notest
cp -f %_bindir/pytest3 .tox/py%{python_version_nodots python3}/bin/pytest

tox.py3 --sitepackages -e py%{python_version_nodots python3} -v -- -v
popd

%files
%python_sitelibdir/toml/
%python_sitelibdir/toml-*.egg-info/

%files -n python3-module-%oname
%python3_sitelibdir/toml/
%python3_sitelibdir/toml-*.egg-info/

%changelog
* Tue Oct 09 2018 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- Initial build for sisyphus.

