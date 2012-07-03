# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname tlomt-league-gothic-fonts
%global fontname tlomt-league-gothic
%global fontconf 61-%{fontname}.conf

Name:           fonts-otf-tlomt-league-gothic
Version:        1.0
Release:        alt2_3
Summary:        A sans serif gothic typeface

Group:          System/Fonts/True type
License:        OFL
URL:            http://www.theleagueofmoveabletype.com/fonts/7-league-gothic
Source0:        http://s3.amazonaws.com/theleague-production/fonts/league-gothic.zip
Source1:        %{oldname}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
League Gothic is a revival of an old classic, Alternate Gothic No.1.
It was originally designed by Morris Fuller Benton for the American
Type Founders Company (ATF) in 1903. The company went bankrupt in 1993.
And since the original typeface was created before 1923, the typeface
is in the public domain. It is a sans serif gothic typeface.

This is actually another version of the font which was made by
The League of Movable Type and contributed to the Open Source Type
Movement.

%prep
%setup -q -c -T
unzip -j -L -q %{SOURCE0}

%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p League\ Gothic.otf %{buildroot}%{_fontdir}/

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}
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


%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.otf


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_3
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_2
- initial release by fcimport

