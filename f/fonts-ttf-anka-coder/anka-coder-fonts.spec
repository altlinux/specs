Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: python
# END SourceDeps(oneline)
%define oldname anka-coder-fonts
%global fontname anka-coder
%global fontconf 65-%{fontname}
%global hgrev 4348cf4ec395


%global common_desc \
The Anka/Coder family is a mono spaced, courier-width (60% of height; em size \
2048x1229) font that contains characters from 437, 866, 1251, 1252 and some \
other code pages and can be used for source code, terminal windows etc. \
There are 3 font sets (regular. italic, bold, bold-italic each): 1. \
Anka/Coder (em size 2048x1229) 2. Anka/Coder Condensed (condensed by \
12.5%; em size 2048x1075) 3. Anka/Coder Narrow (condensed by 25%; em \
size 2048x922)

Name:           fonts-ttf-anka-coder
Version:        1.100
Release:        alt1_0.4.20130409hg%{hgrev}
Summary:        A mono spaced, courier-width font

License:        OFL
URL:            http://code.google.com/p/anka-coder-fonts/

# Generated from an hg clone since sfd sources were available
# hg clone https://code.google.com/p/anka-coder-fonts/
# tar -cvzf anka-coder-fonts-20130409-hg.tar.gz --exclude="\.hg" anka-coder-fonts/
Source0:        anka-coder-fonts-20130409-hg.tar.gz
Source1:        %{oldname}-norm.conf
Source2:        %{oldname}-condensed.conf
Source3:        %{oldname}-narrow.conf
Source4:        %{fontname}.metainfo.xml
Source5:        %{fontname}-condensed.metainfo.xml
Source6:        %{fontname}-narrow.metainfo.xml
Source7:        %{fontname}-norm.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires: fontforge libfontforge
Source44: import.info

%description
%common_desc

%package -n fonts-ttf-anka-coder-common
Group: System/Fonts/True type
Summary:        Common files of %{oldname}

%description -n fonts-ttf-anka-coder-common
%common_desc

This package consists of files used by other %{oldname} packages.


%package -n fonts-ttf-anka-coder-norm
Group: System/Fonts/True type
Summary:        Normal version of %{oldname}
Requires:       fonts-ttf-anka-coder-common = %{version}

%description -n fonts-ttf-anka-coder-norm
%common_desc

"Anka/Coder Norm" simply supplements the family. 


%files -n fonts-ttf-anka-coder-norm
%{_fontconfig_templatedir}/%{fontconf}-norm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-norm.conf
%{_fontbasedir}/*/%{_fontstem}/AnkaCoder-b.ttf
%{_fontbasedir}/*/%{_fontstem}/AnkaCoder-bi.ttf
%{_fontbasedir}/*/%{_fontstem}/AnkaCoder-i.ttf
%{_fontbasedir}/*/%{_fontstem}/AnkaCoder-r.ttf
%doc AnkaCoder-b-sample.pdf AnkaCoder-bi-sample.pdf AnkaCoder-i-sample.pdf AnkaCoder-r-sample.pdf
%{_datadir}/appdata/%{fontname}-norm.metainfo.xml

# Repeat for every font family ➅
%package -n fonts-ttf-anka-coder-condensed
Group: System/Fonts/True type
Summary:        Condensed version of %{oldname}
Requires:       fonts-ttf-anka-coder-common = %{version}

%description -n fonts-ttf-anka-coder-condensed
%common_desc

"Anka/Coder Condensed" can be used for both printing and screen 
viewing of source code, also as for displaying terminal windows.


%files -n fonts-ttf-anka-coder-condensed
%{_fontconfig_templatedir}/%{fontconf}-condensed.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-condensed.conf
%{_fontbasedir}/*/%{_fontstem}/AnkaCoder-C87*.ttf
%doc AnkaCoder-C87-b-sample.pdf AnkaCoder-C87-bi-sample.pdf AnkaCoder-C87-i-sample.pdf AnkaCoder-C87-r-sample.pdf
%{_datadir}/appdata/%{fontname}-condensed.metainfo.xml

%package -n fonts-ttf-anka-coder-narrow
Group: System/Fonts/True type
Summary:        Narrow version of %{oldname}
Requires:       fonts-ttf-anka-coder-common = %{version}

%description -n fonts-ttf-anka-coder-narrow
%common_desc

"Anka/Coder Narrow" was developed for printing of source code; it \
is too tight for screen resolution.

%files -n fonts-ttf-anka-coder-narrow
%{_fontconfig_templatedir}/%{fontconf}-narrow.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-narrow.conf
%{_fontbasedir}/*/%{_fontstem}/AnkaCoder-C75*.ttf
%doc AnkaCoder-C75-b-sample.pdf AnkaCoder-C75-bi-sample.pdf AnkaCoder-C75-i-sample.pdf AnkaCoder-C75-r-sample.pdf
%{_datadir}/appdata/%{fontname}-narrow.metainfo.xml

%prep
%setup -q -n %{oldname}

%build
for family in "AnkaCoder" "AnkaCoder Condensed" "AnkaCoder Narrow"
do
pushd "$family"
fontforge -lang=ff -script "-" *.sfd <<EOF
i = 1 
while ( i < \$argc )
  Open (\$argv[i], 1)
  Generate (\$fontname + ".ttf")
  PrintSetup (5) 
  PrintFont (0, 0, "", \$fontname + "-sample.pdf")
  Close()
  i++
endloop
EOF
mv *.ttf ../ -v
mv *.pdf ../ -v
popd
done

sed -i 's/\r//' AnkaCoder/OFL.txt

%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-norm.conf

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-condensed.conf

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-narrow.conf

mkdir -p %{buildroot}/%{_datadir}/appdata/
cp %{SOURCE4} %{buildroot}/%{_datadir}/appdata/  -v
cp %{SOURCE5} %{buildroot}/%{_datadir}/appdata/  -v
cp %{SOURCE6} %{buildroot}/%{_datadir}/appdata/  -v
cp %{SOURCE7} %{buildroot}/%{_datadir}/appdata/  -v

for fconf in %{fontconf}-norm.conf \
             %{fontconf}-condensed.conf \
             %{fontconf}-narrow.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
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


%files -n fonts-ttf-anka-coder-common
%doc AnkaCoder/OFL.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.100-alt1_0.4.20130409hg4348cf4ec395
- update to new release by fcimport

* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.100-alt1_0.3.20130409hg4348cf4ec395
- new version

