%define oldname apanov-edrip-fonts
%global fontname apanov-edrip
%global fontconf 61-%{fontname}.conf

%global archiveversion r6
%global archivename    edrip-src-%{archiveversion}
%global googlename     edrip

Name:    fonts-ttf-apanov-edrip
Version: 20100430
Release: alt2_4
Summary: A decorative contrast sans-serif font

Group:     System/Fonts/True type
License:   OFL
URL:       http://code.google.com/p/%{googlename}/

# Upstream has still not completed hosting switching
Source0:   ftp://ftp.dvo.ru/pub/Font/edrip/%{archivename}.tar.xz
#Source0:   http://%{googlename}.googlecode.com/files/%{archivename}.tar.xz
Source1:   %{oldname}-fontconfig.conf


BuildArch:     noarch
BuildRequires: fontforge xgridfit >= 2.2-4.a.20100725cvs.fc14
BuildRequires: fontpackages-devel
Source44: import.info

%description
Edrip font is a contrast sans-serif font. It is based on the Teams font
released on 2000 by TopTeam Co. Edrip contains symbols for basic Cyrillic and
Latin alphabets.


%prep
%setup -q -c

%build
make %{?_smp_mflags}

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *\.ttf %{buildroot}%{_fontdir}

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
%doc *.txt README

%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 20100430-alt2_4
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20100430-alt2_2
- rebuild with new rpm-build-fonts

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 20100430-alt1_2
- initial release by fcimport

