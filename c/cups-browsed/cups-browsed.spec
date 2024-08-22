%define _cups_serverbin %_libexecdir/cups

Name: cups-browsed
Version: 2.0.1
Release: alt1
Summary: Daemon for local auto-installation of remote printers
License: Apache-2.0 WITH LLVM-exception
Group: System/Configuration/Printing
Url: https://github.com/OpenPrinting/cups-browsed
Source0: %name-%version.tar
Source1: cups-browsed.init
Conflicts: cups-filters < 2.0
BuildRequires: gettext-devel
BuildRequires: pkgconfig(avahi-client)
BuildRequires: pkgconfig(avahi-glib)
BuildRequires: pkgconfig(cups) >= 2.2.2
BuildRequires: pkgconfig(libcupsfilters) >= 2.0
BuildRequires: pkgconfig(libppd) >= 2.0
BuildRequires: pkgconfig(glib-2.0)

%description
cups-browsed is a helper daemon, which automatically installs printers
locally, provides load balancing and clustering of print queues.
The daemon installs the printers based on found mDNS records and CUPS
broadcast, or by polling a remote print server.

%prep
%setup

%build
./autogen.sh

%configure --enable-auto-setup-driverless-only \
  --disable-rpath \
  --disable-saving-created-queues \
  --disable-frequent-netif-update \
  --with-remote-cups-local-queue-naming=RemoteName \
  --with-cups-rundir=%_runtimedir/cups \
  --without-rcdir \
  #

%make_build

%install
%makeinstall_std
install -D -m 755 %SOURCE1 %buildroot/%_initdir/cups-browsed
mkdir -p %buildroot%_unitdir
install -p -m 644 daemon/cups-browsed.service %buildroot%_unitdir
rm -rf %buildroot%_docdir/%name

%files
%doc COPYING LICENSE NOTICE
%doc ABOUT-NLS AUTHORS CHANGES.md CONTRIBUTING.md DEVELOPING.md README.md
%attr(0744,root,root) %_cups_serverbin/backend/implicitclass
%config(noreplace) %_sysconfdir/cups/cups-browsed.conf
%config(noreplace) %_initdir/cups-browsed
%_man5dir/cups-browsed.conf.5.*
%_man8dir/cups-browsed.8.*
%_sbindir/cups-browsed
%_unitdir/cups-browsed.service

%changelog
* Thu Aug 22 2024 Anton Farygin <rider@altlinux.ru> 2.0.1-alt1
- 2.0.0 -> 2.0.1

* Fri Sep 29 2023 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Tue Jul 25 2023 Anton Farygin <rider@altlinux.ru> 2.0-alt0.rc2
- first build for ALT
