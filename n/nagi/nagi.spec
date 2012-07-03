%define _default_patch_fuzz 2
Summary: An interpreter for AGI games
Name: nagi
Version: 2.06
Release: alt2_10
Group: Games/Other
License: MIT
URL: http://www.agidev.com/projects/nagi/
Source0: http://www.agidev.com/dl_files/nagi/nagi_src_-_2002-11-14.tar.gz
Source1: nagi.sgml
Patch0: nagi-2.06-debian.patch 
Patch1: nagi-2.06-build_with_gcc-3.4.patch
Patch2:nagi-2.06-build_with_gcc-4.0.patch
BuildRequires: docbook-utils libSDL-devel libSDL-devel
Source44: import.info
%description
NAGI is an interpreter for AGI games, such as the early Space Quest,
Leisure Suit Larry and King's Quest games.

%prep
%setup -qcn nagi

%patch0 -p0
%patch1 -p0
%patch2 -p0
sed -i s,-lSDLmain,, src/Makefile.linux

%build
export CFLAGS="$RPM_OPT_FLAGS"
cd src
make -f Makefile.linux
docbook2man %{SOURCE1} 
cd ..
sed -i 's/\r//' license.txt
sed -i 's/\r//' readme.html

%install

mkdir -p %{buildroot}/%{_bindir}
install -Dp -m755 bin/nagi %{buildroot}/%{_bindir}/nagi
mkdir -p %{buildroot}%{_datadir}/nagi
install -Dp -m644 bin/*.nbf %{buildroot}%{_datadir}/nagi/
mkdir -p %{buildroot}%{_sysconfdir}/nagi
install -Dp -m644 bin/nagi.ini %{buildroot}%{_sysconfdir}/nagi/
install -Dp -m644 bin/standard.ini %{buildroot}%{_sysconfdir}/nagi/
mkdir -p %{buildroot}%{_mandir}/man1
install -Dp -m644 src/nagi.1 %{buildroot}%{_mandir}/man1
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
%doc license.txt readme.html
%{_bindir}/nagi 
%{_datadir}/nagi/
%config(noreplace) %{_sysconfdir}/nagi/
%{_mandir}/man1/nagi.1.*

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.06-alt2_10
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1_10
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1_9
- converted from Fedora by srpmconvert script

