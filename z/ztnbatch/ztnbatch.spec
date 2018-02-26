Name: ztnbatch
Version: 0.2
Release: alt2

Summary: ZyXEL modem configurer
License: GPL
Group: System/Configuration/Other

BuildArch: noarch

Url: http://zyxmon.streamclub.ru/other.php
Packager: Lenar Shakirov <snejok@altlinux.org>

Source: %name-%version.tar

Requires: netcat

%description
Script is used to configure ZyXEL modem over telnet

%prep
%setup

%install
install -D ztnbatch_P660HT -m 755 %buildroot%_bindir/ztnbatch_P660HT
install -D ztnbatch_P660HT2 -m 755 %buildroot%_bindir/ztnbatch_P660HT2

%files
%_bindir/ztnbatch_P660HT
%_bindir/ztnbatch_P660HT2

%changelog
* Fri May 29 2009 Lenar Shakirov <snejok@altlinux.ru> 0.2-alt2
- ExclusiveArch deleted from spec

* Thu Mar 20 2008 Lenar Shakirov <snejok@altlinux.ru> 0.2-alt1
- Standalone scripts created. input_data.txt deleted.

* Tue Mar 18 2008 Lenar Shakirov <snejok@altlinux.ru> 0.1-alt1
- Initial build

