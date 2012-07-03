# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/xml2-config
# END SourceDeps(oneline)
Name:           kanatest
Version:        0.4.8
Release:        alt2_8
Summary:        Hiragana and Katakana drill tool

Group:          Games/Other
License:        GPLv2+
URL:            http://clayo.org/kanatest/
Source0:        http://clayo.org/kanatest/%{name}-%{version}.tar.gz

# Already fixed upstream, backported until new release is published
Patch1:         kanatest-0.4.8-gtkfixes.patch


BuildRequires:  desktop-file-utils >= 0.9
BuildRequires:  libgtk+2-devel >= 2.0
BuildRequires:  libxml2-devel
BuildRequires:  gettext
Requires:       fontlang(ja)
Requires:       icon-theme-hicolor
Source44: import.info

%description
Kanatest is a simple, GTK 2-based kana drill tool. It offers three drill modes:
hiragana, katakana, and mixed mode. The tester shows random kana characters
and waits until you enter the romaji equivalent in an entry field. At the end,
statistics are provided

%prep
%setup -q
%patch1 -p1 -b gtkfixes


%build
export PLATFORM_CFLAGS="$RPM_OPT_FLAGS"
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
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


%files -f %{name}.lang
%doc README COPYING ChangeLog
%{_bindir}/kanatest
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/kanatest.png
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/22x22/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/scalable/apps/*


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_8
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_7
- update to new release by fcimport

* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_6
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_5
- initial release by fcimport

