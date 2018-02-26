# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname jisksp16-1990-fonts
%define	fontname	jisksp16-1990
%define	catalogue	%{_sysconfdir}/X11/fontpath.d

Name:		fonts-bitmap-jisksp16-1990
Version:	0.983
Release:	alt4_7
Summary:	16x16 JIS X 0212:1990 Bitmap font
Group:		System/Fonts/True type
License:	Public Domain

URL:		http://kanji.zinbun.kyoto-u.ac.jp/~yasuoka/ftp/fonts/
Source0:	http://kanji.zinbun.kyoto-u.ac.jp/~yasuoka/ftp/fonts/jisksp16-1990.bdf.Z

BuildArch:	noarch
BuildRequires:	gzip mkfontdir xorg-font-utils fontpackages-devel

Provides:	jisksp16-1990 = 0.1-16
Obsoletes:	jisksp16-1990 <= 0.1-16
Source44: import.info

%description
This package provides 16x16 Japanese bitmap font for JIS X 0212:1990.
JIS X 0212:1990 is a character sets that contains the auxiliary kanji
characters.


%prep
%setup -c -T
gunzip -c %{SOURCE0} > jisksp16-1990.bdf

%build
%{_bindir}/bdftopcf jisksp16-1990.bdf | gzip -9c > jisksp16-1990.pcf.gz

%install

install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0755 -d $RPM_BUILD_ROOT%{catalogue}

install -m 0644 -p jisksp16-1990.pcf.gz $RPM_BUILD_ROOT%{_fontdir}/

%{_bindir}/mkfontdir $RPM_BUILD_ROOT%{_fontdir}

# Install catalogue symlink
ln -sf %{_fontdir} $RPM_BUILD_ROOT%{catalogue}/%{oldname}
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
%{_fontbasedir}/*/%{_fontstem}/jisksp16-1990.pcf.gz

%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/fonts.dir
%{catalogue}/*

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.983-alt4_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.983-alt3_7
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.983-alt3_6
- rebuild with new rpm-build-fonts

* Mon Aug 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.983-alt2_6
- initial release by fcimport

* Sun Aug 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.983-alt1_6
- initial release by fcimport

