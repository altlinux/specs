# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:		escape
Version:	200912250
Release:	alt3_8
Summary:	Extensible block-pushing puzzle game

Group:		Games/Other
License:	GPLv3
URL:		http://escape.spacebar.org/

Source0:	http://escape.spacebar.org/source/%{name}-src-%{version}.tar.bz2
Source1:	%{name}.desktop

Patch0:		escape-200912250-update-remove.patch


BuildRequires:	libSDL-devel libSDL_image-devel libSDL_net-devel
BuildRequires:	desktop-file-utils
Requires:	icon-theme-hicolor
Source44: import.info


%description
Escape is a tile-based puzzle game in the style of "Adventures of
Lolo" or "Chip's Challenge." Unlike either of those games, Escape
doesn't rely at all on reflexes--it's all about your brain.

Although Escape comes with hundreds of levels, the game places an
emphasis on the composition of new puzzles. Thus Escape has a
built-in level editor and facilities for automatically sharing
puzzles with other players.


%prep
%setup -q -n %{name}-src

# fix update bug
%patch0 -p1 -b .update-remove

# fix permissions for debuginfo packages
find . \( -name '*.h' -o -name '*.cpp' \) -type f -print0 | xargs -0 chmod 0644


%build
make LINUX=1 \
	LDFLAGS="" \
	LDLIBS="`pkg-config --libs sdl` -lSDL_image -lSDL_net" \
	CXXFLAGS="`pkg-config --cflags sdl` $RPM_OPT_FLAGS" \
	CPPFLAGS="-DMULTIUSER -DDATADIR=\\\"%{_datadir}/%{name}/data/\\\" -DSTARTUP_LEVELS=\\\"%{_datadir}/%{name}/levels/\\\" -DNOSOUND" \
	%{?_smp_mflags}


%install
install -D -m0755 -p escape.exe \
	$RPM_BUILD_ROOT%{_bindir}/escape

# graphics
mkdir -p $RPM_BUILD_ROOT%{_datadir}/escape/data
install -D -m0644 -p -t $RPM_BUILD_ROOT%{_datadir}/escape/data *.png

# levels
mkdir -p $RPM_BUILD_ROOT%{_datadir}/escape/levels
cp -a official triage mylevels $RPM_BUILD_ROOT%{_datadir}/escape/levels
find $RPM_BUILD_ROOT%{_datadir}/escape/levels -type f -print0 | xargs -0 chmod 0644
find $RPM_BUILD_ROOT%{_datadir}/escape/levels -type d -name CVS -print0 | xargs -0 rm -rf

# icon
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
cp -a icon.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# desktop file
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}


%files
%doc COPYING design.txt escape.txt README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/applications/*.desktop


%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 200912250-alt3_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 200912250-alt3_7
- update to new release by fcimport

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 200912250-alt3_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 200912250-alt3_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 200912250-alt3_4
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 200912250-alt3_3
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 200912250-alt2_3
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 200912250-alt2_2
- converted from Fedora by srpmconvert script

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 200912250-alt1_2
- converted from Fedora by srpmconvert script

