Name: python3-module-aiohappyeyeballs
Version: 2.4.0
Release: alt1

Summary: Happy Eyeballs
License: PSF-2.0
Group: Development/Python
Url: https://pypi.org/project/aiohappyeyeballs/

Source0: %name-%version-%release.tar

BuildArch: noarch

BuildRequires: rpm-build-pyproject
BuildRequires: python3(poetry-core)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(pytest-asyncio)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/aiohappyeyeballs
%python3_sitelibdir/aiohappyeyeballs-%version.dist-info

%changelog
* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.4.0-alt1
- 2.4.0 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.2-alt1
- 2.3.2 released

