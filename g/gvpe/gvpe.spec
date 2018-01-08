# spec file for package GVPE
#

Name: gvpe
Version: 3.0
Release: alt2

Summary: virtual ethernet SSL VPN

License: %gpl3plus
Group: System/Servers
Url: http://software.schmorp.de/pck/gvpe.html

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Source1: %name.init
Source2: %name.sysconfig
Source3: %name.if-up
Source4: %name.conf
Source5: README.ALT.utf-8
Source6: %name.service

Patch0:  %name-2.22-alt-using_ip.patch
Patch1:  %name-3.0-alt-getopt.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Thu May 18 2017
# optimized out: glib2-devel libstdc++-devel perl perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl python-base python-modules python3 python3-base xz zlib-devel
BuildRequires: gcc-c++ libssl-devel zlib-devel makeinfo perl-unicore perl-Pod-Usage

BuildRequires: texinfo

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

# Removing built-in getopt
%patch1
rm -f -- lib/getopt*

%build
%autoreconf

# $localstatedir/run/gvpe.pid used as a default location of PID file
%configure \
    --localstatedir=%_var \
    --enable-http-proxy \
    %nil

%make_build

# GVPE 2.25 had an empty gvpe.conf.5 file, generete it from gvpe.conf.5.pod:
[ -s doc/gvpe.conf.5 ] || pod2man doc/gvpe.conf.5.pod  doc/gvpe.conf.5

%install
%make_install DESTDIR=%buildroot install

install -p -D -m 0755 -- %SOURCE1 %buildroot/%_initdir/%name
install -p -D -m 0640 -- %SOURCE2 %buildroot/%_sysconfdir/sysconfig/%name

install -d -m 0750 -- %buildroot%_sysconfdir/%name
install -d -m 0755 -- %buildroot%_sysconfdir/%name/hostkeys
install -d -m 0755 -- %buildroot%_sysconfdir/%name/pubkey
install -p -m 0755 -- %SOURCE3 %buildroot%_sysconfdir/%name/if-up
install -p -m 0644 -- %SOURCE4 %buildroot%_sysconfdir/%name/%name.conf.sample

cp -- %SOURCE5 README.ALT.utf-8

install -D -m 0644 -- %SOURCE6 %buildroot%_unitdir/%name.service


%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS NEWS README TODO README.ALT.utf-8
%doc --no-dereference COPYING
%doc doc/complex-example

%dir %attr(0750,root,root) %_sysconfdir/%name
%dir                       %_sysconfdir/%name/pubkey
%dir                       %_sysconfdir/%name/hostkeys
%config                    %_sysconfdir/%name/%name.conf.sample
%config(noreplace)         %_sysconfdir/%name/if-up

%config(noreplace)         %_sysconfdir/sysconfig/%name
%config                    %_initdir/%name

%_bindir/%{name}ctrl
%_sbindir/%name
%_mandir/man?/*
%_infodir/*

%_unitdir/%{name}*.service

%changelog
* Mon Jan 08 2018 Nikolay A. Fetisov <naf@altlinux.org> 3.0-alt2
- Fix build with glibc-2.26

* Thu May 18 2017 Nikolay A. Fetisov <naf@altlinux.org> 3.0-alt1
- New version
  + UNCOMPATIBLE changes: new protocol version
  + UNCOMPATIBLE changes: regeneration of the RSA keys is needed

* Mon May 16 2017 Nikolay A. Fetisov <naf@altlinux.ru> 2.25-alt1
- New version
- some UNCOMPATIBLE changes from previous versions; see NEWS for details

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.22-alt1.1.qa1.1
- NMU: added BR: texinfo

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.22-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 2.22-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Fri Aug 28 2009 Nikolay A. Fetisov <naf@altlinux.ru> 2.22-alt1
- Initial build for ALT Linux Sisyphus
