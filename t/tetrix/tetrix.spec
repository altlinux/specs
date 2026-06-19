Name: tetrix
Version: 2.7
Release: alt1
License: BSD
Group: Games/Arcade
Summary: A UNIX-hosted, curses-based clone of Tetris
Source: %name-%version.tar.gz
Patch: a2x.patch

# Automatically added by buildreq on Tue Aug 23 2011
# optimized out: docbook-dtds docbook-style-xsl libgpg-error libtinfo-devel xml-common xml-utils xsltproc
BuildRequires: libncurses-devel asciidoc-a2x

%description
A clone of the Tetris game. Documentation for the commands is on-screen.
The optional argument is an initial delay loop count between moves; the
game tries to default to a reasonable value.

%prep
%setup
%patch -p1

%build
%make_build %name %name.6

%install
install -D %name %buildroot%_bindir/%name
install -D %name.6 %buildroot%_man6dir/%name.6

%files
%doc *.adoc
%_bindir/*
%_man6dir/*

%changelog
* Fri Jun 19 2026 Fr. Br. George <george@altlinux.org> 2.7-alt1
- Autobuild version bump to 2.7

* Tue Mar 31 2026 Fr. Br. George <george@altlinux.org> 2.6-alt1
- Autobuild version bump to 2.6

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 2.4-alt1
- Autobuild version bump to 2.4

* Tue Aug 23 2011 Fr. Br. George <george@altlinux.ru> 2.3-alt1
- Autobuild version bump to 2.3
- Initial build

* Tue Aug 23 2011 Fr. Br. George <george@altlinux.ru> 0.0-alt1
- Initial 'zero version' commit

