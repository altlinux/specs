Name: figlet
Version: 2.2.2
Release: alt1

Summary: ASCII-art banners generator
License: Academic Free License
Group: Graphics

URL: http://www.figlet.org
Source: ftp://ftp.figlet.org/pub/figlet/program/unix/figlet222.tar.gz
Patch0: ftp://ftp.debian.org/debian/pool/non-free/f/figlet/figlet_2.2.1-4.diff.gz

%description
Program for generating ASCII-art-like banners by using plenty of
fonts. It can be used for generating logos, e-mail signatures, etc.

%prep
%setup -q -n figlet222
%patch0 -p1

%build
%make_build \
	CFLAGS="%optflags" \
	DEFAULTFONTDIR=%_datadir/%name \
	DESTDIR=%_bindir \
	MANDIR=%_man1dir

%install
%__mkdir_p %buildroot{%_bindir,%_man6dir,%_datadir/%name}
%__install -p -m755 figlet figlist chkfont showfigfonts %buildroot%_bindir/
%__install -p -m644 *.6 debian/*.6 %buildroot%_man6dir/
%__install -p -m644 fonts/* %buildroot%_datadir/%name/

%files
%doc README FAQ CHANGES LICENSE figfont.txt debian/README.Debian
%_bindir/*
%_datadir/%name/
%_man6dir/*.*

%changelog
* Sun Apr 23 2006 Alexey Tourbin <at@altlinux.ru> 2.2.2-alt1
- 2.2.1 -> 2.2.2
- sync debian figlet_2.2.1-4.diff.gz
- license changed from "Artistic License" to "Academic Free License"

* Tue Jan 20 2004 Alexey Tourbin <at@altlinux.ru> 2.2.1-alt1
- inital revision (PLD based)
