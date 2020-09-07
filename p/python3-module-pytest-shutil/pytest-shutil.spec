%define _unpackaged_files_terminate_build 1
%define oname pytest-shutil

%def_with check

Name: python3-module-%oname
Version: 1.7.0
Release: alt3
Summary: A goodie-bag of unix shell and environment tools for py.test
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-shutil
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(contextlib2)
BuildRequires: python3(execnet)
BuildRequires: python3(mock)
BuildRequires: python3(path)
BuildRequires: python3(termcolor)
BuildRequires: python3(tox)
%endif

%description
This library is a goodie-bag of Unix shell and environment management tools for
automated tests. A summary of the available functions is below, look at the
source for the full listing.

%prep
%setup -n %oname-%version

# fix dependency
sed -i -e 's:setuptools-git:setuptools:g' \
	common_setup.py

%build
ptrn="'path.py',"
{ grep -s -l "$ptrn" setup.py | xargs \
    sed -i -e "s/\(^[[:space:]]*\)$ptrn[[:space:]]*$/\1'path',/"; } || exit 1
%python3_build

%install
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} -m pytest {posargs:-vra}
EOF
# HOME env variable is used for testing
export TOX_TESTENV_PASSENV='HOME'
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -vvr

%files
%doc CHANGES.md README.md
%python3_sitelibdir/pytest_shutil/
%python3_sitelibdir/pytest_shutil-%version-py%_python3_version.egg-info/

%changelog
* Mon Sep 07 2020 Stanislav Levin <slev@altlinux.org> 1.7.0-alt3
- Stopped build Python2 package.

* Mon May 04 2020 Stanislav Levin <slev@altlinux.org> 1.7.0-alt2
- Fixed FTBFS.

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
