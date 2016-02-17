# BEGIN SourceDeps(oneline):
BuildRequires: libICE-devel libSM-devel libX11-devel pkgconfig(imlib2)
# END SourceDeps(oneline)
BuildRequires: libXext-devel
Name:           xteddy
Version:        2.2
Release:        alt1_5
Summary:        Tool to sit around silently, look cute, and make you smile

Group:          Games/Other
License:        GPL+
URL:            http://fam-tille.de/debian/xteddy.html
Source0:        http://webstaff.itn.liu.se/~stegu/xteddy/%{name}-%{version}.tar.gz
# This is original artwork by Lubomir Rintel, distributed under same
# terms and condition as xteddy
Source1:        kacicka.png
Patch0:         0001-Link-against-Xext.patch

BuildRequires:  imlib2-devel libpng-devel
Source44: import.info
Patch33: xteddy-2.2-alt-link-X11.patch

%description
Xteddy is your virtual comfort when things get rough. It can do everything
a real teddy bear can do. That is, I can sit around silently, look cute,
and make you smile.


%prep
%setup -q
%patch0 -p1
%patch33 -p1
sed -i -e s,/usr/games/xteddy,xteddy, xtoys


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
install -p -m644 %{SOURCE1} %{buildroot}%{_datadir}/xteddy/

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
%{_mandir}/man6/xteddy.6*
%{_datadir}/xteddy
%doc COPYING README AUTHORS ChangeLog NEWS
%doc xteddy.README images.credit
%_desktopdir/%name.desktop


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_2
- update to new release by fcimport

* Thu Jan 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt5_13
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt5_12
- update to new release by fcimport

* Wed Jan 23 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt5_11
- update to new release by fcimport

* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt5_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt5_9
- update to new release by fcimport

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

