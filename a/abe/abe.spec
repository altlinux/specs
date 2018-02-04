Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ imake libXt-devel xorg-cf-files
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           abe
Version:        1.1
Release:        alt5_32

Summary:        Scrolling, platform-jumping, ancient pyramid exploring game
License:        GPL+
URL:            http://abe.sourceforge.net/
Source0:        http://downloads.sourceforge.net/abe/%{name}-%{version}.tar.gz
Source1:        %{name}-icons.tar.xz
Source2:        %{name}.appdata.xml
# Enable changing the video settings.  Sent upstream 2 Apr 2006:
# https://sourceforge.net/tracker/?func=detail&aid=1463202&group_id=70141&atid=526743
Patch0:         %{name}-1.1-settings.patch
# Fix a double free() bug.  Sent upstream 15 Mar 2011:
# https://sourceforge.net/tracker/?func=detail&aid=3214269&group_id=70141&atid=526745
Patch1:         %{name}-1.1-doublefree.patch
# Fix an incorrect printf format specifier.  Sent upstream 15 Mar 2011:
# https://sourceforge.net/tracker/?func=detail&aid=3214270&group_id=70141&atid=526745
Patch2:         %{name}-1.1-format.patch
# Add support for aarch64.  Sent upstream 25 Mar 2013:
# https://sourceforge.net/tracker/?func=detail&aid=3609029&group_id=70141&atid=526743
Patch3:         %{name}-1.1-aarch64.patch
# Fix build failure with -Werror=format-security
Patch4:         %{name}-1.1-format-security.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libSDL-devel
BuildRequires:  libSDL_mixer-devel

Requires:       icon-theme-hicolor

%global icondir %{_datadir}/icons/hicolor
Source44: import.info

%description
A scrolling, platform-jumping, key-collecting, ancient pyramid exploring game,
vaguely in the style of similar games for the Commodore+4.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4

# Fix the FSF's address
sed 's/59 Temple Place, Suite 330, Boston, MA  02111-1307/51 Franklin Street, Suite 500, Boston, MA  02110-1335/' COPYING > COPYING.new
touch -r COPYING COPYING.new
mv -f COPYING.new COPYING

%build
%configure --with-data-dir=%{_datadir}/%{name}
sed -i "s|^CFLAGS =.*|CFLAGS = ${RPM_OPT_FLAGS} \$\(SDL_CFLAGS\)|" src/Makefile
%make_build

%install
make DESTDIR=$RPM_BUILD_ROOT install

# make install does not copy the game data files.
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/appdata/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications/
mkdir -p $RPM_BUILD_ROOT/%{icondir}
cp -p -r images maps sounds $RPM_BUILD_ROOT/%{_datadir}/%{name}
tar xJf %{SOURCE1} -C $RPM_BUILD_ROOT%{icondir}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/appdata/

cat << EOF > %{name}.desktop
[Desktop Entry]
Name=Abe
Comment="Abe's Amazing Adventure"
Exec=abe
Icon=abe
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications/ %{name}.desktop

%files
%doc README
%doc --no-dereference COPYING
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_32
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_31
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_29
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_28
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_27
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_26
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_25
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_22
- update to new release by fcimport

* Fri Nov 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_21
- update to new release by fcimport

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_20
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_19
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_18
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_17
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_16
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_15
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_15
- update to new release by fcimport

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_14
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_13
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_13
- rebuild with new rpm desktop cleaner

* Fri Mar 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_13
- new origin release

* Mon Feb 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_12
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_12
- converted from Fedora by srpmconvert script

