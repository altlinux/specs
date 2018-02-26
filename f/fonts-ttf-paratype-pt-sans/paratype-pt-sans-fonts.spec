# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname paratype-pt-sans-fonts
%global fontname paratype-pt-sans
%global fontconf 57-%{fontname}

%global archivename PTSans.zip

%global common_desc \
The PT Sans family was developed as part of the a.'Public Types of Russian \
Federationa.' project. This project aims at enabling the peoples of Russia to \
read and write their native languages, using free/libre fonts. It is \
dedicated to the 300-year anniversary of the Russian civil type invented by \
Peter the Great from 1708 to 1710, and was realized with financial support \
from the Russian Federal Agency for Press and Mass Communications. \
\
The fonts include support for all 54 titleA. languages of the Russian \
Federation as well as more common Western, Central European and Cyrillic \
blocks making them unique and a very important tool for modern digital \
communications. \
\
PT Sans is a grotesque font based on Russian type designs of the second part \
of the 20th century. However, it also includes very distinctive features of \
modern humanistic design, fulfilling present day aesthetic and functional \
requirements. \
\
It was designed by Alexandra Korolkova, Olga Umpeleva and Vladimir Yefimov \
and released by ParaType. \
\
A. A a.'titlea.' language is named after an ethnic group.


Name:           fonts-ttf-paratype-pt-sans
Version:        20100408
Release:        alt3_3
Summary:        A pan-Cyrillic typeface

Group:          System/Fonts/True type
License:        OFL
URL:            http://www.paratype.com/public/
Source0:        http://www.fontstock.com/public/PTSans_OFL.zip
Source10:       %{oldname}-fontconfig.conf
Source11:       %{oldname}-caption-fontconfig.conf


BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
%common_desc

This package includes the four basic styles and two narrows styles for
economic setting.

%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/PTS*.ttf
%{_fontbasedir}/*/%{_fontstem}/PTN*.ttf
%doc *.txt


%package -n fonts-ttf-paratype-pt-sans-caption
Group: System/Fonts/True type
Summary:        A pan-Cyrillic typeface (caption forms for small text)
BuildRequires:  fontpackages-devel

%description -n fonts-ttf-paratype-pt-sans-caption
%common_desc

This package includes 2 captions styles for small text sizes.

%files -n fonts-ttf-paratype-pt-sans-caption
%{_fontconfig_templatedir}/%{fontconf}-caption.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-caption.conf
%{_fontbasedir}/*/%{_fontstem}/PTC*.ttf
%doc *.txt


%prep
%setup -q -c

for txt in *.txt ; do
   if $(echo "$txt" | grep -q "rus\.txt") ; then
     iconv --from=UTF-16       --to=UTF-8 "$txt" > "$txt.1"
   else
     iconv --from=WINDOWS-1251 --to=UTF-8 "$txt" > "$txt.1"
   fi
   sed -i 's/\r//' "$txt.1"
   touch -r "$txt" "$txt.1"
   mv "$txt.1" "$txt"
done


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE10} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-caption.conf

for fconf in %{fontconf}.conf \
             %{fontconf}-caption.conf ; do
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


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100408-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100408-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20100408-alt2_2
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 20100408-alt1_2
- initial release by fcimport

