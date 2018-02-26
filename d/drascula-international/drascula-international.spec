# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:           drascula-international
Version:        1.0
Release:        alt4_5
Summary:        Subtitles for Drascula: The Vampire Strikes Back
Group:          Games/Other
# For further discussion on distribution rights see:
# http://www.redhat.com/archives/fedora-extras-list/2006-November/msg00030.html
License:        Freely redistributable without restriction
URL:            http://wiki.scummvm.org/index.php/Drascula:_The_Vampire_Strikes_Back
Source0:        http://downloads.sourceforge.net/scummvm/drascula-int-%{version}.zip
Source1:        drascula-fr.desktop
Source2:        drascula-de.desktop
Source3:        drascula-es.desktop
Source4:        drascula-it.desktop
Buildarch:      noarch
BuildRequires:  desktop-file-utils
Source44: import.info

%description
Spanish, German, French and Italian subtitles for Drascula: The Vampire
Strikes Back.


%package -n drascula-fr
Summary:        French subtitles for Drascula: The Vampire Strikes Back
Group:          Games/Other
Requires:       drascula

%description -n drascula-fr
French subtitles for Drascula: The Vampire Strikes Back.

%package -n drascula-de
Summary:        German subtitles for Drascula: The Vampire Strikes Back
Group:          Games/Other
Requires:       drascula

%description -n drascula-de
German subtitles for Drascula: The Vampire Strikes Back.

%package -n drascula-es
Summary:        Spanish subtitles for Drascula: The Vampire Strikes Back
Group:          Games/Other
Requires:       drascula

%description -n drascula-es
Spanish subtitles for Drascula: The Vampire Strikes Back.

%package -n drascula-it
Summary:        Italian subtitles for Drascula: The Vampire Strikes Back
Group:          Games/Other
Requires:       drascula

%description -n drascula-it
Italian subtitles for Drascula: The Vampire Strikes Back.


%prep
%setup -q -c


%build
# nothing todo content only


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/drascula
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -p -m 644 PACKET.00? $RPM_BUILD_ROOT%{_datadir}/drascula
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE3}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE4}
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


%files -n drascula-fr
%doc readme.txt
%{_datadir}/drascula/PACKET.002
%{_datadir}/applications/drascula-fr.desktop

%files -n drascula-de
%doc readme.txt
%{_datadir}/drascula/PACKET.003
%{_datadir}/applications/drascula-de.desktop

%files -n drascula-es
%doc readme.txt
%{_datadir}/drascula/PACKET.004
%{_datadir}/applications/drascula-es.desktop

%files -n drascula-it
%doc readme.txt
%{_datadir}/drascula/PACKET.005
%{_datadir}/applications/drascula-it.desktop


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_5
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_5
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_4
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_4
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_4
- converted from Fedora by srpmconvert script

