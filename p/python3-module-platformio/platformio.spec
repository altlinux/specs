Name: python3-module-platformio
Version: 5.2.5
Release: alt1

Summary: PlatformIO Core
License: Apache-2.0
Group: Development/Other
Url: https://platformio.org/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

# lemme cite requests/packages.py:
# "I don't like it either. Just look the other way."
%add_python3_req_skip requests.packages.urllib3.util.retry
# urllib.parse vs urlparse
%add_python3_req_skip urlparse
# builtins: configparser, queue, threading
%add_python3_req_skip ConfigParser Queue thread
# optional
%add_python3_req_skip click_completion
# just can't happen
%add_python3_req_skip msvcrt

%set_python3_req_method strict

%files
%_bindir/pio
%_bindir/platformio
%_bindir/piodebuggdb
%python3_sitelibdir/platformio
%python3_sitelibdir/platformio-%version-*-info

%changelog
* Mon Feb 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.2.5-alt1
- 5.2.5 released

* Wed Oct 13 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.2.1-alt1
- 5.2.1 released

* Mon Mar 22 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.1.1-alt1
- 5.1.1 released

* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.1.0-alt1
- initial
