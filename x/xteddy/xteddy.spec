# BEGIN SourceDeps(oneline):
BuildRequires: libICE-devel libSM-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           xteddy
Version:        2.0.1
Release:        alt5_8
Summary:        Tool to sit around silently, look cute, and make you smile

Group:          Games/Other
License:        GPL+
URL:            http://fam-tille.de/debian/xteddy.html
Source0:        http://webstaff.itn.liu.se/~stegu/xteddy/%{name}-%{version}.tar.gz
# Both submitted upstream by mail
Patch0:         xteddy-2.0.1-visual.patch
Patch1:         xteddy-2.0.1-iconname.patch

BuildRequires:  imlib-devel libpng-devel
Source44: import.info
Patch33: xteddy-2.0.1-alt-link-X11.patch

%description
Xteddy is your virtual comfort when things get rough. It can do everything
a real teddy bear can do. That is, I can sit around silently, look cute,
and make you smile. 


%prep
%setup -q
%patch0 -p1 -b .visual
%patch1 -p1 -b .iconname
%patch33 -p1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=Xteddy
GenericName=Virtual teddy bear
Comment=Xteddy is your virtual teddy bear. It can sit around silently, look cute, and make you smile.
Icon=amusement_section
Exec=xteddy
Categories=Game;Amusement;
EOF



%files
%{_bindir}/xteddy
%{_bindir}/xteddy_test
%{_bindir}/xtoys
%{_mandir}/man1/xteddy.1*
%{_datadir}/xteddy
%doc COPYING README AUTHORS ChangeLog NEWS
%doc xteddy.README xtuxxy.credit
%_desktopdir/%name.desktop


%changelog
* Wed Jun 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt5_8
- fixed build

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt4_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt3_8
- update to new release by fcimport

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt3_7
- update to new release by fcimport

* Mon Oct 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt3_6
- fixed desktop file

* Mon Oct 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_6
- added desktop file

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_6
- converted from Fedora by srpmconvert script

