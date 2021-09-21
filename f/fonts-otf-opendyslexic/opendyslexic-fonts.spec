Group: System/Fonts/True type
%define oldname opendyslexic-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname opendyslexic
%global fontconf 60-%{fontname}.conf
%global gitdate 20210904
%global gitrev e7ac50a

Name:		fonts-otf-opendyslexic
# This is the version from the compiled fonts (thanks fontforge)
Version:	0.940
Release:	alt1_1
Summary:	Font designed for dyslexics and high readability
License:	OFL
URL:		http://dyslexicfonts.com/
# No source tarballs that I could find, so we get it from github
# git clone https://github.com/antijingoist/opendyslexic
# tar cfj opendyslexic-20210904gite7ac50a.tar.bz2 opendyslexic
Source0:	%{fontname}-%{gitdate}git%{gitrev}.tar.bz2
Source1:	%{oldname}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Source44: import.info

%description
OpenDyslexic is a new open sourced font created to increase readability for 
readers with dyslexia. The typefaces includes regular, bold, italic and 
bold-italic styles. It is being updated continually and improved based on 
input from dyslexic users. 

%prep
%setup -q -n %{fontname}

%build
# Nothing to do here.

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p compiled/OpenDyslexic*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

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
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc README.md
%doc --no-dereference OFL.txt

%changelog
* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 0.940-alt1_1
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.600-alt1_9
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.600-alt1_5
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.600-alt1_4
- update to new release by fcimport

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.600-alt1_2
- initial fc import

