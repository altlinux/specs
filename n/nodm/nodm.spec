Name: nodm
Version: 0.7
Release: alt2

Summary: minimal display manager
License: GPL
Group: Graphical desktop/Other

Packager: Andriy Stepanov <stanv@altlinux.ru>
Source: %name-%version-%release.tar

BuildRequires: libpam-devel libConsoleKit-devel help2man

%description
nodm is a minimal display manager that simply logs in as a given user
and starts an X session, without asking for username or password.

%prep
%setup

%build
%autoreconf
%configure
make

%install
%makeinstall
install -pm0644 -D nodm.pamd %buildroot%_sysconfdir/pam.d/nodm

%files
%doc AUTHORS README
%_sysconfdir/pam.d/nodm
%_sbindir/nodm
%_man8dir/nodm.8*

%changelog
* Wed Mar 28 2012 Andriy Stepanov <stanv@altlinux.ru> 0.7-alt2
- Rebuild for Sisyphus.

* Fri Apr 29 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7-alt1
- Initial build.

