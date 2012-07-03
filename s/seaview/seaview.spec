Name: seaview
Version: 4.2.6
Release: alt1.2
Summary: Graphical multiple sequence alignment editor
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group: Sciences/Biology
License: GPLv2+
Url: http://pbil.univ-lyon1.fr/software/seaview.html
Source0: ftp://pbil.univ-lyon1.fr/pub/mol_phylogeny/seaview/seaview_4.2.6.tar.gz
Source1: seaview.desktop
Patch0: seaview-chris.patch
Patch1: seaview-unrooted.patch
BuildRequires: libfltk-devel gcc-c++ libX11-devel zlib-devel libXft-devel libXext-devel
BuildRequires: desktop-file-utils

BuildPreReq: libpixman-devel libcairo-devel libXinerama-devel

%description
SeaView is a graphical multiple sequence alignment editor developed by Manolo
Gouy.  SeaView is able to read and write various alignment formats (NEXUS, MSF,
CLUSTAL, FASTA, PHYLIP, MASE).  It allows to manually edit the alignment, and
also to run DOT-PLOT or CLUSTALW/MUSCLE programs to locally improve the
alignment.

%prep
%setup -q -n seaview
%patch0 -p 1 -b .chris
%patch1 -p1
chmod -x *.cxx
chmod -x csrc/*.[ch]

sed -i 's|^\(CFLAGS.*\)|\1 -g -DFL_LIBRARY|' Makefile

%build
make %{?_smp_mflags}

%check

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/seaview
mkdir -p $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT/%_mandir/man1
mkdir -p $RPM_BUILD_ROOT%_datadir/applications/
install -m 755 seaview $RPM_BUILD_ROOT/%_bindir
install -m 644 seaview.html $RPM_BUILD_ROOT%_datadir/seaview/
install -m 644  %SOURCE1 $RPM_BUILD_ROOT%_datadir/applications/
mkdir -p $RPM_BUILD_ROOT%_datadir/pixmaps/
install -m 0644 -p seaview.xpm $RPM_BUILD_ROOT%_datadir/pixmaps/seaview.xpm
install -m 644 seaview.1 $RPM_BUILD_ROOT/%_mandir/man1

%files
%doc seaview.1.xml example.nxs
%_bindir/seaview
%_datadir/seaview/
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.xpm
%_man1dir/*

%changelog
* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.6-alt1.2
- Rebuilt with FLTK 1.3.0.r8575

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.6-alt1.1
- Rebuilt with libfltk13 and for debuginfo

* Mon Jan 24 2011 Ilya Mashkin <oddity@altlinux.ru> 4.2.6-alt1
- Build for ALT Linux

* Sat Jul 31 2010 Christian Iseli <Christian.Iseli@licr.org> - 4.2.6-2
- Rebuild to solve libfltk broken dep

* Tue Jul 20 2010 Christian Iseli <Christian.Iseli@licr.org> - 4.2.6-1
- New upstream version

* Wed Feb 17 2010 Christian Iseli <Christian.Iseli@licr.org> - 4.2.2-2
- Fix thinko

* Wed Feb 17 2010 Christian Iseli <Christian.Iseli@licr.org> - 4.2.2-1
- New upstream version
- Update patch file to cause link against fontconfig library to resolve
  bugzilla 564977

* Fri Jan  8 2010 Christian Iseli <Christian.Iseli@licr.org> - 4.2.1-1
- New upstream version
- tarball does not expand to a versioned directory
- seaview.help -> seaview.html
- resync patches
- add man page
- remove exec bit on source files (they end up in the debug package)
- add doc files

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Christian Iseli <Christian.Iseli@licr.org> - 4.0-1
- New upstream version
- Fix GCC 4.4 compile issues
- README and protein.mase are gone

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun 12 2008 Christian Iseli <Christian.Iseli@licr.org> - 2.4-1
- New upstream version 2.4
- Cleanup changelog formatting

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0-2
- Autorebuild for GCC 4.3

* Mon Sep 10 2007 Christian Iseli <Christian.Iseli@licr.org> - 2.0-1
- New upstream version, with a true version number :)

* Thu Aug 16 2007 Christian Iseli <Christian.Iseli@licr.org> - 0-0.1.20070616
- Fix License tag to GPLv2+.

* Thu Jun 28 2007 Christian Iseli <Christian.Iseli@licr.org> - 0-0.1.20070615
- New upstream tarball.
- Add desktop file and icon.

* Wed Jun 13 2007 Christian Iseli <Christian.Iseli@licr.org> - 0-0.1.20070515
- Actually follow pre-release strategy for version/release...
- New upstream "version".

* Tue May  8 2007 Christian Iseli <Christian.Iseli@licr.org> - 0-0.20070417
- Follow pre-release strategy for version/release.

* Mon May  7 2007 Christian Iseli <Christian.Iseli@licr.org> - 0.20070417-0
- Create spec file.
