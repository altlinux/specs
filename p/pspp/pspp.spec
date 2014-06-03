Name: pspp
Version: 0.8.3
Release: alt1
Summary: A program for statistical analysis of sampled data
Group: Sciences/Mathematics
License: GPLv3+
Url: http://www.gnu.org/software/pspp/
Source0: ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.gz
#BuildRequires: plotutils-devel, ncurses-devel, readline-devel
#BuildRequires: gsl-devel >= 1.11-2
#BuildRequires: postgresql-devel
#BuildRequires: glade3-libgladeui-devel, libglade2-devel
#BuildRequires: gettext, desktop-file-utils
#BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: autoconf automake libtool gettext-devel texinfo libxml2
#BuildRequires: gtksourceview2-devel

# Automatically added by buildreq on Mon May 26 2014
# optimized out: fontconfig fontconfig-devel glib2-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libncurses-devel libpango-devel libtinfo-devel libwayland-client libwayland-server makeinfo pkg-config tzdata xml-utils zlib-devel
BuildRequires: libgsl-devel libgtksourceview-devel libreadline-devel libxml2-devel perl-devel perl-podlators

%description
PSPP is a program for statistical analysis of sampled data. It
interprets commands in the SPSS language and produces tabular
output in ASCII, PostScript, or HTML format.

PSPP development is ongoing. It already supports a large subset
of SPSS's transformation language. Its statistical procedure
support is currently limited, but growing.

%prep
%setup

TMPTHANKS=$(mktemp %name.XXXXXXXX)
iconv -f ISO-8859-1 -t UTF-8 THANKS >$TMPTHANKS
chmod --reference=THANKS $TMPTHANKS
touch --reference=THANKS $TMPTHANKS
mv $TMPTHANKS THANKS
find . -exec chmod g-s '{}' \;

%build
%autoreconf
%add_optflags -fgnu89-inline
%configure --disable-static --disable-rpath
%make_build

%install
%makeinstall_std
rm %buildroot%_libdir/pspp/*.la

%find_lang %name

%check
make check

%files -f %name.lang
%doc AUTHORS COPYING NEWS ONEWS README THANKS
%_bindir/pspp
%_bindir/psppire
%_bindir/pspp-convert
%_bindir/pspp-dump-sav
%_infodir/pspp*
%_libdir/%name/
%_mandir/man1/pspp-dump-sav.*
%_datadir/appdata/pspp.appdata.xml
%_datadir/applications/pspp.desktop
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/icons/hicolor/*/mimetypes/*.png
%_datadir/icons/hicolor/scalable/apps/pspp.svg
%_datadir/pspp/
# FIXME this should be marked as doc
%_datadir/doc/pspp/
%_mandir/man1/pspp-convert.1.*

%changelog
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
