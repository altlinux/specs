%define origrelease 2
Name: freedup
Summary: Links substantially identical, duplicate files to save file system space
Version: 1.6
Release: alt1
License: GPL
Group: File tools
Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: http://freedup.org/freedup-%version-%origrelease-src.tar
#.bz2
Url: http://freedup.org/

# Automatically added by buildreq on Thu Jul 28 2011 (-bi)
# optimized out: elfutils
BuildRequires: fakeroot

%description
Freedup eliminates duplicate files by linking them, and thus reduces the amount
of used disk space within one or more file systems. By default, hardlinks are
used on a single device, symbolic links when the devices differ. A set of
options allows you to modify the methods of file comparison, the hash functions,
the linking behavior, and the reporting style. You may use batch or interactive
mode. Freedup usually only considers identical files, but when comparing audio
or graphics files, you may elect to ignore the tags. Multimedia files often are
a good target for deduplication.

%prep
%setup
rm -f *.o %name symharden

%build
make %name symharden \
	CFLAGS="%optflags -Wall -pedantic -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 -DFLAVOUR='' -std=gnu99"

%check
fakeroot make test

%install
mkdir -p %buildroot{/usr/bin,%_man1dir}
install -s -p -m 755 %name symharden %buildroot%_bindir/
install -p -m 644 %name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/*
%doc TODO README README.SHA COPYING.SHA verify ChangeLog html
%_man1dir/%name.1*

%changelog
* Sun Jul 31 2011 Ildar Mulyukov <ildar@altlinux.ru> 1.6-alt1
- initial build for ALT Linux Sisyphus

* Thu Feb 04 2011 devel (AN) <AN@freedup.org>
- Bugfixes in version 1.6-2
  + replaced softlink to symharden.c

* Thu Jan 11 2011 devel (AN) <AN@freedup.org>
- Changes to version 1.6-1
  + signal handler catches CTRL-C to free duplicates discovered so far
  + added if-defines to avoid double parsing of *.h files
  + removed inline directive [due to compile errors by request of Andres Meyer]
- Enhancement in version 1.6-1
  + added listener interface
  + added new platform makefile for Apple Mac Version 10.6.0 i386 [tested]
  + catch filesystem errors (e.g. /sys) and print warnings instead of assertions
  + added (sp)lint rule for linux
  + added symharden tool to convert softlinks into hardlinks whereever possible
- Bugfixes in version 1.6-1
  + added missing #ifdef HASHSUM statements [notified by Linc Davis]
  + using include of <sys/stat.h> instead of <linux/stat.h> [by Linc Davis]
  + added fclose() to mp4.c and checking all fclose()/fseek() result codes
  + linted mp3.c, mp4.c mpc.c, auto.c, ogg.c, jpg.c and my.c
  + partially linted freedup.c (e.g. splint does not fail anymore)
  + moved filesize variables in "extra" functions from size_t=int to ulong
  + incorporated patch to avoid segfaults [by Charles Duppy]
- Known Bug in 1.6-1
  + Apple Mac version does not link different ownerships (yet reason unclear)

* Thu Mar 06 2008 devel (AN) <AN@freedup.org>
- Changes to unpublished version 1.5-4
  + Corrected Copyright statements to comply with OSF (GPL) requirements
- Enhancement in unpublished version 1.5-4
  + minor corrections to man page

* Thu Mar 06 2008 devel (AN) <AN@freedup.org>
- Changes to version 1.5-3
  + gui defaults to off, activate and deactivate using "make webon/weboff/state"

* Thu Mar 06 2008 devel (AN) <AN@freedup.org>
- Changes to version 1.5-3
  + the features provided with option -W are for testing purpose only
  + basic web interface offered (reply not accepted yet)
  + changed invisible default option for sorting criteria to '.'
- Enhancement in version 1.5-3
  + automated installation routine for xinetd and inetd
  + deinstall script for xinetd only
  + added html pages to rpm package as well
- Bugfixes in version 1.5-3
  + removed a leftover debug command

* Sun Mar 02 2008 devel (AN) <AN@freedup.org>
- Enhancement in version 1.5-2
  + enable freedup to restore directory time stamp after linking (option -T)
  + added usage help, man page and syntax web page for option -T
  + extended test3 in Makefile.tests to check new option -T
  + streamlined Makefile.tests using for-loops and 'test -ef'(25%% reduced size)
  + Makefile.tests now needs gnu 'test' facility '[' to work correctly
- Bugfixes in version 1.5-2
  + corrected date in copyright notice for -V
  + added '+' and '-' to -k option in online syntax help

* Sat Feb 02 2008 devel (AN) <AN@freedup.org>
- Enhancement in version 1.5-1
  + file trees are now scanned by an internal routine, find is called on demand
  + output during tree scanning changes every 1000 files (i.e. find activity)
  + updated man page to show how to use find instead of the internal routine
  + testing did not proof performance gain when using internal routine
- Changes in version 1.5-1
  + first helper routines for web-based GUI
  + corrected and completed copyright information
- Bugfixes in version 1.5-1
  + minor corrections to freedup man page

* Mon Dec 31 2007 devel (AN) <AN@freedup.org>
- Enhancement in version 1.4-4
  + report deleted files and the space saved (avail in interactive mode only)
  + link directions '+'/'-' allow to select source by size (extra style only)
- Bugfixes in version 1.4-4
  + Makefile copies so that rpm cygwin executable is executable under cygwin
  + initialize all *source variables in dupinfo_entry() to avoid segfaults
  + do not offer linking when files already linked in interactive mode (w/o -H)
  + report linked files and bytes in interactive mode for extra styles

* Fri Dec 28 2007 devel (AN) <AN@freedup.org>
- Enhancement in version 1.4-3
  + one common routine to open config file (simplifies later extensions)
  + added routine to print existing environments in help (for a test period)
- Bugfixes in version 1.4-3
  + use character instead of ascii code for '-k' in config file
  + finally fixed missing initialisation to avoid failing (n+m) assertion
  + if mp4 module is applied on mp3 files no more infinite loops should occur

* Mon Dec 24 2007 devel (AN) <AN@freedup.org>
- Enhancement in version 1.4-2
  + there are no more restrictions on the number of identical files
  + added '-H' for the same use as in fdupes: show hardlinked files too
  + added man page description for '-k' and '-H'
- Bugfixes in version 1.4-2
  + improved test routine for MP3 and JPG Mix
  + added new line before printing statistics
  + stop printing interactive selection list, when there are no more letters

* Sat Dec 21 2007 devel (AN) <AN@freedup.org>
- Enhancement in version 1.4-1
  + '-k' option changed and recognized key pattern (same key as interactive)
  + '-ni' now reports reliable predictions on linked files and bytes
  + '-n' is reported (and indicated) to report to much for multiple links.
  + options '-qin' (add '-q') now print file clusters like "fdupes -r"
  + erased code that was not active anymore
  + reduction of qsort calls gave more performance which ate up more lstat()s
- Bugfixes in version 1.4-1
  + '--timediff' is only set to 0 if '--sametime' is disabled
  + fixed algorithm stability problem, i.e. one qsort run is now sufficient.
- New in version 1.3-2
  + ability set a mask for file permissions if 'same' permission is desired.
  + group commands in interactive mode
   - '@' suggests to link all files to entry with maximum link count
   - '#' suggests to link all files to first entry given on command line
   - '<' suggests to link all files to the oldest identical entry
   - '>' suggests to link all files to the newest identical entry
  + '-k' forces link source by sequence of file naming (compare with '@' above)
- Enhancement in version 1.3-2
  + changed default to NOT to use hash functions
  + writing also given directories to config file (w/o probing for existance)
  + first preparations for a netbsd translation
- Bugfixes in version 1.3-2
  + findoptions need not to be defined for reading directories from config file
  + assertion in compare_..._hash moved into parenthesis where it belongs to.

* Sat Dec 15 2007 devel (AN) <AN@freedup.org>
- New in version 1.3-1
  + '-#' now requires an integer option (watch out for difficulties!)
  + advanced hash sum calculation is now usable (nearly no penalty, but gain)
  + freedup.org is the new website (the old address remains valid)
- Enhancement in version 1.3-1
  + new algorithm calculates internal hash sum during file comparison
  + defaults to new hash algorithm (use --hash 1 to switch to old behaviour)
  + more detailed man page sections on -e, -# and -o.
- Bugfixes in version 1.3-1
  + hash sum counter counted double for internal hash algorithm

* Mon Dec 10 2007 devel (AN) <AN@freedup.org>
- New in version 1.2-1
  + Easy storeing & loading of options using environments (not: -Vhaq? )
    Options given before are overwritten if present in that environment
  + option -b to set basedir (may be useful with environments)
  + option -D allows to set a maximum time difference
- Enhancement in version 1.2-1
  + long options are offered
  + help screen adopted
  + added inactive, buggy code for delayed hash calculation ("hi performance")
  + a test for -D was introduced
- Bugfixes in version 1.2-1
  + ignore failed calls of gethash() (e.g. due to file removal)		  [rare]
  + expect that ferror() may be set in case of feof()	      [not reported yet]
  + qsort() now gets the difference in contents for files of the same size.[nry]

* Thu Dec 06 2007 devel (AN) <AN@freedup.org>
- Enhancement in version 1.1-3
  + extended test6 to check for symlinking of full and partial filename
  + description in spec file renewed
- Bugfixes in version 1.1-3
  + corrected symlinking files with partial filename to those with full
  + added rules to have html files for rpm with cygwin where they are expected

* Sun Dec 02 2007 devel (AN) <AN@freedup.org>
- Enhancement in version 1.1-2
  + allow one more start token 'moov' for mp4 style (mov-Suffix)
  + added -x and -e switch with explanation to man page
- Bugfixes in version 1.1-2
  + corrected MANPAGE definition in spec file for rpm with cygwin
  + replaced dependencies in Makefile.tests to ensure correct linking

* Wed Nov 28 2007 devel (AN) <AN@freedup.org>
- New in version 1.1-1
  + header/tail skipping and tag skipping introduced for extra modules
  + extra modules for mp3, mp4, mpc, ogg and jpeg tags (still beta testing)
  + the extra module "auto" selects extra modules by their magic automatically
  + enabled extra modules inhibit external hashing functions
  + test11 was added to check the extra style modules mp3, mp4 and jpg
  + extra modules allow to be compiled as individual testing utilities
- Enhancement in version 1.1-1
  + print only available hashmodes and extramodules with help
  + now using defines for internal hash method (simplifies replacement)
  + a message is printed if root privileges were missing during tests
  + using a size that may differ from the file size
- Bugfixes in version 1.1-1
  + test10 now recognizes non-default sort order
  + correction to help/usage message
  + added missing stop conditions to byte-by-byte-comparison

* Sat Nov 10 2007 devel (AN) <AN@freedup.org>
- Enhancement in version 1.0-5
  + now compiles unchanged with Cygwin and Linux
  + Makefiles were modified to simplify testing and compilation
  + removed conversion untility "encap"
  + ignore missing "html2text"
  + generate a readable plain text README from README.html
  + more file groups in the header section of Makefile
  + sha1.c is now taken from and referenced to original source.
  + added COLLATERAL section to man page
  + added verification program to distribution

* Wed Nov 07 2007 devel (AN) <AN@freedup.org>
- Enhancement in version 1.0-4
  + report version and copyright on '-V'
  + included Allan Saddis SHA1 implementation as found in duff
  + added more hash functions to default list
  + use '-t' to select certain hash methods manually
  + internal hash function is default, external ones require options
  + introduced colour into Makefile testing routines
  + Makefile relies on GNU make to auto-include OS specific settings
  + added rules and other parts to generate debian packages
- Bugfixes in version 1.0-4
  + errors on hash function testing are easier to understand now.
  + errors on hash function selection are reported only with '-v'
  + full special character support if internal hash methods chosen
  + more recent list of files for tarball, clean and distclean

* Sat Nov 03 2007 devel (AN) <AN@freedup.org>
- Enhancement in version 1.0-3
  + Hash Algorithms now are included and work for cygwin as well
  + improved interactive dialogues
  + build symbolic link path in shortest distance to given target path
- Bugfixes in version 1.0-3
  + Successful testing with AIX 5.3
  + do not stop interactive mode if setting the terminal discipline fails
  + More intense Testing of comparison function (Makefile)
  + More reliable testing of interactive mode and relative Path (Makefile)
  + removed DANGER message due to program improvements
  + special character support if external hash methods are disabled (-#)

* Wed Oct 31 2007 devel (AN) <AN@freedup.org>
- Enhancement in version 1.0-2
  + runtime check for one out of three usable external hash methods (SHA1, MD5, SUM)
- Bugfixes in version 1.0-2
  + corrected comparison length when comparing by memcmp() / failed with cygwin
  + renamed finfo structure to frdinfo to avoid collisions with AIX
  + added ALLPERMS define for non-Linux systems
  + added Makefile define for FREEDUPEXE, since cygwin fails on ./freedup
  + added Makefile define for echo with backslash translation
  + added Makefile check for valid HASH executables in freedup.h
  + print "ln -f <file1> <file2>" , so you may execute it without changes

* Sat Oct 27 2007 devel (AN) <AN@freedup.org>
- Enhancements in version 1.0
  + new interactive mode with full choice list
  + separated linking task into explicit function
  + option -i asks for manual replacement selections
  + options -in print file clusters like "fdupes -r"
  + partial code clean up
- Bugfixes
  + avoid name collisions by generating temporary filenames
  + always check files for existance to avoid early termination
  + previously checked that permissions differ (instead of being identical)
  + previously checked that groups differ (instead of being identical)
  + previously checked that users differ (instead of being identical)
  + previously checked that times differ (instead of being identical)

* Tue Oct 09 2007 devel (AN) <AN@freedup.org>
- Enhancements in version 0.9 freedup.c
  + added interactive mode (option -i) [this option is still beta]
  + added delete selections in interactive mode
  + added html documentation to archive
  + added tolerance to unavailable files on fopen() [Rel.2]
- Enhancements in version 0.9 Makefile
  + added definitions: INSTALLDIR, MANPAGEDIR, etc
  + added targets: tarball, install, clean, distclean
  + version and release are now defined in freedup.spec only
  + added test that tries all numeric options during interaction [Rel.2]
- Enhancements in version 0.9 freedup.spec
  + use install instead of cp

* Thu Oct 04 2007 devel (AN) <AN@freedup.org>
- Enhancements in version 0.8
  + avoid linking empty files (new option -0)
  + avoid printing any information (new option -q)
  + updated man page to reflect all options
  + added test7 to check for correct handling of empty files
- Bugfixes
  + use mode instead of size to determine file type
  + starting with release 1 (not with 0)
  + added aditional file to distribution

* Tue Oct 02 2007 devel (AN) <AN@freedup.org>
- Enhancements in version 0.7
  + compiles under cygwin (no hash  support with cygwin)
  + works for NTFS file systems (at least test cases worked)

* Fri Sep 21 2007 devel (AN) <AN@freedup.org>
- Enhancements in version 0.6
  + MD5 hash scanning may be disabled by options now

* Wed Sep 12 2007 devel (AN) <AN@freedup.org>
- Enhancements in version 0.5
  + exclude non-regular files from investigation using lstat
  + error handling for OS functions now with messages instead of asserts
  + corrected and completed some text messages
  + Tested 400000 multimedia files in upto 20 trees

* Wed Aug 29 2007 devel (AN) <AN@freedup.org>
- Enhancements in version 0.4
  + now a single run should be sufficient in most cases
  + added -w to force symlinks instead of hardlinks
  + added -l to allow only hardlinks and no symlinks
  + first test comparing results for different trees
  + more structured web page
- Bugfixes
  + no more overwriting of previously scanned trees
  + comparision return values are not zero if additional tests fail
  + completed bug fixes from version 0.2

* Fri Aug 24 2007 devel (AN) <AN@freedup.org>
- Enhancements in version 0.3
  + splitted user and group comparison into separate tests
- Bugfixes
  + argument position is now less important than existing link count
    This was needed to avoid alternating link replacements
  + stop when number of changes gets constant :-(healing symptoms)
  + do not reset file counter when deciding to realloc()

* Tue Aug 21 2007 devel (AN) <AN@freedup.org>
- Enhancements in version 0.2
  + call "find" only once
  + allow input from stdin
  + some code cleaning
  + added man page
  + added more tests
  + improved Makefile
- Bugfixes
  + added -a to getopt string
  + report correct version
  + corrected basename macro

* Thu Aug 16 2007 devel (AN) <AN@freedup.org>
- Initial Release
