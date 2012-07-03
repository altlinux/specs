Name: surfraw
Version: 2.2.7
Release: alt2

Summary: Shell Users' Revolutionary Front Rage Against the Web
License: GPL
Group: Networking/WWW
Url: http://surfraw.sourceforge.net/
Packager: Egor Glukhov <kaman@altlinux.org>
BuildArch: noarch
BuildRequires: perl-Pod-Parser
Source: %name-%version.tar
Requires: links

%description
Surfraw provides a fast unix command line interface to a variety
of popular WWW search engines and other artifacts of power.
Forsake GUI idolatry! Aposate return!

%prep
%setup

%build
%configure --with-text-browser=links --with-graphical-browser=firefox --with-elvidir=%_datadir/%name
%make_build

%install
%makeinstall_std

%files
%doc README NEWS TODO
%config(noreplace) /etc/xdg/%name
%_bindir/*
%_datadir/%name
%_man1dir/*

%changelog
* Tue Nov 16 2010 Egor Glukhov <kaman@altlinux.org> 2.2.7-alt2
- Rebuilt with perl-Pod-Parser

* Sat Nov 06 2010 Egor Glukhov <kaman@altlinux.org> 2.2.7-alt1
- Package returned to Sisyphus

* Thu Mar 13 2008 Nick S. Grechukh <gns@altlinux.org> 2.2.1-alt1
- new version

* Sat Oct 12 2002 Dmitry V. Levin <ldv@altlinux.org> 1.0.7-alt5
- BuildArch: noarch.
- Additional convention enforcement on patch file names.
- Chached in default browsers to cleanup build dependencies.

* Sat Aug 17 2002 Nazar Yurpeak <phoenix@altlinux.ru> 1.0.7-alt4
- update BuildReq

* Mon Aug 5 2002 Nazar Yurpeak <phoenix@altlinux.ru> 1.0.7-alt3
- fix spec

* Fri Jun 21 2002 Nazar Yurpeak <phoenix@altlinux.ru> 1.0.7-alt1
- new version

* Thu Jul 05 2001 Sergie Pugachev <fd_rag@altlinux.ru> 1.0.3-alt1
- new version

* Tue Jan 16 2001 AEN <aen@logic.ru>
- RE adaptations

* Wed Sep 27 2000 Pixel <pixel@mandrakesoft.com> 1.0.2-1mdk
- initial spec

# end of file

