%define oldname ucs-miscfixed-fonts
%global fontname ucs-miscfixed
%global fontconf 66-%{fontname}.conf

Name: fonts-bitmap-ucs-miscfixed
Version: 0.3
Release: alt1_8
License: Public Domain
URL: http://www.cl.cam.ac.uk/~mgk25/ucs-fonts.html
Source0: http://www.cl.cam.ac.uk/~mgk25/download/ucs-fonts.tar.gz
Source1: 66-ucs-miscfixed.conf
BuildArch: noarch
Group: System/Fonts/X11 bitmap
Summary: Selected set of bitmap fonts
BuildRequires: fontpackages-devel
BuildRequires: xorg-x11-font-utils
Source44: import.info

%description
The usc-fixed-fonts package provides bitmap fonts for
locations such as terminals.


%prep
%setup -q -c
rm helvR12.bdf

%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.bdf %{buildroot}%{_fontdir}

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
%{_fontbasedir}/*/%{_fontstem}/*.bdf

%doc README	

%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_8
- update to new fc release

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_7
- update to new release by fcimport

* Wed Aug 31 2011 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_6
- new release by fcimport

