Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname adobe-source-han-sans-cn-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname adobe-source-han-sans-cn
%global fontconf 65-2-%{fontname}.conf

%global archivename SourceHanSansCN

Name:           fonts-otf-adobe-source-han-sans-cn
Version:        2.004
Release:        alt1_1
Summary:        Adobe OpenType Pan-CJK font family for Simplified Chinese

License:        OFL
URL:            https://github.com/adobe-fonts/source-han-sans/
Source0:        https://github.com/adobe-fonts/source-han-sans/releases/latest/download/%{archivename}.zip
Source1:        %{oldname}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
Source Han Sans is a sans serif Pan-CJK font family 
that is offered in seven weightsa..ExtraLight, Light, 
Normal, Regular, Medium, Bold, and Heavya..and 
in several OpenType/CFF-based deployment configurations
to accommodate various system requirements or limitations.

As the name suggests, Pan-CJK fonts are intended to
support the characters necessary to render or
display text in Simplified Chinese, Traditional Chinese,
Japanese, and Korean.


%prep
%setup -n %{oldname}-%{version} -q -c


%build


%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p SubsetOTF/CN/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
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
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/*.otf

%doc --no-dereference LICENSE.txt


%changelog
* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 2.004-alt1_1
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 2.002-alt1_1
- update to new release by fcimport

* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 2.001-alt1_1
- update to new release by fcimport

* Sun Jan 27 2019 Igor Vlasenko <viy@altlinux.ru> 2.000-alt1_1
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_8
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_6
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_5
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_2
- update to new release by fcimport

* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_1
- new version

