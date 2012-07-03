%define oldname iso8859-2-fonts
%global fontname iso8859-2

%global __mkfontdir umask 133;mkfontdir
%global catalogue        %{_sysconfdir}/X11/fontpath.d

Name: fonts-bitmap-iso8859-2
Version: 1.0
Release: alt2_26
License: MIT
# Upstream url http://www.biz.net.pl/images/ISO8859-2-bdf.tar.gz is dead now.
Source: ISO8859-2-bdf.tar.gz

Patch0: XFree86-ISO8859-2-1.0-redhat.patch
BuildArch: noarch
Group: System/Fonts/X11 bitmap
Summary: Central European language fonts for the X Window System
Buildrequires: xorg-font-utils
BuildRequires: fontpackages-devel
Requires: mkfontdir
Source44: import.info
 
%description
If you use the X Window System and you want to display Central
European fonts, you should install this package.

%package common
Group: System/Fonts/X11 bitmap
Summary:        Common files of %{oldname}

%description common
Common files of %{oldname}.

%package -n fonts-bitmap-iso8859-2-misc
Group: System/Fonts/X11 bitmap
Summary: A set of misc Central European language fonts for X
Requires: mkfontdir
Obsoletes: fonts-ISO8859-2 < 1.0-23
Provides: fonts-ISO8859-2 = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-bitmap-iso8859-2-misc
This package contains a set of Central European fonts, in
compliance with the ISO8859-2 standard.

%package -n fonts-bitmap-iso8859-2-75dpi
Group: System/Fonts/X11 bitmap
Summary: A set of 75dpi Central European language fonts for X
Requires: mkfontdir
Obsoletes: fonts-ISO8859-2-75dpi < 1.0-23
Provides: fonts-ISO8859-2-75dpi = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-bitmap-iso8859-2-75dpi
This package contains a set of Central European language fonts in 75 dpi
resolution for the X Window System. 


%package -n fonts-bitmap-iso8859-2-100dpi
Group: System/Fonts/X11 bitmap
Summary: A set of 100dpi Central European language fonts for X
Requires: mkfontdir
Obsoletes: fonts-ISO8859-2-100dpi < 1.0-23
Provides: fonts-ISO8859-2-100dpi = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-bitmap-iso8859-2-100dpi
This package includes Central European (ISO8859-2) fonts, in 100 dpi
resolution, for the X Window System.


%prep
%setup -c -q
chmod 644 RELEASE_NOTES.TXT

%patch0 -p1 -b .redhat

%build
make all

%install
make install PREFIX=$RPM_BUILD_ROOT \
           FONTDIR=$RPM_BUILD_ROOT%{_fontdir}

# Install catalogue symlink
mkdir -p $RPM_BUILD_ROOT%{catalogue}
ln -sf %{_fontdir}/misc $RPM_BUILD_ROOT%{catalogue}/%{fontname}-misc-fonts
ln -sf %{_fontdir}/75dpi $RPM_BUILD_ROOT%{catalogue}/%{fontname}-75dpi-fonts
ln -sf %{_fontdir}/100dpi $RPM_BUILD_ROOT%{catalogue}/%{fontname}-100dpi-fonts
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

%post -n fonts-bitmap-iso8859-2-misc
{
    %__mkfontdir %{_fontdir}/misc
} &> /dev/null || :

%post -n fonts-bitmap-iso8859-2-75dpi
{
    %__mkfontdir %{_fontdir}/75dpi
} &> /dev/null || :

%post -n fonts-bitmap-iso8859-2-100dpi
{
    %__mkfontdir %{_fontdir}/100dpi
} &> /dev/null || :


%files -n fonts-bitmap-iso8859-2-misc
%doc
%dir %{_fontbasedir}/*/%{_fontstem}/misc
%{_fontbasedir}/*/%{_fontstem}/misc/*.gz
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/misc/fonts.alias
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/misc/fonts.dir
%{catalogue}/%{fontname}-misc*

%files -n fonts-bitmap-iso8859-2-75dpi
%doc
%dir %{_fontbasedir}/*/%{_fontstem}/75dpi
%{_fontbasedir}/*/%{_fontstem}/75dpi/*.gz
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/75dpi/fonts.alias
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/75dpi/fonts.dir
%{catalogue}/%{fontname}-75dpi*

%files -n fonts-bitmap-iso8859-2-100dpi
%doc
%dir %{_fontbasedir}/*/%{_fontstem}/100dpi
%{_fontbasedir}/*/%{_fontstem}/100dpi/*.gz
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/100dpi/fonts.alias
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/100dpi/fonts.dir
%{catalogue}/%{fontname}-100dpi*

%files common
%doc *.TXT
%dir %{_fontbasedir}/*/%{_fontstem}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_26
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_26
- update to new release by fcimport

* Wed Aug 31 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_25
- new release by fcimport

