# BEGIN SourceDeps(oneline):
BuildRequires: unzip zlib-devel
# END SourceDeps(oneline)
Name:           raidem
Version:        0.3.1
Release:        alt1_20
Summary:        2d top-down shoot'em up
Group:          Games/Other
License:        zlib
URL:            http://home.exetel.com.au/tjaden/raidem/
# This is an exacy copy of the upstream src except that lib/almp3 which is
# an included mp3 decoder has been removed.
Source0:        %{name}-%{version}-src.zip
Source1:        raidem.png
Source2:        raidem.desktop
Patch0:         raidem-0.3.1-syslibs.patch
Patch1:         raidem-0.3.1-zziplib.patch
Patch2:         raidem-libpng15.patch
Patch3:         raidem-gcc4.7-stdio.patch
Patch4:         raidem-new-api.patch
BuildRequires:  gcc-objc glyph-keeper-allegro-devel libfreetype-devel libadime-devel
BuildRequires:  zziplib-devel libpng-devel AllegroOGG-devel
BuildRequires:  automake desktop-file-utils gnustep-base-devel
Requires:       icon-theme-hicolor
Source44: import.info

%description
Raid'em is a 2d top-down shoot'em up. It began as a remake of Raid II
(abandoned long ago), but has turned out very differently.
Features: Neat looking graphics, LOTS of explosions and scrap
metal, Eye candy a-plenty, Many different powerups, A desert. And a space
platform. And some snow, 2 player mode, Demo recording and playback, Loads of
fun.


%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1 -z .syslibs
%patch1 -p1
%patch2 -z .libpng
%patch3 -p0 -z .gcc47
%patch4 -p0 -z .newapi
# remove all included system libs, to avoid using the included system headers.
mv lib/loadpng .
rm -fr lib/*
mv loadpng lib
aclocal
autoconf


%build
# override _datadir otherwise it expects its datafile directly under /use/share
%configure --datadir=%{_datadir}/%{name} --disable-id3
make %{?_smp_mflags}


%install
# DIY, since the Makefile uses install -s and install -g games, etc.
# Fixable but this is easier
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a data demos maps $RPM_BUILD_ROOT%{_datadir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps


%files
%doc ChangeLog docs/LICENCE.txt docs/README.txt docs/damages.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_20
- update to new release by fcimport

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_19
- update to new release by fcimport

* Tue Nov 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_17
- update to new release by fcimport

* Wed Jul 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_16
- initial release by fcimport

