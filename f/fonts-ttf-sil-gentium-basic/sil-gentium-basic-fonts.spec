# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname sil-gentium-basic-fonts
%define fontname sil-gentium-basic
%define fontconf 59-%{fontname}

%define common_desc \
Gentium Basic and Gentium Book Basic are font families based on the\
original Gentium design, but with additional weights. Both families come \
with a complete regular, bold, italic and bold italic set of fonts. \
These "Basic" fonts support only the Basic Latin and Latin-1 Supplement \
Unicode ranges, plus a selection of the more commonly used extended Latin\
characters, with miscellaneous diacritical marks, symbols and punctuation.


Name: fonts-ttf-sil-gentium-basic
Version: 1.1
Release: alt3_7
Summary: SIL Gentium Basic font family

Group:     System/Fonts/True type
License:   OFL
URL:       http://scripts.sil.org/Gentium_Basic
Source0:   GentiumBasic_110.zip
Source1:   %{fontname}-fontconfig.conf
Source2:   %{fontname}-book-fontconfig.conf
BuildArch:     noarch
BuildRequires: fontpackages-devel

Requires: %{name}-common = %{version}-%{release}
Source44: import.info

%description
%common_desc

This is the base variant.

%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/GenBas*.ttf

%package common
Group: System/Fonts/True type
Summary:  Common files of %{fontname}

%description common
%common_desc

This package consists of files used by other %{fontname} packages.

%package  -n fonts-ttf-sil-gentium-basic-book
Group: System/Fonts/True type
Summary:  SIL Gentium Book Basic font family
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-sil-gentium-basic-book
%common_desc

The "Book" family is slightly heavier.

%files -n fonts-ttf-sil-gentium-basic-book
%{_fontconfig_templatedir}/%{fontconf}-book.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-book.conf
%{_fontbasedir}/*/%{_fontstem}/GenBkBas*.ttf


%prep
%setup -q -n "Gentium Basic 1.1"
for txt in *.txt ; do
        fold -s $txt > $txt.new
        sed -i 's/\r//' $txt.new
        touch -r $txt $txt.new
        mv $txt.new $txt
done

# Convert to UTF-8
iconv -f iso-8859-1 -t utf-8 GENTIUM-FAQ.txt -o GENTIUM-FAQ.txt_
touch -r GENTIUM-FAQ.txt GENTIUM-FAQ.txt_
mv GENTIUM-FAQ.txt_ GENTIUM-FAQ.txt

%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}


install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

install -m 0644 -p %{SOURCE2} \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-book.conf

for fconf in %{fontconf}.conf\
         %{fontconf}-book.conf ; do
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
%doc FONTLOG.txt GENTIUM-FAQ.txt OFL-FAQ.txt OFL.txt



%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_7
- rebuild to get rid of #27020

* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_7
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_6
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_6
- initial release by fcimport

