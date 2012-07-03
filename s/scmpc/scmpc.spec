Name: scmpc
Version: 0.2.2
Release: alt1.0

Summary: Audioscrobbler client for MPD
License: GPL
Group: Sound
Url: http://scmpc.berlios.de/

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: %name-%version.tar.bz2

BuildPreReq: libargtable2-devel libconfuse-devel libcurl-devel libdaemon-devel

%description
scmpc is a client for MPD (the Music Player Daemon) which submits your
tracks to Audioscrobbler. It can be run as a daemon, which is the
default behaviour, or it can be run in the foreground with the logs
directed to standard out.

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall
%__mkdir_p %buildroot%_docdir/%name-%version/
mv %buildroot{%_datadir/%name/scmpc.conf,%_docdir/%name-%version/}

%files
%_bindir/*
%_man1dir/*
%doc %_docdir/%name-%version/

%changelog
* Fri Mar 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.2-alt1.0
- Rebuilt due to libcurl.so.3 -> libcurl.so.4 soname change.

* Sun Dec 17 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Thu Oct 26 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.2.1-alt1
- initial build
