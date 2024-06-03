%define _unpackaged_files_terminate_build 1
%define oname RestrictedPython

%def_with check

Name: python3-module-%oname
Version: 7.1
Release: alt1
Summary: Provides a restricted execution environment for Python, e.g. for running untrusted code
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/RestrictedPython/
#Git: https://github.com/zopefoundation/RestrictedPython.git

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
RestrictedPython provides a restricted execution environment for Python,
e.g. for running untrusted code.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
        %buildroot%python3_sitelibdir/
%endif

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.txt
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info/

%changelog
* Mon Jun 03 2024 Grigory Ustinov <grenka@altlinux.org> 7.1-alt1
- Automatically updated to 7.1.

* Wed Jan 31 2024 Grigory Ustinov <grenka@altlinux.org> 7.0-alt1
- NMU: Automatically updated to 7.0.

* Sun Aug 27 2023 Nikolai Kostrigin <nickel@altlinux.org> 6.1-alt1
- 5.2 -> 6.1

* Thu Apr 07 2022 Stanislav Levin <slev@altlinux.org> 5.2-alt1
- 5.1 -> 5.2.

* Sun Feb 28 2021 Nikolai Kostrigin <nickel@altlinux.org> 5.1-alt1
- 5.0 -> 5.1

* Thu Jan 16 2020 Nikolai Kostrigin <nickel@altlinux.org> 5.0-alt1
- NMU: 4.0 -> 5.0
- Remove python2 module build
- Rearrange unittests execution
- Remove tests subpackage
- Fix license

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0-alt1.a3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0-alt1.a3
- Updated to upstream version 4.0a3.
- Enabled build with python-3.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2.dev.git20130312
- Added tests

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1.dev.git20130312
- Version 3.6.1dev

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt1.1
- Rebuild with Python-2.7

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

