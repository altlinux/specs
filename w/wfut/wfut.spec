Name:           wfut
Version:        1.1.0
Release:        alt2_10
Summary:        Software updater tool for WorldForge applications

Group:          Development/C
License:        GPL+
URL:            http://www.worldforge.org
Source0:        http://downloads.sourceforge.net/worldforge/WFUT-1.1.0.tar.gz
Source1:        wfut.desktop
Source2:        wfut.png

BuildRequires:  gcc-java desktop-file-utils
Source44: import.info

%description
Software updater tool for WorldForge applications.


%prep
%setup -q -n WFUT-%{version}
sed -i -e 's/gcj -c/gcj $(RPM_OPT_FLAGS) -c/' src/Makefile.in


%build
# This should be compiling to native code now, making the JAR
# override unnecessary.  Leave it in for now as a reminder of
# how to use it with gcc's jar program.
JAR=fastjar
export JAR
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# The start script checks for a native binary, and if not found, will
# try to use java + jar file instead.  But we are only building the
# native binary, so don't bother with this check.
mv $RPM_BUILD_ROOT%{_bindir}/wfut-bin $RPM_BUILD_ROOT%{_bindir}/wfut

desktop-file-install                             \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications         \
        %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/
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
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_10
- rebuild with fixed sourcedep analyser (#27020)

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_10
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_9
- initial release by fcimport

