Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/desktop-file-validate ImageMagick-tools gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           slashem
Version:        0.0.8
Release:        alt2_0.36.E0F1
Summary:        Super Lotsa Added Stuff Hack - Extended Magic

License:        NGPL
URL:            https://slashem.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/se008e0f1.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Patch0:         slashem-config.patch
# fix building with libpng 1.5
Patch1:         slashem-libpng-1.5.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1037330
Patch2:         slashem-format-security.patch
# https://sourceforge.net/p/slashem/bugs/963/
Patch3:         slashem-add-FDECLs-c99.patch
Patch4:         slashem-configure-c99.patch
Patch5:         slashem-c99.patch

BuildRequires:  gcc
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/convert
BuildRequires:  libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel
BuildRequires:  bison, flex, desktop-file-utils
BuildRequires:  bdftopcf, libX11-devel, libXext-devel
BuildRequires:  libXmu-devel libXpm libXpm-devel, libXt-devel
BuildRequires:  libSDL-devel  libGL-devel libpng-devel libpng17-tools zlib-devel
BuildRequires:  pkgconfig(xaw7)
# to compress save files
Requires:       bzip2
# For icon theme directories.
Requires:       icon-theme-hicolor
# for X11 core fonts

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%global fa_var      /var/games/%{name}
%global fa_save     /var/games/%{name}/save
%global fa_share    %{_datadir}/games/%{name}
%global fa_unshare  %{_libdir}/games/%{name}
%global fa_doc      %{_docdir}/%{name}
Source44: import.info

%description
From the land before 3DFX, before VGA graphics and DOOM, before the IBM PC, way
back in the dark ages of Unixland, there was a game. They called it Rogue.
People played it, and found it good. From this basis, Hack was born. Soon Hack
became Nethack, because it was developed by many people (and has nothing to do
with hacking the internet). And people played this on many machines, from
Unices to Macs to PCs, due to the amazing power of Open Source Code.

But the DevTeam, the reclusive masterminds of Nethack, are a rather quiet
bunch, gracing the world with new versions as they see fit, and when they see
fit. Which is usually a new version every good number of years.

And there was much gnashing of teeth.

But because of the Freely Available Source Code Phenomenon, people began making
their own versions of Nethack to tide themselves between magical releases.

SLASH'EM is the (continuing) saga of one such variant...


%prep
%setup -q -n %{name}-%{version}E0F1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1


sed -i \
    -e 's:^\(#define FILE_AREA_VAR\).*:\1 "%{fa_var}/":' \
    -e 's:^\(#define FILE_AREA_SAVE\).*:\1 "%{fa_save}/":'  \
    -e 's:^\(#define FILE_AREA_SHARE\).*:\1 "%{fa_share}/":' \
    -e 's:^\(#define FILE_AREA_UNSHARE\).*:\1 "%{fa_unshare}/":' \
    -e 's:^\(#define FILE_AREA_DOC\).*:\1 "%{fa_doc}/":' \
    include/unixconf.h

for f in *.txt ; do
  iconv -f iso8859-1 -t utf-8 $f >$f.conv
  touch -r $f $f.conv
  mv $f.conv $f
done


%build
export LIBXAW_CFLAGS="-I/usr/include"
export LIBXAW_LIBS="$(pkg-config --libs xaw7)"
%configure \
    --enable-tty-graphics   \
    --enable-x11-graphics   \
    --enable-sdl-graphics   \
    --enable-gl-graphics    \
    --enable-data-librarian \
    --enable-sinks          \
    --enable-reincarnation  \
    --enable-zouthern       \
    --enable-score-on-botl  \
    --enable-wizmode=games
# smp_mflags fails
make \
    FILE_AREA_VAR=%{fa_var} \
    FILE_AREA_SAVE=%{fa_save} \
    FILE_AREA_SHARE=%{fa_share} \
    FILE_AREA_UNSHARE=%{fa_unshare} \
    FILE_AREA_DOC=%{fa_doc} \
    SHELLDIR=%{_bindir}


%install
make install DESTDIR=%{buildroot} \
    FILE_AREA_VAR=%{buildroot}%{fa_var} \
    FILE_AREA_SAVE=%{buildroot}%{fa_save} \
    FILE_AREA_SHARE=%{buildroot}%{fa_share} \
    FILE_AREA_UNSHARE=%{buildroot}%{fa_unshare} \
    FILE_AREA_DOC=%{buildroot}%{fa_doc} \
    INSTALL="install -p" \
    SHELLDIR=%{buildroot}%{_bindir} \
    CHOWN=/bin/true \
    CHGRP=/bin/true

install -d -m 0755 %{buildroot}%{_mandir}/man6
make -C doc MANDIR=%{buildroot}%{_mandir}/man6 manpages

sed -i \
    -e 's!%{buildroot}!!g' \
    -e '/XUSERFILE/s!\$HACKDIR!%{fa_share}!' \
    %{buildroot}%{_bindir}/slashem

mv %{buildroot}%{fa_unshare}/recover %{buildroot}%{_bindir}/slashem-recover
mv %{buildroot}%{_mandir}/man6/recover.6 %{buildroot}%{_mandir}/man6/slashem-recover.6
rm %{buildroot}%{_mandir}/man6/[^s]*
rm %{buildroot}%{_docdir}/%{name}/license

sed -i -e 's:^!\(SlashEM.tile_file.*\):\1:' %{buildroot}%{fa_share}/SlashEM.ad

install -d %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
convert win/X11/nh_icon.xpm %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc history.txt doc/*.txt README.34 readme.* slamfaq.txt dat/history
%doc --no-dereference dat/license
%{_bindir}/slashem
%{_bindir}/slashem-recover
%{fa_share}
%dir %{fa_unshare}
%{fa_unshare}/nhushare
%{_mandir}/man6/*.6*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/slashem.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%defattr(0664,root,games)
%config(noreplace) %{fa_var}/logfile
%config(noreplace) %{fa_var}/perm
%config(noreplace) %{fa_var}/record
%attr(0775,root,games) %dir %{fa_var}
%attr(0775,root,games) %dir %{fa_var}/save
%attr(2711,root,games) %{fa_unshare}/slashem


%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 0.0.8-alt2_0.36.E0F1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2_0.23.E0F1
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2_0.21.E0F1
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2_0.20.E0F1
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2_0.19.E0F1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2_0.18.E0F1
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2_0.17.E0F1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2_0.16.E0F1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2_0.15.E0F1
- update to new release by fcimport

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2_0.14.E0F1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2_0.13.E0F1
- update to new release by fcimport

* Mon Mar 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2_0.11.E0F1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2_0.10.E0F1
- update to new release by fcimport

* Mon Oct 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt2_0.9.E0F1.1
- Rebuilt with libpng15

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2_0.9.E0F1
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2_0.8.E0F1
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1_0.8.E0F1
- update to new release by fcimport

* Sat Jul 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1_0.6.E0F1
- initial release by fcimport

