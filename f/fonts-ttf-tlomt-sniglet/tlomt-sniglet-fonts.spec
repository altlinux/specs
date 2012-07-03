# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname tlomt-sniglet-fonts
%define fontname tlomt-sniglet
%define fontconf 60-%{fontname}

Name:		fonts-ttf-tlomt-sniglet
Summary:	A rounded, sans-serif font useful for headlines
Version:	1.000
Release:	alt3_4
# License attribution confirmed by author
# See: sniglet-license-confirmation-email.txt
License:	OFL
Group:		System/Fonts/True type
Source0:	https://s3.amazonaws.com/theleague-production/fonts/sniglet.zip
Source1:	%{oldname}-fontconfig.conf
Source2:	sniglet-license-confirmation-email.txt
URL:		http://www.theleagueofmoveabletype.com/fonts/2-sniglet
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Source44: import.info

%description
Sniglet is a fun rounded, sans-serif font useful for headlines and other
creative treaments. The font was created by Haley Fiege, and it supports a
full Latin character set including diacritics (accent marks). Notably, it
has full coverage for Icelandic and French characters.

%prep
%setup -q -c -n %{oldname}
cp %{SOURCE2} .

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}.conf %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf
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
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/Sniglet.ttf
%doc sniglet-license-confirmation-email.txt

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.000-alt3_4
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.000-alt2_4
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.000-alt2_3
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.000-alt1_3
- initial release by fcimport

