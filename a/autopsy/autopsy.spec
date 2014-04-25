Name: autopsy
Version: 2.24
Release: alt1

Summary: Autopsy Forensic Browser
License: GPLv2+
Group: System/Base

Url: http://www.sleuthkit.org
Source0: http://dfn.dl.sourceforge.net/sourceforge/autopsy/%name-%version.tar.gz
Source1:   Autopsy
Source2:   autopsy.desktop
Source3:   autopsy.png
Patch: autopsy-2.24-1.patch
Packager: Michael Shigorin <mike@altlinux.org>

Requires: beesu binutils file grep
Requires: sleuthkit >= 1.61
Requires: aff-tools

BuildRequires: /usr/bin/convert
BuildArch: noarch

# found by perl.req
Requires: perl(File/Glob.pm), perl(POSIX.pm), perl(Socket.pm) perl(lib.pm)
# *.pm aren't installed properly
AutoReqProv: yes, noperl

%add_perl_lib_path %_datadir/autopsy
%add_perl_lib_path %_datadir/autopsy/lib

%description
The Autopsy Forensic Browser is a graphical interface to the
command line digital forensic analysis tools in The Sleuth Kit.
Together, The Sleuth Kit and Autopsy provide many of the same
features as commercial digital forensics tools for the analysis
of Windows(tm) and UNIX file systems (NTFS, FAT, FFS, EXT2FS,
and EXT3FS).

The Sleuth Kit and Autopsy are both Open Source and run on UNIX
platforms. As Autopsy is HTML-based, the investigator can connect
to the Autopsy server from any platform using an HTML browser.
Autopsy provides a "File Manager"-like interface and shows
details about deleted data and file system structures.

%prep
%setup
%patch -p1

%build
# "build" autopsy
cat > autopsy << EOF
#!%_bindir/perl -wT
use lib '%_datadir/autopsy/';
use lib '%_datadir/autopsy/lib/';
EOF
cat base/autopsy.base >> autopsy

# "build" make-live-cd
cat > make-live-cd << EOF
#!%_bindir/perl
use lib '%_datadir/autopsy/';
use lib '%_datadir/autopsy/lib/';
EOF
cat base/make-live-cd.base >> make-live-cd

# "build" conf.pl
cat > conf.pl << EOF
# Autopsy configuration settings

# when set to 1, the server will stop after it receives no
# connections for STIMEOUT seconds.
\$USE_STIMEOUT = 0;
\$STIMEOUT = 3600;

# number of seconds that child waits for input from client
\$CTIMEOUT = 15;

# set to 1 to save the cookie value in a file (for scripting)
\$SAVE_COOKIE = 1;

\$INSTALLDIR = '%_datadir/autopsy/';

# System Utilities
\$STRINGS_EXE = '%_bindir/strings';
\$GREP_EXE = '/bin/grep';
\$FILE_EXE = '%_bindir/file';
\$MD5_EXE = '%_bindir/md5sum';
\$SHA1_EXE = '%_bindir/sha1sum';

# Directories
\$TSKDIR = '%_bindir/';
\$NSRLDB = '';
\$LOCKDIR = '%_localstatedir/morgue';
EOF

%install
install -d %buildroot{%_sbindir,%_man1dir}
install -d %buildroot{%_logdir/autopsy,%_localstatedir/morgue}
install -d %buildroot%_datadir/autopsy/{help,lib,pict}

install -pm755 autopsy %buildroot%_sbindir/autopsy
install -pm755 make-live-cd %buildroot%_sbindir/make-live-cd
install -pm755 conf.pl %buildroot%_datadir/autopsy/
install -pm644 help/*.html %buildroot%_datadir/autopsy/help/
install -pm644 lib/*.p* %buildroot%_datadir/autopsy/lib/
install -pm644 man/man1/autopsy.1 %buildroot%_man1dir/
install -pm644 pict/* %buildroot%_datadir/autopsy/pict/

install -pDm755 %SOURCE1 %buildroot%_bindir/Autopsy
install -pDm644 %SOURCE2 %buildroot%_desktopdir/autopsy.desktop

# Install icon
for res in 16x16 32x32 48x48 96x96; do \
	mkdir -p %buildroot%_iconsdir/hicolor/$res/apps
	convert -size 248x248 %SOURCE3 \
		-resize $res %buildroot%_iconsdir/hicolor/$res/apps/%name.png
done

%files
%doc COPYING docs/*.txt *.txt
%_sbindir/autopsy
%_sbindir/make-live-cd
%_man1dir/*
%_datadir/autopsy
%_bindir/Autopsy
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.png
%dir %attr(700,root,root) %_logdir/autopsy
%dir %attr(700,root,root) %_localstatedir/morgue

%changelog
* Fri Apr 25 2014 Michael Shigorin <mike@altlinux.org> 2.24-alt1
- initial build for ALT Linux Sisyphus (based on openSUSE/ROSA packages)
- added ext4 support and fixup patch by Maxim Suhanov

