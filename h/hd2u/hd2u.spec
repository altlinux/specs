
Name: hd2u
Version: 1.0.3
Release: alt1

Group: Text tools
Summary: Converts DOS-style EOLs to UNIX-style EOLs and vice versa.
Url: http://www.megaloman.com/~hany/software/hd2u/
License: GPL

Provides: dos2unix unix2dos
Obsoletes: dos2unix unix2dos

Source: %name-%version.tar.bz2

# Automatically added by buildreq on Wed Apr 21 2004 (-bi)
BuildRequires: libpopt-devel

%description
hd2u is "Hany's Dos2Unix convertor". It provides 'dos2unix'.

'dos2unix' is filter used to convert DOS-style EOLs to UNIX-style EOLs and vice
versa (EOL - End Of Line character). Aditionaly it can also handle files
with Macintosh-style EOLs and convert them into other EOLs.

unix2dos is symbolic link to dos2unix

%prep
%setup -q

%build
%configure
%make_build

%install
mkdir -p %buildroot/%_bindir
%make BUILD_ROOT="%buildroot" install
ln -s dos2unix %buildroot/%_bindir/unix2dos

%files
%_bindir/dos2unix
%_bindir/unix2dos
%doc AUTHORS CREDITS ChangeLog NEWS README TODO

%changelog
* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt1
- new version

* Sat Apr 28 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.1-alt1
- new version

* Wed Aug 17 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.0-alt1
- new version

* Wed Apr 21 2004 Sergey V Turchin <zerg at altlinux dot org> 0.9.1-alt1
- new version

* Mon Jun 16 2003 Sergey V Turchin <zerg at altlinux dot org> 0.8.1-alt1
- build for ALT

* Wed Feb 26 2003 Peter Hanecak <hanecak@megaloman.sk> 0.8.1-1
- dos2unix.c:
  - mkstemp() used instead of tmpnam()
  - temporary directory specified by TMPDIR or TMP environment variable
    used; if none of them is avialable, then "/tmp" is used
- spec:
  - group changed from Utilities/Text to Applications/Text
  - s/Copyright/License

* Tue May  7 2002 Peter Hanecak <hanecak@megaloman.sk>
[0.8.0-1]
- ChangeLog: fixed typo
- README: updated "Usage" chapter
- dos2unix.c: updated help
- applied patch from Philip White <pwhite@mailhaven.com>
  (minor grammar corrections and miscellaneous beautifying in help & docs)

* Fri Jan  4 2002 Peter Hanecak <hanecak@megaloman.sk>
[0.7.2-1]
- INSTALL: fixed info about changing prefix
- Makefile.in: create bin directory before installing hd2u binary into it;
  this should solve the problem when using custom prefix in which 'bin'
  directory does not exists (thanks to Emanuele Olivetti <olivetti@itc.it>
  for reporting the problem)
- dos2unix.c: fix gcc 2.96 warning: string length '687' is greater than the
  minimum length '509' ISO C89 is required to support

* Sun Feb 11 2001 Peter Hanecak <hanecak@megaloman.sk>
[0.7.1-1]
- dos2unix.c: --skipbin (-b) switch added: binary files won't be converted
- dos2unix.c: --test (-t): NO output (not even verbose)
- dos2unix.c: conversion of input data from stdin works again
- dos2unix.c: reworked convert(): conversion of input data from stdin works
  again; better separation of detection, verbose info output and other logic
- dos2unix.c: rouge '\r' are reported but only conversion dos -> unix affects
  them (they are skipped)
- dos2unix.c: directories when given as input are skipped

%changelog
* Sun Feb 11 2001 Peter Hanecak <hanecak@megaloman.sk>
[0.7.0-1]
- documentation updates

* Wed Feb  7 2001 Rob Ginda <rginda@netscape.com>
- dos2unix.c: more robust source format detection can detect binary files,
  mixed mode files, and files with no line endings at all
- dos2unix.c: added automatic skipping of binary files
- dos2unix.c: added --test mode to check filetype without converting
- dos2unix.c: added --verbose option to show status messages while working
- dos2unix.c: converted C++ style (//) comments to C style (/**/) (some C
  compilers will choke on //)
- dos2unix.c: reorderd function definition to avoid prototypes
- dos2unix.c: replaced hard tabs with 4 spaces
- dos2unix.c: added emacs modeline

* Sun Jan 21 2001 Peter Hanecak <hanecak@megaloman.sk>
[0.6.0-1]
- documentation: fixed typos
- dos2unix.c: handle NULL when returned by tmpnam()
- Makefile.in: added '-Wall -pedantic' to CFLAGS

* Tue Oct  3 2000 Peter Hanecak <hanecak@megaloman.sk>
[0.5.12-1]
- documentation extended (popt) and updated (configure)
- configure.in: check for getopt_long() function

* Tue Sep 26 2000 Peter Hanecak <hanecak@megaloman.sk>
[0.5.11-1]
- configure.in: check for popt library

* Mon Aug  7 2000 Peter Hanecak <hanecak@megaloman.sk>
[0.5.10-1]
- autoconfigure

* Sat Aug  5 2000 Peter Hanecak <hanecak@megaloman.sk>
[0.5.9-2]
- --auto switch
- do not touch files which are alredy in specified target format
- spec: Prefix, %%{_tmppath} and %%{_bindir} used

* Thu Nov 25 1999 Peter Hanecak <hanecak@megaloman.sk>
[0.5.0-2]
- added URL to spec
- mostly typo fixes

* Thu Nov 25 1999 Peter Hanecak <hanecak@megaloman.sk>
[0.5.0]
- renamed package to 'hd2u' to avoid conflicts with alredy existing
  dos2unix package(s) (is 'hd2u' original enough? :)
- moved binary to '/usr/bin'
- added some documentation
- first public release

* Thu Oct 21 1999 Peter Hanecak <hanecak@megaloman.sk>
[0.5.0]
- speed optimisation

* Thu Oct 21 1999 Peter Hanecak <hanecak@megaloman.sk>
[0.4.0]
- coversion of file(s) specified as command line parameters

* Tue Oct 19 1999 Peter Hanecak <hanecak@megaloman.sk>
[0.3.0]
- getopt used to process parameters
- help displayed when incorect options

* Sun Sep 26 1999 Peter Hanecak <hanecak@megaloman.sk>
[0.3.0]

* Fri Mar 26 1999 Peter Hanecak <hanecak@megaloman.sk>
[0.2.0]
- initial spec
