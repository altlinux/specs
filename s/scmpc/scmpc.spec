Name: scmpc
Version: 0.4.1
Release: alt1.git20130304

Summary: Audioscrobbler client for MPD
License: GPL
Group: Sound
Url: https://bitbucket.org/cmende/scmpc/

# https://bitbucket.org/cmende/scmpc.git
Source: %name-%version.tar.bz2

BuildPreReq: libargtable2-devel libconfuse-devel libcurl-devel
BuildPreReq: libdaemon-devel libmpdclient-devel glib2-devel

%description
scmpc is a client for MPD (the Music Player Daemon) which submits your
tracks to Audioscrobbler. It can be run as a daemon, which is the
default behaviour, or it can be run in the foreground with the logs
directed to standard out.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS NEWS *.md scmpc.conf.example
%_bindir/*
%_man1dir/*

%changelog
* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20130304
- Version 0.4.1

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.2.2-alt1.0.qa1
- NMU: rebuilt for debuginfo.

* Fri Mar 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.2-alt1.0
- Rebuilt due to libcurl.so.3 -> libcurl.so.4 soname change.

* Sun Dec 17 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Thu Oct 26 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.2.1-alt1
- initial build
