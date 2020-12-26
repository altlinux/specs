# BEGIN SourceDeps(oneline):
BuildRequires: unzip zip
# END SourceDeps(oneline)
%define oldname larabie-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontname larabie

%define common_desc \
Larabie Fonts offer hundreds of free fonts for personal and commercial use in\
TrueType format. They consist of three collections: "decorative", "straight",\
"uncommon" fonts, created by Ray Larabie.

Summary:       A Collection of High Quality TrueType Fonts
Name:          fonts-ttf-larabie
Version:       0
Release:       alt1_0.17.20011216
License:       Larabie Fonts License
Group:         System/Fonts/True type
URL:           http://www.larabiefonts.com/
# Although all the fonts in this tarball can be downloaded
# one-by-one from the above website, the website does not
# offer a collective file of fonts. This tarball provides a 
# good collection and is borrowed from Ubuntu:
# File downloaded from:
# https://launchpad.net/ubuntu/jaunty/+source/ttf-larabie/1:20011216-1.1
Source0:       ttf-%{fontname}_20011216.orig.tar.gz
# This file sorts the fonts into families. Extracted from the build
# scripts of Ubuntu (same location as above):
Source1:       %{oldname}.sort
BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
%common_desc

%package -n fonts-ttf-larabie-common
Summary:       Common files for %{oldname}
Group:         System/Fonts/True type

%description -n fonts-ttf-larabie-common
%common_desc

This package consists of files used by other %{oldname} packages.

%package -n fonts-ttf-larabie-decorative
Summary:       Larabie TrueType Decorative Fonts
Group:         System/Fonts/True type
Requires:      %{name}-common = %{version}-%{release}
Obsoletes:     %{fontname}-fonts-deco < 0-0.3.20011216

%description -n fonts-ttf-larabie-decorative
%common_desc

This package contains the "decorative" ones of his fonts, which are great for 
headlines and other decorations.

%package -n fonts-ttf-larabie-straight
Summary:       Larabie TrueType Straight Fonts
Group:         System/Fonts/True type
Requires:      %{name}-common = %{version}-%{release}
Obsoletes:     %{fontname}-fonts-straight < 0-0.3.20011216

%description -n fonts-ttf-larabie-straight
%common_desc

This package contains the "straight"er ones of his fonts, which are suitable 
for everyday use. 

%package -n fonts-ttf-larabie-uncommon
Summary:       Larabie TrueType Uncommon Fonts
Group:         System/Fonts/True type
Requires:      %{name}-common = %{version}-%{release}
Obsoletes:     %{fontname}-fonts-uncommon < 0-0.3.20011216

%description -n fonts-ttf-larabie-uncommon
%common_desc

This package contains less common fonts which are beautiful for special 
decorations and headlines.


%prep
%setup -q -n ttf-%{fontname}-20011216

SORTFILE=%{SOURCE1}
groups=`cut -f2 $SORTFILE | sort -u`
basedir=`pwd`

#
# Create Directories for fonts
#
for group in $groups; do
        if [ ! -d $group ]; then
                mkdir $group
        fi
done

#
# Extract font .zip files
#
for nam in *.zip; do
        group=`grep "^$nam[[:space:]]" $SORTFILE | cut -f2`
        if [ -z $group ]; then
                echo Font $nam is unsorted.
        else
                unzip -j -L -u -qq $nam -d $group -x read_me.txt
        fi
done

#
# Rename some problematic files
#
mv deco/let*seat.ttf deco/let_seat.ttf
mv uncommon/chr*32*.ttf uncommon/chr32.ttf

#
# Fix permission and EOL encoding issues.
#
for txtfile in straight/*.txt uncommon/*.txt; do
  sed 's/\r//' "$txtfile" > tmpfile
  touch -r "$txtfile" tmpfile
  mv -f tmpfile "$txtfile"
done

%build
echo "Nothing to build."


%install
# fonts
install -m 0755 -d              %{buildroot}%{_fontdir}/decorative
install -m 0755 -d              %{buildroot}%{_fontdir}/straight
install -m 0755 -d              %{buildroot}%{_fontdir}/uncommon
install -pm 0644 deco/*.ttf     %{buildroot}%{_fontdir}/decorative
install -pm 0644 straight/*.ttf %{buildroot}%{_fontdir}/straight
install -pm 0644 uncommon/*.ttf %{buildroot}%{_fontdir}/uncommon
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

%files -n fonts-ttf-larabie-common
%doc READ_ME.TXT
%dir %{_fontbasedir}/*/%{_fontstem}


%files -n fonts-ttf-larabie-decorative
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/decorative/*.ttf
%dir %{_fontbasedir}/*/%{_fontstem}/decorative

%files -n fonts-ttf-larabie-straight
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/straight/*.ttf
%doc straight/*.txt
%dir %{_fontbasedir}/*/%{_fontstem}/straight

%files -n fonts-ttf-larabie-uncommon
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/uncommon/*.ttf
%doc uncommon/*.txt
%dir %{_fontbasedir}/*/%{_fontstem}/uncommon

%changelog
* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.17.20011216
- update to new release by fcimport

* Wed Feb 26 2020 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.16.20011216
- update to new release by fcimport

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.15.20011216
- update to new release by fcimport

* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.14.20011216
- update to new release by fcimport

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.13.20011216
- new version

