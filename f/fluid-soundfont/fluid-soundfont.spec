Name:           fluid-soundfont
Version:        3.1
Release:        alt1_15
Summary:        Pro-quality GM/GS soundfont
Group:          Sound
License:        MIT
# The original URL (http://www.powermage.com/fluid) seems dead. Therefore we point
# to the Hammersound archives:
URL:            http://www.hammersound.com/cgi-bin/soundlink.pl?action=view_category&category=Collections&ListStart=0&ListLength=20
# The Hammersound source gives us a soundfont in a linux-unfriendly .sfArk format. 
# In order to convert this to a linux-friendly .sf2 format one needs to use a 
# non-free utility sfarkxtc from 
#    http://www.melodymachine.com
# This page explains how this conversion is done:
#    http://vsr.informatik.tu-chemnitz.de/staff/jan/nted/doc/ch01s46.html
# Debian folks already did this and we will borrow their source tarball:
Source0:        http://ftp.de.debian.org/debian/pool/main/f/%{name}/%{name}_%{version}.orig.tar.gz
# Some information about the soundfont that can be found in the Hammersound archive:
Source1:        Fluid_R3_Readme.pdf
# Optimized cfg files for fluid usage with timidity, written by Saito, one of
# the TiMidity++ developers
Source2:        timidity++.cfg
Source3:        fluid3gm.cfg
Source4:        fluid3gs.cfg
Source5:        fluid_altassign.cfg
BuildArch:      noarch
BuildRequires:  soundfont-utils


%define common_description \
FluidR3 is the third release of Frank Wen's pro-quality GM/GS soundfont.\
The soundfont has lots of excellent samples, including all the GM instruments\
along side with the GS instruments that are recycled and reprogrammed versions\
of the GM presets.
Source44: import.info

%description
%common_description

%package common
Summary:        Common files for FluidR3 soundfont
Group:          Sound

%description common
%common_description

This package contains common files shared among all FluidR3 soundfont packages.

%package gm
Summary:        Pro-quality General Midi soundfont
Group:          Sound
Requires:       %{name}-common = %{version}
Provides:       soundfont2
Provides:       soundfont2-default
# If timidity++ is installed it must understand the trysouce configfile keyword
Conflicts:      TiMidity++ <= 2.13.2-30.cvs20111110%{?dist}

%description gm
%common_description

This package contains Fluid General Midi (GM) soundfont in soundfont 2.0 (.sf2)
format.

%package gs
Summary:        Pro-quality General Standard Extension soundfont
Group:          Sound
Requires:       %{name}-common = %{version}
Requires:       %{name}-gm = %{version}
Provides:       soundfont2


%description gs
%common_description

This package contains instruments belonging to General Midi's General Standard
(GS) Extension in soundfont 2.0 (.sf2) format.

%package lite-patches
Summary:        Pro-quality General Midi soundfont in GUS patch format
Group:          Sound
Requires:       %{name}-common = %{version}
Provides:       timidity++-patches = 5
Obsoletes:      timidity++-patches < 5
Obsoletes:      PersonalCopy-Lite-patches < 5

%description lite-patches
%common_description

This package contains Fluid General Midi (GM) soundfont in Gravis Ultrasound
(GUS) patch (.pat) format.


%prep
%setup -q
cp -a %{SOURCE1} .

%build
unsf -v -s -m FluidR3_GM.sf2
unsf -v -s -m FluidR3_GS.sf2

# Cut the size of the patches subpackage:
for bank in GM-B{8,9,16} Standard{1,2,3,4,5,6,7} Room{1,2,3,4,5,6,7} Power{1,2,3} Jazz{1,2,3,4} Brush{1,2}; do
   sed -i "/$bank/d" FluidR3_GM.cfg
   rm -fr *$bank*
done

cat FluidR3_GM.cfg FluidR3_GS.cfg > FluidR3.cfg

# The gus patches get used by a lot of different programs and some need the
# path to the patches to be absolute
sed -i 's|FluidR3_GM-|%{_datadir}/soundfonts/%{name}-lite-patches/FluidR3_GM-|g' FluidR3.cfg
sed -i 's|FluidR3_GS-|%{_datadir}/soundfonts/%{name}-lite-patches/FluidR3_GS-|g' FluidR3.cfg

%install
# The actual soundfonts:
mkdir -p $RPM_BUILD_ROOT%{_datadir}/soundfonts
mkdir -p $RPM_BUILD_ROOT%{_datadir}/sounds/sf2
install -p -m 644 FluidR3_GM.sf2 $RPM_BUILD_ROOT%{_datadir}/soundfonts
install -p -m 644 FluidR3_GS.sf2 $RPM_BUILD_ROOT%{_datadir}/soundfonts
# Create a symlink to denote that this is the Fedora default soundfont
ln -s FluidR3_GM.sf2 $RPM_BUILD_ROOT%{_datadir}/soundfonts/default.sf2
ln -s ../../soundfonts/default.sf2 $RPM_BUILD_ROOT%{_datadir}/sounds/sf2

# timidity++.cfg files for usage of the sf2 files with the real timidity
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 644 %{SOURCE3} %{SOURCE4} %{SOURCE5} \
    $RPM_BUILD_ROOT%{_datadir}/soundfonts

# Gus patches + timidity.cfg, for programs which want the "old" timidity.cfg
mkdir -p $RPM_BUILD_ROOT%{_datadir}/soundfonts/%{name}-lite-patches
cp -a FluidR3_GM-* $RPM_BUILD_ROOT%{_datadir}/soundfonts/%{name}-lite-patches
cp -a FluidR3_GS-* $RPM_BUILD_ROOT%{_datadir}/soundfonts/%{name}-lite-patches
install -p -m 644 FluidR3.cfg $RPM_BUILD_ROOT%{_sysconfdir}/timidity.cfg


%files common
%doc COPYING README *Readme*
%dir %{_datadir}/soundfonts/

%files gm
%{_sysconfdir}/timidity++.cfg
%{_datadir}/soundfonts/FluidR3_GM.sf2
%{_datadir}/soundfonts/default.sf2
%{_datadir}/soundfonts/fluid3gm.cfg
%{_datadir}/soundfonts/fluid_altassign.cfg
%{_datadir}/sounds/sf2

%files gs
%{_datadir}/soundfonts/FluidR3_GS.sf2
%{_datadir}/soundfonts/fluid3gs.cfg

%files lite-patches
%config %{_sysconfdir}/timidity.cfg
%{_datadir}/soundfonts/%{name}-lite-patches/


%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_13
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_10
- update to new release by fcimport

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_9
- new version

