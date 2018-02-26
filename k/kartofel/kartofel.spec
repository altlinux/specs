Name: 		kartofel
Version:	1.2
Release:	alt5
License:	GPL
Source:		http://kartofel.jfedor.org/downloads/%name-%version.tar.gz
URL:		http://kartofel.jfedor.org
#		wget -pk http://kartofel.jfedor.org
Source1:	kartofel.jfedor.org-%version.tar
Patch1:		%name-gcc44.patch
Summary:	Connect the numbered dots in order, without crossing over yourself
Group:		Games/Puzzles
Packager:	Fr. Br. George <george@altlinux.ru>
%define _gamescoredir %_localstatedir/games/%name

BuildPreReq:	rpm-build-fonts
BuildRequires:	fonts-ttf-freefont

# Automatically added by buildreq on Tue Apr 05 2011
# optimized out: libSDL-devel libstdc++-devel pkg-config
BuildRequires: gcc-c++ libSDL_gfx-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libcurl-devel zlib-devel

%description

Kartofel is a game of skill and logic.  The objective is to connect the
numbered dots in order, without crossing over yourself.  The game is
covered by the GNU General Public License.  The Kartofel webpage is
http://kartofel.jfedor.org

%prep
%setup
%patch1 -p1
sed -i '/HIGH_SCORES_FILENAME/{
	s@"[.]/@"%_gamescoredir/@
	n
}
/_FILENAME/s@ "@ "%_gamesdatadir/%name/@
' config.h
tar xf %SOURCE1

%build
%make_build

%install
mkdir -p %buildroot%_gamesdatadir/%name
install -D %name %buildroot%_gamesbindir/%name
install -D %name.txt %buildroot%_gamescoredir/%name.txt
cp -rp `find [^k]* -type d ` %buildroot%_gamesdatadir/%name/
rm %buildroot%_gamesdatadir/%name/fonts/FreeSans.ttf
ln -s %_ttffontsdir/freefont/FreeMono.ttf %buildroot%_gamesdatadir/%name/fonts/FreeSans.ttf

%files
%doc README CHANGES kartofel.jfedor.org-%version/*
%dir %_gamesdatadir/%name
%dir %_gamescoredir
%_gamesdatadir/%name/*
%attr(664,root,games) %_gamescoredir/%name.txt
%attr(2711,root,games) %_gamesbindir/%name

%changelog
* Thu Jun 30 2011 Fr. Br. George <george@altlinux.ru> 1.2-alt5
- Replace shipped font with system one

* Tue Apr 05 2011 Fr. Br. George <george@altlinux.ru> 1.2-alt4
- BuildRequires recalculated

* Mon May 25 2009 Fr. Br. George <george@altlinux.ru> 1.2-alt2
- GCC4.4 build fixup

* Mon Feb 09 2009 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Initial build from scratch
- Homepage documentation added
- TODO: desktop file
