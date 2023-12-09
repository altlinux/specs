Name: liquidwar6
Version: 0.6.3902
Release: alt7

Summary: A unique multiplayer wargame
License: GPL
Group: Games/Strategy

Url: http://www.gnu.org/software/liquidwar6
Source: %name-%version.tar

Patch0: liquidwar6-0.6.3902-alt-drop-Werror.patch
Patch1: liquidwar6-0.6.3902-alt-guile22.patch

# Automatically added by buildreq on Sat Jun 06 2020
# optimized out: fontconfig fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 guile guile-devel guile22 libGLU-devel libSDL-devel libatk-devel libcairo-devel libfreetype-devel libgc-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglvnd-devel libgmp-devel libgpg-error libharfbuzz-devel libpango-devel libpng-devel libsasl2-3 libtinfo-devel perl perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl perl-parent pkg-config python2-base sh4 shared-mime-info xz zlib-devel
BuildRequires: doxygen guile22-devel lcov libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libcurl-devel libexpat-devel libgomp-devel libgperftools-devel libgtk+2-devel libjpeg-devel libltdl7-devel libncurses-devel libreadline-devel libsqlite3-devel makeinfo

%description
Liquid War 6 is a unique multiplayer wargame. Your army is a blob of
liquid and you have to try and eat your opponents. Rules are very
simple yet original, they have been invented by Thomas Colcombet. It
is possible to play alone against the computer but the game is really
designed to be played with friends, on a single computer, on a LAN, or
on Internet.

# Preparation of the package
%prep
%setup
%patch0 -p1
%patch1 -p1

# Building the package
%build
%autoreconf
%configure --docdir=%_defaultdocdir/%name-%version --enable-allinone --disable-mod-csound --enable-console
%make_build
( cd doc; make liquidwar6.html )

# Installing the package
%install
mkdir -p %buildroot%_defaultdocdir/%name-%version
%makeinstall docdir=%buildroot%_defaultdocdir/%name-%version
## No devel stuff in this RPM
rm -rf %buildroot%prefix/include
rm -rf %buildroot%prefix/lib
rm -rf %buildroot%prefix/libexec
%find_lang %name

%files -f %name.lang
%doc ChangeLog README NEWS AUTHORS
%_bindir/*
%_datadir/%{name}*
%_pixmapsdir/*
%_infodir/%{name}*
%_man6dir/*
%_desktopdir/%{name}*

%changelog
* Sun Dec 10 2023 Michael Shigorin <mike@altlinux.org> 0.6.3902-alt7
- E2K: no special handling required

* Thu Jun 25 2020 Michael Shigorin <mike@altlinux.org> 0.6.3902-alt6
- E2K: guile 2.0 so far, no need for patch1

* Sat Jun 06 2020 Fr. Br. George <george@altlinux.ru> 0.6.3902-alt5
- Fix build

* Wed Nov 21 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.3902-alt4
- rebuilt with guile-2.2

* Mon Aug 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.3902-alt3
- NMU: fixed build.

* Wed Jul 18 2018 Fr. Br. George <george@altlinux.ru> 0.6.3902-alt2
- Fix buildreqs

* Thu Nov 17 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.6.3902-alt1.1.qa1
- Fixed build with glibc >= 2.24.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.6.3902-alt1.1
- NMU: added BR: texinfo

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 0.6.3902-alt1
- Autobuild version bump to 0.6.3902

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 0.4.3681-alt1
- Autobuild version bump to 0.4.3681

* Tue Feb 18 2014 Fr. Br. George <george@altlinux.ru> 0.2.3551-alt1
- Autobuild version bump to 0.2.3551

* Thu Feb 28 2013 Fr. Br. George <george@altlinux.ru> 0.0.13beta-alt2
- Rebuild without perftools

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.13beta-alt1.1
- Rebuilt with libpng15

* Tue May 29 2012 Fr. Br. George <george@altlinux.ru> 0.0.13beta-alt1
- Autobuild version bump to 0.0.13beta

* Wed Aug 24 2011 Fr. Br. George <george@altlinux.ru> 0.0.10beta-alt1
- Initial build from upstream spec

* Fri Jul 09 2010 Christian Mauduit <ufoot@ufoot.org>
- Added applications directory (contains .desktop file).

* Tue Oct 20 2009 Christian Mauduit <ufoot@ufoot.org>
- Added proper GPG info.

* Mon Oct 05 2009 Christian Mauduit <ufoot@ufoot.org>
- Fixed info postinstall script.

* Wed Sep 09 2009 Christian Mauduit <ufoot@ufoot.org>
- Added Requires and BuildRequires declarations.

* Sat Jan 10 2009 Christian Mauduit <ufoot@ufoot.org>
- Fixed source URL.

* Thu Jan 08 2009 Christian Mauduit <ufoot@ufoot.org>
- Disabled csound support by default.
- Fixed info file handling.

* Wed Nov 07 2007 Christian Mauduit <ufoot@ufoot.org>
- Added version in data path.

* Mon Dec 18 2006 Christian Mauduit <ufoot@ufoot.org>
- Minor fixes, only a single jumbo binary is generated.

* Tue Dec 05 2006 Christian Mauduit <ufoot@ufoot.org>
- First RPM, inspired from Liquid War 5

