# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		biniax
Version:	1.2
Release:	alt3_22
Summary:	A unique arcade logic game

Group:		Games/Other
License:	zlib
URL:		http://www.biniax.com/
Source0:	http://mordred.dir.bg/%{name}/%{name}-src.zip
Source1:	%{name}.desktop
# Icon taken from the source, icon.ico
Source2:	%{name}.png
# Fixes the path in gfx.c, snd.c. and creates a ~/.biniax subdir 
# with "autosave" and "highscore" data. Patches send to upstream!
Patch0:		%{name}-%{version}-gfx.patch
Patch1:		%{name}-%{version}-snd.patch
Patch2:		%{name}-%{version}-save.patch
Patch3:		%{name}-%{version}-optflags.patch
Patch4:		%{name}-%{version}-close.patch

Requires:	icon-theme-hicolor
BuildRequires:	libSDL-devel libSDL_mixer-devel desktop-file-utils
Source44: import.info

%description
The gaming field is 5x7 pairs of elements. Every pair consists of two elements 
out of four possible types (colors). Player is a single element, who can move on
empty fields or can take a pair, if the player's element is present in the pair.
If a pair is taken, the player's element is swapped to the other element of the 
pair. The field is scrolling down on time event or after certain moves are spend
(depending on the game mode). Game over is when there is no move for the player.


%prep
%setup -q -c -n %{name}
%patch0 -p0 -b .gfx
%patch1 -p0 -b .snd
%patch2 -p0 -b .save
%patch3 -p0 -b .optflags
%patch4 -p0 -b .close
# Needed because of this rpmlint warning "W: wrong-file-end-of-line-encoding"
sed -i 's/\r//' Readme.txt LICENSE.txt
# Set datadir prefix, snd.patch and gfx.patch
sed -i 's!@DATADIR@!%{_datadir}!' desktop/gfx.c
sed -i 's!@DATADIR@!%{_datadir}!' desktop/snd.c


%build

%make_build


%install

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/data

install -p -m 755 biniax %{buildroot}%{_bindir}/%{name}
install -p -m 644 data/* %{buildroot}%{_datadir}/%{name}/data/


# below the desktop file and icon stuff
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications \
	%{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

install -p -m 0644 %{SOURCE2} \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%files
%doc LICENSE.txt Readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_22
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_21
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_19
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_18
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_17
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_16
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_15
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_14
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_13
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_12
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_10
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_9
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_9
- update to new release by fcimport

* Mon Feb 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_8
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_8
- converted from Fedora by srpmconvert script

