Name: wavsplit
Version: 1.2.1
Release: alt5

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Splits wavfiles into tracks
License: GPLv2
Group: Sound

URL: http://sourceforge.net/projects/wavsplit/
Source: http://downloads.sourceforge.net/wavsplit/%name-%version.tar
Patch: %name-1.2.1-alt.patch

%description
This small program splits large wav files at given time positions. This
is very handy if you want to transfer your gramophone records to CDs.
To find out split positions you can use any Wav player or editor with a
time display. You'll get the splitting done much faster and reliably
than with complex algorithms, which split your a capella songs in
pieces and won't process live albums.

%prep
%setup
%patch -p1

%build
%make clean
%make_build CFLAGS="%optflags"

%install
install -d %buildroot{%_bindir,%_man1dir}
%make_install BIN=%buildroot%_bindir MAN=%buildroot%_man1dir install

%files
%doc README README.wavren
%_bindir/*
%_man1dir/*

%changelog
* Mon Oct 19 2009 Victor Forsyuk <force@altlinux.org> 1.2.1-alt5
- Remove in-spec translations.

* Sun Oct 12 2008 Led <led@altlinux.ru> 1.2.1-alt4
- fixed License

* Sun Nov 11 2007 Led <led@altlinux.ru> 1.2.1-alt3
- added %name-1.2.1-x86_64.patch

* Thu Sep 14 2006 Led <led@altlinux.ru> 1.2.1-alt2
- cleaned up spec

* Mon Feb 20 2006 led <led@altlinux.ru> 1.2.1-alt1
- initial build
