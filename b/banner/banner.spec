Name: banner
Release: alt1
Version: 1.3.5

Summary: Prints a short string to the console in very large letters
Group: Text tools
License: GPLv2
Url: https://github.com/pronovic/%name

Packager: Michael Shigorin <mike@altlinux.org>

Vcs: https://github.com/pronovic/banner.git
Source: %url/releases/download/BANNER_V%version/%name-%version.tar.gz
Source100: %name.watch

%description
Classic-style banner program similar to the one found in Solaris or AIX.
The banner program prints a short string to the console in very large
letters.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README ChangeLog
%_man1dir/*
%_bindir/%name

%changelog
* Sat Apr 16 2022 Yuri N. Sedunov <aris@altlinux.org> 1.3.5-alt1
- 1.3.5 (new homepage on GitHub)

* Fri Feb 27 2015 Michael Shigorin <mike@altlinux.org> 1.3.4-alt1
- new version (watch file uupdate)

* Wed Jun 18 2014 Michael Shigorin <mike@altlinux.org> 1.3.3-alt1
- new version (watch file uupdate)
- added manpage and watch file

* Sat Sep 24 2011 Michael Shigorin <mike@altlinux.org> 1.3.2-alt1
- 1.3.2: fix problem with ^ character

* Fri Aug 07 2009 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- built for ALT Linux based on heavily cleaned up fedora spec
