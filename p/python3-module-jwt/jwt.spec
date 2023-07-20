%define _unpackaged_files_terminate_build 1
%define pypi_name PyJWT
%define mod_name jwt

%def_with check

Name: python3-module-%mod_name
Version: 2.8.0
Release: alt1
Summary: JSON Web Token implementation in Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/PyJWT/
Vcs: https://github.com/jpadilla/pyjwt
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
Conflicts: python-module-%mod_name
Obsoletes: python-module-%mod_name
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
%pyproject_builddeps_metadata_extra crypto
%endif

BuildRequires(pre): rpm-build-python3

%description
A Python implementation of RFC 7519.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Wed Jul 19 2023 Stanislav Levin <slev@altlinux.org> 2.8.0-alt1
- 2.6.0 -> 2.8.0.

* Tue Jan 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.0-alt1
- 2.6.0 released

* Thu Jul 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.0-alt1
- 2.4.0 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.0-alt1
- 2.3.0 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0-alt1
- 2.1.0 released

* Tue Aug 03 2021 Grigory Ustinov <grenka@altlinux.org> 1.7.1-alt2
- Drop python2 support.

* Fri Nov 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.1-alt1
- 1.7.1 released

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20150118.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150118
- Version 0.4.1

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20140922
- Initial build for Sisyphus

