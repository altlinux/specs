%define oldname kacst-fonts
%define fontname kacst
%define fontdir %{_datadir}/fonts/%{fontname}
%define	fontconf	67-%{fontname}

# Common description
%define common_desc \
This package contains fonts for the display of Arabic \
from the King Abdulaziz City for Science & Technology(kacst).

Name: fonts-ttf-kacst
Version: 2.0
Release: alt3_9
License: GPLv2
Source: http://downloads.sourceforge.net/sourceforge/arabeyes/%{fontname}_fonts_%{version}.tar.bz2
Source1: %{fontconf}-art.conf
Source2: %{fontconf}-book.conf
Source3: %{fontconf}-decorative.conf
Source4: %{fontconf}-digital.conf
Source5: %{fontconf}-farsi.conf
Source6: %{fontconf}-letter.conf
Source7: %{fontconf}-naskh.conf
Source8: %{fontconf}-office.conf
Source9: %{fontconf}-one.conf
Source10: %{fontconf}-pen.conf
Source11: %{fontconf}-poster.conf
Source12: %{fontconf}-qurn.conf
Source13: %{fontconf}-screen.conf
Source14: %{fontconf}-title.conf
Source15: %{fontconf}-titlel.conf

BuildArch: noarch
BuildRequires:	dos2unix
BuildRequires:	fontpackages-devel > 1.13
Group: System/Fonts/True type
Obsoletes: fonts-arabic <= 2.1-2
Summary: Fonts for arabic from arabeyes project 
URL: http://www.arabeyes.org/resources.php
Source44: import.info
 
%description
%common_desc

%package common
Summary:  Common files for kacst-fonts
Group:	System/Fonts/True type

%description common
%common_desc

%package -n fonts-ttf-kacst-book
Summary: Fonts for arabic from arabeyes project 
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0-3
%description -n fonts-ttf-kacst-book
This package contains book type fonts for the display of Arabic 

%files -n fonts-ttf-kacst-book
%{_fontconfig_templatedir}/%{fontconf}-book*
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-book*
%{_fontbasedir}/*/%{_fontstem}/KacstBook.ttf

%package -n fonts-ttf-kacst-digital
Summary: Fonts for arabic from arabeyes project 
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0-3
%description -n fonts-ttf-kacst-digital
This package contains digital type fonts for the display of Arabic 

%files -n fonts-ttf-kacst-digital
%{_fontconfig_templatedir}/%{fontconf}-digital*
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-digital*
%{_fontbasedir}/*/%{_fontstem}/KacstDigital.ttf

%package -n fonts-ttf-kacst-letter
Summary: Fonts for arabic from arabeyes project 
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0-3
%description -n fonts-ttf-kacst-letter
This package contains book kacst fonts for the display of Arabic 

%files -n fonts-ttf-kacst-letter
%{_fontconfig_templatedir}/%{fontconf}-letter*
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-letter*
%{_fontbasedir}/*/%{_fontstem}/KacstLetter.ttf

%package -n fonts-ttf-kacst-office
Summary: Fonts for arabic from arabeyes project 
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0-3
%description -n fonts-ttf-kacst-office
This package contains office type fonts for the display of Arabic 

%files -n fonts-ttf-kacst-office
%{_fontconfig_templatedir}/%{fontconf}-office*
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-office*
%{_fontbasedir}/*/%{_fontstem}/KacstOffice.ttf

%package -n fonts-ttf-kacst-pen
Summary: Fonts for arabic from arabeyes project 
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0-3
%description -n fonts-ttf-kacst-pen
This package contains pen type fonts for the display of Arabic 

%files -n fonts-ttf-kacst-pen
%{_fontconfig_templatedir}/%{fontconf}-pen*
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-pen*
%{_fontbasedir}/*/%{_fontstem}/kacstPen.ttf

%package -n fonts-ttf-kacst-qurn
Summary: Fonts for arabic from arabeyes project 
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0-3
%description -n fonts-ttf-kacst-qurn
This package contains qurn type fonts for the display of Arabic 

%files -n fonts-ttf-kacst-qurn
%{_fontconfig_templatedir}/%{fontconf}-qurn*
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-qurn*
%{_fontbasedir}/*/%{_fontstem}/KacstQurn.ttf

%package -n fonts-ttf-kacst-titlel
Summary: Fonts for arabic from arabeyes project 
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0-3
%description -n fonts-ttf-kacst-titlel
This package contains title large type fonts for the display of Arabic 

%files -n fonts-ttf-kacst-titlel
%{_fontconfig_templatedir}/%{fontconf}-titlel.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-titlel.conf
%{_fontbasedir}/*/%{_fontstem}/KacstTitleL.ttf

%package -n fonts-ttf-kacst-art
Summary: Fonts for arabic from arabeyes project 
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0-3
%description -n fonts-ttf-kacst-art
This package contains art type fonts for the display of Arabic 

%files -n fonts-ttf-kacst-art
%{_fontconfig_templatedir}/%{fontconf}-art*
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-art*
%{_fontbasedir}/*/%{_fontstem}/KacstArt.ttf

%package -n fonts-ttf-kacst-decorative
Summary: Fonts for arabic from arabeyes project 
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0-3
%description -n fonts-ttf-kacst-decorative
This package contains decorative type fonts for the display of Arabic 

%files -n fonts-ttf-kacst-decorative
%{_fontconfig_templatedir}/%{fontconf}-decorative*
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-decorative*
%{_fontbasedir}/*/%{_fontstem}/KacstDecorative.ttf

%package -n fonts-ttf-kacst-farsi
Summary: Fonts for arabic from arabeyes project 
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0-3
%description -n fonts-ttf-kacst-farsi
This package contains farsi type fonts for the display of Arabic 

%files -n fonts-ttf-kacst-farsi
%{_fontconfig_templatedir}/%{fontconf}-farsi*
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-farsi*
%{_fontbasedir}/*/%{_fontstem}/KacstFarsi.ttf

%package -n fonts-ttf-kacst-naskh
Summary: Fonts for arabic from arabeyes project 
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0-3
%description -n fonts-ttf-kacst-naskh
This package contains naskh type fonts for the display of Arabic 

%files -n fonts-ttf-kacst-naskh
%{_fontconfig_templatedir}/%{fontconf}-naskh*
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-naskh*
%{_fontbasedir}/*/%{_fontstem}/KacstNaskh.ttf

%package -n fonts-ttf-kacst-one
Summary: Fonts for arabic from arabeyes project 
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0-3
%description -n fonts-ttf-kacst-one
This package contains one type fonts for the display of Arabic 

%files -n fonts-ttf-kacst-one
%{_fontconfig_templatedir}/%{fontconf}-one*
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-one*
%{_fontbasedir}/*/%{_fontstem}/KacstOne.ttf

%package -n fonts-ttf-kacst-poster
Summary: Fonts for arabic from arabeyes project 
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0-3
%description -n fonts-ttf-kacst-poster
This package contains poster type fonts for the display of Arabic 

%files -n fonts-ttf-kacst-poster
%{_fontconfig_templatedir}/%{fontconf}-poster*
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-poster*
%{_fontbasedir}/*/%{_fontstem}/KacstPoster.ttf

%package -n fonts-ttf-kacst-screen
Summary: Fonts for arabic from arabeyes project 
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0-3
%description -n fonts-ttf-kacst-screen
This package contains screen type fonts for the display of Arabic 

%files -n fonts-ttf-kacst-screen
%{_fontconfig_templatedir}/%{fontconf}-screen*
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-screen*
%{_fontbasedir}/*/%{_fontstem}/KacstScreen.ttf

%package -n fonts-ttf-kacst-title
Summary: Fonts for arabic from arabeyes project 
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0-3
%description -n fonts-ttf-kacst-title
This package contains title type fonts for the display of Arabic 

%files -n fonts-ttf-kacst-title
%{_fontconfig_templatedir}/%{fontconf}-title.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-title.conf
%{_fontbasedir}/*/%{_fontstem}/KacstTitle.ttf


%prep
%setup -q -n KacstArabicFonts-%{version}
find . -not -name \*.ttf -type f -exec dos2unix -k {} \;

%build
echo "Nothing to do in Build."

%install

install -m 0755 -d %{buildroot}%{fontdir}
install -m 0644 -p *.ttf %{buildroot}%{fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-art.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-book.conf
install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-decorative.conf
install -m 0644 -p %{SOURCE4} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-digital.conf
install -m 0644 -p %{SOURCE5} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-farsi.conf
install -m 0644 -p %{SOURCE6} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-letter.conf
install -m 0644 -p %{SOURCE7} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-naskh.conf
install -m 0644 -p %{SOURCE8} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-office.conf
install -m 0644 -p %{SOURCE9} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-one.conf
install -m 0644 -p %{SOURCE10} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pen.conf
install -m 0644 -p %{SOURCE11} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-poster.conf
install -m 0644 -p %{SOURCE12} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-qurn.conf
install -m 0644 -p %{SOURCE13} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-screen.conf
install -m 0644 -p %{SOURCE14} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-title.conf
install -m 0644 -p %{SOURCE15} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-titlel.conf

for fconf in %{fontconf}-art.conf \
		%{fontconf}-book.conf \
		%{fontconf}-decorative.conf \
		%{fontconf}-digital.conf \
		%{fontconf}-farsi.conf \
		%{fontconf}-letter.conf \
		%{fontconf}-naskh.conf \
		%{fontconf}-office.conf \
		%{fontconf}-one.conf \
		%{fontconf}-pen.conf \
		%{fontconf}-poster.conf \
		%{fontconf}-qurn.conf \
		%{fontconf}-screen.conf \
		%{fontconf}-title.conf \
		%{fontconf}-titlel.conf ; do
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


%files common
%doc Copyright LICENSE README

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_9
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_9
- update to new release by fcimport

* Thu Aug 25 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_8
- rebuild woth new rpm-build-fonts

* Sun Aug 07 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_8
- initial release by fcimport

