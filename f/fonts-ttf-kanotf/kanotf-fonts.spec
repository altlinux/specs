# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname kanotf-fonts
%global fontname kanotf
%global fontconf 65-%{fontname}.conf
%global _subdir /fonts

Name:           fonts-ttf-kanotf
Version:        20050515
Release:        alt3_2
Summary:        OpenType Kannada fonts
Group:          System/Fonts/True type
License:        GPLv2
URL:            http://sourceforge.net/projects/brahmi/
Source0:        http://sourceforge.net/projects/brahmi/files/Brahmi%%20OpenType%%20Fonts/OpenType%%20font%%20for%%20Kannada%%20-%%20Kedgae%%20and%%20Mallige%%20Ver%%201.0/kanotf.zip
Source1:        %{oldname}-fontconfig.conf
BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
Consists of two Kannada open-type fonts named "Kedage" and "Mallige". 

%define debug_package %{nil}

%prep
%setup -q -n %{fontname}%{_subdir}
sed -i 's/\r//' ../readme.txt
%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.TTF %{buildroot}%{_fontdir}
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
%{_fontbasedir}/*/%{_fontstem}/*.TTF



%doc ../readme.txt ../gpl.txt

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20050515-alt3_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20050515-alt2_2
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20050515-alt2_1
- rebuild with new rpm-build-fonts

* Sun Aug 07 2011 Igor Vlasenko <viy@altlinux.ru> 20050515-alt1_1
- initial release by fcimport

