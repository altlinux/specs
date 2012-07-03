Name:           ularn
Version:        1.5p4
Release:        alt2_17
Summary:        Simple roguelike game

Group:          Games/Other
License:        GPL+
URL:            http://www.ularn.org
Source0:        http://downloads.sourceforge.net/ularn/Ularn-1.5ishPL4.tar.gz
Source1:        config.sh.in
Source2:        ularn.desktop
Source3:        ularn.png
Patch0:         ularn-build.patch
Patch1:         ularn-euid.patch
Patch2:         ularn-datadir.patch
Patch3:         ularn-drop-setgid.patch

BuildRequires:  libncurses-devel
BuildRequires:  desktop-file-utils
Requires:       ncompress
Requires(post): coreutils
Requires(postun): coreutils
Source44: import.info

%description
A text-based roguelike game based on the original Larn.  Travel through
dungeons collecting weapons, killing monsters, in order to find and sell the
Eye of Larn to save your sick daughter.

%prep
%setup -q -n Ularn

# The configure script for this package is interactive.  However, it
# produces a config.sh script that can be customized if necessary.
# a pre-built config.sh script is used to avoid running an interactive
# configure script, but still must be customized slightly.
sed -e 's#@bindir@#%{_bindir}#' \
        -e 's#@datadir@#%{_datadir}#' \
        -e 's#@var@#%{_var}#' < %{SOURCE1} > config.sh
chmod +x config.h.SH
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# Keep track of where we are.  Some of the configuration scripts change
# the current working directory.
builddir=`pwd`
. ./config.h.SH
${builddir}/Makefile.u.SH
cd ${builddir}
mv Makefile.u Makefile
CC="gcc $RPM_OPT_FLAGS" make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_var}/games
touch $RPM_BUILD_ROOT/%{_var}/games/Ularn-scoreboard

desktop-file-install                             \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/
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
%attr(2711,root,games) %{_bindir}/Ularn
%{_datadir}/%{name}
%config(noreplace) %attr (0664,root,games) %{_var}/games/Ularn-scoreboard
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%doc README README.spoilers GPL CHANGES.text Ularnopts


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt2_17
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt1_17
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt1_16
- converted from Fedora by srpmconvert script

