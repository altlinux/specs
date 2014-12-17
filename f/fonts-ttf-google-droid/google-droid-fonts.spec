Group: System/Fonts/True type
%define oldname google-droid-fonts
# %%oldname or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name google-droid-fonts
%define version 20120715
%global fontname google-droid
%global archivename %{oldname}-%{version}

%global common_desc \
The Droid typeface family was designed in the fall of 2006 by Ascender's \
Steve Matteson, as a commission from Google to create a set of system fonts \
for its Android platform. The goal was to provide optimal quality and comfort \
on a mobile handset when rendered in application menus, web browsers and for \
other screen text. \
The family was later extended in collaboration with other designers such as \
Pascal Zoghbi of 29ArabicLetters.

Name:    fonts-ttf-google-droid
# No sane versionning upstream, use git clone timestamp
Version: 20120715
Release: alt3_8
Summary: General-purpose fonts released by Google as part of Android

License:   ASL 2.0
URL:       https://android.googlesource.com/
Source0:   %{archivename}.tar.xz
#Brutal script used to pull sources from upstream git
Source1:   getdroid.sh
Source10:  %{oldname}-sans-fontconfig.conf
Source11:  %{oldname}-sans-mono-fontconfig.conf
Source12:  %{oldname}-serif-fontconfig.conf
Source13:  %{oldname}-kufi-fontconfig.conf
Source14:  %{fontname}-sans.metainfo.xml
Source15:  %{fontname}-sans-mono.metainfo.xml
Source16:  %{fontname}-serif.metainfo.xml
Source17:  %{fontname}-kufi.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
%common_desc


%package -n fonts-ttf-google-droid-sans
Group: System/Fonts/True type
Summary:   A humanist sans serif typeface
Obsoletes: %{oldname}-common <= 20090906-5.fc12

Provides: fonts-ttf-droid = %version
Obsoletes: fonts-ttf-droid < 1.01
Conflicts: fonts-ttf-droid < 1.01


%description -n fonts-ttf-google-droid-sans
%common_desc

Droid Sans is a humanist sans serif typeface designed for user interfaces and
electronic communication.

%files -n fonts-ttf-google-droid-sans
%{_fontconfig_templatedir}/??-%{fontname}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/??-%{fontname}-sans.conf
%{_fontbasedir}/*/%{_fontstem}/DroidSans*ttf
%exclude %{_fontbasedir}/*/%{_fontstem}/DroidSansMono*ttf
%doc README.txt NOTICE
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml

%package -n fonts-ttf-google-droid-sans-mono
Group: System/Fonts/True type
Summary:  A humanist monospace sans serif typeface

Provides: fonts-ttf-droid = %version
Obsoletes: fonts-ttf-droid < 1.01
Conflicts: fonts-ttf-droid < 1.01


%description -n fonts-ttf-google-droid-sans-mono
%common_desc

Droid Sans Mono is a humanist monospace sans serif typeface designed for user
interfaces and electronic communication.

%files -n fonts-ttf-google-droid-sans-mono
%{_fontconfig_templatedir}/??-%{fontname}-sans-mono.conf
%config(noreplace) %{_fontconfig_confdir}/??-%{fontname}-sans-mono.conf
%{_fontbasedir}/*/%{_fontstem}/DroidSansMono.ttf
%doc README.txt NOTICE
%{_datadir}/appdata/%{fontname}-sans-mono.metainfo.xml

%package -n fonts-ttf-google-droid-serif
Group: System/Fonts/True type
Summary:  A contemporary serif typeface
Provides: %{fontname}-naskh-fonts = %{version}-%{release}

Provides: fonts-ttf-droid = %version
Obsoletes: fonts-ttf-droid < 1.01
Conflicts: fonts-ttf-droid < 1.01


%description -n fonts-ttf-google-droid-serif
%common_desc

Droid Serif is a contemporary serif typeface family designed for comfortable
reading on screen. Droid Serif is slightly condensed to maximize the amount of
text displayed on small screens. Vertical stress and open forms contribute to
its readability while its proportion and overall design complement its
companion Droid Sans.
The Arabic block was designed by Pascal Zoghbi of 29ArabicLetters under the
Droid Naskh name.

%files -n fonts-ttf-google-droid-serif
%{_fontconfig_templatedir}/??-%{fontname}-serif.conf
%config(noreplace) %{_fontconfig_confdir}/??-%{fontname}-serif.conf
%{_fontbasedir}/*/%{_fontstem}/DroidSerif*ttf
%{_fontbasedir}/*/%{_fontstem}/DroidNaskh*ttf
%doc README.txt NOTICE
%{_datadir}/appdata/%{fontname}-serif.metainfo.xml

%package -n fonts-ttf-google-droid-kufi
Group: System/Fonts/True type
Summary:  A kufi Arabic titling typeface designed to complement Droid Sans
Requires: fonts-ttf-google-droid-kufi

%description -n fonts-ttf-google-droid-kufi
%common_desc

Droid Kufi is a stylized display font suitable for titles and short runs of
text, and designed to complement Droid Sans. It was initialy designed by
Steve Matteson of Ascender with consulting by Pascal Zoghbi of 29ArabicLetters
to finalize the font family.

%files -n fonts-ttf-google-droid-kufi
%{_fontconfig_templatedir}/??-%{fontname}-kufi.conf
%config(noreplace) %{_fontconfig_confdir}/??-%{fontname}-kufi.conf
%{_fontbasedir}/*/%{_fontstem}/DroidKufi*ttf
%{_datadir}/appdata/%{fontname}-kufi.metainfo.xml

%prep
%setup -q -n %{archivename}


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p $(ls *ttf | grep -v DroidSansFallbackFull\
                             | grep -v DroidSansFallbackLegacy\
                             | grep -v DroidNaskh-Regular-SystemUI) \
                    %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE10} \
        %{buildroot}%{_fontconfig_templatedir}/65-%{fontname}-sans.conf
install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/60-%{fontname}-sans-mono.conf
install -m 0644 -p %{SOURCE12} \
        %{buildroot}%{_fontconfig_templatedir}/65-%{fontname}-serif.conf
install -m 0644 -p %{SOURCE13} \
        %{buildroot}%{_fontconfig_templatedir}/65-%{fontname}-kufi.conf

for fontconf in 65-%{fontname}-sans.conf \
                60-%{fontname}-sans-mono.conf \
                65-%{fontname}-serif.conf \
                65-%{fontname}-kufi.conf ; do
  ln -s %{_fontconfig_templatedir}/$fontconf \
        %{buildroot}%{_fontconfig_confdir}/$fontconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE14} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE15} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans-mono.metainfo.xml
install -Dm 0644 -p %{SOURCE16} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-serif.metainfo.xml
install -Dm 0644 -p %{SOURCE17} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-kufi.metainfo.xml
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
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

%changelog
* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 20120715-alt3_8
- update to new release by fcimport

* Thu Sep 04 2014 Igor Vlasenko <viy@altlinux.ru> 20120715-alt3_7
- added conflict to fonts-ttf-droid

* Fri Jun 27 2014 Igor Vlasenko <viy@altlinux.ru> 20120715-alt2_7
- added obsoletes on fonts-ttf-droid

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20120715-alt1_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20120715-alt1_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20120715-alt1_4
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 20120715-alt1_3
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100409-alt2_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100409-alt1_3
- update to new release by fcimport

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 20100409-alt1_2
- initial release by fcimport

