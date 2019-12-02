%define _unpackaged_files_terminate_build 1
%define oname pytest-relaxed

%def_with check

Name: python-module-%oname
Version: 1.1.5
Release: alt2
Summary: pytest plugin for relaxed test discovery
License: BSD-2-Clause
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/pytest-relaxed/

# https://github.com/bitprophet/pytest-relaxed.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(decorator)
BuildRequires: python2.7(pytest)
BuildRequires: python3(decorator)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%py_provides %oname

%description
This pytest plugin takes a page from the rest of Python, where you don't have
to explicitly note public module/class members, but only need to hint as to
which ones are private. By default, all files and objects pytest is told to
scan will be considered tests; to mark something as not-a-test, simply prefix
it with an underscore.

%package -n python3-module-%oname
Summary: pytest plugin for relaxed test discovery
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This pytest plugin takes a page from the rest of Python, where you don't have
to explicitly note public module/class members, but only need to hint as to
which ones are private. By default, all files and objects pytest is told to
scan will be considered tests; to mark something as not-a-test, simply prefix
it with an underscore.

%prep
%setup
%autopatch -p1

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} -m pytest {posargs:-vra}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v -- -v

%files
%doc README.rst
%python_sitelibdir/pytest_relaxed/
%python_sitelibdir/pytest_relaxed-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/pytest_relaxed/
%python3_sitelibdir/pytest_relaxed-%version-py%_python3_version.egg-info/

%changelog
* Fri Dec 06 2019 Stanislav Levin <slev@altlinux.org> 1.1.5-alt2
- Fixed testing against Pytest 5.3+.

* Fri Oct 18 2019 Stanislav Levin <slev@altlinux.org> 1.1.5-alt1
- Initial build for Sisyphus.
