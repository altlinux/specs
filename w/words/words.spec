Name: words
Version: 2
Release: alt1
Epoch: 1

%define _dictdir %_datadir/dict

Summary: A dictionary of English words for the %_dictdir directory
License: Public domain
Group: Text tools
BuildArch: noarch
Packager: Stanislav Ievlev <inger@altlinux.org>

# ftp://ibiblio.org/pub/Linux/libs/linux.words.%version.tar.bz2
Source: linux.words.%version.tar
Patch: linux.words.%version-jbj.patch
Source1: EWORDS.TXT

Patch1: linux.words.2-mmm.patch
Patch2: linux.words.2-meat.patch 
Patch3: linux.words.2-gullible.patch

%description
The words file is a dictionary of English words for the %_dictdir
directory.  Programs like ispell use this database of words to check
spelling.

%prep
%setup -qc
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

chmod a-x usr/dict/README*

%install
mkdir -p %buildroot%_dictdir

cat usr/dict/{extra,linux}.words %SOURCE1 |
	sort -u >%buildroot%_dictdir/linux.words
ln -s linux.words %buildroot%_dictdir/words

%files
%_dictdir/*
%doc usr/dict/README*.linux.words

%changelog
* Wed Apr 23 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2-alt1
- Updated release numbering.

* Fri Nov 19 2004 Stanislav Ievlev <inger@altlinux.org> 2-ipl19mdk
- added more words from multitran.ru

* Thu Oct 24 2002 Stanislav Ievlev <inger@altlinux.ru> 2-ipl18mdk
- rebuild

* Mon Apr 01 2002 Stanislav Ievlev <inger@altlinux.ru> 2-ipl17mdk
- Rebuilt
- Update words list (from RH)

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 2-ipl16mdk
- RE adaptions.

* Mon Jul 24 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2-16mdk
- BM

* Sat Apr 08 2000 - Christopher Molnar <molnarc@mandrakesoft.com> 2-15mdk
- Chnaged to new groups

* Wed Nov 24 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Build release
- Remove de locale

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- add de locale

* Wed Sep 30 1998 Bill Nottingham <notting@redhat.com>
- take out extra.words (they're all in linux.words)

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- correct desiccate (problem #794)

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Tue Sep 23 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
