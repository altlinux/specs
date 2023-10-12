Name: fatback
Version: 1.3
Release: alt1.1

Summary: A forensic tool for recovering files from FAT file systems
License: GPLv2 and Public Domain
Group: File tools

Url: http://sourceforge.net/projects/fatback
Source: http://downloads.sourceforge.net/%name/%name-%version.tar.gz
Source1: README.Mageia
Patch: fatback-1.3-texinfo.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: flex gcc-c++ texinfo

%description
Fatback is a forensic tool for undeleting files from Microsoft FAT file
systems. Fatback is different from other undelete tools in that
it does the following:
   * Runs under UNIX environments
   * Can undelete files automatically
   * Supports Long File Names
   * Supports FAT12, FAT16, and FAT32
   * Powerful interactive mode
   * Recursively undeletes deleted directories
   * Recovers lost cluster chains
   * Works with single partitions or whole disks

%prep
%setup
cp -a %SOURCE1 .
%patch -p1

%build
%configure
%make
makeinfo --html fatback-manual.texi

%install
%makeinstall_std

mkdir -p %buildroot%_datadir/%name
cp -a fatback-manual_html %buildroot%_datadir/%name/fatback-manual
# Change .info filename to match instructions in man page
mv %buildroot%_infodir/%name{-manual,}.info

%files
%doc README.Mageia
%_bindir/%name
%_mandir/man?/%name.?.*
%_infodir/%name.info.*
%_datadir/%name

%changelog
* Thu Oct 12 2023 Anton Midyukov <antohami@altlinux.org> 1.3-alt1.1
- fix FTBFS

* Tue Apr 15 2014 Michael Shigorin <mike@altlinux.org> 1.3-alt1
- initial build for ALT Linux Sisyphus (based on Mageia package)

* Sat Oct 19 2013 umeabot <umeabot> 1.3-6.mga4
+ Revision: 532154
- Mageia 4 Mass Rebuild

* Sat Aug 17 2013 fwang <fwang> 1.3-5.mga4
+ Revision: 467136
- fix build with recent texinfo

* Fri Jan 11 2013 umeabot <umeabot> 1.3-5.mga3
+ Revision: 350071
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Fri Oct 26 2012 malo <malo> 1.3-4.mga3
+ Revision: 310547
- update RPM group

* Sun Aug 26 2012 barjac <barjac> 1.3-3.mga3
+ Revision: 284270
- Added README.Mageia explaining license validity
- removed .desktop file file for manual as we have no icon
- Corrected GPL version
- Fixed minor typo in description
- imported package fatback

