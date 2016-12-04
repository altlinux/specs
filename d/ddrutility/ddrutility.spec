Name: ddrutility
Version: 2.8
Release: alt1

Summary: Utility for use with gnuddrescue to aid with data recovery
License: GPLv3+
Group: Archiving/Backup

Url: http://sourceforge.net/projects/ddrutility/
Source0: %name-%version.tar.gz
Source1: %name.watch
# explicitly added texinfo for info files
BuildRequires: texinfo

Requires: sleuthkit ntfs-3g gdisk ddrescue

%description
%name is meant to be a compliment to gnuddrescue.
It is a set of utilities to help with hard drive data rescue.
It currently contains the following utilities:

ddru_findbad
ddru_ntfsbitmap
ddru_ntfsfindbad

%prep
%setup

%build
%make_build

%install
%makeinstall_std \
	bindir=%buildroot%_bindir/ \
	infodir=%buildroot%_infodir/ \
	mandir=%buildroot%_man1dir/

%files
%_bindir/*
%_man1dir/*
%_infodir/*

%changelog
* Sun Dec 04 2016 Michael Shigorin <mike@altlinux.org> 2.8-alt1
- new version (watch file uupdate)
  + why on Earth have they dropped autoconf for manual make?
- added missing Requires: according to README

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1.1
- NMU: added BR: texinfo

* Fri Feb 27 2015 Michael Shigorin <mike@altlinux.org> 2.7-alt1
- new version (watch file uupdate)

* Thu Oct 16 2014 Michael Shigorin <mike@altlinux.org> 2.6-alt1
- new version (watch file uupdate)

* Tue Jun 10 2014 Michael Shigorin <mike@altlinux.org> 2.5-alt1
- new version (watch file uupdate)

* Fri May 16 2014 Michael Shigorin <mike@altlinux.org> 2.4-alt1
- new version (watch file uupdate)

* Sun Apr 27 2014 Michael Shigorin <mike@altlinux.org> 2.3-alt1
- new version (watch file uupdate)

* Wed Apr 23 2014 Michael Shigorin <mike@altlinux.org> 2.2-alt1
- initial package

