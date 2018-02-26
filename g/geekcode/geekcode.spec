Summary(pl): Generator Geek Code
Summary(pl): Generator Geek Code
Summary(pl): Generator Geek Code
Name:           geekcode
Version:        1.7.3
Release:        alt2_8
Summary:        Geek Code generator
Summary(pl):    Generator Geek Code
Group:          Games/Other
License:        GPLv2+
URL:            http://sourceforge.net/projects/%{name}/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source44: import.info

%description
The Geek Code Generator will generate a geek code block for you by asking you a
series of questions about yourself. The generated code can be pasted into your
.sig or anywhere else you would like to display your geekiness.

%description -l pl
Generator ten potrafi wygenerować blok Geek Code po odpowiedzi na serię
pytań. Tak wygenerowany kod można umieścić w swoim podpisie lub
gdziekolwiek indziej, gdzie chcemy się pochwalić swoją geekowatością.

%prep
%setup -q
sed -i 's/\r//' COPYING

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 geekcode %{buildroot}%{_bindir}
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
%doc CHANGES COPYING README
%{_bindir}/%{name}

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt1_8
- update to new release by fcimport

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt1_7
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt1_6
- update to new release by fcimport

* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt1_5
- converted from Fedora by srpmconvert script

