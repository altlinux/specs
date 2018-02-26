Name: tcl-xmpp
Version: 0.1
Release: alt4

Summary: XMPP library for Tcl
License: BSD
Group: Development/Tcl
Url: http://code.google.com/p/tclxmpp

Source: %name-%version-%release.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-tcl >= 0.2.1-alt2
BuildRequires: cpio tcl tcllib

%description
This project implements an XMPP (RFC-3920 and RFC-3921) library
which is to be used for clients, bots and components written in Tcl.

%prep
%setup

%build
dtplite -o . -ext n nroff doc

%install
mkdir -p %buildroot%_tcldatadir %buildroot%_mandir/mann
cp -a xmpp %buildroot%_tcldatadir
install -pm0644 files/*.n %buildroot%_mandir/mann
gzip ChangeLog

%files
%doc ChangeLog* examples license.terms
%_tcldatadir/xmpp
%_mandir/mann/*

%changelog
* Mon Dec 27 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt4
- updated to svn rev.158

* Fri Aug 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt3
- updated to svn rev.119

* Thu Jan 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt2
- updated to svn rev.68

* Thu Oct 23 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt1
- initial build
