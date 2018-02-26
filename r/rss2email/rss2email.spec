Name: rss2email
Version: 2.65
Release: alt1.1
Summary: Receive RSS or Atom feeds by email

Group: Networking/News
License: GPLv2+
Url: http://rss2email.infogami.com/
BuildArch: noarch

Source0: http://rss2email.infogami.com/rss2email.py
Source1: config.py
Source2: r2e
Source3: r2e.1

BuildRequires: python-module-feedparser, python-module-html2text

%description
rss2email is a simple program which you can run in your crontab.
It watches RSS (or Atom) feeds and sends you a nicely formatted
email message for each new item.

%install
mkdir -p %buildroot{%_bindir,%_man1dir,%_datadir/%name}
install -pm755 %_sourcedir/r2e %buildroot%_bindir/
install -pm755 %_sourcedir/rss2email.py %buildroot%_datadir/%name/
install -pm644 %_sourcedir/config.py %buildroot%_datadir/%name/
install -pm644 %_sourcedir/r2e.1 %buildroot%_man1dir/
sed -i 's/\r//' %buildroot%_datadir/%name/rss2email.py

%files
%_bindir/*
%_datadir/%name/
%_man1dir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.65-alt1.1
- Rebuild with Python-2.7

* Mon Feb 01 2010 Dmitry V. Levin <ldv@altlinux.org> 2.65-alt1
- Initial revision.
