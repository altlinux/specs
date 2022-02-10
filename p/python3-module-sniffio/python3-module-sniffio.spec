%define  modulename sniffio

Name:    python3-module-%modulename
Version: 1.2.0
Release: alt1

Summary: Sniff out which async library your code is running under
License: MIT or Apache-2.0
Group:   Development/Python3
URL:     https://github.com/python-trio/sniffio

Packager: Evgeny Sinelnikov <sin@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
This is a tiny package whose only purpose is to let you detect which async
library (like Trio, and asyncio, and ...) your code is running under.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%exclude %python3_sitelibdir/%modulename/_tests
%python3_sitelibdir/*.egg-info
%doc *.md *.rst

%changelog
* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Fri Nov 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt2
- exclude tests from package due to excessive reqs

* Tue Jan 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
