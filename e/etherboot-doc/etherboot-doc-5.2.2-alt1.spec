%define bname etherboot
Name: %bname-doc
Serial: 1
Version: 5.2.2
Release: alt1
Summary: Etherboot documentation
License: GPL
Group: Documentation
Url: http://%bname.sourceforge.net
#Source: %name-%version.tar.bz2
Source: %name-%version-nosrc.tar.bz2
BuildArch: noarch
Requires: %name-html = %serial:%version-%release
Requires: %name-ps = %serial:%version-%release
Requires: %name-text = %serial:%version-%release

# Automatically added by buildreq on Wed Aug 01 2007 (-bi)
BuildRequires: gzip-utils

%description
Etherboot is a software package for creating ROM images that can
download code over an Ethernet network to be executed on an x86
computer. Many network adapters have a socket where a ROM chip can be
installed. Etherboot is code that can be put in such a ROM. Etherboot
is normally used for for booting PCs diskless.

This package contains extensive %bname documentation in plain text,
HTML and PostScript.


%package html
Summary: Etherboot HTML documentation
Group: Documentation

%description html
Etherboot is a software package for creating ROM images that can
download code over an Ethernet network to be executed on an x86
computer. Many network adapters have a socket where a ROM chip can be
installed. Etherboot is code that can be put in such a ROM. Etherboot
is normally used for for booting PCs diskless.

This package contains extensive %bname documentation in HTML.


%package ps
Summary: Etherboot PostScript documentation
Group: Documentation

%description ps
Etherboot is a software package for creating ROM images that can
download code over an Ethernet network to be executed on an x86
computer. Many network adapters have a socket where a ROM chip can be
installed. Etherboot is code that can be put in such a ROM. Etherboot
is normally used for for booting PCs diskless.

This package contains extensive %bname documentation in PostScript.


%package text
Summary: Etherboot documentation in plain text format
Group: Documentation

%description text
Etherboot is a software package for creating ROM images that can
download code over an Ethernet network to be executed on an x86
computer. Many network adapters have a socket where a ROM chip can be
installed. Etherboot is code that can be put in such a ROM. Etherboot
is normally used for for booting PCs diskless.

This package contains extensive %bname documentation in plain text
format.


%prep
#%%setup -n doc
%setup


%install
#find html ps text -type f \! -name '.*' -print0 | xargs -0 -I{} install -pD -m 0644 {} %buildroot%_docdir/%bname/{}
find html ps text -type f -print0 | xargs -0 -I{} install -pD -m 0644 {} %buildroot%_docdir/%bname/{}
install -d -m 0755 %buildroot%_docdir/%bname/{ps,text}
gzip --best --force %buildroot%_docdir/%bname/{ps,text}/*
zme %buildroot%_docdir/%bname/{ps,text}/*


%files


%files html
%_docdir/%bname/html


%files ps
%_docdir/%bname/ps


%files text
%_docdir/%bname/text


%changelog
* Fri Aug 03 2007 Led <led@altlinux.ru> 1:5.2.2-alt1
- separate %name package

* Thu Jul 26 2007 Led <led@altlinux.ru> 5.4.3-alt1.3
- updated %bname-5.4.3-forcedeth.patch
- cleaned up BuildRequires
- cleaned up spec

* Wed Jul 25 2007 Led <led@altlinux.ru> 5.4.3-alt1.2
- updated %bname-5.4.3-forcedeth.patch

* Wed Jul 04 2007 Led <led@altlinux.ru> 5.4.3-alt1.1
- added %bname-5.4.3-forcedeth.patch

* Tue Mar 06 2007 Grigory Milev <week@altlinux.ru> 5.4.3-alt1
- update to last version
- clean up specfile
- remove unneeded pathces.

* Sat Oct 14 2006 Michael Shigorin <mike@altlinux.org> 5.4.2-alt1
- fix build with SSP-enabled gcc4.1 (well link should be fixed
  properly but I feel it won't matter much for this package)

* Wed Apr 26 2006 Michael Shigorin <mike@altlinux.org> 5.4.2-alt0.2
- added ExclusiveArch since fixing x86_64 build is 
  out of question for a moment

* Thu Apr 20 2006 Michael Shigorin <mike@altlinux.org> 5.4.2-alt0.1
- 5.4.2 (NMU)

* Mon Mar 20 2006 Michael Shigorin <mike@altlinux.org> 5.4.1-alt0.1
- 5.4.1 (NMU)
  + fix build with recent gcc
- peek inside current Mandriva package
  + borrow gcc4 patch
  + rearrange %%install
  + re-clean-up resulting stuff
- separate doc subpackage
  + use common docdir
  + compress LOG
  + include gzipped PostScript docs
- updated buildrequires

* Tue Feb 24 2004 Grigory Milev <week@altlinux.ru> 5.3.6-alt1
- new version released

* Fri Oct  3 2003 Grigory Milev <week@altlinux.ru> 5.3.2-alt1
- new version released
- fix buildrequires

* Wed Oct 23 2002 Grigory Milev <week@altlinux.ru> 5.0.7-alt1
- new version released
- correct buildrequires
- remover perl from build requires

* Thu Jan  3 2002 Grigory Milev <week@altlinux.ru> 5.0.5-alt1
- new version released

* Thu Sep 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.0.4-alt2
- Minor specfile cleanup.
- Changed BuildArch.
- Updated requires and buildrequires.

* Tue Sep 25 2001 Grigory Milev <week@altlinux.ru> 5.0.4-alt1
- New version released

* Fri Jul 13 2001 Grigory Milev <week@altlinux.ru> 5.0.2-alt1
- First build for Sisyphus

