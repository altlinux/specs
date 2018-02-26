# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname adf-accanthis-fonts
%global fontname adf-accanthis
%global fontconf 60-%{fontname}

%global archivename Accanthis-Std

%global common_desc \
A latin typeface published by Hirwen Harendal's Arkandis Digital Foundry, \
Accanthis was inspired from the a.'Cloister Oldstylea.' typeface found in the \
a.'American Specimen Book of Typefaces Suplementa.'. Its medium contrast is \
sufficient to be reader-frendly and deliver a elegant and refined experience.\
\
Its creator considers it as a a.'modernizeda.' garaldic typeface. \
\
Accanthis is well suited to book typesetting and refined presentations.


Name:      fonts-otf-adf-accanthis
# Use the main PS version (as documented in NOTICE)
Version:   1.6
Release:   alt3_6
Summary:   A a.'modernizeda.' garaldic serif typeface, a.'Galliarda.' alternative

Group:     System/Fonts/True type
License:   GPLv2+ with exceptions
URL:       http://arkandis.tuxfamily.org/adffonts.html
Source0:   http://arkandis.tuxfamily.org/fonts/%{archivename}.zip
Source1:   http://arkandis.tuxfamily.org/docs/Accanthis-Cat.pdf
Source11:  %{oldname}-fontconfig.conf
Source12:  %{oldname}-fontconfig-2.conf
Source13:  %{oldname}-fontconfig-3.conf


BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
%common_desc

It is intended to serve as alternative to the a.'Galliarda.' typeface.

%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/AccanthisADFStd-*.otf


%package common
Group: System/Fonts/True type
Summary:  Common files of %{oldname}

%description common
%common_desc

This package consists of files used by other %{oldname} packages.


%package -n fonts-ttf-adf-accanthis-2
Group: System/Fonts/True type
Summary:  A a.'modernizeda.' garaldic serif, a.'Horley old stylea.' alternative
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-adf-accanthis-2
%common_desc

This variant is closer to the a.'Horley old stylea.' typeface than the original \
version.

%files -n fonts-ttf-adf-accanthis-2
%{_fontconfig_templatedir}/%{fontconf}-2.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-2.conf
%{_fontbasedir}/*/%{_fontstem}/AccanthisADFStdNo2-*.otf


%package -n fonts-ttf-adf-accanthis-3
Group: System/Fonts/True type
Summary:  A a.'modernizeda.' garaldic serif typeface
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-adf-accanthis-3
%common_desc

This variant remixes a slightly modified Accanthis nA.2 with elements from the
original Italic and changes to k, p, z and numbers.


%files -n fonts-ttf-adf-accanthis-3
%{_fontconfig_templatedir}/%{fontconf}-3.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-3.conf
%{_fontbasedir}/*/%{_fontstem}/AccanthisADFStdNo3-*.otf


%prep
%setup -q -n %{archivename}
install -m 0644 -p %{SOURCE1} .
for txt in NOTICE */COPYING ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p OTF/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE12} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-2.conf
install -m 0644 -p %{SOURCE13} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-3.conf

for fconf in %{fontconf}.conf \
             %{fontconf}-2.conf \
             %{fontconf}-3.conf ; do
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
%doc NOTICE OTF/COPYING *.pdf


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt3_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2_6
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2_5
- rebuild with new rpm-build-fonts

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_5
- initial release by fcimport

