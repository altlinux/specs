Name: python3-module-platformio
Version: 6.1.6
Release: alt1

Summary: PlatformIO Core
License: Apache-2.0
Group: Development/Other
Url: https://platformio.org/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)
BuildRequires: python3(click)
BuildRequires: python3(semantic_version)
BuildRequires: python3(wsproto)
BuildRequires: python3(bottle)
BuildRequires: python3(ajsonrpc)
BuildRequires: python3(elftools)
BuildRequires: python3(aiofiles)
BuildRequires: python3(tabulate)
BuildRequires: python3(zeroconf)
BuildRequires: python3(marshmallow)
BuildRequires: python3(uvicorn)
BuildRequires: python3(starlette)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# lemme cite requests/packages.py:
# "I don't like it either. Just look the other way."
%add_python3_req_skip requests.packages.urllib3.util.retry
# can't happen
%add_python3_req_skip msvcrt

%set_python3_req_method strict

%check
%tox_check_pyproject

%files
%_bindir/pio
%_bindir/platformio
%_bindir/piodebuggdb
%python3_sitelibdir/platformio
%python3_sitelibdir/platformio-%version.dist-info

%changelog
* Wed Jan 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.6-alt1
- 6.1.6 released

* Tue Nov 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.5-alt1
- 6.1.5 released

* Thu Jul 28 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.3-alt1
- 6.1.3 released

* Tue May 24 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.0.1-alt1
- 6.0.1 released

* Mon Feb 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.2.5-alt1
- 5.2.5 released

* Wed Oct 13 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.2.1-alt1
- 5.2.1 released

* Mon Mar 22 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.1.1-alt1
- 5.1.1 released

* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.1.0-alt1
- initial
