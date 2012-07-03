# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           puzzle-master
Version:        2.0.0
Release:        alt2_1
Summary:        Fun and addictive jigsaw puzzle game

Group:          Games/Other
License:        GPLv2+
URL:            http://puzzle-master.colorful.hu/

Source0:        %{name}-%{version}.tar.gz
# This package is generated from upstream's SCM, in the following way;
# %{name} refers to the package name and %{version} to the release version.
#
# git clone git://gitorious.org/colorful-apps/%{name}.git; cd %{name};
# git archive --format=tar --prefix=%{name}-%{version}/ v%{version} | gzip -n > %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(QtCore) pkgconfig(QtGui) pkgconfig(QtOpenGL) pkgconfig(QtDeclarative)
BuildRequires: desktop-file-utils
Source44: import.info

%description
%{name} is a jigsaw puzzle game that lets you use your own
images (and contains some built-in ones) for generating puzzles.
You can decide the size and the difficulty of the puzzle.

%prep
%setup -q

%build
# This ensures that the files will be placed to the correct location
QMAKEFLAGS=''
QMAKEFLAGS+=' -after target.path=%{_bindir}'
QMAKEFLAGS+=' -after desktopfile.path=%{_datadir}/applications'
QMAKEFLAGS+=' -after iconfile.path=%{_datadir}/icons/hicolor/scalable/apps'
# This will find qmake on both Fedora and MeeGo
qmake-qt4 $QMAKEFLAGS || qmake $QMAKEFLAGS
make %{?_smp_mflags}

%install
make INSTALL_ROOT=$RPM_BUILD_ROOT install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
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
%{_bindir}/%{name}
%attr(644,root,root) %{_datadir}/applications/%{name}.desktop
%attr(644,root,root) %{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%doc LICENSE
%doc LICENSE-DOCS

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_1
- rebuild with fixed sourcedep analyser (#27020)

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_3
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_2
- converted from Fedora by srpmconvert script

