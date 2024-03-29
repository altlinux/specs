Name: sysctl-conf-userns
Version: 0.2
Release: alt1

Group: System/Base
Summary: Enable user namespace cloning
Url: https://git.altlinux.org/gears/s/sysctl-conf-userns.git
License: GPL-2.0

BuildArch: noarch

Source: userns.conf

#BuildRequires:

%description
Unprivileged user namespaces are generally fine to enable, but in some cases
they open up more kernel attack surface for (unsandboxed) non-root processes
to elevate to kernel privileges.

%prep
%setup -Tc

%install
install -D -m 0644 %SOURCE0 %buildroot/%_sysctldir/48-userns.conf

%files
%_sysctldir/48-userns.conf

%changelog
* Fri Nov 26 2021 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- fix package Url, Name
- fix files location

* Fri Nov 26 2021 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
