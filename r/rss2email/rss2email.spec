Name: rss2email
Version: 2.71
Release: alt1
Summary: Receive RSS or Atom feeds by email

Group: Networking/News
License: GPLv2+
Url: http://rss2email.infogami.com/
BuildArch: noarch

# http://www.allthingsrss.com/rss2email/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: config.py.template
Source2: r2e
Source3: r2e.1

Patch3: 0003-Setup-the-correct-version-number-in-rss2email.py.patch
Patch4: 0004-convert-tabs-to-spaces.patch
Patch5: 0005-Use-a-simpler-default-email-address.patch
Patch6: 0006-Prefer-utf8-in-CHARSET_LIST.patch
Patch7: 0007-Fix-email-header-injection.patch
Patch8: 0008-Fix-encoding-of-From-and-To-headers.patch
Patch10: rss2email-rh-config-location.patch

BuildRequires: python-module-feedparser python-module-html2text

%description
rss2email is a simple program which you can run in your crontab.
It watches RSS (or Atom) feeds and sends you a nicely formatted
email message for each new item.

%prep
%setup
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch10 -p1
sed -i 's/\r//' CHANGELOG readme.html

%install
mkdir -p %buildroot{%_bindir,%_man1dir,%_datadir/%name}
install -pm755 rss2email.py %buildroot%_datadir/%name/
install -pm644 %_sourcedir/config.py.template %buildroot%_datadir/%name/
install -pm755 %_sourcedir/r2e %buildroot%_bindir/
install -pm644 %_sourcedir/r2e.1 %buildroot%_man1dir/
%add_python_compile_include %_datadir/%name

%files
%_bindir/*
%_datadir/%name/
%_man1dir/*
%doc CHANGELOG readme.html

%changelog
* Sun Apr 07 2013 Dmitry V. Levin <ldv@altlinux.org> 2.71-alt1
- Updated to 2.71.
- Imported patches from Debian and Fedora.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.65-alt1.1
- Rebuild with Python-2.7

* Mon Feb 01 2010 Dmitry V. Levin <ldv@altlinux.org> 2.65-alt1
- Initial revision.
