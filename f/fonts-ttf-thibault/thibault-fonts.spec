%define oldname thibault-fonts
# Due to changes in the Fedora legal environment, rpm spec files are now specifically listed as a "contribution" 
# in/to Fedora (refer to FPCA FAQ here: https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement ).
# Quote: 
# "Q. Are RPM spec files covered by the FPCA?
# A. Sure. They're a contribution, aren't they? :) Nevertheless, they are explicitly named as an example of a contribution, to clear up a past confusion."
# 
# As a result of this change, I have decided to specifically license all of my rpm spec files as GPLv2.
# See program source for a copy of this license.
#

%global fontname        thibault
%global conf1           69-essays1743.conf
%global conf2           69-isabella.conf
%global conf3           69-rockets.conf
%global conf4           69-staypuft.conf

%define common_desc \
A collection of fonts from thibault.org,\
including Isabella, Essays1743, StayPuft,\
and Rockets.

Name:           fonts-ttf-thibault
Version:        0.1
Release:        alt3_18

Summary:        Thibault.org font collection
Group:          System/Fonts/True type
License:        LGPLv2+

URL:            http://www.thibault.org/fonts
Source0:        http://www.thibault.org/fonts/essays/essays1743-2.000-1-ttf.tar.gz
Source1:        http://thibault.org/fonts/isabella/Isabella-1.2-ttf.tar.gz
Source2:        http://www.thibault.org/fonts/rockets/Rockets-ttf.tar.gz
Source3:        http://www.thibault.org/fonts/staypuft/StayPuft.tar.gz
Source4:        %{oldname}-essays1743-fontconfig.conf
Source5:        %{oldname}-isabella-fontconfig.conf
Source6:        %{oldname}-rockets-fontconfig.conf
Source7:        %{oldname}-staypuft-fontconfig.conf

#Not included due to legal concerns
#Engadget: A sort of modernistic font done to match the logo of http://www.engadget.com


BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  fontforge >= 20061025-1
Source44: import.info

%description
%common_desc

%package common
Summary:        Common files for thibault (documentationa..)
Group:          System/Fonts/True type

%description common
%common_desc

This package consists of files used by other %{oldname} packages.

%package -n fonts-ttf-thibault-essays1743
Group: System/Fonts/True type

Summary:  Thibault.org Montaigne's Essays typeface font

Requires: %{name}-common = %{version}-%{release}
Obsoletes: %{oldname}-essays1743 < 0.1-17

%description -n fonts-ttf-thibault-essays1743
%common_desc

A font by John Stracke, based on the
typeface used in a 1743 English
translation of Montaigne's Essays.

%files -n fonts-ttf-thibault-essays1743
%{_fontconfig_templatedir}/%{conf1}
%config(noreplace) %{_fontconfig_confdir}/%{conf1}
%{_fontbasedir}/*/%{_fontstem}/Essays1743*.ttf

%package -n fonts-ttf-thibault-isabella
Group: System/Fonts/True type

Summary: Thibault.org Isabella Breviary calligraphic font

Requires: %{name}-common = %{version}-%{release}
Obsoletes: %{oldname}-isabella < 0.1-17

%description -n fonts-ttf-thibault-isabella
%common_desc

This font is called Isabella because it is based on the
calligraphic hand used in the Isabella Breviary, made around 1497, in
Holland, for Isabella of Castille, the first queen of united Spain.

%files -n fonts-ttf-thibault-isabella
%{_fontconfig_templatedir}/%{conf2}
%config(noreplace) %{_fontconfig_confdir}/%{conf2}
%{_fontbasedir}/*/%{_fontstem}/Isabella*.ttf

%package -n fonts-ttf-thibault-rockets
Group: System/Fonts/True type

Summary:  Thibault.org font, vaguely space themed

Requires: %{name}-common = %{version}-%{release}
Obsoletes: %{oldname}-rockets < 0.1-17

%description -n fonts-ttf-thibault-rockets
%common_desc

This font is called Rockets because it's vaguely space
themed.  The A is, more or less, a 1950s SF rocket; the O is meant to
be Earth, with the Americas visible.  The other capitals are based on
curves from either A or O, to keep the theme consistent.

%files -n fonts-ttf-thibault-rockets
%{_fontconfig_templatedir}/%{conf3}
%config(noreplace) %{_fontconfig_confdir}/%{conf3}
%{_fontbasedir}/*/%{_fontstem}/Rockets*.ttf

%package -n fonts-ttf-thibault-staypuft
Group: System/Fonts/True type

Summary: Thibault.org font, rounded and marshmellowy

Requires: %{name}-common = %{version}-%{release}
Obsoletes: %{oldname}-staypuft < 0.1-17

%description -n fonts-ttf-thibault-staypuft
%common_desc

A rounded marshmellow type font. Good for frivolous things
like banners, and birthday cards.

%files -n fonts-ttf-thibault-staypuft
%{_fontconfig_templatedir}/%{conf4}
%config(noreplace) %{_fontconfig_confdir}/%{conf4}
%{_fontbasedir}/*/%{_fontstem}/StayPuft*.ttf

%prep
mkdir -p staypuft
tar xvzf %{SOURCE0}
tar xvzf %{SOURCE1}
tar xvzf %{SOURCE2}
tar xvzf %{SOURCE3} -C staypuft

%build

pushd essays1743
fontforge -lang=ff -c 'Open($1); Generate($2)' Essays1743.sfd ../Essays1743.ttf
fontforge -lang=ff -c 'Open($1); Generate($2)' Essays1743-Bold.sfd ../Essays1743-Bold.ttf
fontforge -lang=ff -c 'Open($1); Generate($2)' Essays1743-BoldItalic.sfd ../Essays1743-BoldItalic.ttf
fontforge -lang=ff -c 'Open($1); Generate($2)' Essays1743-Italic.sfd ../Essays1743-Italic.ttf
popd

pushd Isabella
fontforge -lang=ff -c 'Open($1); Generate($2)' Isabella-first.sfd ../Isabella.ttf
popd

pushd rockets
fontforge -lang=ff -c 'Open($1); Generate($2)' Rockets.sfd ../Rockets.ttf
popd

pushd staypuft
fontforge -lang=ff -c 'Open($1); Generate($2)' StayPuft.sfd ../StayPuft.ttf
popd

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{conf1}


install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{conf2}

install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{conf3}

install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/%{conf4}

for fconf in %{conf1} \
                %{conf2} \
                %{conf3} \
                %{conf4} ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz afm pfa pfb; do
    case "$fontpatt" in 
	pcf*) type=bitmap;;
	tt*|TT*) type=ttf;;
	otf|OTF) type=otf;;
	afm*|pf*) type=type1;;
    esac
    find $RPM_BUILD_ROOT/usr/share/fonts -type f -name '*.'$fontpatt | while read i; do
	j=`echo "$i" | sed -e s,/usr/share/fonts/,/usr/share/fonts/$type/,`;
	install -Dm644 "$i" "$j";
	rm -f "$i";
	olddir=`dirname "$i"`;
	mv -f "$olddir"/{encodings.dir,fonts.{dir,scale,alias}} `dirname "$j"`/ 2>/dev/null ||:
	rmdir -p "$olddir" 2>/dev/null ||:
    done
done
# kill invalid catalogue links
if [ -d $RPM_BUILD_ROOT/etc/X11/fontpath.d ]; then
    find -L $RPM_BUILD_ROOT/etc/X11/fontpath.d -type l -print -delete ||:
    # relink catalogue
    find $RPM_BUILD_ROOT/usr/share/fonts -name fonts.dir | while read i; do
	pri=10;
	j=`echo $i | sed -e s,$RPM_BUILD_ROOT/usr/share/fonts/,,`; type=${j%%%%/*}; 
	pre_stem=${j##$type/}; stem=`dirname $pre_stem|sed -e s,/,-,g`;
	case "$type" in 
	    bitmap) pri=10;;
	    ttf|ttf) pri=50;;
	    type1) pri=40;;
	esac
	ln -s /usr/share/fonts/$j $RPM_BUILD_ROOT/etc/X11/fontpath.d/"$stem:pri=$pri"
    done ||:
fi

%files common
%doc essays1743/COPYING essays1743/README
%doc Isabella/COPYING.LIB Isabella/README.txt
%doc rockets/COPYING.LIB rockets/README.txt
%doc staypuft/COPYING.LIB staypuft/README.txt

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_18
- rebuild to get rid of #27020

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_18
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_15
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_15
- initial release by fcimport

