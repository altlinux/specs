# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install ImageMagick-tools gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		vodovod
Version:	1.10r22
Release:	alt1_10
Summary:	A pipe connecting game

Group:		Games/Other
License:	GPLv2+
URL:		http://home.gna.org/vodovod/
#Source:	http://download.gna.org/vodovod/%%{name}-%%{version}-src.tar.gz
# svn export -r 22 svn://svn.gna.org/svn/vodovod/trunk vodovod
# tar czvf vodovod-1.10r22-src.tar.gz vodovod
Source:		%{name}-%{version}-src.tar.gz
Patch0:		vodovod-1.10r22-locales.patch
Patch1:		vodovod-1.10r22-format-string.patch

BuildRequires:	desktop-file-utils libSDL-devel libSDL_image-devel libSDL_mixer-devel
BuildRequires:	libSDL_ttf-devel gettext gettext-tools ImageMagick

Requires:	fonts-ttf-dejavu
Requires(post): coreutils
Requires(postun): coreutils
Source44: import.info

%description
A free cross-platform pipe connecting game. You get a limited number
of pipes on each level and need to combine them to lead the water from
the house at the top of the screen to the storage tank at the bottom.

%description -l cs_CZ.UTF-8
Svobodná, multiplatformní logická hra založená na propojování potrubí.
Každá úroveň začíná s omezeným množstvím trubek, které je potřeba umístit
tak, aby svedly vodu z domku na vrchu obrazovky do nádrže dole.

%description -l sk_SK.UTF-8
Slobodná, multiplatformná logická hra založená na spojovaní potrubia.
Každá úroveň začína s obmedzeným množstvom trubiek, ktoré musíte umiestniť tak,
aby viedli vodu z domčeka v hornej časti obrazovky do nádrže v dolnej časti.


%prep
#%%setup -q -n %%{name}-%%{version}-src
%setup -q -n %{name}
# update locales
%patch0 -p1
# fix bug #1037377
%patch1 -p1
# replace the bundled font usage with the one provided by font package
rm data/font1.ttf
sed -i -e "s|data/font1.ttf|../fonts/dejavu/DejaVuSansMono.ttf|" \
	allmenus.cpp main.cpp game.cpp


%build
make PREFIX=%{_prefix} HIGHSCOREDIR=%{_localstatedir}/games \
	%{?_smp_mflags} CXX="%{__cxx}" CXXFLAGS="%{optflags}"
# .desktop file 
cat <<EOF > %{name}.desktop
[Desktop Entry]
Name=Vodovod
GenericName=Logic Game
GenericName[cs]=Logická hra
GenericName[sk]=Logická hra
Comment=A pipe connecting game
Comment[cs]=Propojování potrubí
Comment[sk]=Spojovanie potrubia
Exec=vodovod
Icon=vodovod
Terminal=false
Type=Application
Categories=Game;LogicGame;
EOF


%install
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install
# since the game sources do not come with the hiscore file, we have to create it
# this will result in empty hiscore table, but it is not such a big deal
mkdir -p %{buildroot}%{_localstatedir}/games
touch %{buildroot}%{_localstatedir}/games/%{name}.sco
# add icon and .desktop file
mkdir -p -m 0755 %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
convert data/abicon.bmp %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/vodovod.xpm
desktop-file-install  \
	--dir=%{buildroot}%{_datadir}/applications %{name}.desktop
%find_lang %{name}


%files -f %{name}.lang
%doc CHANGES COPYING html
%attr(2711,root,games) %{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
%config(noreplace) %attr (0664,root,games) %{_localstatedir}/games/%{name}.sco


%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.10r22-alt1_10
- update to new version by fcimport

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.10r19-alt1.qa3
- NMU: rebuilt for debuginfo.

* Fri Dec 24 2010 Michael Shigorin <mike@altlinux.org> 1.10r19-alt1.qa2
- adjusted default font location (closes: #21062)

* Mon Dec 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.10r19-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pkg-contains-cvs-or-svn-control-dir for vodovod
  * obsolete-call-in-post-gtk-update-icon-cache for vodovod
  * postclean-05-filetriggers for spec file

* Thu Aug 13 2009 Ilya Mashkin <oddity@altlinux.ru> 1.10r19-alt1
- Build for ALT Linux

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10r19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May  7 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.10r19-5
- Build with $RPM_OPT_FLAGS.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10r19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Karel Volny <kvolny@redhat.com> 1.10r19-3
- Required font package got renamed to dejavu-sans-mono-fonts (bug #480478)

* Thu Jan 15 2009 Karel Volny <kvolny@redhat.com> 1.10r19-2
- Use dejavu-fonts-sans-mono instead of bundling the font file (bug #477480)

* Thu Dec 11 2008 Karel Volny <kvolny@redhat.com> 1.10r19-1
- Added coreutils to post(un) (fixes bug #475921)
- New version requires SDL_ttf-devel

* Wed Mar 05 2008 Karel Volny <kvolny@redhat.com> 1.10r13-1
- development version
- Removed gcc43 patch (fixed upstream)
- Removed wrapper stuff and harcoded paths, upstream now uses variables
- Use hiscore file %%{_localstatedir}/games/%%{name}.sco
- Added language files handling
- Added Czech localisation

* Mon Feb 04 2008 Karel Volny <kvolny@redhat.com> 1.10-2
- Some fixes as per bug #428973:
- Fixed summary
- Added gtk-update-icon-cache
- Added patch to compile with gcc 4.3
- Modified compiler flags

* Wed Jan 16 2008 Karel Volny <kvolny@redhat.com> 1.10-1
- Initial release
