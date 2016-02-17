Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/adonthell-0.3 /usr/bin/desktop-file-install python-devel
# END SourceDeps(oneline)
Name:           wastesedge
Version:        0.3.5
Release:        alt1_6
Summary:        Official game package for Adonthell

License:        GPL+
URL:            http://adonthell.linuxgames.com/

## Due to legal issues (RHBZ#477481), upstream sources need to be modified
# Here is how are obtained the sources used in this package:
# $ VERSION=0.3.5
# $ wget http://savannah.nongnu.org/download/adonthell/wastesedge-src-$VERSION.tar.gz
# $ tar xzvf wastesedge-src-$VERSION.tar.gz
# $ rm wastesedge-$VERSION/gfx/window/font/avatar.ttf
# $ sed -i 's|avatar.ttf||g' wastesedge-$VERSION/gfx/window/font/Makefile.in
# $ tar czvf wastesedge-src-$VERSION-modified.tar.gz wastesedge-$VERSION/
Source0:        %{name}-src-%{version}-modified.tar.gz

# This release is 4 years old and upstream moved on since then to work on
# adonthell/wastesedge 0.4 (and I'll update to it once it's ready). So they
# aren't really interested in this old version any more, and I won't bother
# them with something as trivial, unless I have another more important patch
# to submit at the same time.
Patch0:         wastesedge-0.3.5-Fix-upstream-desktop-file.patch

BuildArch:      noarch

BuildRequires:  adonthell >= %{version}
BuildRequires:  gettext
BuildRequires:  desktop-file-utils

Requires:       adonthell >= %{version}
Requires:       icon-theme-hicolor
Source44: import.info


%description
As a loyal servant of the elven Lady Silverhair, you arrive at the remote
trading post of Waste's Edge, where she is engaged in negotiations with the
dwarvish merchant Bjarn Fingolson. But not all is well at Waste's Edge, and
soon you are confronted with circumstances that are about to destroy your
mistress' high reputation. And you are the only one to avert this ...


%prep
%setup -q

# fix wrong file permissions (fixed upstream for future release)
chmod a-x AUTHORS COPYING INSTALL README

# install locale files in the right place
sed -i 's|datadir = @gamedatadir@|datadir = ${prefix}/share|' po/Makefile.in.in

%patch0 -p1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

# install images in the correct folders
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32}/apps
mv %{buildroot}%{_datadir}/pixmaps/%{name}_16x16.xpm %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.xpm
mv %{buildroot}%{_datadir}/pixmaps/%{name}_32x32.xpm %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

# install desktop file
desktop-file-install                               \
        --dir=%{buildroot}%{_datadir}/applications \
        %{name}.desktop

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING PLAYING README
%{_bindir}/adonthell-%{name}
%{_datadir}/adonthell/games/%{name}/
%{_datadir}/icons/hicolor/16x16/apps/%{name}.xpm
%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1_2
- update to new release by fcimport

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt2_0.18
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt2_0.17
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt1_0.17
- update to new release by fcimport

* Sat Jul 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt1_0.16
- initial release by fcimport

