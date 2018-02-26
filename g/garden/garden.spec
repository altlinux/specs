# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/update-desktop-database
# END SourceDeps(oneline)
Name:           garden
Version:        1.0.8
Release:        alt2_5
Summary:        An innovative old-school 2D vertical shoot-em-up

Group:          Games/Other
License:        GPLv3+
URL:            http://garden.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         garden-dso.patch

BuildRequires:  liballegro-devel
BuildRequires:  desktop-file-utils
BuildRequires:  automake
BuildRequires:  autoconf
Requires:       liballegro4.4
Source44: import.info

%description
Garden of colored lights is an old school 2D vertical shoot-em-up with some
innovative elements. Innovative graphics, soundtrack and game concept. The
game itself is very challenging and as you progress, you will understand that
you are dealing with a true piece of art...

%prep
%setup -q

# patch for DSO-linking
# https://sourceforge.net/tracker/?func=detail&aid=2982590&group_id=242667&atid=1121672
%patch0 -p1 -b .dso

%build
%configure 
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate \
%{buildroot}%{_datadir}/applications/%{name}.desktop
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
%doc README NEWS AUTHORS ChangeLog COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_5
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_5
- update to new release by fcimport

* Mon Oct 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_4
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_3
- initial release by fcimport

