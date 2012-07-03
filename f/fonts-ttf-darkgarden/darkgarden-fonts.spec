# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname darkgarden-fonts
# Due to changes in the Fedora legal environment, rpm spec files are now specifically listed as a "contribution" 
# in/to Fedora (refer to FPCA FAQ here: https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement ).
# Quote: 
# "Q. Are RPM spec files covered by the FPCA?
# A. Sure. They're a contribution, aren't they? :) Nevertheless, they are explicitly named as an example of a contribution, to clear up a past confusion."
# 
# As a result of this change, I have decided to specifically license all of my rpm spec files as GPLv2.
# See program source for a copy of this license.
# 

%global fontname darkgarden
%global fontconf 69-darkgarden.conf

Name:           fonts-ttf-darkgarden
Version:	1.1
Release:        alt3_13
Summary:	Dark Garden is a decorative outline font of unusual shape

Group:          System/Fonts/True type
License:        GPLv2
URL:            http://darkgarden.sourceforge.net/

Source0:        http://darkgarden.sourceforge.net/darkgarden-1.1.src.zip
Source1:        %{oldname}-fontconfig.conf


BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: fontforge >= 20061025-1
Source44: import.info

%description
Dark Garden is a decorative outline font of unusual shape.
The typeface is based on author's original hand drawings.
The letterform is complex, with all characters decorated
with spikes resembling thorns or flames, character spacing
is very dense. Such a theme makes it a great font for titles,
banners, logos etc. Due to the font's complicated form,
long text passages are not very legible, but short paragraphs
such as titles or lyrics / poetry look very well.

%prep
%setup -q -n darkgarden-1.1 %{SOURCE0}

%build
fontforge -lang=ff -c 'Open($1); Generate($2)' DarkGarden.sfd DarkGarden.ttf

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

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

%doc COPYING.txt
%doc README.txt
%doc COPYING-GPL.txt


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_13
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_13
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_12
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_12
- initial release by fcimport

