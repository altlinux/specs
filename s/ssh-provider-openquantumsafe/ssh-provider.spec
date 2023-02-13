%if 0
%define weight 8
%define provider openssh
#define req_prfx %nil
#define req_sffx %nil
%endif
%if 0
%define weight 4
%define provider gostcrypto
#define req_prfx %nil
%define req_sffx %provider
%endif
%if 1
%define weight 2
%define provider openquantumsafe
%define req_prfx %provider
#define req_sffx %nil
%endif

Name: ssh-provider-%provider
Version: 1.1
Release: alt1

Group: System/Configuration/Other
Summary: Virtual SSH packages
Url: https://altlinux.org
License: GPL-3.0-only

BuildArch: noarch

Source0: macros

%description
SSH packages provides to allow ssh requires more flexible.

%include %SOURCE0

%package_start openssh
Requires: %name-openssh-clients %name-openssh-server
%package_end openssh

%package_start openssh-clients
Requires: %name-openssh-common
%package_end openssh-clients

%package_start openssh-askpass-common
Requires: %name-openssh-common
%package_end openssh-askpass-common

%package_start openssh-server
Requires: %name-openssh-server-control
%package_end openssh-server

%package_start openssh-server-control
Requires: %name-openssh-common
%package_end openssh-server-control

%package_start openssh-common
%package_end openssh-common

%changelog
* Mon Feb 13 2023 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- initial build
