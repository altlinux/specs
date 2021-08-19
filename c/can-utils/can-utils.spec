Name: can-utils
Version: v2021.08.0
Release: alt1

Summary: SocketCAN userspace utilities and tools

License: BSD like
Group: Development/Tools
Url: https://github.com/linux-can/can-utils

Packager: Pavel Vainerman <pv@altlinux.ru>

# Source-url: https://github.com/linux-can/can-utils/archive/%{version}.tar.gz
Source: %name-%version.tar

BuildRequires: cmake gcc
Obsoletes: can-uilts

%description
Basic tools to display, record, generate and replay CAN traffic

- candump : display, filter and log CAN data to files
- canplayer : replay CAN logfiles
- cansend : send a single frame
- cangen : generate (random) CAN traffic
- cansniffer : display CAN data content differences (just 11bit CAN IDs)


%prep
%setup

subst 's|#include <sys/socket.h>|#include <linux/sockios.h>\n#include <sys/socket.h>|g' *.c


%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%doc README.md
%_bindir/*


%changelog
* Thu Aug 19 2021 Pavel Vainerman <pv@altlinux.ru> v2021.08.0-alt1
- new version (v2021.08.0) with rpmgs script

* Fri Jan 08 2021 Pavel Vainerman <pv@altlinux.ru> v2020.12.0-alt1
- new version (v2020.12.0) with rpmgs script
- fix package name (fixed #39526)

* Tue Jul 09 2019 Pavel Vainerman <pv@altlinux.ru> v2019.00.0-alt1
- new version (commit bb2cc1140fafe799b20fd94996d8f10d17e888e4)

* Tue Jul 09 2019 Pavel Vainerman <pv@altlinux.ru> v2018.02.0-alt0.1
- init commit: version (v2018.02.0) with rpmgs script

