# spec file for package GVPE
#

%define version 2.22
%define release alt1

Name: gvpe
Version: %version
Release: %release.1

Summary: virtual ethernet SSL VPN

License: %gpl3plus
Group: System/Servers
Url: http://savannah.gnu.org/projects/gvpe

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Source1: %name.init
Source2: %name.sysconfig
Source3: %name.if-up
Source4: %name.conf
Source5: README.ALT.utf-8

Patch0:  %name-2.22-alt-using_ip.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Jul 19 2009
BuildRequires: cvs gcc-c++ libssl-devel

%description
The GNU Virtual Private Ethernet suite implements a virtual
(uses udp, tcp, rawip and other protocols for tunneling),
private (encrypted, authenticated) ethernet (mac-based, 
broadcast-based network) that is shared among multiple nodes,
in effect implementing an ethernet bus over public networks.

%prep
%setup -n %name-%version
%patch0

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-3 %_docdir/%name/COPYING) COPYING

%build
%autoreconf

# $localstatedir/run/gvpe.pid used as a default location of PID file
%configure \
    --localstatedir=%_var \
    --enable-http-proxy \
    %nil

%make_build

%install
%make_install DESTDIR=%buildroot install

install -p -D -m 0755 -- %SOURCE1 %buildroot/%_initdir/%name
install -p -D -m 0640 -- %SOURCE2 %buildroot/%_sysconfdir/sysconfig/%name

install -d -m 0750 -- %buildroot%_sysconfdir/%name
install -p -m 0755 -- %SOURCE3 %buildroot%_sysconfdir/%name/if-up
install -p -m 0644 -- %SOURCE4 %buildroot%_sysconfdir/%name/%name.conf.sample

cp -- %SOURCE5 README.ALT.utf-8

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS NEWS README TODO README.ALT.utf-8
%doc --no-dereference COPYING
%doc doc/complex-example

%dir %attr(0750,root,root) %_sysconfdir/%name
%config                    %_sysconfdir/%name/%name.conf.sample
%config(noreplace)         %_sysconfdir/%name/if-up

%config(noreplace)         %_sysconfdir/sysconfig/%name
%config                    %_initdir/%name

%_bindir/%{name}ctrl
%_sbindir/%name
%_mandir/man?/*
%_infodir/*

%changelog
* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 2.22-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Fri Aug 28 2009 Nikolay A. Fetisov <naf@altlinux.ru> 2.22-alt1
- Initial build for ALT Linux Sisyphus
