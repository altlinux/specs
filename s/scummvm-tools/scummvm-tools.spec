Name: scummvm-tools
Version: 2.7.0
Release: alt1

Summary: Utilities for the SCUMM graphic adventure game interpreter
Group: Games/Adventure
License: GPLv2
Url: http://www.scummvm.org

Source: %name-%version.tar.gz

# Automatically added by buildreq on Thu Mar 12 2009
BuildRequires: gcc-c++ libflac-devel libpng-devel libvorbis-devel libwxGTK3.2-devel

%description
This is a collection of various tools that may be useful to use
in conjunction with ScummVM.

%prep
%setup
# Make arm64/ppc64le happy
cp /usr/share/gnu-config/config.guess .

%build
./configure --prefix=%prefix
%make_build

%install
mkdir -p %buildroot%_bindir
%makeinstall_std

%files
%doc README TODO
%_bindir/*
%_datadir/scummvm-tools

%changelog
* Sun Oct 15 2023 Anton Midyukov <antohami@altlinux.org> 2.7.0-alt1
- Autobuild version bump to 2.7.0
- rebuild with wxGTK3.2

* Wed Sep 21 2022 Anton Midyukov <antohami@altlinux.org> 2.6.0-alt2
- rebuild with wxGTK3.0 (Closes: 43838)

* Thu Aug 04 2022 Fr. Br. George <george@altlinux.org> 2.6.0-alt1
- Autobuild version bump to 2.6.0

* Wed Oct 20 2021 Fr. Br. George <george@altlinux.ru> 2.5.0-alt1
- Autobuild version bump to 2.5.0

* Sun Oct 04 2020 Fr. Br. George <george@altlinux.ru> 2.2.0-alt1
- Autobuild version bump to 2.2.0

* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 2.1.0-alt1
- Autobuild version bump to 2.1.0
- Fix build

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 2.0.0-alt1
- Autobuild version bump to 2.0.0

* Thu Jul 27 2017 Fr. Br. George <george@altlinux.ru> 1.9.0-alt1
- Autobuild version bump to 1.9.0

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 1.8.0-alt1
- Autobuild version bump to 1.8.0

* Mon Sep 14 2015 Fr. Br. George <george@altlinux.ru> 1.7.0-alt2
- Rebuild with new C++,wx ABI

* Mon Jul 14 2014 Fr. Br. George <george@altlinux.ru> 1.7.0-alt1
- Autobuild version bump to 1.7.0

* Mon Jun 10 2013 Fr. Br. George <george@altlinux.ru> 1.6.0-alt1
- Autobuild version bump to 1.6.0

* Tue Sep 25 2012 Repocop Q. A. Robot <repocop@altlinux.org> 1.4.0-alt1.1
- rebuild with new wxGTK

* Mon Nov 07 2011 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1
- Autobuild version bump to 1.4.0

* Wed Jun 01 2011 Fr. Br. George <george@altlinux.ru> 1.3.0-alt1
- Autobuild version bump to 1.3.0

* Thu Nov 18 2010 Alexey I. Froloff <raorn@altlinux.org> 1.2.0-alt1
- [1.2.0]

* Tue Sep 28 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.1-alt1
- [1.1.1]
 + extract_* and compress_* merged into scummvm-tools-cli

* Mon Feb 15 2010 Alexey I. Froloff <raorn@altlinux.org> 1.0.0-alt1
- [1.0.0]
 + added tools:
  * compress_gob
  * compress_tinsel
  * extract_cruise_pc

* Tue Jun 23 2009 Alexey I. Froloff <raorn@altlinux.org> 0.13.0-alt2
- Rebuilt with new libpng12

* Thu Mar 12 2009 Sir Raorn <raorn@altlinux.ru> 0.13.0-alt1
- [0.13.0]
 + added tools:
  * compress_tucker
  * decine
  * degob
  * extract_cine
  * extract_gob_stk
  * extract_t7g_mac
 + tools_gui - GUI for all tools

* Thu Jan 24 2008 Sir Raorn <raorn@altlinux.ru> 0.11.0-alt1
- [0.11.0]
 + added extract_parallaction

* Fri Aug 24 2007 Sir Raorn <raorn@altlinux.ru> 0.10.0-alt1
- [0.10.0]
 + compress_simon renamed to compress_agos
 + extract_simon1_amiga renamed to extract_agos
 + added compress_touche
 + added extract_mm_apple

* Tue Jul 04 2006 Sir Raorn <raorn@altlinux.ru> 0.9.0-alt1
- [0.9.0]
 + compress_san renamed to compress_scumm_san
 + added compress_kyra
 + added encode_dxa

* Mon Oct 31 2005 Sir Raorn <raorn@altlinux.ru> 0.8.0-alt1
- [0.8.0]
- Removed summary/description translations (use specspo)

* Fri Dec 24 2004 Sir Raorn <raorn@altlinux.ru> 0.7.0-alt1
- [0.7.0]

* Tue Aug 03 2004 Sir Raorn <raorn@altlinux.ru> 0.6.1-alt1
- [0.6.1]

* Sat Mar 27 2004 Sir Raorn <raorn@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Tue Feb 24 2004 Sir Raorn <raorn@altlinux.ru> 0.5.0-alt2
- CVS snapshot 20040223
- spec cleanup

* Wed Aug 13 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Sun Jun 29 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Mon Dec 23 2002 Vyacheslav Dikonov <slava@altlinux.ru> 0.3.0b-alt1
- ALTLnux build

