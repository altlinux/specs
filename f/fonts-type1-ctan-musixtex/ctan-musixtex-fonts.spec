%define oldname ctan-musixtex-fonts
%define fontname ctan-musixtex
%define archivename musixps-unix

Name:           fonts-type1-ctan-musixtex
Version:        1.13
Release:        alt2_5
Summary:        Type 1 versions of MusiXTeX fonts
Group:          System/Fonts/True type
License:        LPPL
URL:            http://tug.ctan.org/cgi-bin/ctanPackageInformation.py?id=musixtex-t1fonts
Source0:        http://tug.ctan.org/tex-archive/fonts/musixtex/ps-type1/%{archivename}.tar.gz
BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
This package provides Type 1 fonts (PFB format) for  MusiXTeX (musixtex). The
fonts are based on the original MetaFont sources, such as musix20.mf, which are 
distributed with MusiXTeX. The fonts provided here may be used to produce 
printer-independent PostScript files or PDF files.

%prep
%setup -q -n %{archivename}

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p pfb/*.pfb %{buildroot}%{_fontdir}
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
%{_fontbasedir}/*/%{_fontstem}/*.pfb
%doc CHANGES README
%dir %{_fontbasedir}/*/%{_fontstem}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.13-alt2_5
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_5
- update to new release by fcimport

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_4
- initial release by fcimport

