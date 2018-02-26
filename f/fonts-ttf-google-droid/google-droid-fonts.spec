%define oldname google-droid-fonts
%global fontname google-droid

%global download_root http://android.git.kernel.org/?p=platform/frameworks/base.git;a=blob_plain;f=data/fonts/

%global common_desc \
The Droid typeface family was designed in the fall of 2006 by Ascender's \
Steve Matteson, as a commission from Google to create a set of system fonts \
for its Android platform. The goal was to provide optimal quality and comfort \
on a mobile handset when rendered in application menus, web browsers and for \
other screen text.

Name:    fonts-ttf-google-droid
# No sane versionning upstream, use the most recent file datestamp
Version: 20100409
Release: alt2_3
Summary: General-purpose fonts released by Google as part of Android

Group:     System/Fonts/True type
License:   ASL 2.0
URL:       http://android.git.kernel.org/?p=platform/frameworks/base.git;a=tree;f=data/fonts
Source0:   %{download_root}NOTICE
Source1:   %{download_root}README.txt
Source10:  %{download_root}DroidSans.ttf
Source11:  %{download_root}DroidSans-Bold.ttf
Source12:  %{download_root}DroidSansJapanese.ttf
#DroidSansFallbackLegacy.ttf is an old version with less coverage
Source13:  %{download_root}DroidSansFallback.ttf
Source14:  %{download_root}DroidSansArabic.ttf
Source15:  %{download_root}DroidSansHebrew.ttf
Source16:  %{download_root}DroidSansThai.ttf
Source20:  %{download_root}DroidSansMono.ttf
Source30:  %{download_root}DroidSerif-Regular.ttf
Source31:  %{download_root}DroidSerif-Bold.ttf
Source32:  %{download_root}DroidSerif-Italic.ttf
Source33:  %{download_root}DroidSerif-BoldItalic.ttf
Source41:  %{oldname}-sans-fontconfig.conf
Source42:  %{oldname}-sans-mono-fontconfig.conf
Source43:  %{oldname}-serif-fontconfig.conf


BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
%common_desc


%package -n fonts-ttf-google-droid-sans
Group: System/Fonts/True type
Summary:   A humanist sans serif typeface
Obsoletes: %{oldname}-common <= 20090906-5.fc12

%description -n fonts-ttf-google-droid-sans
%common_desc

Droid Sans is a humanist sans serif typeface designed for user interfaces and
electronic communication.

%files -n fonts-ttf-google-droid-sans
%{_fontconfig_templatedir}/??-%{fontname}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/??-%{fontname}-sans.conf
%{_fontbasedir}/*/%{_fontstem}/DroidSans.ttf
%{_fontbasedir}/*/%{_fontstem}/DroidSans-Bold.ttf
%{_fontbasedir}/*/%{_fontstem}/DroidSansArabic.ttf
%{_fontbasedir}/*/%{_fontstem}/DroidSansHebrew.ttf
%{_fontbasedir}/*/%{_fontstem}/DroidSansJapanese.ttf
%{_fontbasedir}/*/%{_fontstem}/DroidSansThai.ttf
%{_fontbasedir}/*/%{_fontstem}/DroidSansFallback.ttf
%doc *.txt

%package -n fonts-ttf-google-droid-sans-mono
Group: System/Fonts/True type
Summary:  A humanist monospace sans serif typeface

%description -n fonts-ttf-google-droid-sans-mono
%common_desc

Droid Sans Mono is a humanist monospace sans serif typeface designed for user
interfaces and electronic communication.

%files -n fonts-ttf-google-droid-sans-mono
%{_fontconfig_templatedir}/??-%{fontname}-sans-mono.conf
%config(noreplace) %{_fontconfig_confdir}/??-%{fontname}-sans-mono.conf
%{_fontbasedir}/*/%{_fontstem}/DroidSansMono.ttf
%doc *.txt

%package -n fonts-ttf-google-droid-serif
Group: System/Fonts/True type
Summary:  A contemporary serif typeface

%description -n fonts-ttf-google-droid-serif
%common_desc

Droid Serif is a contemporary serif typeface family designed for comfortable
reading on screen. Droid Serif is slightly condensed to maximize the amount of
text displayed on small screens. Vertical stress and open forms contribute to
its readability while its proportion and overall design complement its
companion Droid Sans.

%files -n fonts-ttf-google-droid-serif
%{_fontconfig_templatedir}/??-%{fontname}-serif.conf
%config(noreplace) %{_fontconfig_confdir}/??-%{fontname}-serif.conf
%{_fontbasedir}/*/%{_fontstem}/DroidSerif*ttf
%doc *.txt

%prep
%setup -q -c -T
install -m 0644 -p %{SOURCE0} notice.txt
install -m 0644 -p %{SOURCE1} readme.txt


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p  %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} \
                    %{SOURCE14} %{SOURCE15} %{SOURCE16} \
                    %{SOURCE20} \
                    %{SOURCE30} %{SOURCE31} %{SOURCE32} %{SOURCE33}\
                    %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE41} \
        %{buildroot}%{_fontconfig_templatedir}/65-%{fontname}-sans.conf
install -m 0644 -p %{SOURCE42} \
        %{buildroot}%{_fontconfig_templatedir}/60-%{fontname}-sans-mono.conf
install -m 0644 -p %{SOURCE43} \
        %{buildroot}%{_fontconfig_templatedir}/59-%{fontname}-serif.conf

for fontconf in 65-%{fontname}-sans.conf \
                60-%{fontname}-sans-mono.conf \
                59-%{fontname}-serif.conf ; do
  ln -s %{_fontconfig_templatedir}/$fontconf \
        %{buildroot}%{_fontconfig_confdir}/$fontconf
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


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100409-alt2_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100409-alt1_3
- update to new release by fcimport

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 20100409-alt1_2
- initial release by fcimport

