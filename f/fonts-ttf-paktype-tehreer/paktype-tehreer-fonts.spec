%define oldname paktype-tehreer-fonts
%define fontname paktype-tehreer
%define fontconf 67-paktype
%define fontdir %{_datadir}/fonts/%{fontname}

Name:	fonts-ttf-paktype-tehreer
Version:     2.0
Release:     alt3_12
Summary:     Fonts for Arabic from PakType
Group:		System/Fonts/True type
License:     GPLv2 with exceptions
URL:		https://sourceforge.net/projects/paktype/
Source0:     http://downloads.sourceforge.net/project/paktype/Tehreer-2.0.tar.gz
Source1:	%{fontconf}-tehreer.conf
BuildArch:   noarch
BuildRequires:	fontpackages-devel
Obsoletes: paktype-fonts-common < %{version}i-%{release}
Source44: import.info

%description 
The paktype-tehreer-fonts package contains fonts for the display of \
Arabic from the PakType by Lateef Sagar.

%prep
%setup -q -c
rm -rf Tehreer-2.0/Project\ files/
# get rid of the white space (' ')
mv Tehreer-2.0/Ready*/PakType\ Tehreer.ttf PakType_Tehreer.ttf
mv Tehreer-2.0/License\ files/PakType\ Tehreer\ License.txt PakType_Tehreer_License.txt

%{__sed} -i 's/\r//' PakType_Tehreer_License.txt

for txt in Tehreer-2.0/Readme.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\x92//g' $txt.new
   sed -i 's/\x93//g' $txt.new
   sed -i 's/\x94//g' $txt.new
   sed -i 's/\x96//g' $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done

%build
echo "Nothing to do in Build."

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p PakType_Tehreer.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-tehreer.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}-tehreer.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}-tehreer.conf
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
%{_fontconfig_templatedir}/%{fontconf}-tehreer.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-tehreer.conf
%{_fontbasedir}/*/%{_fontstem}/PakType_Tehreer.ttf

%doc PakType_Tehreer_License.txt Tehreer-2.0/Readme.txt

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_12
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_12
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_11
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_11
- initial release by fcimport

