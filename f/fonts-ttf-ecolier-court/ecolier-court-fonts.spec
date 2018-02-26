%define oldname ecolier-court-fonts
%global fontname ecolier-court
%global fontconf 61-%{fontname}

%global common_desc\
A.colier court fonts were created by Jean-Marie Douteau to mimic the \
traditional cursive writing French children are taught in school. \
\
He kindly released two of them under the OFL, which are redistributed in \
this package.


Name:    fonts-ttf-ecolier-court
Version: 20070702
Release: alt3_14
Summary: Schoolchildren cursive fonts

Group:     System/Fonts/True type
License:   OFL
URL:       http://perso.orange.fr/jm.douteau/page_ecolier.htm
# The author links to third-party licence documents not included there
Source0:   http://perso.orange.fr/jm.douteau/polices/ecl_cour.ttf
Source1:   http://perso.orange.fr/jm.douteau/polices/ec_cour.ttf
Source2:   http://perso.orange.fr/jm.douteau/polices/lisez_moi.txt
Source3:   README-Fedora.txt
Source4:   %{oldname}-fontconfig.conf
Source5:   %{oldname}-lignes-fontconfig.conf


BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      %{name}-common = %{version}-%{release}
Source44: import.info

%description
%common_desc

%files
%{_fontconfig_templatedir}/%{fontconf}-lignes.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-lignes.conf
%{_fontbasedir}/*/%{_fontstem}/ecl_cour.ttf


%package common
Group: System/Fonts/True type
Summary:  Common files of the A.colier Court font set

%description common
%common_desc

This package consists of files used by other %{oldname} packages.


%package -n fonts-ttf-ecolier-court-lignes
Group: System/Fonts/True type
Summary:  Schoolchildren cursive fonts with lines
Requires: %{name}-common = %{version}-%{release}

Obsoletes: %{oldname}-lignes < 20070702-7

%description -n fonts-ttf-ecolier-court-lignes
%common_desc

The A. lignes A. (lines) A.colier court font variant includes the Seyes lining
commonly used by schoolchildren notepads.

%files -n fonts-ttf-ecolier-court-lignes
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/ec_cour.ttf


%prep
%setup -q -c -T
iconv -f iso-8859-15 -t utf-8 %{SOURCE2} > lisez_moi.txt
touch -r %{SOURCE2} lisez_moi.txt
for txt in *.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done
install -m 0644 -p %{SOURCE3} .


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{SOURCE1} %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-lignes.conf

for fconf in %{fontconf}.conf \
             %{fontconf}-lignes.conf ; do
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
%doc *.txt


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070702-alt3_14
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070702-alt2_14
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20070702-alt2_13
- rebuild with new rpm-build-fonts

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 20070702-alt1_13
- initial release by fcimport

