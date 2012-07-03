%define svn_rev 852
Name: cdrkit
Version: 1.1.11
Release: alt1
Epoch: 1

Summary: A collection of command-line CD/DVD recording utilities
License: GPLv2
Group: Archiving/Cd burning
Url: http://www.cdrkit.org/

# http://cdrkit.org/releases/%name-%version.tar.gz
# svn://svn.debian.org/debburn/cdrkit/trunk
Source: %name-%version.tar
Patch1: cdrkit-1.1.11-owl-fixes.patch
Patch2: cdrkit-1.1.9-owl-tmp.patch
Patch3: cdrkit-1.1.9-owl-doc.patch
Patch4: cdrkit-1.1.9-owl-rcfile.patch
Patch5: cdrkit-1.1.9-owl-privacy.patch
Patch6: cdrkit-1.1.9-owl-messages.patch
Patch7: cdrkit-1.1.9-alt-bound.patch
Patch8: cdrkit-1.1.9-alt-format.patch

Requires: wodim = %epoch:%version-%release
Requires: readom = %epoch:%version-%release
Requires: genisoimage = %epoch:%version-%release
Requires: icedax = %epoch:%version-%release
Requires: dirsplit = %epoch:%version-%release
Requires: %name-doc = %epoch:%version-%release
Requires: %name-utils = %epoch:%version-%release

BuildRequires: bzlib-devel cmake libcap-devel libmagic-devel zlib-devel

%description
cdrkit is a suite of programs for recording CDs and DVDs, blanking CD-RW
media, creating ISO-9660 filesystem images, extracting audio CD data,
and more.  The programs included in this suite were originally derived
from several sources, most notably mkisofs by Eric Youngdale and others,
cdda2wav by Heiko Eissfeldt, and cdrecord by Jrg Schilling.
However, cdrkit is not affiliated with any of these authors; it is now
an independent project.

%package -n wodim
Summary: A command line utility to write data to optical disk media
Group: Archiving/Cd burning
Requires: cdrkit-control
Provides: cdrecord = 6:2.01.01, cdrecord-classic = 6:2.01.01
Obsoletes: cdrecord, cdrecord-classic
Provides: dvdrecord = 0:0.3.1
Obsoletes: dvdrecord

%package -n readom
Summary: A command line utility to read or write data Compact Discs
Group: Archiving/Cd burning
Requires: cdrkit-control
Provides: readcd = 6:2.01.01
Obsoletes: readcd

%package -n genisoimage
Summary: A command line utility to create an ISO9660/Joliet/HFS filesystem
Group: Archiving/Cd burning
Provides: mkisofs = 6:2.01.01
Obsoletes: mkisofs

%package -n icedax
Group: Sound
Summary: A command line utility for sampling/copying .wav files from digital audio CDs
Provides: cdda2wav = 6:2.01.01
Obsoletes: cdda2wav

%package -n dirsplit
Summary: A dirsplit utility
Group: Archiving/Cd burning

%package doc
Summary: Documentation for the cdrkit package suite
Group: Archiving/Cd burning
BuildArch: noarch

%package utils
Summary: Command line utilities for dumping and verifying ISO9660 images
Group: Archiving/Cd burning
Provides: isoutils = 6:2.01.01
Obsoletes: isoutils

%package -n netscsid
Summary: NET SCSI Daemon
Group: Archiving/Cd burning

%description -n wodim
Wodim is an application for creating audio and data CDs.  Wodim
works with many different brands of CD recorders, fully supports
multi-sessions and provides human-readable error messages.

%description -n readom
readom is a command line utility to read or write data Compact Discs.

%description -n genisoimage
The genisoimage program is used as a pre-mastering program; i.e.,
it generates the ISO9660 filesystem.  genisoimage takes a snapshot of
a given directory tree and generates a binary image of the tree which
will correspond to an ISO9660 filesystem when written to a block device.
genisoimage is used for writing CD-ROMs, and includes support for
creating bootable El Torito CD-ROMs.

%description -n icedax
icedax is a sampling utility for CD-ROM drives that are capable of
providing a CD's audio data in digital form to your host.  Audio data
read from the CD can be saved as .wav or .sun format sound files.
Recording formats include stereo/mono, 8/12/16 bits and different
rates.  icedax can also be used as a CD player.

%description -n dirsplit
The dirsplit utility splits directory into multiple with equal size.

%description doc
This package contains documentation for the cdrkit package suite,
namely wodim, readom, genisoimage, icedax, etc.

%description utils
This package contains several command line utilities for dumping and
verifying ISO9660 images.

%description -n netscsid
netscsid is a NET SCSI Daemon.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
#patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

sed -i '/^require v5\.8\.1;$/d' 3rd-party/dirsplit/dirsplit
find -type f -print0 |
	xargs -r0 sed -i s,/usr/local/bin/perl,/usr/bin/perl,g --
find doc -type f -print0 |
	xargs -r0 chmod a-x --

%build
%add_optflags -fno-strict-aliasing -Wno-unused
%make_build CFLAGS='%optflags' VERBOSE=1

%install
make install PREFIX=%buildroot%prefix VERBOSE=1

%define docdir %_docdir/%name
mkdir -p %buildroot%docdir
cp -a ABOUT COPYING FAQ FORK START doc/WHY doc/READMEs \
	doc/wodim doc/genisoimage doc/icedax %buildroot%docdir/

cd %buildroot%_bindir
chmod 700 wodim readom
ln -s wodim cdrecord
ln -s wodim dvdrecord
ln -s readom readcd
ln -s genisoimage mkisofs
ln -s genisoimage mkhybrid
ln -s icedax cdda2wav
cd %buildroot%_man1dir
ln -s wodim.1 cdrecord.1
ln -s wodim.1 dvdrecord.1
ln -s readom.1 readcd.1
ln -s genisoimage.1 mkisofs.1
ln -s genisoimage.1 mkhybrid.1
ln -s icedax.1 cdda2wav.1

%pre -n wodim
%pre_control wodim

%post -n wodim
%post_control wodim

%triggerpostun -n wodim -- cdrecord, cdrecord-classic, dvdrecord
rm -f '/etc/alternatives/links/|usr|bin|cdrecord'
ln -snf wodim %_bindir/cdrecord

%pre -n readom
%pre_control readom

%post -n readom
%post_control readom

%files

%files doc
%docdir

%files -n wodim
%_bindir/wodim
%_bindir/*record
%_man1dir/wodim.*
%_man1dir/*record.*

%files -n readom
%_bindir/read??
%_man1dir/read??.*

%files -n genisoimage
%_bindir/genisoimage
%_bindir/mk*
%_man5dir/genisoimage*
%_man1dir/genisoimage.*
%_man1dir/mk*.*

%files -n icedax
%_bindir/icedax
%_bindir/cdda2*
%_bindir/readmult
%_bindir/pitchplay
%_man1dir/icedax.*
%_man1dir/cdda2*.*
%_man1dir/readmult.*
%_man1dir/pitchplay.*
%_man1dir/list_audio_tracks.*

%files -n dirsplit
%_bindir/dirsplit
%_man1dir/dirsplit.*

%files -n netscsid
%_sbindir/*

%files utils
%_bindir/*
%exclude %_bindir/wodim
%exclude %_bindir/*record
%exclude %_bindir/read*
%exclude %_bindir/genisoimage
%exclude %_bindir/mk*
%exclude %_bindir/icedax
%exclude %_bindir/cdda2*
%exclude %_bindir/pitchplay
%exclude %_bindir/dirsplit
%_man1dir/*
%exclude %_man1dir/wodim.*
%exclude %_man1dir/*record.*
%exclude %_man1dir/read*.*
%exclude %_man1dir/genisoimage.*
%exclude %_man1dir/mk*.*
%exclude %_man1dir/icedax.*
%exclude %_man1dir/cdda2*.*
%exclude %_man1dir/pitchplay.*
%exclude %_man1dir/list_audio_tracks.*
%exclude %_man1dir/dirsplit.*

%changelog
* Sat Dec 04 2010 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.11-alt1
- Updated to cdrkit-1.1.11 release.

* Thu Mar 25 2010 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.10.841-alt1
- Updated to cdrkit-1.1.10 release.

* Tue Nov 24 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.9.832-alt4
- Fixed build with cmake-2.8.0 (by Andrey Rahmatullin).

* Mon Sep 07 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.9.832-alt3
- Removed erroneous hunk in bound checking patch.

* Mon Sep 07 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.9.832-alt2
- Changed wodim subpackage dependencies and triggers:
  + Fixed update in place of dvdrecord package (closes: #21415).
  + Fixed install in place of cdrecord-classic package.

* Thu Sep 03 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.9.832-alt1
- Initial revision, based on cdrkit post-1.1.9 svn revision 832 and
  patches from cdrkit-1.1.9-owl3.
