# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           manaworld
Version:        0.5.2
Release:        alt3_9.1
Summary:        2D MMORPG world

Group:          Games/Other
License:        GPLv2+
URL:            http://themanaworld.org
Source0:        http://downloads.sourceforge.net/themanaworld/The%%20Mana%%20World/%{version}/tmw-%{version}.tar.bz2
Patch0:         manaworld-removeflagoverride.patch

Requires:       fonts-ttf-dejavu
BuildRequires:  libguichan-devel >= 0.8.1 desktop-file-utils libphysfs-devel
BuildRequires:  curl-devel libxml2-devel libpng-devel
BuildRequires:  libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libSDL_ttf-devel
BuildRequires:  libSDL_gfx-devel gzip ctest cmake gettext
Source44: import.info

%description
The Mana World (TMW) is a serious effort to create an innovative free and open
source MMORPG. TMW uses 2D graphics and aims to create a large and diverse
interactive world.

%prep
%setup -q -c -n tmw-%{version}
%patch0 -p0


%build
%{fedora_cmake}

%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install \
        --vendor fedora \
        --dir $RPM_BUILD_ROOT/%{_datadir}/applications/ \
        --delete-original \
        --remove-category=Application \
        --add-category=RolePlaying \
        $RPM_BUILD_ROOT%{_datadir}/applications/mana.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mv $RPM_BUILD_ROOT%{_datadir}/pixmaps/mana.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
rmdir $RPM_BUILD_ROOT%{_datadir}/pixmaps

# Use system fonts instead of bundled fonts

rm -f $RPM_BUILD_ROOT%{_datadir}/mana/data/fonts/*.ttf
ln -s %{_datadir}/fonts/ttf/dejavu/DejaVuSans.ttf $RPM_BUILD_ROOT%{_datadir}/mana/data/fonts/dejavusans.ttf
ln -s %{_datadir}/fonts/ttf/dejavu/DejaVuSans-Bold.ttf $RPM_BUILD_ROOT%{_datadir}/mana/data/fonts/dejavusans-bold.ttf

mkdir -p $RPM_BUILD_ROOT%{_datadir}/man/man6
gzip -c docs/mana.6 > $RPM_BUILD_ROOT%{_datadir}/man/man6/mana.6.gz

%find_lang mana
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

%files -f mana.lang
%{_bindir}/mana
%{_datadir}/mana
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/32x32/apps/*.png
%{_mandir}/man6/*.*
%doc AUTHORS COPYING NEWS README docs/*.txt



%changelog
* Thu Dec 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt3_9.1
- rebuild with new SDL

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt2_9.1
- Rebuilt with libpng15

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt2_9
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt2_8
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_6
- update to new release by fcimport

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_5
- update to new release by fcimport

* Tue Nov 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_4
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_3
- update to new release by fcimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_2
- update to new release by fcimport

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.29.1-alt1_4.1
- Rebuilt with libphysfs 2.0.2

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.29.1-alt1_4
- converted from Fedora by srpmconvert script

