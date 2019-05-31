%define _unpackaged_files_terminate_build 1
%define oname pytest-shutil

%def_with check

Name: python-module-%oname
Version: 1.7.0
Release: alt1
Summary: A goodie-bag of unix shell and environment tools for py.test
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-shutil
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(contextlib2)
BuildRequires: python2.7(execnet)
BuildRequires: python2.7(mock)
BuildRequires: python2.7(path.py)
BuildRequires: python2.7(pytest)
BuildRequires: python2.7(termcolor)
BuildRequires: python3(contextlib2)
BuildRequires: python3(execnet)
BuildRequires: python3(mock)
BuildRequires: python3(path.py)
BuildRequires: python3(termcolor)
BuildRequires: python3(tox)
%endif

%py_requires contextlib2
%py_requires path.py
%py_requires termcolor

%description
This library is a goodie-bag of Unix shell and environment management tools for
automated tests. A summary of the available functions is below, look at the
source for the full listing.

%package -n python3-module-%oname
Summary: A goodie-bag of unix shell and environment tools for py.test
Group: Development/Python3
%py3_requires contextlib2
%py3_requires path.py
%py3_requires termcolor

%description -n python3-module-%oname
This library is a goodie-bag of Unix shell and environment management tools for
automated tests. A summary of the available functions is below, look at the
source for the full listing.

%prep
%setup -n %oname-%version

# fix dependency
sed -i -e 's:setuptools-git:setuptools:g' \
	common_setup.py

cp -fR . ../python3

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
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} -m pytest {posargs:-vra}
EOF
# HOME env variable is used for testing
export TOX_TESTENV_PASSENV='HOME'
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc CHANGES.md README.md
%python_sitelibdir/pytest_shutil/
%python_sitelibdir/pytest_shutil-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%doc CHANGES.md README.md
%python3_sitelibdir/pytest_shutil/
%python3_sitelibdir/pytest_shutil-%version-py%_python3_version.egg-info/

%changelog
* Fri May 31 2019 Stanislav Levin <slev@altlinux.org> 1.7.0-alt1
- 1.6.0 -> 1.7.0.

* Fri Mar 22 2019 Stanislav Levin <slev@altlinux.org> 1.6.0-alt2
- Fixed minor typo in tox.ini.

* Fri Mar 22 2019 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1
- 1.2.11 -> 1.6.0.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.11-alt1.qa1
- NMU: applied repocop patch

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.11-alt1
- Initial build for ALT.
