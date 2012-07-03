Name:           pmars
Version:        0.9.2
Release:        alt2_6
Summary:        Portable corewar system with ICWS'94 extensions

Group:          Games/Other
License:        GPLv2+
URL:            http://www.koth.org/pmars/
Source0:        http://downloads.sourceforge.net/corewar/%{name}-%{version}.tar.gz
# Patch to disable stripping of binary in spec file
Patch0:         pmars-0.9.2-nostrip.patch
#Show compiler commands
Patch1:         pmars-0.9.2-CCat.patch
BuildRequires:  libX11-devel
Requires:       fonts-bitmap-75dpi
Source44: import.info

%description
pMARS is a Memory Array Redcode Simulator (MARS) for corewar.

    * portable, run it on your Mac at home or VAX at work
    * free and comes with source
    * core displays for DOS, Mac and UNIX
    * implements a new redcode dialect, ICWS'94, while remaining compatible
      with ICWS'88
    * powerful redcode extensions: multi-line EQUates, FOR/ROF text repetition
    * one of the fastest simulators written in a high level language
    * full-featured, programmable debugger
    * runs the automated tournament "KotH" at http://www.koth.org and
      http://www.ecst.csuchico.edu/~pizza/koth/ and the annual ICWS tournaments

%prep
%setup -q
%patch0 -p0 -b .nostrip
%patch1 -p0 -b .CCat

# Make temporary doc dir
mkdir doc_install
cp -a doc doc_install
rm doc_install/doc/pmars.6


%build
make -C src CFLAGS="%{optflags} -DEXT94 -DXWINGRAPHX -DPERMUTATE"


%install
install -D -p -m 755 src/pmars %{buildroot}%{_bindir}/pmars
install -D -p -m 644 doc/pmars.6 %{buildroot}%{_mandir}/man6/pmars.6
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
%doc AUTHORS ChangeLog CONTRIB COPYING README config/ doc_install/doc/ warriors/
%{_bindir}/pmars
%{_mandir}/man6/pmars.6.*

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt1_6
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt1_5
- converted from Fedora by srpmconvert script

