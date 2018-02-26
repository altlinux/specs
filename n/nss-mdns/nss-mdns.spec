Name: nss-mdns
Version: 0.10
Release: alt3

Summary: nss-mdns provides host name resolution via Multicast DNS
License: GPL
Group: System/Libraries
Url: http://www.avahi.org/

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libavahi-devel lynx

%package -n lib%name
Group: System/Libraries
Summary: nss-mdns provides host name resolution via Multicast DNS
Requires: avahi-daemon >= 0.6.21-alt1
Requires(pre): chrooted >= 0.3.5-alt1 chrooted-resolv sed
Requires(postun): chrooted >= 0.3.5-alt1 sed

%description
nss-mdns is a plugin for the GNU Name Service Switch (NSS) functionality
of the GNU C Library (glibc) providing host name resolution via
Multicast DNS (aka Zeroconf, aka Apple Rendezvous, aka Apple Bonjour),
effectively allowing name resolution by common Unix/Linux programs in
the ad-hoc mDNS domain .local.

nss-mdns provides client functionality only, which means that you have to run
a mDNS responder daemon seperately from nss-mdns if you want to register
the local host name via mDNS.

It is necessary to change "hosts" in /etc/nsswitch.conf to
hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4

%description -n lib%name
nss-mdns is a plugin for the GNU Name Service Switch (NSS) functionality
of the GNU C Library (glibc) providing host name resolution via
Multicast DNS (aka Zeroconf, aka Apple Rendezvous, aka Apple Bonjour),
effectively allowing name resolution by common Unix/Linux programs in
the ad-hoc mDNS domain .local.

nss-mdns provides client functionality only, which means that you have to run
a mDNS responder daemon seperately from nss-mdns if you want to register
the local host name via mDNS.

It is necessary to change "hosts" in /etc/nsswitch.conf to
hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4

%prep
%setup

%build
%autoreconf
%configure  --libdir=/%_lib --localstatedir=%_var --enable-avahi --disable-static
%make_build

%install
%make install DESTDIR=%buildroot

%post -n lib%name
if ! grep -q '^hosts:[[:blank:]].\+mdns' /etc/nsswitch.conf; then
sed -i.rpmorig 's/^\(hosts:[[:blank:]].\+\)\(dns\)$/\1mdns4_minimal [NOTFOUND=return] \2 mdns4/' /etc/nsswitch.conf
update_chrooted all
fi

%postun -n lib%name
if [ "$1" = "0" ]; then
sed -i -e 's/ mdns4_minimal \[NOTFOUND=return\]//' -e 's/ mdns4//' /etc/nsswitch.conf
update_chrooted all
fi

%triggerpostun -n lib%name -- lib%name < 0.10-alt3
if ! grep -q '^hosts:[[:blank:]].\+mdns' /etc/nsswitch.conf; then
sed -i 's/^\(hosts:[[:blank:]].\+\)\(dns\)$/\1mdns4_minimal [NOTFOUND=return] \2 mdns4/' /etc/nsswitch.conf
update_chrooted all
fi

%files -n lib%name
%doc README doc/README.html doc/style.css
/%_lib/libnss_*.so.*

%changelog
* Tue Dec 30 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10-alt3
- prereq on chrooted >= 0.3.5-alt1 moved to subpackage (#18401)

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10-alt2
- obsolete by filetriggers macros removed

* Thu Aug 23 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10-alt1
- 0.10 released

* Tue Jan 30 2007 Sergey V Turchin <zerg at altlinux dot org> 0.9-alt1
- initial specfile
