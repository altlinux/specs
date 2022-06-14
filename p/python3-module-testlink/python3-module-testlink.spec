%define _unpackaged_files_terminate_build 1
%define oname testlink

Name: python3-module-%oname
Version: 0.8.1
Release: alt5
Summary: A Python client to use the TestLink API
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/lczub/TestLink-API-Python-client
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
TestLink-API-Python-client is a Python XML-RPC client for TestLink.

%prep
%setup

%build
%python3_build

%install
%python3_install
cp -r example test %buildroot%python3_sitelibdir/%oname

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/TestLink_API_Python_client-%version-py%_python3_version.egg-info
%doc LICENSE-2.0.txt doc/{install.rst,usage.rst}

%changelog
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
