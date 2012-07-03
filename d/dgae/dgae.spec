# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:		dgae
Version:	1.1
Release:	alt4_8
Summary:	DG, a short AGI adventure game

Group:		Games/Other
License:	Public Domain
URL:		http://membres.lycos.fr/agisite/agisite.htm
Source0:	dgae.zip
#Original from http://membres.lycos.fr/agisite/dgae.zip includes
#copyrighted executables. Generated new source by unzipping, removing
#DOS-related content, running dos2unix on the text file, and changing
#all filenames to lowercase for agistudio compatibility.
Source1:	dgae.desktop
Source2:	dgae-wrapper.sh
Source3:	dgae.xpm
BuildArch:	noarch

BuildRequires:	desktop-file-utils
Requires:	nagi icon-theme-hicolor
Source44: import.info

%description
Help DG to seek out his twin brother's stick.
This game is a public domain: you can look out the codes and make your own
AGI game.

%prep
%setup -q -c

%build
iconv -f IBM850 -t UTF8 readme.txt > readme.txt.tmp
mv readme.txt.tmp readme.txt

%install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -D -m0644 -p * $RPM_BUILD_ROOT%{_datadir}/%{name}
install -D -m0755 -p %{SOURCE2} $RPM_BUILD_ROOT/%{_bindir}

# desktop file
desktop-file-install  \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}

# icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
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
%doc readme.txt
%{_datadir}/dgae
%{_datadir}/applications/dgae.desktop
%{_datadir}/icons/hicolor/32x32/apps/dgae.xpm
%{_bindir}/dgae-wrapper.sh

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_8
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_7
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_7
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_7
- converted from Fedora by srpmconvert script

