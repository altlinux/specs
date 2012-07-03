%global           upstream_version 4.0

Summary:          The card game Skat
Name:             xskat
# Upstream License requires to alter the version number
# for re-distribution
Version:          %{upstream_version}.0
Release:          alt2_7
# https://fedoraproject.org/wiki/Licensing/XSkat_License
License:          XSkat
Group:            Games/Other
Source0:          http://www.xskat.de/xskat-%{upstream_version}.tar.gz
Source1:          xskat.desktop
URL:              http://www.xskat.de/xskat.html
# xskat requires an 10x20 font
Requires:         fonts-bitmap-misc
BuildRequires:    xorg-cf-files gccmakedep imake
BuildRequires:    libX11-devel
BuildRequires:    desktop-file-utils
BuildRequires:    ImageMagick
Source44: import.info


%description
XSkat lets you play the card game Skat as defined by the official Skat Order.

Features:
    * Single- and multiplayer mode
    * Playing over LAN or IRC
    * Game lists and logs
    * Three types of scoring
    * English or German text
    * German or French suited cards
    * Selectable computer playing strength
    * Pre-definable card distributions
    * Variations: Ramsch, Bock, Kontra & Re, ... 

%prep
%setup -q -n %{name}-%{upstream_version}

# fix encoding
iconv -f iso8859-1 -t utf-8 CHANGES-de > CHANGES-de.conv && \
touch -r CHANGES-de CHANGES-de.conv && \
mv -f CHANGES-de.conv CHANGES-de

iconv -f iso8859-1 -t utf-8 README-de > README-de.conv && \
touch -r README-de README-de.conv && \
mv -f README-de.conv README-de

iconv -f iso8859-1 -t utf-8 README.IRC-de > README.IRC-de.conv && \
touch -r README.IRC-de README.IRC-de.conv && \
mv -f README.IRC-de.conv README.IRC-de

%build
%configure
make CDEBUGFLAGS="%{optflags}"

%install
make DESTDIR=$RPM_BUILD_ROOT MANDIR=%{_mandir}/man6 MANSUFFIX=6 install install.man
install -d $RPM_BUILD_ROOT%{_mandir}/de/man6
mv $RPM_BUILD_ROOT%{_mandir}/man6/xskat-de.6 $RPM_BUILD_ROOT%{_mandir}/de/man6/xskat.6
chmod 644 $RPM_BUILD_ROOT%{_mandir}/man6/xskat.6*
chmod 644 $RPM_BUILD_ROOT%{_mandir}/de/man6/xskat.6*

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
convert icon.xbm $RPM_BUILD_ROOT%{_datadir}/pixmaps/xskat.xpm
touch -r icon.xbm $RPM_BUILD_ROOT%{_datadir}/pixmaps/xskat.xpm
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
%doc README* CHANGES*
%{_bindir}/xskat
%{_mandir}/man6/xskat.6.*
%lang(de) %{_mandir}/de/man6/xskat.6.*
%{_datadir}/applications/*
%{_datadir}/pixmaps/%{name}.xpm


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt2_7
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_7
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_6
- initial release by fcimport

