%define oldname baekmuk-bdf-fonts
BuildRequires: fontpackages-devel
%define fontname   baekmuk-bdf

%define fontdir      %{_datadir}/fonts/%{fontname}
%define catalogue    %{_sysconfdir}/X11/fontpath.d

Name:           fonts-bitmap-baekmuk
Version:        2.2
Release:        alt3_11
Summary:        Korean bitmap fonts

Group:          System/Fonts/True type
License:        Baekmuk
URL:            http://kldp.net/projects/baekmuk/
Source:  http://kldp.net/frs/download.php/1428/%{fontname}-%{version}.tar.gz
Patch0:	 baekmuk-bdf-fonts-fix-fonts-alias.patch
BuildArch:      noarch
BuildRequires:  xorg-font-utils
Source44: import.info

%description
This package provides the Korean Baekmuk bitmap fonts.


%prep
%setup -q -n %{fontname}-%{version}
%patch0 -p1 -b .fix-fonts-alias

%build
for file in bdf/*.bdf; do
    bdftopcf $file | gzip -9 > ${file%.bdf}.pcf.gz
done

%install

install -d $RPM_BUILD_ROOT%{fontdir}

# for bmp font
install -m 0644 bdf/*.pcf.gz $RPM_BUILD_ROOT%{fontdir}/
install -m 0444 bdf/fonts.alias $RPM_BUILD_ROOT%{fontdir}/

# for catalogue
install -d $RPM_BUILD_ROOT%{catalogue}
ln -sf ../../..%{fontdir} $RPM_BUILD_ROOT%{catalogue}/%{oldname}

mkfontdir $RPM_BUILD_ROOT%{fontdir} 

# convert Korean copyright file to utf8
iconv -f EUC-KR -t UTF-8 COPYRIGHT.ks > COPYRIGHT.ko
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
%define fontdir %{_datadir}/fonts/bitmap/%{_fontstem}
%doc COPYRIGHT COPYRIGHT.ko README
%dir %{fontdir}
%{fontdir}/*.gz
%{fontdir}/fonts.alias
%verify(not md5 size mtime) %{fontdir}/fonts.dir
%{catalogue}/*


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_11
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_11
- update to new release by fcimport

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_10
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_9
- rebuild with rpm-build-fonts alt3

* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_9
- initial release by fcimport

