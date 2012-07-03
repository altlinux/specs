# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname nafees-web-naskh-fonts
%global fontname        nafees-web-naskh
%global fontconf        67-%{fontname}.conf
%global archivename     NafeesWeb
%global archivedate     20080509

Name:           fonts-ttf-nafees-web-naskh
Version:        1.2
Release:        alt3_8
Summary:        Nafees Web font for writing Urdu in the Naskh script 

Group:          System/Fonts/True type
License:        Bitstream Vera
URL:            http://www.crulp.org/Downloads/NafeesWeb.zip

## NOTE: the original archive is unversioned, so we rename it to add a date stamp
# The Source0 is obtained by doing the following:
# $ wget -S http://www.crulp.org/Downloads/NafeesWeb.zip
# $ mv %{archivename}.zip %{fontname}-%{archivedate}.zip
Source0:        %{fontname}-%{archivedate}.zip

## Fix RHBZ# while not fixed upstream
Source1:        %{fontname}-update-preferred-family.pe
Source2:        %{fontconf}

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  fontforge
Source44: import.info

%description

Character based Nafees Web Naskh Open Type Font for writing Urdu in Naskh
script based on Unicode standard. This version has complete support of
Aerabs for Urdu and updated glyphs for Latin characters.
Nafees Web Naskh OTF contains approximately 330 glyphs, including 5 ligatures.


%prep
%setup -q -c

%build
# Fix RHBZ#490830 while not fixed upstream
%{_bindir}/fontforge %{SOURCE1} %{archivename}.ttf

%install

#fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
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
%{_fontbasedir}/*/%{_fontstem}/*.ttf

%doc


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_8
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_8
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_7
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_7
- initial release by fcimport

