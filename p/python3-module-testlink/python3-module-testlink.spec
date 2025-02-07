%define _unpackaged_files_terminate_build 1
%define module_name testlink
%define pypi_name TestLink_API_Python_client
%def_with check

Name: python3-module-%module_name
Version: 0.8.1
Release: alt10.1
Summary: A Python client to use the TestLink API
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/lczub/TestLink-API-Python-client
Source: %name-%version.tar
Patch1: alt-disable-online-tests.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
TestLink-API-Python-client is a Python XML-RPC client for TestLink.

%prep
%setup
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install
cp -r example %buildroot%python3_sitelibdir/%module_name

%check
%tox_check_pyproject

%files
%python3_sitelibdir/%module_name
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Fri Feb 07 2025 Stanislav Levin <slev@altlinux.org> 0.8.1-alt10.1
- NMU: fixed FTBFS (tox 4).

* Wed Aug 07 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.1-alt10
- Packed examples.
- Fixed post-install unowned files.

* Tue Jun 04 2024 Evgeny Shesteperov <alimektor@altlinux.org> 0.8.1-alt9
- Added updateTestSuiteParentID function.

* Mon May 27 2024 Evgeny Shesteperov <alimektor@altlinux.org> 0.8.1-alt8
- Added updateTestCaseVersionToTheLatest function.

* Tue May 21 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.1-alt7
- createPlatform(): Added support for platformondesign and platformonexecution args.

* Sat Jan 20 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.1-alt6
- Enabled offline tests.

* Fri Jun 10 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.1-alt5
- Added closeBuild function
- Removed patches
- Removed Packager tag
- Fixed License tag

* Mon May 30 2022 Mikhail Chernonog <snowmix@altlinux.org> 0.8.1-alt4
- Fix name of the activeBuildInTestPlan function in patch

* Wed Apr 20 2022 Mikhail Chernonog <snowmix@altlinux.org> 0.8.1-alt3
- Add inactive and active feature for build in testplan

* Thu Oct 31 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.1-alt2
- Add inactive and active feature for testplan

* Tue Oct 29 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.1-alt1
- New version

* Thu Oct 17 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.4-alt1
- Initial build for ALT
