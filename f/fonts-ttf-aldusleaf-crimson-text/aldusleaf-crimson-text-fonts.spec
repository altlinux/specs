# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname aldusleaf-crimson-text-fonts
%global fontname aldusleaf-crimson-text
%global fontconf 62-%{fontname}.conf

Name:           fonts-ttf-aldusleaf-crimson-text
Version:        0.1
Release:        alt3_0.4.20100628
Summary:        A latin font for the production of technical books and papers

Group:          System/Fonts/True type
License:        OFL
URL:            http://aldusleaf.org/
Source0:        http://aldusleaf.org/crimson_text_100628.zip
Source1:        %{oldname}-fontconfig.conf
Source2:        generate.pe

BuildArch:      noarch
BuildRequires:  fontpackages-devel fontforge
Obsoletes:      crimson-text-fonts < 0-0.2.20100523
Source44: import.info

%description
A latin font for a quality typeface for the production of books and
papers, particularly technical ones.


%prep
%setup -q -n crimson_text
cp -p %{SOURCE2} fontforge_sources

%build
pushd fontforge_sources
./generate.pe *.sfd
popd

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fontforge_sources/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
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

%doc README.txt 


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_0.4.20100628
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_0.4.20100628
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_0.3.20100628
- rebuild with new rpm-build-fonts

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_0.3.20100628
- initial release by fcimport

