Name: lcdf-typetools
Version: 2.92
Release: alt1
Summary: Tools for manipulating OpenType fonts
Group: Publishing
License: GPLv2+
Url: http://www.lcdf.org
Source: %name-%version.tar.gz

#BuildRequires: kpathsea-devel

# Automatically added by buildreq on Sun Jun 20 2010
BuildRequires: gcc-c++ libkpathsea-devel texlive-base-bin

%description
The LCDF Typetools package contains several programs for manipulating
PostScript Type 1, Type 1 multiple master, and PostScript-flavored OpenType
fonts.  LCDF Typetools includes the mmafm and mmpfb programs, which were
formerly distributed as part of a different package (mminstance)

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%doc COPYING NEWS ONEWS README *.txt *.tex
%_bindir/cfftot1
%_bindir/mmafm
%_bindir/mmpfb
%_bindir/otfinfo
%_bindir/otftotfm
%_bindir/t1dotlessj
%_bindir/t1lint
%_bindir/t1reencode
%_bindir/t1testpage
%_bindir/ttftotype42
%_bindir/t1rawafm
%_mandir/man*/*
%_datadir/lcdf-typetools

%changelog
* Tue Aug 16 2011 Fr. Br. George <george@altlinux.ru> 2.92-alt1
- Autobuild version bump to 2.92

* Sat Jul 23 2011 Fr. Br. George <george@altlinux.ru> 2.91-alt1
- Autobuild version bump to 2.91
- Add some documentation

* Mon Jun 21 2010 Fr. Br. George <george@altlinux.ru> 2.83-alt1
- Version up

* Sun Jun 20 2010 Fr. Br. George <george@altlinux.ru> 2.80-alt1
- Initial ALT build from FC

* Wed Dec 02 2009 Parag Nemade <pnemade AT redhat.com>- 2.80-1
- Update to next upstream release 2.80

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Parag Nemade <pnemade AT redhat.com>- 2.79-1
- Update to next upstream release 2.79

* Thu May 21 2009 Parag Nemade <pnemade AT redhat.com>- 2.78-1
- Initial specfile for Fedora

