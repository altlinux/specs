%define realver svn-1586

Summary: A multi-threaded implementation of Apple's DAAP server
Name: mt-daapd
Version: 0.2.4.1586
Release: alt1
License: GPL
Group: System/Servers
URL: http://www.mt-daapd.org
Source: http://download.sourceforge.net/sourceforge/mt-daapd/%name-%realver.tar.gz
Source1: %name-init.d
Source2: %name-logrotate.d
Patch: plugins-libdir.patch
Packager: Stanislav Yadykin <tosick@altlinux.ru>

# Automatically added by buildreq on Thu Nov 06 2008
BuildRequires: gcc-c++ libavahi-devel libflac-devel libgdbm-devel libid3tag-devel libsqlite3-devel libvorbis-devel

%description
A multi-threaded implementation of Apple's DAAP server, mt-daapd
allows a Linux machine to advertise MP3 files to to used by 
Windows or Mac iTunes clients.  This version uses Apple's ASPL Rendezvous
daemon.

%package devel
Summary: Development libraries for mt-daapd
Group: Development/C

%description devel
Development libraries for mt-daapd.

%prep
%setup -n %name-%realver
%patch0 -p1

%build
%configure \
	--enable-oggvorbis \
	--enable-flac \
	--enable-avahi \
	--enable-upnp \
	--enable-sqlite3 \
	--enable-gdbm
%make

%install
%makeinstall

%__install -d %buildroot/%_sysconfdir
%__cat contrib/mt-daapd.conf | %__sed -e "s|runas = nobody|runus = %name|" | %__sed -e "s|db_type = sqlite|db_type = sqlite3|" \
| %__sed -e "s|#logfile = /var/log/mt-daapd.log|logfile = /var/log/mt-daapd/mt-daapd.log|" > %buildroot/%_sysconfdir/%name.conf

%__install -d %buildroot/%_sysconfdir/rc.d/init.d
%__install -m 755 %SOURCE1 %buildroot/%_sysconfdir/rc.d/init.d/%name

%__install -d %buildroot/%_sysconfdir/logrotate.d
%__install -m 644 %SOURCE2 %buildroot/%_sysconfdir/logrotate.d/%name

%__install -d %buildroot/%_var/log/%name
%__install -d %buildroot/%_var/run/%name
%__install -d %buildroot/%_var/cache/%name

%pre
/usr/sbin/useradd -r -d %_var/cache/%name -s /sbin/nologin -c "mt-daapd Network Multimedia Server" %name 2>/dev/null || true

%post
/sbin/chkconfig --add %name

%preun
if [ $1 = 0 ]; then
        /sbin/service %name condstop &>/dev/null ||  true
        /sbin/chkconfig --del %name
fi

%postun
/sbin/service %name condrestart &>/dev/null || true

%files
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL NEWS README TODO
%config %_sysconfdir/rc.d/init.d/%name
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/logrotate.d/%name
%_bindir/*
%_sbindir/%name
%_datadir/%name/admin-root
%_libdir/%name/plugins/*.so
%_var/log/%name
%_var/run/%name
%_var/cache/%name

%files devel
%_libdir/%name/plugins/*.a
%_libdir/%name/plugins/*.la


%changelog
* Thu Jan 15 2009 Stanislav Yadykin <tosick@altlinux.org> 0.2.4.1586-alt1
- new version
- init script improvements

* Thu Nov 20 2008 Stanislav Yadykin <tosick@altlinux.ru> 0.2.4.1571-alt2
- added /var directories

* Thu Nov 06 2008 Stanislav Yadykin <tosick@altlinux.org> 0.2.4.1571-alt1
- Initial version

