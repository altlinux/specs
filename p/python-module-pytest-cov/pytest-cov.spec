%define _unpackaged_files_terminate_build 1
%define oname pytest-cov

%def_with check

Name: python-module-%oname
Version: 2.6.1
Release: alt2

Summary: pytest plugin for coverage reporting with support for centralised and distributed testing
License: MIT
Group: Development/Python
# Source-git: https://github.com/pytest-dev/pytest-cov.git
Url: https://pypi.org/project/pytest-cov/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python-module-coverage
BuildRequires: python-module-fields
BuildRequires: python-module-process-tests
BuildRequires: python-module-pytest-xdist
BuildRequires: python-module-virtualenv
BuildRequires: python3-module-coverage
BuildRequires: python3-module-fields
BuildRequires: python3-module-process-tests
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-tox
%endif

BuildArch: noarch

%description
This plugin produces coverage reports. It supports centralised testing
and distributed testing in both load and each modes. It also supports
coverage of subprocesses.

All features offered by the coverage package should be available, either
through pytest-cov or through coverage's config file.

%package -n python3-module-%oname
Summary: pytest plugin for coverage reporting with support for centralised and distributed testing
Group: Development/Python3

%description -n python3-module-%oname
This plugin produces coverage reports. It supports centralised testing
and distributed testing in both load and each modes. It also supports
coverage of subprocesses.

All features offered by the coverage package should be available, either
through pytest-cov or through coverage's config file.

%prep
%setup
%patch -p1

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
# to read a custom pth-file one should add a such path to site-dir
# this only needs for tests at RPM build time
echo "import site;site.addsitedir(\"$(pwd)/src\")" > tests/sitecustomize.py
sed -i '/\[testenv\]/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    cp %_bindir\/py.test3 \{envbindir\}\/pytest\
    sed -i \x271c \#!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini

grep -qs '[[:space:]]*hunter[[:space:]]*$' tox.ini || exit 1
sed -i '/[[:space:]]*hunter[[:space:]]*$/d' tox.ini
# don't use a specific version
sed -i 's/==/>=/g' tox.ini

export PIP_NO_INDEX=YES
export TOX_TESTENV_PASSENV='RPM_BUILD_DIR'
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc README.rst CHANGELOG.rst
%python_sitelibdir/pytest-cov.pth
%python_sitelibdir/pytest_cov/
%python_sitelibdir/pytest_cov-*.egg-info/

%files -n python3-module-%oname
%doc README.rst CHANGELOG.rst
%python3_sitelibdir/pytest-cov.pth
%python3_sitelibdir/pytest_cov/
%python3_sitelibdir/pytest_cov-*.egg-info/

%changelog
* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 2.6.1-alt2
- Fixed build.

* Tue Jan 15 2019 Stanislav Levin <slev@altlinux.org> 2.6.1-alt1
- 2.6.0 -> 2.6.1.

* Mon Oct 29 2018 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1
- 2.4.0 -> 2.6.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.0-alt1.git20150823.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.0-alt1.git20150823.1
- NMU: Use buildreq for BR.

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.git20150823
- Version 2.1.0

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20150801
- New snapshot

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20150728
- Version 2.0.0

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1.git20141125
- New snapshot

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1.git20141106
- Version 1.8.1

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.git20140822
- Initial build for Sisyphus

