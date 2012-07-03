%define oldname knm-new-fixed-fonts
%global		priority	69
%global		fontname	knm-new-fixed
%global		fontconf	%{priority}-%{fontname}.conf
%global		catalogue	%{_sysconfdir}/X11/fontpath.d

Name:		fonts-bitmap-knm-new-fixed
Version:	1.1
Release:	alt4_15

Summary:	12x12 JIS X 0208 Bitmap fonts
Group:		System/Fonts/True type
License:	GPL+

## the following upstream URL is a dead link anymore.
#URL:		http://www.din.or.jp/~storm/fonts/
#Source0:	http://www.din.or.jp/~storm/fonts/knm_new.tar.gz
Source0:	knm_new.tar.gz
Source1:	%{oldname}-fontconfig.conf
BuildArch:	noarch
BuildRequires:	mkfontdir fontpackages-devel

Obsoletes:	knm_new <= 1.1-16 knm_new-fonts < 1.1-7
Source44: import.info

%description
This package provides 12x12 Japanese bitmap fonts for JIS X 0208.
The JIS X 0208 character set contains the most often used Kanji glyphs.


%prep
%setup -q -T -c -a 0

%build

%install

install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0755 -d $RPM_BUILD_ROOT%{catalogue}

install -m 0644 -p fonts/*.pcf.gz $RPM_BUILD_ROOT%{_fontdir}/

install -m 0755 -d	$RPM_BUILD_ROOT%{_fontconfig_templatedir}	\
			$RPM_BUILD_ROOT%{_fontconfig_confdir}
install -m 0644 -p	%{SOURCE1}	\
			$RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}

ln -s	%{_fontconfig_templatedir}/%{fontconf}	\
	$RPM_BUILD_ROOT%{_fontconfig_confdir}/%{fontconf}

mkfontdir $RPM_BUILD_ROOT%{_fontdir}

# Install catalogue symlink
ln -s -f %{_fontdir} $RPM_BUILD_ROOT%{catalogue}/%{fontname}
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
%{_fontbasedir}/*/%{_fontstem}/*.pcf.gz

%lang(ja) %doc fonts/readme fonts/changes
%doc fonts/gtkrc.sample
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/fonts.dir
%{catalogue}/*


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_15
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_15
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_14
- rebuild with new rpm-build-fonts

* Mon Aug 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_14
- initial release by fcimport

* Sun Aug 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_14
- initial release by fcimport

