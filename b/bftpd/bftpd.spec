Name:      bftpd
Version:   2.1
Release:   alt0.1
Summary:   A small, fast and easy-to-configure FTP server.
License:   GPL
Group:     System/Servers
URL:       http://bftpd.sourceforge.net/
Source0:   http://bftpd.sourceforge.net/downloads/rpm/%{name}-%{version}.tar.gz
Patch1:    bftpd-makefile-install.patch

%description
A very configurable small FTP server
bftpd is a easy-to-configure and small FTP server that supports chroot
without special directory preparation or configuration. Most FTP commands
are supported.

%prep
%setup -n %name
%patch1
%__autoreconf

%build
%configure
%make

%install
%makeinstall
mkdir -p %buildroot/%_var/run/bftpd

%files
%defattr(-,root,root)
%attr(600,root,root) %config(noreplace) %_sysconfdir/bftpd.conf
%attr(700,root,root) %_sbindir/bftpd
%_man8dir/*
%_var/run/bftpd

%changelog
* Mon Feb 18 2008 Nick S. Grechukh <gns@altlinux.org> 2.1-alt0.1
- initial build for ALT Sisyphus

* Mon Jan 1 2007 Joe Klemmer <joe@webtrek.com>
- updated the version number.

* Mon Jan 9 2006 Joe Klemmer <joe@webtrek.com>
- added defined variables to the top of the file.
- set the config file in the %files section so it won't
  be over written on upgrades.
- added a default attributes to the %files section.
- redid the summery section to bring it in line with "rpm
  spec file standards" (an oxymoron if ever there was one).
- changed the depricated "Copyright" into "License".

