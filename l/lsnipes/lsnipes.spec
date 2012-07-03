Summary:	A text-mode maze game
Name:		lsnipes
Version:	0.9.4
Release:	alt2_8
License:	GPLv2+
Group:		Games/Other
Source:		http://www.ugcs.caltech.edu/~boultonj/snipes/%{name}-%{version}.tgz
URL:		http://www.ugcs.caltech.edu/~boultonj/snipes.html
Patch1:		lsnipes-adapt-CFLAGS-LIBS.patch
# Man page update about levels from Debian package
Patch2:		lsnipes-man-levels-doc.patch

BuildRequires:	libncurses-devel
Source44: import.info

%description
Linux Snipes is a reimplementation of an old text-mode DOS game. You
are in a maze with a number of enemies (the "snipes") and a few
"hives" which create more of the enemies. Your job is to kill the
snipes and their hives before they get the best of you.  26 "option
levels" let you change characteristics of the game such as whether or
not diagonal shots bounce off the walls.  10 levels of difficulty (only
partially implemented) let you build your skills gradually.

%prep
%setup -q
%patch1 -p1 -b .cflags
%patch2 -p1 -b .man-levels

# as-needed
sed -i -e 's,${LIBS} ${OBJS},${OBJS} ${LIBS},' Makefile

%build
%{__make} RPM_CFLAGS="%{optflags}"

%install
%{__install} -p -m 0755 -d	%{buildroot}%{_bindir}
%{__install} -p -m 0755 snipes	%{buildroot}%{_bindir}/snipes
%{__install} -p -m 0755 -d	%{buildroot}%{_mandir}/man6
%{__install} -p -m 0644 snipes.6 %{buildroot}%{_mandir}/man6/snipes.6
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
%doc README TODO COPYING CHANGELOG
%{_bindir}/snipes
%{_mandir}/man6/snipes.6*

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_8
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_7
- initial release by fcimport

