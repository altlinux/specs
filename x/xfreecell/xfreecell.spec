%define bsdver nb2
Summary: Popular freecell card game for X
Name: xfreecell
Version: 1.0.5b
Release: alt6.%bsdver
License: free
Group: Games/Cards
Url: http://www2.giganet.net/~nakayama/
Source: %name-%version.tgz
Source1: MSNumbers.gz
Source2: %{name}_16.png
Source3: %{name}_32.png
Source4: %{name}_48.png
Patch1: http://mirror.vmmatrix.net/NetBSD/packages/pkgsrc/games/xfreecell/patches/patch-aa.fixed
Patch2: http://mirror.vmmatrix.net/NetBSD/packages/pkgsrc/games/xfreecell/patches/patch-ab
Patch3: http://mirror.vmmatrix.net/NetBSD/packages/pkgsrc/games/xfreecell/patches/patch-ac
Patch4: http://mirror.vmmatrix.net/NetBSD/packages/pkgsrc/games/xfreecell/patches/patch-ad
Patch5: http://mirror.vmmatrix.net/NetBSD/packages/pkgsrc/games/xfreecell/patches/patch-ae
Patch10: xfreecell-1.0.5b-alt-makefile-optflags.patch
Patch11: xfreecell-1.0.5b-alt-datadir.patch
Patch12: xfreecell-1.0.5b-alt-gcc4.3.patch

Packager: Igor Yu. Vlasenko <viy@altlinux.org>
Prefix: /usr

# Automatically added by buildreq on Fri Apr 04 2008 (-bi)
BuildRequires: gcc-c++ libXext-devel libX11-devel libstdc++-devel xorg-proto-devel

%description
Popular freecell card game for X

%prep
%setup -q -n %name
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
export OPTFLAGS="$RPM_OPT_FLAGS"
make X11BASE=%{_x11dir} GMAKE=make

%install
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_man6dir},%{_datadir}/%{name}}
install -s -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
install -m 644 %{name}.6 $RPM_BUILD_ROOT%{_man6dir}/%{name}.6

zcat %SOURCE1 > $RPM_BUILD_ROOT%_datadir/%name/MSNumbers

%__install -D -m644 %SOURCE2 $RPM_BUILD_ROOT%_miconsdir/%name.png
%__install -D -m644 %SOURCE3 $RPM_BUILD_ROOT%_niconsdir/%name.png
%__install -D -m644 %SOURCE4 $RPM_BUILD_ROOT%_liconsdir/%name.png

mkdir -p $RPM_BUILD_ROOT%_desktopdir
cat > $RPM_BUILD_ROOT%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=X freecell
GenericName=X freecell
Comment=%{summary}
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=Game;CardGame;
EOF

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}
%{_man6dir}/%{name}.*
%_datadir/%name/MSNumbers
%_desktopdir/%{name}.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.5b-alt6.nb2
- converted debian menu to freedesktop

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 1.0.5b-alt5.nb2.1
- NMU (by repocop): the following fixes applied:
 * update_menus for xfreecell

* Wed Oct 29 2008 Igor Yu. Vlasenko <viy@altlinux.org> 1.0.5b-alt5.nb2
- synced patches w/NetBSD nb2 

* Fri Apr 04 2008 Igor Yu. Vlasenko <viy@altlinux.org> 1.0.5b-alt4.nb1
- updated buildreq

* Fri Apr 07 2006 Igor Vlasenko <viy@altlinux.ru> 1.0.5b-alt3.nb1
- fixed buildreq

* Tue Apr 04 2006 Igor Vlasenko <viy@altlinux.ru> 1.0.5b-alt2.nb1
- fixed group

* Sat Apr 01 2006 Igor Vlasenko <viy@altlinux.ru> 1.0.5b-alt1.nb1
- first build for Sisyphus

