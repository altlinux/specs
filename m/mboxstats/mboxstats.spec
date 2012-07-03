Name: mboxstats
Version: 3.1
Release: alt1

Summary: mbox stats
License: GPL
Group: File tools

Url: http://www.vanheusden.com/mboxstats/
Source: %url/%name-%version.tgz
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Dec 24 2008
BuildRequires: gcc-c++

%description
%name is an utility to calculate all sorts of statistics
on a given mailbox (or maildir).  Output can be plain text
or XML.

%prep
%setup

%build
%make

%install
install -pD -m755 %name %buildroot%_bindir/%name

%files
%_bindir/%name
%doc license.txt

# TODO:
# - MIME/cyrillics support, if ever ;-) [from:, subject:]

%changelog
* Wed Dec 24 2008 Michael Shigorin <mike@altlinux.org> 3.1-alt1
- built for ALT Linux

