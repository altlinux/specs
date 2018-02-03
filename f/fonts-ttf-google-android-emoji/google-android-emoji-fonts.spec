Group: System/Fonts/True type
%define oldname google-android-emoji-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name google-android-emoji-fonts
%global fontname google-android-emoji
%global checkout 20120228git
%global archivename %{oldname}-%{checkout}

Name:    fonts-ttf-google-android-emoji
# No sane versionning upstream, use git clone timestamp
Version: 1.01
Release: alt1_0.8.%{checkout}
Summary: Android Emoji font released by Google

License:   ASL 2.0
URL:       https://android.googlesource.com/platform/frameworks/base.git/+/jb-release/data/fonts/
Source0:   %{archivename}.tar.xz
Source1:   get-source-from-git.sh
Source2:   AndroidEmoji.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info


%description
The Android Emoji typeface contains a number of pictographs and smileys,
popularly used in instant messages and chat forums.  The style of the
typeface is playful.  It is taken from Google's Android Jelly Bean
mobile phone operating system.


%prep
%setup -q -n %{archivename}


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p AndroidEmoji.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/appdata
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
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/*.ttf
%doc README.txt NOTICE
%{_datadir}/appdata/AndroidEmoji.metainfo.xml


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_0.8.20120228git
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_0.7.20120228git
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_0.3.20120228git
- update to new release by fcimport

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_0.2.20120228git
- converted for ALT Linux by srpmconvert tools

