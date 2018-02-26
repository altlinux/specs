# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:           crystal-stacker-themes
Version:        1.0
Release:        alt2_7
Summary:        Themes for the Crystal Stacker game
Group:          Games/Other
License:        Crystal Stacker
URL:            http://www.t3-i.com/cstacker.htm
Source0:        http://ncdgames.t3-i.com/csdream.zip
Source1:        http://ncdgames.t3-i.com/csfood.zip
Source2:        http://ncdgames.t3-i.com/csgems.zip
Source3:        http://ncdgames.t3-i.com/cslcd.zip
Source4:        http://ncdgames.t3-i.com/csmatrix.zip
Source5:        http://ncdgames.t3-i.com/csoldcs.zip
Source6:        http://ncdgames.t3-i.com/csstone.zip
Source7:        crystal-stacker-theme-license.txt
Source8:        cs-readme.txt
BuildArch:      noarch
Requires:       crystal-stacker
Source44: import.info

%description
7 new / extra themes for the Crystal Stacker game.


%prep
%setup -q -c -a5 -a6
# don't pass these to %setup, their filenames must be forced to lowercase
unzip -qqLL %{SOURCE1}
unzip -qqLL %{SOURCE2}
unzip -qqLL %{SOURCE3}
unzip -qqLL %{SOURCE4}
# put these somewhere were %%doc can find them
cp %{SOURCE7} %{SOURCE8} .


%build
# nothing to build datafiles only


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/crystal-stacker
install -p -m 644 *.xm *.cth $RPM_BUILD_ROOT%{_datadir}/crystal-stacker
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
%doc crystal-stacker-theme-license.txt cs-readme.txt
%{_datadir}/crystal-stacker/*.xm
%{_datadir}/crystal-stacker/*.cth


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_7
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6
- converted from Fedora by srpmconvert script

