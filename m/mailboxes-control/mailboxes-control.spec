Name: mailboxes-control
Version: 1.0
Release: alt3

Summary: Mailboxes access facilities control
License: GPL
Group: System/Servers
BuildArch: noarch

PreReq: shadow-utils > 1:4.1.4
Conflicts: vixie-cron < 0:4.0b1-alt1

Source: mailboxes
Source1: README.alt

%description
Control rules for mail spool boxes access and creation.
See control(8) for details.

# TODO: unhack using 'validate' (findreq find it in to xmlbeans-scripts)

%prep
cp %SOURCE1 .

%install
install -pD -m755 %SOURCE0 %buildroot%_controldir/mailboxes

%files
%doc README*
%config %_controldir/*

%pre
# HACK
sed -i '/CREATE_MAIL_SPOOL/d' /etc/login.defs

%changelog
* Thu Jun 07 2012 Fr. Br. George <george@altlinux.ru> 1.0-alt3
- Fix incorrectly placed config

* Mon Jun 04 2012 Fr. Br. George <george@altlinux.ru> 1.0-alt2
- Do not use rpm in scripts

* Mon Jun 04 2012 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial bulid

