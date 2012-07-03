
Name: nss-myhostname
Summary: glibc plugin for local system host name resolution
Version: 0.3
Release: alt1
License: LGPLv2+
Url: http://0pointer.de/lennart/projects/nss-myhostname/
Group: System/Libraries
Source: %name-%version.tar

BuildRequires: lynx

%description
nss-myhostname is a plugin for the GNU Name Service Switch (NSS)
functionality of the GNU C Library (glibc) providing host name
resolution for the locally configured system hostname as returned by
gethostname(2). Various software relies on an always resolvable local
host name. When using dynamic hostnames this is usually achieved by
patching /etc/hosts at the same time as changing the host name. This
however is not ideal since it requires a writable /etc file system and
is fragile because the file might be edited by the administrator at
the same time. nss-myhostname simply returns all locally configure
public IP addresses, or -- if none are configured -- the IPv4 address
127.0.0.2 (wich is on the local loopback) and the IPv6 address ::1
(which is the local host) for whatever system hostname is configured
locally. Patching /etc/hosts is thus no longer necessary.

It is necessary to change "hosts" in /etc/nsswitch.conf to 
hosts: files myhostname

%package -n lib%name
Group: System/Libraries
Summary: glibc plugin for local system host name resolution
Requires(pre): chrooted >= 0.3.5-alt1 chrooted-resolv sed
Requires(postun): chrooted >= 0.3.5-alt1 sed


%description -n lib%name
nss-myhostname is a plugin for the GNU Name Service Switch (NSS)
functionality of the GNU C Library (glibc) providing host name
resolution for the locally configured system hostname as returned by
gethostname(2). Various software relies on an always resolvable local
host name. When using dynamic hostnames this is usually achieved by
patching /etc/hosts at the same time as changing the host name. This
however is not ideal since it requires a writable /etc file system and
is fragile because the file might be edited by the administrator at
the same time. nss-myhostname simply returns all locally configure
public IP addresses, or -- if none are configured -- the IPv4 address
127.0.0.2 (wich is on the local loopback) and the IPv6 address ::1
(which is the local host) for whatever system hostname is configured
locally. Patching /etc/hosts is thus no longer necessary.

It is necessary to change "hosts" in /etc/nsswitch.conf to 
hosts: files myhostname

%prep
%setup

%build
%autoreconf
%configure --prefix=/usr --libdir=/%_lib
%make_build

%install

%makeinstall_std
rm -rf %buildroot%_docdir/nss-myhostname

%post -n lib%name
if [ "$1" = "1" ]; then
    grep -q '^hosts:[[:blank:]].\+myhostname' \
    /etc/nsswitch.conf || \
    sed -i.rpmorig 's/^\(hosts:.\+\)$/\1 myhostname/' /etc/nsswitch.conf
fi
update_chrooted all

%postun -n lib%name
if [ "$1" = "0" ]; then
    grep -q '^hosts:[[:blank:]].\+myhostname' \
        /etc/nsswitch.conf && \
    sed -i 's/ myhostname//' /etc/nsswitch.conf
fi
update_chrooted all

%files -n lib%name
%doc README LICENSE
/%_lib/libnss_*.so.*

%changelog
* Fri May 20 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3-alt1
- initial build for ALT Linux Sisyphus
