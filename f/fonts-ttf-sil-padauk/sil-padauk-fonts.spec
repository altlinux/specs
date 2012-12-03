# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ perl(English.pm) unzip
# END SourceDeps(oneline)
%define oldname sil-padauk-fonts
%global fontname sil-padauk
%global fontconf 65-%{fontname}
%global archivename padauk-2.8

%global common_desc \
Padauk is a Myanmar font covering all currently used characters \
in the Myanmar block. The font aims to cover all minority language needs. \
At the moment, these do not extend to stylistic variation needs. \
The font is a smart font using a Graphite description.

Name:    fonts-ttf-sil-padauk
Version: 2.8
Release: alt1_2
Summary: A font for Burmese and the Myanmar script

Group:   System/Fonts/True type
License: OFL
URL:     http://scripts.sil.org/Padauk
# The source link is a redirect and is not directly accessible
Source0: %{archivename}.zip
Source1: %{oldname}-fontconfig.conf
Source2: %{oldname}-book-fontconfig.conf

BuildArch: noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
%common_desc

%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/Padauk.ttf
%{_fontbasedir}/*/%{_fontstem}/Padauk-bold.ttf
%doc *.txt

%package -n %{fontname}-book-fonts
Group: System/Fonts/True type
Summary:  A font for Burmese and the Myanmar script

%description -n %{fontname}-book-fonts
Padauk Book family font.

%common_desc

%files -n %{?fontname:%fontname}%{!?fontname:%oldname}-book-fonts
%{_fontconfig_templatedir}/%{fontconf}-book.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-book.conf
%{_fontbasedir}/*/%{_fontstem}/Padauk-book*.ttf
%doc *.txt

%prep
%setup -q -n padauk-2.80
sed -i 's/\r//' OFL.txt

%build
# Nothing there


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-book.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}-book.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}-book.conf
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
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_2
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt3_9
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt3_8
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_8
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_7
- rebuild with new rpm-build-fonts

* Thu Aug 04 2011 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_7
- initial release by fcimport

