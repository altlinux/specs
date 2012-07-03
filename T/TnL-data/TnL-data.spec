Name:           TnL-data
Version:        071111
Release:        alt2_7
Summary:        Datafiles for Thunder and Lightning
Group:          Games/Other
License:        GPL+
URL:            http://tnlgame.net
# This is: http://tnlgame.net/downloads/tnl/%{version}/TnL-data-%{version}.tar.bz2
# With the non free Gunship and Commonwealth fonts removed
Source0:        TnL-data-%{version}-clean.tar.bz2
BuildArch:      noarch
Requires:       icon-theme-hicolor
# So that we get uninstalled when TnL gets uninstalled
Requires:       TnL >= %{version} fonts-ttf-dejavu
Source44: import.info

%description
Datafiles for Thunder and Lightning.


%prep
%setup -q -n %{name}


%build
# nothing to build data only


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}
cp -a share/tnl share/icons $RPM_BUILD_ROOT%{_datadir}
ln -s ../../../fonts/ttf/dejavu/DejaVuSans.ttf \
  $RPM_BUILD_ROOT%{_datadir}/tnl/cegui/fonts/Commonv2c.ttf
ln -s ../../../fonts/ttf/dejavu/DejaVuSans.ttf \
  $RPM_BUILD_ROOT%{_datadir}/tnl/cegui/fonts/gun4f.ttf
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
# all docs are in the main package
%{_datadir}/tnl
%{_datadir}/icons/hicolor/*/apps/tnlgame.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 071111-alt2_7
- rebuild with fixed sourcedep analyser (#27020)

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 071111-alt1_7
- update to new release by fcimport

* Thu Jul 21 2011 Igor Vlasenko <viy@altlinux.ru> 071111-alt1_6
- initial release by fcimport

