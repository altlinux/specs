%define _unpackaged_files_terminate_build 1
%define oname pytest-cov

%def_with check

Name: python-module-%oname
Version: 2.7.1
Release: alt1

Summary: pytest plugin for coverage reporting with support for centralised and distributed testing
License: MIT
Group: Development/Python
# Source-git: https://github.com/pytest-dev/pytest-cov.git
Url: https://pypi.org/project/pytest-cov/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(coverage)
BuildRequires: python2.7(fields)
BuildRequires: python2.7(process_tests)
BuildRequires: python2.7(pytest-xdist)
BuildRequires: python2.7(virtualenv)
BuildRequires: python3(coverage)
BuildRequires: python3(fields)
BuildRequires: python3(process_tests)
BuildRequires: python3(pytest-xdist)
BuildRequires: python3(tox)
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

grep -qsF 'time.sleep(1)' tests/test_pytest_cov.py || exit 1
sed -i 's/time\.sleep(1)/time.sleep(5)/g' tests/test_pytest_cov.py

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
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    cp %_bindir\/py.test3 \{envbindir\}\/pytest\
    sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini

grep -qs "'hunter',$" setup.py || exit 1
sed -i '/\x27hunter\x27,$/d' setup.py
# don't use a specific version
sed -i 's/==/>=/g' tox.ini setup.py

export PIP_NO_INDEX=YES
export PYTHONPATH_PY2=%_libdir/python%_python_version/site-packages
export PYTHONPATH_PY3=%_libdir/python3/site-packages
export TOX_TESTENV_PASSENV='PYTHONPATH_PY2 PYTHONPATH_PY3'
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -rv

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
* Fri May 03 2019 Stanislav Levin <slev@altlinux.org> 2.7.1-alt1
- 2.6.1 -> 2.7.1.

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

