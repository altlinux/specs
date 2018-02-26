Summary:	A set of Solitaire type games for the X Window System
Name:		xpat2
Version:	1.07
Release:    	alt1
License:	GPLv2+
Group:		Games/Cards
Source:		ftp://sunsite.unc.edu/pub/Linux/games/solitaires/%{name}-%{version}-src.tar.bz2	
Patch0:		xpat2-fixes.patch
Patch1:		xpat2-1.07-lib64.patch
Patch2:		xpat2-1.07-gcc41.patch
Patch3:		xpat2-1.07-fix-str-fmt.patch
# Automatically added by buildreq on Fri Oct 23 2009
BuildRequires: imake libXawM1-devel libXext-devel libXmu-devel libXp-devel libXpm-devel xorg-cf-files

%description
Xpat2 is a generic patience or Solitaire game for the X Window System.

Xpat2 can be used with different rules sets, so it can be used to play
Spider, Klondike, and other card games.

%prep
%setup -q
%patch0 -p1 -b kk1
%patch1 -p1 -b .lib64
%patch2 -p0 -b .gcc41
%patch3 -p0

%build
make clean

sed -i 's|define useX|undef useX| ; s|undef useXaw|define useXaw|' src/Xpat.tmpl

find -type f | xargs sed -i 's,/Xaw/,/XawM/,;s,-lXaw,-lXawM,'
find -type f | xargs sed -i "s|/var/games/|/var/lib/games/|g"

sed -i "s|chown.*||" src/Imakefile
sed -i "/LANGUAGES/ s,de_DE fr_FR it_IT,," src/Imakefile
sed -i "s|LN = ln -s|LN = echo|" src/Imakefile

make CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	XAWLIB=-lXawM

%install
%makeinstall DESTDIR=%buildroot \
	XPATROOT=%buildroot%_gamesdatadir/xpat2 \
	XPATMANDIR=%buildroot/%_man6dir \
	APPDEFSDIR=%buildroot/%_gamesdatadir/xpat2

install -m 755 -d %buildroot%{_menudir}
mkdir -p %buildroot/var/lib/games/
touch %buildroot/var/lib/games/xpat2.log
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=A set of Solitaire type games for the X Window System
Exec=%{_bindir}/%{name} 
Icon=cards_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Qt;Game;CardGame;X-MandrivaLinux-MoreApplications-Games-Cards;
EOF

%files
%defattr(-,root,root)
%attr(2711, root, games) %{_bindir}/xpat2
%_gamesdatadir/xpat2
%_man6dir/*
%{_datadir}/applications/mandriva-%{name}.desktop
%attr(660, root, games) %ghost /var/lib/games/xpat2.log


%changelog
* Fri Oct 23 2009 Mykola Grechukh <gns@altlinux.ru> 1.07-alt1
- initial build for ALT Linux

