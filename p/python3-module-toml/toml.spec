%define _unpackaged_files_terminate_build 1
%define oname toml

%def_with check

Name: python3-module-%oname
Version: 0.10.1
Release: alt1

Summary: A Python library for parsing and creating TOML.
License: MIT
Group: Development/Python3
# Source-git: https://github.com/uiri/toml.git
Url: https://pypi.org/project/toml/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: golang-github-burntsushi-toml-test
BuildRequires: python3(numpy)
BuildRequires: python3(tox)
%endif

BuildArch: noarch
%py3_requires numpy

%description
TOML aims to be a minimal configuration file format that's easy to read due to
obvious semantics. TOML is designed to map unambiguously to a hash table. TOML
should be easy to parse into data structures in a wide variety of languages.
This package loads toml file into python dictionary and dump dictionary into
toml file.

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install

%check
ln -s %_datadir/toml-test toml-test
sed -i '/^\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py3: _PYTEST_BIN=%_bindir\/py.test3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%python3_sitelibdir/toml/
%python3_sitelibdir/toml-*.egg-info/

%changelog
* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 0.10.1-alt1
- 0.10.0 -> 0.10.1.
- Built Python3 module from its own src package.

* Mon Apr 27 2020 Stanislav Levin <slev@altlinux.org> 0.10.0-alt4
- Applied upstream fix.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 0.10.0-alt3
- Fixed testing against Pytest 5.

* Fri Mar 15 2019 Stanislav Levin <slev@altlinux.org> 0.10.0-alt2
- Fixed FTBFS.

* Tue Oct 09 2018 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- Initial build for sisyphus.

