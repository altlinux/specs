# BEGIN SourceDeps(oneline):
BuildRequires: python-devel
# END SourceDeps(oneline)
Name: inksmoto
Version: 0.7.0
Release:  alt2_6
Summary: The new xmoto level editor for Inkscape

Group: Games/Other
License: GPLv2
URL: http://xmoto.sourceforge.net/
Source0: http://download.tuxfamily.org/xmoto/svg2lvl/%{version}~rc1/inksmoto-%{version}.tar.gz
Requires: xmoto inkscape python-module-PyXML tkinter python-module-imaging
BuildArch: noarch

Patch0: inksmoto-0.7.0-pypath.patch
Source44: import.info

%description
Inksmoto Level Editor is the new xmoto level editor. It uses Inkscape to
draw levels, then it allows you to save your drawing as a xmoto level
(.lvl file). It also allow you to edit xmoto level properties from 
within Inkscape such as make background block, strawberries, ...

Inksmoto Level Editor is written in Python, it's an Inkscape extension. 

%prep
%setup -qn extensions

%patch0 -p0

%build

%install
mkdir -p %{buildroot}%{_datadir}/inkscape/extensions
rm -f bezmisc.py
rm -f inkex.py
cp -p *.inx *.py %{buildroot}%{_datadir}/inkscape/extensions/
chmod 644 %{buildroot}%{_datadir}/inkscape/extensions/*
cp -pr inksmoto %{buildroot}%{_datadir}/inkscape/extensions/
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
%{_datadir}/inkscape/extensions/*
%doc AUTHORS COPYING INSTALL README

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_6
- update to new release by fcimport

* Wed Dec 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_5
- initial import by fcimport

