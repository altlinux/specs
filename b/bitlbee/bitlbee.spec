Name:		bitlbee
Version:	1.2.5
Release:	alt1
Group:		Networking/IRC
License:	GPLv2
URL:		http://www.bitlbee.org
Summary:	IRC gateway to IM chat networks
Source:		http://get.bitlbee.org/src/%name-%version.tar.gz
Patch:		%name-1.2.5-g_malloc.patch
Packager:	Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Thu Apr 01 2010
BuildRequires: glib2-devel libgnutls-devel

%description
BitlBee is an IRC daemon that can talk to instant messaging
networks and acts as a gateway. Users can connect to the server
with any normal IRC client and see their 'buddy list' in
&bitlbee. BitlBee's protocol support is based on the gaim
protocol plugins. BitlBee currently supports Oscar (aim and icq),
MSN, Jabber and Yahoo.

%prep
%setup
%patch
for N in doc/* ; do sed -i 's@/usr/local@/usr@g' $N || :; done
sed -i 's/}/\tdisable\t= yes\n}/
s/nobody/%name/g
' doc/%name.xinetd

%build
./configure --prefix=/usr --etcdir=%_sysconfdir/%name
%make_build

%install
%makeinstall DESTDIR=%buildroot ETCDIR=%_sysconfdir/%name
%make DESTDIR=%buildroot install-etc ETCDIR=%_sysconfdir/%name
mkdir -p %buildroot%_localstatedir/%name
install -D doc/%name.xinetd %buildroot%_sysconfdir/xinetd.d/%name

%pre
/usr/sbin/useradd -r -d %_localstatedir/%name -s /dev/null %name || :

%postun
test -d %_sysconfdir/%name ||
{ /usr/sbin/userdel %name && /usr/sbin/groupdel %name; }

%files
%doc doc/{README,AUTHORS,CHANGES,CREDITS,FAQ,INSTALL,bitlbee.schema,example_plugin.c} doc/user-guide/user-guide.{txt,html}
%_sbindir/%name
%_datadir/%name
%attr(0755,%name,%name) %_localstatedir/%name
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_mandir/*/%name.*
%_sysconfdir/xinetd.d/%name

%changelog
* Fri Apr 02 2010 Fr. Br. George <george@altlinux.ru> 1.2.5-alt1
- Initial build from scratch
- Chkconfig off and separate user by default
