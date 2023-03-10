%define _unpackaged_files_terminate_build 1

Name: pspp
Version: 1.6.2
Release: alt1

Summary: A program for statistical analysis of sampled data.
License: GPLv3+
Group: Sciences/Mathematics

Url: http://www.gnu.org/software/pspp/

Source: %name-%version.tar.zst

BuildRequires: libgsl-devel
BuildRequires: perl-devel
BuildRequires: python3
BuildRequires: iconv
BuildRequires: zlib
BuildRequires: libxml2-devel
BuildRequires: libcairo-devel
BuildRequires: libpango-devel
#to enable PSPPIRE
BuildRequires: libgtk+3
BuildRequires: libgtksourceview4-devel
BuildRequires: libspread-sheet-widget-devel
#Optional according to INSTALL file
BuildRequires: libreadline-devel
BuildRequires: texinfo
BuildRequires: fonts-ttf-liberation
BuildRequires: texlive-dist

%description
GNU PSPP is a program for statistical analysis of sampled data. It is a free as
in freedom replacement for the proprietary program SPSS, and appears very
similar to it with a few exceptions.

%prep
%setup 

%build
%ifarch i586 armh
%configure --disable-static --disable-rpath --disable-year2038
%else
%configure --disable-static --disable-rpath
%endif
%make_build

%install
%makeinstall_std
%makeinstall_std install-html
%makeinstall_std install-pdf

rm -rf %buildroot%_infodir/screenshots
rm -rf %buildroot%_infodir/pspp-figures

%find_lang --output=%name.lang %name

%check
%make_build check

%files -f %name.lang
%doc NEWS ONEWS COPYING THANKS AUTHORS README
%doc %_datadir/doc/%name
%_bindir/pspp
%_bindir/pspp-convert
%_bindir/pspp-dump-sav
%_bindir/pspp-output
%_bindir/psppire
%_libdir/%name/
%exclude %_libdir/%name/*.la
%_iconsdir/hicolor/*/mimetypes/application-x-spss-*.png
%_iconsdir/hicolor/*/apps/org.gnu.pspp.*
%_desktopdir/org.gnu.pspp.desktop
%_datadir/metainfo/org.gnu.pspp.metainfo.xml
%_datadir/mime/packages/org.gnu.pspp.xml
%_infodir/pspp*
%_man1dir/*
%_datadir/%name/

%changelog
* Tue Feb 28 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 1.6.2-alt1
- Updated to 1.6.2

* Wed Apr 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.4.1-alt1
- Recovered package for sisyphus.
- Updated to 1.4.1

* Thu Aug 27 2020 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1
- Autobuild version bump to 1.4.0

* Mon Jan 13 2020 Fr. Br. George <george@altlinux.ru> 1.2.0-alt2
- Fix tests

* Tue Feb 05 2019 Fr. Br. George <george@altlinux.ru> 1.2.0-alt1
- Autobuild version bump to 1.2.0

* Mon Sep 18 2017 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Autobuild version bump to 1.0.1

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt1.1
- NMU: added BR: texinfo

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 0.8.5-alt1
- Autobuild version bump to 0.8.5
- Package mans

* Thu Oct 23 2014 Fr. Br. George <george@altlinux.ru> 0.8.4-alt1
- Autobuild version bump to 0.8.4
- Fix buildreq for pango warning evasion

* Tue May 27 2014 Fr. Br. George <george@altlinux.ru> 0.8.3-alt1
- Autobuild version bump to 0.8.3

* Tue May 27 2014 Fr. Br. George <george@altlinux.ru> 0.8.2-alt1
- Initial build from FC

* Tue Jan 21 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-1
- Ver. 0.8.2

* Tue Sep 24 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.8.1-1
- Ver. 0.8.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.8.0-1
- Ver. 0.8.0

* Sun Feb 24 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.7.9-5
- Fixed FTBFS in Rawhide / Fedora 19 (see rhbz #914398)
- Added provides(gnulib) (see rhbz #821785)
- Added accidentally removed pspp docs (see rhbz #822610)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.7.9-2
- Drop useless patch

* Sun Apr 15 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.7.9-1
- Ver. 0.7.9

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 17 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.7.8-1
- Ver. 0.7.8

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6.2-5
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.6.2-3
- Rebuilt for gcc bug 634757

* Thu Sep 23 2010 Peter Lemenkov <lemenkov@gmail.com> 0.6.2-2
- Rebuild (fixes ftbfs rhbz #599955)

* Fri Oct 16 2009 Peter Lemenkov <lemenkov@gmail.com> 0.6.2-1
- Ver. 0.6.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 22 2009 Matěj Cepl <mcepl@redhat.com> - 0.6.1-3
- Make .so symlink to versioned libraries -- shouldn't be needed
  but helps to fix bug 471180

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 28 2008 Matěj Cepl <mcepl@redhat.com> 0.6.1-1
- New upstream release.
- Added home made logo.
- Fix file permissions.

* Wed Nov 12 2008 Matěj Cepl <mcepl@redhat.com> - 0.6.0-9
- Fix in the %%preun script -- install-info wants only .info file
  as an argument.

* Thu Sep 25 2008 Matěj Cepl <mcepl@redhat.com> - 0.6.0-8
- Fix wrong CFLAGS -- add -fgnu89-inline

* Mon Jul 07 2008 Matej Cepl <mcepl@redhat.com> 0.6.0-7
- Fix BuildRequires.

* Wed Jun 18 2008 Matej Cepl <mcepl@redhat.com> 0.6.0-6
- Bug 451006 has been resolved, so we don't have to munge CFLAGS
  anymore.

* Sat Jun 14 2008 Matěj Cepl <mcepl@redhat.com> 0.6.0-5
- Approved version with fixed duplicate %%{_sysconfdir}/pspp

* Fri Jun 13 2008 Matěj Cepl <mcepl@redhat.com> 0.6.0-4
- Second wave of Package Review -- .desktop file
- Mysterious libraries eliminated

* Thu Jun 12 2008 Matěj Cepl <mcepl@redhat.com> 0.6.0-3
- First wave of Package Review nitpicking -- added %%doc and fixed Texinfo
  handling.

* Thu Jun 12 2008 Matěj Cepl <mcepl@redhat.com> 0.6.0-2
- Upstream release, this build is to be put into the package review.

* Tue Apr 22 2008 Matěj Cepl <mcepl@redhat.com> 0.6.0-0.1.pre2
- Upstream pre-release.

* Mon Apr 23 2007 Matej Cepl <mcepl@redhat.com> - 0.4.0-1
- The first experimental package of PSPP for Fedora.
