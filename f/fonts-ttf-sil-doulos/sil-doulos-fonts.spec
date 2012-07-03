# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname sil-doulos-fonts
%define fontname sil-doulos
%define archivename DoulosSIL
%define docversion 4.100

Name:           fonts-ttf-sil-doulos
Version:        4.104
Release:        alt3_7
Summary:        Doulos SIL fonts

Group:          System/Fonts/True type
License:        OFL
URL:            http://scripts.sil.org/DoulosSILFont
Source0:        %{archivename}%{version}.zip

BuildArch:      noarch
BuildRequires:  fontpackages-devel

# Obsoleting and providing the old RPM name
Obsoletes:      doulos-fonts < 4.104-2
Source44: import.info

%description
Doulos SIL provides glyphs for a wide range of Latin and Cyrillic
characters. Doulos's design is similar to the design of the Times-like
fonts, but only has a single regular face. It is intended for use alongside
other Times-like fonts where a range of styles (italic, bold) are not
needed.


%prep
%setup -q -n %{archivename}
sed -i 's/\r$//' *.txt


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
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
%{_fontbasedir}/*/%{_fontstem}/*.ttf

%doc FONTLOG.txt OFL.txt OFL-FAQ.txt README.txt
%doc DoulosSIL%{docversion}FontDocumentation.pdf

%dir %{_fontbasedir}/*/%{_fontstem}


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.104-alt3_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.104-alt2_7
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 4.104-alt2_6
- rebuild with new rpm-build-fonts

* Thu Aug 04 2011 Igor Vlasenko <viy@altlinux.ru> 4.104-alt1_6
- initial release by fcimport

