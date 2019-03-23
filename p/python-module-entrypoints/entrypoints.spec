%define _unpackaged_files_terminate_build 1
%define oname entrypoints

%def_with check

Name: python-module-%oname
Version: 0.3
Release: alt1
Summary: Discover and load entry points from installed packages
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/entrypoints

# https://github.com/takluyver/entrypoints.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(configparser)
BuildRequires: python2.7(json)
BuildRequires: python2.7(pytest)
BuildRequires: python3(tox)
%endif
%py_requires configparser

%description
Discover and load entry points from installed packages.

%package -n python3-module-%oname
Summary: Discover and load entry points from installed packages
Group: Development/Python3

%description -n python3-module-%oname
Discover and load entry points from installed packages.

%prep
%setup

cp -fR . ../python3

%build
%python_build_debug
pushd ../python3
%python3_build_debug
popd

%install
pushd ../python3
%python3_install
popd

%python_install

%check
cat > tox.ini <<EOF
[tox]
envlist = py27,py36,py37

[testenv]
commands =
    {envpython} -m pytest {posargs:-vra}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%python_sitelibdir/entrypoints.py*
%python_sitelibdir/entrypoints-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%python3_sitelibdir/entrypoints.py
%python3_sitelibdir/__pycache__/entrypoints.cpython-*
%python3_sitelibdir/entrypoints-%version-py%_python3_version.egg-info/

%changelog
* Fri Mar 22 2019 Stanislav Levin <slev@altlinux.org> 0.3-alt1
- 0.2.3 -> 0.3.

* Wed Dec 19 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.2.3-alt2
- Added egg-info

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.3-alt1
- Initial build for ALT.
