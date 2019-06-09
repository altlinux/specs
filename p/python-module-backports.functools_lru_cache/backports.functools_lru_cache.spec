%define _unpackaged_files_terminate_build 1
%define oname backports.functools_lru_cache

Name:           python-module-%oname
Version:        1.5
Release:        alt1
Summary:        Backport of functools.lru_cache from Python 3.3 as published at ActiveState.
Group:          Development/Python
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/backports.functools_lru_cache

# https://github.com/jaraco/backports.functools_lru_cache.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(pytest)
BuildRequires: python2.7(tox)
%py_requires backports
%py_provides backports.functools_lru_cache

%description
Backport of functools.lru_cache from Python 3.3 as published at ActiveState.

%prep
%setup
# remove extra dep
grep -qsF 'collective.checkdocs' setup.py || exit 1
sed -i '/collective\.checkdocs/d' setup.py
# don't check docs
sed -i '/python setup\.py checkdocs/d' tox.ini

# don't use scm to determine version, just substitute it
sed -i \
	-e 's|setuptools_scm|setuptools|g' \
	-e "s|use_scm_version=.*|version='%version',|g" \
	setup.py

%build
%python_build

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

rm -f %buildroot%python_sitelibdir/backports/__init__.py*

%check
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    cp %_bindir\/py.test \{envbindir\}\/py.test\
    sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python}
tox --sitepackages -p auto -o -v

%files
%doc README.rst
%python_sitelibdir/*

%changelog
* Sun Jun 09 2019 Stanislav Levin <slev@altlinux.org> 1.5-alt1
- 1.4 -> 1.5.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1.qa1
- NMU: applied repocop patch

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4-alt1
- Initial build for ALT.
