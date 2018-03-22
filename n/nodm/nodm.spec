Name: nodm
Version: 0.7
Release: alt3.1

Summary: minimal display manager
License: GPL
Group: Graphical desktop/Other
Url: https://github.com/spanezz/nodm

Source: %name-%version-%release.tar

BuildRequires: libpam-devel help2man

%description
nodm is a minimal display manager that simply logs in as a given user
and starts an X session, without asking for username or password.

%prep
%setup

%build
%autoreconf
%configure --without-consolekit
make

%install
%makeinstall
install -pm0644 -D nodm.service %buildroot%systemd_unitdir/nodm.service
install -pm0644 -D nodm.pamd %buildroot%_sysconfdir/pam.d/nodm

%files
%doc AUTHORS README
%systemd_unitdir/nodm.service
%_sysconfdir/pam.d/nodm
%_sbindir/nodm
%_man8dir/nodm.8*

%changelog
* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.7-alt3.1
- NMU: added URL

* Sun Jan 04 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7-alt3
- modiified for use with systemd

* Wed Mar 28 2012 Andriy Stepanov <stanv@altlinux.ru> 0.7-alt2
- Rebuild for Sisyphus.

* Fri Apr 29 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7-alt1
- Initial build.

