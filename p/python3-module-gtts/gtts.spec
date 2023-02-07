Name: python3-module-gtts
Version: 2.3.1
Release: alt1

Summary: Python interface with Google Translate's TTS API
License: MIT
Group: Development/Python
Url: https://pypi.org/project/gTTS/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(click)
BuildRequires: python3(requests)
BuildRequires: python3(testfixtures)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# nb: most are online
%pyproject_run_pytest ||:

%files
%_bindir/gtts-cli
%python3_sitelibdir/gtts
%exclude %python3_sitelibdir/gtts/tests
%python3_sitelibdir/gTTS-%version.dist-info

%changelog
* Tue Feb 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.1-alt1
- 2.3.1 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.4-alt1
- 2.2.4 released

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.3-alt1
- 2.2.3 released

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.2-alt2
- exclude tests to minimize dependencies

* Fri Feb 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.2-alt1
- 2.2.2 released

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt1
- initial
