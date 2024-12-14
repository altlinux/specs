Name: zsync
Summary: An rsync like transfer software over http
Version: 0.6.2
Release: alt3
License: Artistic License v2
Group: Networking/File transfer
Source: %name-%version.tar
Patch1: %name-0.6.2-fix-FTBS.patch
Url: https://github.com/cph6/zsync.git

%description
zsync is a file transfer program. It allows you to download a file
from a remote web server, where you have a copy of an older version of
the file on your computer already. zsync downloads only the new parts
of the file. It uses the same algorithm as rsync.

zsync does not require any special server software or a shell account
on the remote system (rsync, in comparison, requires that you have an
rsh or ssh account, or that the remote system runs rsyncd). Instead,
it uses a control file - a .zsync file - that describes the file to be
downloaded and enables zsync to work out which blocks it needs. This
file can be created by the admin of the web server hosting the
download, and placed alongside the file to download - it is generated
once, then any downloaders with zsync can use it.

%prep
%setup
%patch1 -p2

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std BUILDROOT=%{buildroot}

%files
%doc NEWS README COPYING
%_bindir/*
%_man1dir/*

%changelog
* Sat Dec 14 2024 Lenar Shakirov <snejok@altlinux.org> 0.6.2-alt3
- Fix FTBS, get patch from https://github.com/cph6/zsync/issues/20

* Tue Apr 10 2018 Lenar Shakirov <snejok@altlinux.ru> 0.6.2-alt2
- Summary/Description improved: thks to autoimport robot!

* Fri Apr 06 2018 Lenar Shakirov <snejok@altlinux.ru> 0.6.2-alt1
- Initial build for ALT

