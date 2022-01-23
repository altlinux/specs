%define _unpackaged_files_terminate_build 1
%define oname entrypoints

%def_with check

Name: python3-module-%oname
Version: 0.3
Release: alt3
Summary: Discover and load entry points from installed packages
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/entrypoints

# https://github.com/takluyver/entrypoints.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(flit)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%description
Discover and load entry points from installed packages.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
cat > tox.ini <<EOF
[tox]
envlist = py3
usedevelop = True

[testenv]
commands =
    {envpython} -m pytest {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false

%files
%python3_sitelibdir/entrypoints.py
%python3_sitelibdir/__pycache__/entrypoints.cpython-*
%python3_sitelibdir/entrypoints-%version-py%_python3_version.egg-info/

%changelog
* Mon Jan 17 2022 Stanislav Levin <slev@altlinux.org> 0.3-alt3
- Fixed FTBFS (setuptools 60+).

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 0.3-alt2
- Built Python3 package from its ows src.

* Fri Mar 22 2019 Stanislav Levin <slev@altlinux.org> 0.3-alt1
- 0.2.3 -> 0.3.

* Wed Dec 19 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.2.3-alt2
- Added egg-info

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.3-alt1
- Initial build for ALT.
