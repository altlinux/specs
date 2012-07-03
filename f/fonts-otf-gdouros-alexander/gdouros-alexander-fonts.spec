# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname gdouros-alexander-fonts
%global fontname gdouros-alexander
%global fontconf 62-%{fontname}.conf

Name:           fonts-otf-gdouros-alexander
Version:        3.01
Release:        alt3_4
Summary:        A Greek typeface inspired by Alexander Wilson

Group:          System/Fonts/True type
License:        Copyright only
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/Alexander.zip
Source1:        %{oldname}-fontconfig.conf
Source2:        http://users.teilar.gr/~g1951d/Samples.pdf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
A text typeface using the Greek letters designed by Alexander Wilson
(1714-1786), a Scottish doctor, astronomer, and typefounder, who established a
typefoundry in Glasgow in 1744. The type was especially designed for an edition
of Homera.'s epics, published in 1756-8 by Andrew and Robert Foulis, printers to
the University of Glasgow. A modern revival, Wilson Greek, was designed by
Matthew Carter in 1995. Peter S. Baker is also using Wilsona.'s Greek type in his
Junicode font for medieval scholars (2007).

Latin and Cyrillic are based on a Garamond typeface. The font covers the
Windows Glyph List, IPA Extensions, Greek Extended, Ancient Greek Numbers,
Byzantine and Ancient Greek Musical Notation, various typographic extras and
several Open Type features (Case-Sensitive Forms, Small Capitals, Subscript,
Superscript, Numerators, Denominators, Fractions, Old Style Figures, Historical
Forms, Stylistic Alternates, Ligatures).

It was created by George Douros.
%prep
%setup -q -c

%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Alexander.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

install -m 0755 -d %{buildroot}%{_docdir}/%{oldname}-%{version}
install -m 0644 -p %{SOURCE2} %{buildroot}%{_docdir}/%{oldname}-%{version}
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
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/Alexander.otf

%doc %{_docdir}/%{oldname}-%{version}/Samples.pdf
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{oldname}-%{version}


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.01-alt3_4
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.01-alt2_4
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 3.01-alt2_3
- rebuild with new rpm-build-fonts

* Tue Aug 02 2011 Igor Vlasenko <viy@altlinux.ru> 3.01-alt1_3
- initial release by fcimport

