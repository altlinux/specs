# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/gconftool-2 /usr/bin/sdl-config /usr/bin/update-desktop-database /usr/bin/xml2-config dumb-devel gcc-c++ gcc-fortran libICE-devel libSDL_gfx-devel libSDL_image-devel libSDL_ttf-devel libSM-devel liballegro-devel libguichan-devel libmikmod-devel libxml2-devel pkgconfig(gmodule-2.0) pkgconfig(gtk+-2.0) python-devel radius-engine-devel unzip zlib-devel
# END SourceDeps(oneline)
Name:		maxr
Version:	0.2.6
Release:	alt2_3
Summary:	A classic turn-based strategy game

Group:		Games/Other
License:	GPLv2+ and GFDL
URL:		http://www.maxr.org
Source0:	http://www.maxr.org/downloads/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png

Requires:	icon-theme-hicolor
BuildRequires:	libSDL-devel libSDL_mixer-devel libSDL_net-devel
BuildRequires:	desktop-file-utils
Source44: import.info

%description
M.A.X.R. (Mechanized Assault and eXploration Reloaded) is a fanmade strategy 
game by the community of maxr.org. MAXR is OpenSource and a remake of
the old M.A.X.by Interplay from 1996 featuring network games based on TCP/IP 
(e.g. over the internet). The game can be played in a turn-based mode (with or 
without time limit), or simultaneous mode (all the players take their turns at 
the same time), and features combat in air, land, and sea. Three resources are 
present on the maps - Raw Materials, which are needed to manufacture units, 
structures and ammunition, Fuel, which power generators need to function, and 
Gold, which is used to purchase upgrades. This game is a mix of realtime and 
turnbased strategy with battle chess character.


%prep
%setup -q
# Needed because of this rpmlint warning "W: wrong-file-end-of-line-encoding"
sed -i 's/\r//' CHANGELOG
# Convert everything to UTF-8
# COPYING.README
iconv -f iso-8859-1 -t utf-8 -o COPYING.README.utf8 COPYING.README
touch -c -r COPYING.README COPYING.README.utf8
mv -f COPYING.README.utf8 COPYING.README
# ABOUT
iconv -f iso-8859-1 -t utf-8 -o ABOUT.utf8 ABOUT
touch -c -r ABOUT ABOUT.utf8
mv -f ABOUT.utf8 ABOUT


%build
%configure
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p' install

desktop-file-install \
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

install -p -m 0644 %{SOURCE2} \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png


%files
%doc ABOUT CHANGELOG COPYING COPYING.README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_3
- update to new release by fcimport

* Wed Mar 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_2
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_2
- converted from Fedora by srpmconvert script

