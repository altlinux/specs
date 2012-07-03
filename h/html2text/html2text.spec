Name: html2text
Version: 1.3.2a
Release: alt2

Summary: An HTML-to-text converter
License: GPL
Group: Text tools
Url: http://www.mbayer.de/html2text/
Packager: Dmitry V. Levin <ldv@altlinux.org> 

Source: ftp://ftp.ibiblio.org/pub/linux/apps/www/converters/%name-%version.tar.bz2
Patch: %name-1.3.2a-alt-urlistream-get.patch

BuildRequires: gcc-c++

%description
html2text is a command line utility that converts HTML documents into
plain text.
Each HTML document is read from standard input or a (local or remote)
URI, and formatted into a stream of plain text characters that is written
to standard output or into an output-file.  The program preserves the
original positions of table fields and accepts also syntactically
incorrect input, attempting to interpret it "reasonably".  The rendering
is largely customisable through an RC file.

%description -l de
html2text ist ein Programm fuer die Kommandozeile, das HTML-Dateien in
reinen Text umwandelt.
Die HTML-Dateien koennen von Standard Input gelesen werden, als lokale
Dateien vorliegen oder ueber Hypertext Transfer Protocol (HTTP) von
anderen Rechnern geladen werden; die Ausgabe erfolgt auf Standard Output
oder in eine Datei.  html2text setzt Tabellen moeglichst getreu um und
toleriert auch syntaktisch unkorrektes HTML.  Die Art der Umsetzung
urspruenglicher Formatierungen ist dabei weitgehend durch eine
Konfigurationsdatei beeinflussbar.

%prep
%setup -q
%patch -p1
%__gzip -d *.[15].gz

%build
./configure
%make_build DEBUG="%optflags"
%__bzip2 -9kf CHANGES

%install
%__mkdir_p %buildroot%_bindir
%__install -pD -m755 %name %buildroot%_bindir/%name
%__install -pD -m644 %name.1 %buildroot%_man1dir/%name.1
%__install -pD -m644 %{name}rc.5 %buildroot%_man5dir/%{name}rc.5

%files
%_bindir/*
%_mandir/man?/*
%doc CHANGES.bz2 CREDITS KNOWN_BUGS README RELEASE_NOTES TODO

%changelog
* Wed Sep 07 2005 Dmitry V. Levin <ldv@altlinux.org> 1.3.2a-alt2
- Additional convention enforcement on patch file names.

* Wed Sep 07 2005 php-coder <php-coder@altlinux.ru> 1.3.2a-alt1.1
- Fixed handling of 8-bit characters (#7452).
- Added Packager tag.
- Changed %%URL tag.
- Spec cleanup.

* Sun Feb 27 2005 Dmitry V. Levin <ldv@altlinux.org> 1.3.2a-alt1
- Packaged for ALT Linux, based on spec from
  http://userpage.fu-berlin.de/~mbayer/tools/html2text.spec
