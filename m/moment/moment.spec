Name: moment
Version: 1.2.0
Release: alt2
License: GPL
Url: http://momentvideo.org
Summary: Moment Video Server allows you to organize live video streaming
Group: System/Servers
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Source: %name-%version.tar
Patch: %name-%version-alt-changes.patch

BuildRequires: gcc-c++ libmary-devel libmylang-devel libmycpp-devel libpargen-devel libscruffy-devel libmconfig-devel libctemplate-devel >= 2.1
BuildRequires: xsltproc

%description
Moment Video Server allows you to organize live video streaming on the
Internet or in your local network. All the user has to do to watch
the video is to open server's web page in a browser.

Moment VS can stream video from various sources: files on disk,
IP cameras, web cameras, from other streaming servers.

%package -n lib%name
Summary: Library for %name
Group: System/Libraries

%description -n lib%name
This package contains shared libraries used by %name's daemons
and clients.

%package -n lib%name-devel
Summary: Development package that includes the %name header files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The devel package contains the include files

%package myplayer
Summary: Flash player for %name
Group: System/Libraries

%description myplayer
This package contains flash player for %name's daemon.

%package mychat
Summary: Flash player for %name
Group: System/Libraries

%description mychat
This package contains flash player for %name's daemon.

%prep
%setup
%patch -p1

%build
./autogen.sh
%configure --disable-static
%make

%install
%make DESTDIR=%buildroot install
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_logrotatedir
mkdir -p %buildroot%_logdir/%name

install -m 0755 %name.init %buildroot%_initdir/%name
install -m 0644 %name.logrotate %buildroot%_logrotatedir/%name
install -m 0644 %name/%name.dist.conf %buildroot%_sysconfdir/%name/%name.conf
cp %name/%{name}*.conf %buildroot%_sysconfdir/%name/

mv %buildroot%_datadir/%name/myplayer/playlist.json.tpl %buildroot%_sysconfdir/%name/
ln -s ../../../..%_sysconfdir/%name/playlist.json.tpl %buildroot%_datadir/%name/myplayer/playlist.json.tpl
install -m 0644 web/myplayer/playlist.dist.json.tpl %buildroot%_sysconfdir/%name/
install -m 0644 web/myplayer/playlist.example.json %buildroot%_sysconfdir/%name/
install -m 0644 web/myplayer/jquery.js %buildroot%_datadir/%name/myplayer/

cd www
mkdir %buildroot%_datadir/%name/welcome
make
cp -r *.tpl *.html *.php *.xml *.xsl *.svg *.ico Makefile img %buildroot%_datadir/%name/welcome
ln -s welcome.tpl %buildroot%_datadir/%name/welcome/index.tpl
ln -s welcome.ru.tpl %buildroot%_datadir/%name/welcome/index.ru.tpl
cd -

cat > %buildroot%_sysconfdir/sysconfig/%name  <<EOF
#Options:
#  -c --config <config_file>  Configuration file to use (default: /etc/moment/moment.conf)
#  -l --log <log_file>        Log file to use (default: /var/log/moment/moment.log)
#  --loglevel <loglevel>      Loglevel, one of A/D/I/W/E/H/F/N (default: I, "Info")
#  -d --daemonize             Daemonize (run in the background as a daemon).
#  --exit-after <number>      Exit after specified timeout in seconds.

ARGS=""
EOF


%check
#make test

%pre
/usr/sbin/groupadd -r -f _%name
/usr/sbin/useradd -r -g _%name -G video -d /usr/share/moment -s /dev/null -n -c "Moment Video Server" _%name >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%_bindir/*
%_libdir/%{name}*
%_initdir/*
%_logrotatedir/*
%config(noreplace) %_sysconfdir/%name/%name.*
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %_sysconfdir/%name
%dir %_datadir/%name
%_datadir/%name/welcome
%dir %attr(3770,_%name,_%name) %_logdir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/lib*so
%_pkgconfigdir/*

%files myplayer
%_datadir/%name/myplayer
%config(noreplace) %_sysconfdir/%name/*.json*

%files mychat
%_datadir/%name/mychat

%changelog
* Tue Apr 17 2012 Evgeny Sinelnikov <sin@altlinux.ru> 1.2.0-alt2
- Rebuild with libctemplate.so.2
- Add default welcome www files
- Add moment mychat subpackage

* Thu Nov 24 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.0-alt1
- New version

* Wed Jul 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- Build for ALT
