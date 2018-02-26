# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen gcc-c++
# END SourceDeps(oneline)
Name:           amoebax
Version:        0.2.0
Release:        alt5_9
Summary:        Action-Puzzle Game
Group:          Games/Other
License:        GPLv2+ and Free Art
URL:            http://www.emma-soft.com/games/amoebax/
Source0:        http://www.emma-soft.com/games/amoebax/download/amoebax-%{version}.tar.bz2
Patch0:         amoebax-0.2.0-gcc43.patch
BuildRequires:  libSDL_mixer-devel libSDL_image-devel zlib-devel libpng-devel
BuildRequires:  libvorbis-devel doxygen desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
Amoebax is a cute and addictive action-puzzle game. Due an awful mutation,
some amoeba's species have started to multiply until they take the world if
you can't stop them. Fortunately the mutation made then too unstable and
lining up four or more will make them disappear.

Follow Kim or Tom through 6 levels in their quest to prevent the cute
multiplying amoebas to take the world and become the new Amoeba Master. Watch
out for the cute but amoeba's controlled creatures that will try to put and
end to your quest.

Amoebax is designed with levels for everyone, from children to adults. With
the training mode everybody will quickly become a master and the tournament
mode will let you have a good time with your friends. There is also catchy
music, funny sound effects, and beautiful screens that sure appeal to everyone
in the family.


%prep
%setup -q
%patch0 -p1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/manual.pdf

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install  --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
mv $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.svg \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps


%files
%doc AUTHORS COPYING* NEWS README* THANKS TODO doc/manual.pdf
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt5_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt5_8
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt4_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt4_7
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3_7
- rebuild with new rpm desktop cleaner

* Mon Feb 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_7
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_7
- converted from Fedora by srpmconvert script

