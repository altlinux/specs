Name: figlet
Version: 2.2.5
Release: alt1

Summary: ASCII-art banners generator
License: Academic Free License
Group: Graphics

Url: http://www.figlet.org
Source: %name-%version.tar.gz

%description
Program for generating ASCII-art-like banners by using plenty of
fonts. It can be used for generating logos, e-mail signatures, etc.

%prep
%setup

%build
%make_build \
	CFLAGS="%optflags" \
	DEFAULTFONTDIR=%_datadir/%name \
	DESTDIR=%_bindir \
	MANDIR=%_man1dir

%install
mkdir -p %buildroot{%_bindir,%_man6dir,%_datadir/%name}
install -p -m755 figlet figlist chkfont showfigfonts %buildroot%_bindir/
install -p -m644 *.6 %buildroot%_man6dir/
install -p -m644 fonts/* %buildroot%_datadir/%name/

%files
%doc README FAQ CHANGES LICENSE figfont.txt
%_bindir/*
%_datadir/%name/
%_man6dir/*.*

%changelog
* Tue Nov 20 2012 Fr. Br. George <george@altlinux.ru> 2.2.5-alt1
- Autobuild version bump to 2.2.5
- Remove debian patch

* Sun Apr 23 2006 Alexey Tourbin <at@altlinux.ru> 2.2.2-alt1
- 2.2.1 -> 2.2.2
- sync debian figlet_2.2.1-4.diff.gz
- license changed from "Artistic License" to "Academic Free License"

* Tue Jan 20 2004 Alexey Tourbin <at@altlinux.ru> 2.2.1-alt1
- inital revision (PLD based)
