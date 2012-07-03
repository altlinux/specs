# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libICE-devel libSM-devel
# END SourceDeps(oneline)
Name:		flaw
Version:	1.2.4
Release:	alt3_4
Summary:	Free top-down wizard battle game
Group:		Games/Other
License:	GPLv3+
URL:		http://flaw.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libSDL-devel
BuildRequires:	libSDL_gfx-devel desktop-file-utils fonts-ttf-gnu-freefont-sans
Requires:	fonts-ttf-gnu-freefont-sans
Source44: import.info

%description
FLAW is a free top-down wizard battle game.
It can be played by up to 5 players simultaneously. The goal of the game is to
survive as long as possible while more and more fireballs appear in the arena.
Game play is simple and self-explanatory. It's all about evading the fireballs
and knocking your opponents down. In addition there are collectible magic gems
that provide special abilities.

%prep
%setup -q

# Fix spurious executable permissions
chmod 644 src/*.cc
chmod 644 src/*.h

# Fix incorrect lines on flaw.desktop
sed -i -e '3d' data/flaw.desktop
sed -i -e '2d' data/flaw.desktop

%build
%configure --docdir=%{_docdir}/%{name}-%{version} --enable-fontpath=%{_datadir}/fonts/ttf/gnu-free/
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
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
%{_bindir}/flaw
%{_datadir}/flaw
%{_datadir}/pixmaps/flaw.xpm
%{_datadir}/applications/flaw.desktop
%exclude %{_docdir}/%{name}-%{version}/INSTALL
%doc %{_docdir}/%{name}-%{version}

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt3_4
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt2_4
- update to new release by fcimport

* Fri Oct 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt2_3
- bugfix release, close 33627 from ALTLinux Testers Team

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_3
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_2
- converted from Fedora by srpmconvert script

