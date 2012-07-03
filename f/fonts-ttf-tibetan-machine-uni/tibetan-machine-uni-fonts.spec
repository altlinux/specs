# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname tibetan-machine-uni-fonts
%define	fontname	tibetan-machine-uni

Name:		fonts-ttf-tibetan-machine-uni
Version:	1.901
Release:	alt3_8
Summary:	Tibetan Machine Uni font for Tibetan, Dzongkha and Ladakhi

Group:		System/Fonts/True type
# .ttf file now states GPLv3+ with fonts exceptions
License:	GPLv3+ with exceptions
URL:		http://www.thlib.org/tools/#wiki=/access/wiki/site/26a34146-33a6-48ce-001e-f16ce7908a6a/tibetan%%20machine%%20uni.html
Source0:	https://collab.itc.virginia.edu/access/content/group/26a34146-33a6-48ce-001e-f16ce7908a6a/Tibetan%%20fonts/Tibetan%%20Unicode%%20Fonts/TibetanMachineUnicodeFont.zip

BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	dos2unix
Source44: import.info

%description
Tibetan Machine Uni is an TrueType OpenType, Unicode font released by THDL
project. The font supports Tibetan, Dzongkha and Ladakhi in dbu-can script
with full support for the Sanskrit combinations found in chos skad text.

%prep
%setup -q -c

%build
# Empty build section

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

dos2unix -o gpl.txt
dos2unix -o ReadMe.txt
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
%doc gpl.txt ReadMe.txt

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.901-alt3_8
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.901-alt2_8
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.901-alt2_7
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.901-alt1_7
- initial release by fcimport

