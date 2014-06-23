Name: banner
Release: alt1
Version: 1.3.3

Summary: Prints a short string to the console in very large letters
License: GPLv2
Group: Text tools

Url: http://cedar-solutions.com/software/utilities.html
Source: http://cedar-solutions.com/ftp/software/%name-%version.tar.gz
Source100: %name.watch
Packager: Michael Shigorin <mike@altlinux.org>

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
* Wed Jun 18 2014 Michael Shigorin <mike@altlinux.org> 1.3.3-alt1
- new version (watch file uupdate)
- added manpage and watch file

* Sat Sep 24 2011 Michael Shigorin <mike@altlinux.org> 1.3.2-alt1
- 1.3.2: fix problem with ^ character

* Fri Aug 07 2009 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- built for ALT Linux based on heavily cleaned up fedora spec
