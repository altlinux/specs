# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:		coco-coq
Version:	0.1
Release:	alt4_7
Summary:	Coco Coq in Grostesteing's base, an AGI adventure game

Group:		Games/Other
License:	Redistributable, no modification permitted
URL:		http://membres.lycos.fr/agisite/coco-c.htm
Source0:	cococe.zip
#Original from http://membres.lycos.fr/agisite/cococe.zip includes
#copyrighted executables. Generated new source by unzipping, removing
#DOS-related content.
Source1:	coco-coq.desktop
Source2:	coco-coq-wrapper.sh
Source3:	coco-coq.xpm
Source4:	coco-coq-LICENSE.fedora
BuildArch:	noarch

BuildRequires:	desktop-file-utils
Requires:	nagi icon-theme-hicolor
Source44: import.info

%description
Grostesteing is back for troubles: he's kidnapped the Coco Coq's friends
to turn them into monsters. Coco must go inside the deadly base, avoids 
traps, free his friends and beat the bad scientist Grostesteing.

%prep

%setup -q -c

#drop case
mv LOGDIR logdir
mv OBJECT object
mv PICDIR picdir
mv SNDDIR snddir
mv VIEWDIR viewdir
mv VOL.0 vol.0
mv WORDS.TOK words.tok

%build
cp %{SOURCE4} .

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
%doc coco-coq-LICENSE.fedora
%{_datadir}/coco-coq
%{_datadir}/applications/coco-coq.desktop
%{_datadir}/icons/hicolor/32x32/apps/coco-coq.xpm
%{_bindir}/coco-coq-wrapper.sh

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_7
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_7
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_6
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_6
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_6
- converted from Fedora by srpmconvert script

