Name: tetrix
Version: 2.3
Release: alt1
License: GPL
Group: Games/Arcade
Summary: A UNIX-hosted, curses-based clone of Tetris
Source: %name-%version.tar.gz

# Automatically added by buildreq on Tue Aug 23 2011
# optimized out: docbook-dtds docbook-style-xsl libgpg-error libtinfo-devel xml-common xml-utils xsltproc
BuildRequires: libncurses-devel xmlto

%description
A clone of the Tetris game. Documentation for the commands is on-screen.
The optional argument is an initial delay loop count between moves; the
game tries to default to a reasonable value.

%prep
%setup
rm %name.6

%build
%make_build %name %name.6

%install
install -D %name %buildroot%_bindir/%name
install -D %name.6 %buildroot%_man6dir/%name.6

%files
%doc README
%_bindir/*
%_man6dir/*

%changelog
* Tue Aug 23 2011 Fr. Br. George <george@altlinux.ru> 2.3-alt1
- Autobuild version bump to 2.3
- Initial build

* Tue Aug 23 2011 Fr. Br. George <george@altlinux.ru> 0.0-alt1
- Initial 'zero version' commit

