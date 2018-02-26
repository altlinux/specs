Name: ve-kannel
Version: 0.1
Release: alt1

Packager: Michael Bochkaryov <misha@altlinux.org>

Summary: Kannel VE
License: GPL
Group: System/Base
BuildArch: noarch

#basic packages
Requires: apt
Requires: basesystem
Requires: sysklogd
Requires: etcnet
Requires: glibc-nss
Requires: glibc-locales

#service packages
Requires: kannel

#additional packages 
Requires: openssh-server
Requires: passwd
Requires: less
Requires: lynx

%description
virtual package for SMS/WAP gateway appliance

%files


%changelog
* Sat Apr 25 2009 Michael Bochkaryov <misha@altlinux.ru> 0.1-alt1
- initial release

