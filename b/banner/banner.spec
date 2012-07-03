Name: banner
Release: alt1
Version: 1.3.2

Summary: Prints a short string to the console in very large letters
License: GPLv2
Group: Text tools

Url: http://cedar-solutions.com/software/utilities.html
Source: http://cedar-solutions.com/ftp/software/%name-%version.tar.gz
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
%_bindir/%name

%changelog
* Sat Sep 24 2011 Michael Shigorin <mike@altlinux.org> 1.3.2-alt1
- 1.3.2: fix problem with ^ character

* Fri Aug 07 2009 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- built for ALT Linux based on heavily cleaned up fedora spec
