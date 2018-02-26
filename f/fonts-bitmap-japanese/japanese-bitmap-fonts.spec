# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/awk /usr/bin/gawk /usr/bin/mkfontdir /usr/bin/perl unzip
# END SourceDeps(oneline)
%define oldname japanese-bitmap-fonts
%define version 0.20080710
%define name japanese-bitmap-fonts
%global	fontname        japanese-bitmap
%define cataloguedir    %{_sysconfdir}/X11/fontpath.d
%define cidmapdir       %{_datadir}/ghostscript/conf.d

%define chxlfd          /usr/bin/perl $RPM_BUILD_DIR/%{name}-%{version}/%{vft}/chbdfxlfd.pl
%define mkalias         /usr/bin/perl $RPM_BUILD_DIR/%{name}-%{version}/%{vft}/mkalias.pl
%define mkbold          $RPM_BUILD_DIR/%{name}-%{version}/%{shinonome}-src/tools/mkbold
%define mkitalic        $RPM_BUILD_DIR/%{name}-%{version}/%{vft}/mkitalic

%define kappa           Kappa20-0.396
%define shinonome       shinonome-0.9.11
%define warabi12        warabi12-0.19a
%define mplus           mplus_bitmap_fonts-2.2.4
%define vft             vine-fonttools-0.1

Name:           fonts-bitmap-japanese
Version:        0.20080710
Release:        alt2_11
License:        Public Domain and BSD and mplus
Group:          System/Fonts/True type
BuildArch:      noarch
BuildRequires:  xorg-font-utils mkfontdir gawk fontpackages-devel

## files in ttfonts-ja
Source2:        FAPIcidfmap.ja
Source3:        cidfmap.ja
Source4:        CIDFnmap.ja
## files in jisksp14
### Licensed under Public Domain
Source10:       jisksp14.bdf.gz
## files in kaname
### Licensed under Public Domain
Source41:       ftp://ftp.freebsd.org/pub/FreeBSD/ports/distfiles/kaname_k12_bdf.tar.gz
## files in fonts-ja
Source50:       xfonts_jp.tgz
### Licensed under Public Domain
Source51:       http://kappa.allnet.ne.jp/20dot.fonts/%{kappa}.tar.bz2
### Licensed under Public Domain
Source52:       http://openlab.ring.gr.jp/efont/dist/shinonome/%{shinonome}-src.tar.bz2
## http://mlnews.com/marumoji/
### Licensed under Public Domain
Source53:       marumoji.tgz
# JIS X 0213-2000 fonts (14pxl, 16pxl)
# http://www.mars.sphere.ne.jp/imamura/jisx0213.html
# http://www.mars.sphere.ne.jp/imamura/K14-1.bdf.gz
# http://www.mars.sphere.ne.jp/imamura/K14-2.bdf.gz
# http://www.mars.sphere.ne.jp/imamura/jiskan16-2000-1.bdf.gz
# http://www.mars.sphere.ne.jp/imamura/jiskan16-2000-2.bdf.gz
### Licensed under Public Domain
Source54:       imamura-jisx0213.tgz
# jiskan16 JIS X 0208:1990 by Yasuoka
# http://kanji.zinbun.kyoto-u.ac.jp/~yasuoka/ftp/fonts/
### Licensed under Public Domain
Source55:       http://kanji.zinbun.kyoto-u.ac.jp/~yasuoka/ftp/fonts/jiskan16-1990.bdf.Z
# jiskan16 JIS X 0208:1997 Old Kanji
### Licensed under Public Domain
Source56:       http://kanji.zinbun.kyoto-u.ac.jp/~yasuoka/ftp/fonts/jiskano16-1997.bdf.Z
# k14 Old-Kanji
### Licensed under Public Domain
Source57:       k14-oldkanji.tar.gz
## k14 invalid glyphs patch
## http://kappa.allnet.ne.jp/kanou/fonts/k14-patch.html
# Warabi12 (12pxl) jisx0213
# http://www.gelgoog.org/warabi12/
### Licensed under BSD
Source58:       http://www.gelgoog.org/warabi12/archives/%{warabi12}.tar.gz
# mplus fonts
# http://mplus-fonts.sourceforge.jp/
### Licensed under mplus
Source59:       http://osdn.dl.sourceforge.jp/mplus-fonts/5030/%{mplus}.tar.gz
Source60:       %{vft}.tgz
# jiskan24 JIS X 0213
# http://gitatsu.hp.infoseek.co.jp/bdf/
### Licensed under Public Domain
Source61:	http://gitatsu.hp.infoseek.co.jp/bdf/jiskan24-2000-1.bdf.gz
Source62:	http://gitatsu.hp.infoseek.co.jp/bdf/jiskan24-2000-2.bdf.gz
Source63:	http://gitatsu.hp.infoseek.co.jp/bdf/jiskan24-2003-1.bdf.gz

Patch50:        http://kappa.allnet.ne.jp/kanou/fonts/k14.patch
# k14 to jisx0208.1990 patch
# http://www.brl.ntt.co.jp/people/takada/goodies/k14-1990/
# http://www.brl.ntt.co.jp/people/takada/goodies/k14-1990/patch.txt
Patch51:        k14-1990.patch
Patch52:        fonts-ja-8.0-gcc-warnings.patch
Patch53:        mplus_bitmap_fonts-install.patch
Patch54:        fonttools-replace.patch


Summary:        Free Japanese Bitmap fonts

Provides:	jisksp14 = 0.1-16 kappa20 = 0.3-15 fonts-ja = 8.0-16 fonts-japanese = 0.20061016-13
Source44: import.info

%description
This package provides various free Japanese Bitmap fonts.


%prep
#%%setup -q -T -c -a 5 -a 40 -a 41 -a 50 -a 51 -a 52 -a 53 -a 54 -a 57 -a 58 -a 59 -a 60
%setup -q -T -c -a 41 -a 50 -a 51 -a 52 -a 53 -a 54 -a 57 -a 58 -a 59 -a 60
## ttfonts-ja
## jisksp14
gunzip -c %{SOURCE10} > jisksp14.bdf
## kappa20
## fonts-ja
gunzip -c %{SOURCE55} > jiskan16-1990.bdf
gunzip -c %{SOURCE56} > jiskano16-1997.bdf
%patch50 -p0
cp k14.bdf k14-1990.bdf
%patch51 -p0
%patch52 -p1
pushd %{mplus}
%patch53 -p1
popd
%patch54 -p1
zcat %{SOURCE61} > jiskan24-2000-1.bdf
zcat %{SOURCE62} > jiskan24-2000-2.bdf
zcat %{SOURCE63} > jiskan24-2003-1.bdf

%build
## jisksp14
bdftopcf jisksp14.bdf | gzip -9 > jisksp14.pcf.gz
## kappa20
## fonts-ja
pushd %{shinonome}-src
%configure --disable-bold --disable-italic --with-fontdir=$RPM_BUILD_ROOT%{fontdir}
make bdf
popd
### rename Kappa and remove the bold fonts
pushd %{kappa}
  mv k20m.bdf k20.bdf
  mv 10x20rkm.bdf 10x20rk.bdf
  rm k20b.bdf 10x20rkb.bdf
popd
### rename in xfonts_jp
mv 7x14.bdf 7x14a.bdf
mv 8x16.bdf 8x16a.bdf
mv 12x24.bdf 12x24a.bdf
### marumoji
pushd marumoji
  for i in *.bdf; do
      %{chxlfd} $i '-Marumoji Club-Marumoji-.-.-.-.-.-.-.-.-.-.-.-.' $i.new && mv -f $i.new $i
  done
popd
### imamura jiskan16
pushd imamura-jisx0213
  for i in *.bdf; do
      %{chxlfd} $i '-Imamura-Fixed-.-.-.-.-.-.-.-.-.-.-.-.' $i.new && mv -f $i.new $i
  done
  mv K14-1.bdf k14-2000-1.bdf
  mv K14-2.bdf k14-2000-2.bdf
popd
### k14 and k14-1990 is used as Mincho
for i in k14.bdf k14-1990.bdf; do
    %{chxlfd} $i '-Misc-Mincho-.-.-.-.-.-.-.-.-.-.-.-.' $i.new && mv $i.new $i
done
### oldkanji
rm k14-oldkanji.pcf*
for i in k14-oldkanji.bdf jiskano16-1997.bdf; do
    %{chxlfd} $i '-Misc-.-.-.-.-Old Style-.-.-.-.-.-.-.-.' $i.new && mv $i.new $i
done
### warabi12
pushd %{warabi12}
  mv warabi12-1.bdf warabi12-2000-1.bdf
popd
### mplus
pushd %{mplus}
  DESTDIR=`pwd`/tmp/ ./install_mplus_fonts
popd

### move bdfs to topdir
mkdir fonts-ja
find -name "*.bdf" -path "./*/*" ! -path "./fonts-ja/*" ! -path "./fonts/*" -exec mv {} ./fonts-ja \;
mv k14-oldkanji.bdf jiskano16-1997.bdf k14-1990.bdf jiskan16-1990.bdf 7x14a.bdf 7x14rk.bdf 12x24a.bdf 12x24rk.bdf 8x16a.bdf 8x16rk.bdf k14.bdf jiskan16.bdf jiskan24*.bdf ./fonts-ja/
### move the documents to topdir
for i in */README */COPYRIGHT */{LICENSE,README}_{E,J}; do
    mv $i fonts-ja/`basename $i`-`dirname $i`
done

ALL_MEDIUM_BDF_FONT="\
  shnmk12maru/     maru14/-L        maru16/                        \
  k14-oldkanji/    jiskano16-1997/                                 \
  k14-1990/-L      jiskan16-1990/                                  \
  warabi12-2000-1/                                                 \
  k14-2000-1/-L    k14-2000-2/-L                                   \
  jiskan16-2000-1/ jiskan16-2000-2/                                \
  shnm6x12a/-r     shnm6x12r/-r     shnmk12/ shnmk12p/ shnmk12min/ \
  shnm8x16a/-r     shnm8x16r/-r     shnmk16/           shnmk16min/ \
  7x14a/           7x14rk/          shnmk14/ k14/-L    shnmk14min/ \
  8x16a/           8x16rk/          jiskan16/                      \
  shnm9x18a/-r     shnm9x18r/-r                                    \
  10x20rk/         k20/                                            \
  12x24a/          12x24rk/         jiskan24/                      \
  jiskan24-2000-1/ jiskan24-2000-2/ jiskan24-2003-1/
"
ALL_BOLD_BDF_FONT="\
mplus_f10WEIGHT-euro/-r mplus_f10WEIGHT/-r                             \
mplus_f12WEIGHT-euro/-r mplus_f12WEIGHT-jisx0201/-r mplus_f12WEIGHT/-r \
mplus_h10WEIGHT-euro/-r mplus_h10WEIGHT-jisx0201/-r mplus_h10WEIGHT/-r \
mplus_h12WEIGHT-euro/-r mplus_h12WEIGHT-jisx0201/-r mplus_h12WEIGHT/-r \
mplus_j10WEIGHT-iso/-r  mplus_j10WEIGHT-jisx0201/-r mplus_j10WEIGHT/-r \
mplus_j12WEIGHT/-r                                                     \
mplus_s10WEIGHT-euro/-r mplus_s10WEIGHT/-r
"
gcc $RPM_OPT_FLAGS %{vft}/mkitalic.c -o %{vft}/mkitalic

pushd fonts-ja
### delete 'r' from the filenames
for src in $ALL_BOLD_BDF_FONT; do
    mv `echo ${src%/*}.bdf | sed -e 's/WEIGHT/r/'` `echo ${src%/*}.bdf | sed -e 's/WEIGHT//'`
done

### making roman-bold fonts
for src in $ALL_MEDIUM_BDF_FONT; do
    %{mkbold} ${src#*/} -V ${src%/*}.bdf > ${src%/*}b.bdf
done
### making italic-medium fonts
for src in $ALL_MEDIUM_BDF_FONT; do
    %{mkitalic} -s 0.2 ${src%/*}.bdf > ${src%/*}i.bdf
done
for src in $ALL_BOLD_BDF_FONT; do
    %{mkitalic} -s 0.2 `echo ${src%/*}.bdf | sed -e 's/WEIGHT//'` > `echo ${src%/*}.bdf | sed -e 's/WEIGHT/i/'`
done
### making italic-bold fonts
for src in $ALL_MEDIUM_BDF_FONT; do
    %{mkbold} ${src#*/} -V ${src%/*}i.bdf > ${src%/*}bi.bdf
done
for src in $ALL_BOLD_BDF_FONT; do
    %{mkitalic} -s 0.2 `echo ${src%/*}.bdf | sed -e 's/WEIGHT/b/'` > `echo ${src%/*}.bdf | sed -e 's/WEIGHT/bi/'`
done

grep '^FONT ' *.bdf | sed -e 's/\.bdf:FONT//' > ALLFONTS.txt

### check the duplicated xlfds
DUP="`cut -d' ' -f2- ALLFONTS.txt | sort | uniq -d`"
if [ ! -z "$DUP" ]; then
    echo Duplicated XLFDs found. Please fix.
    echo -----------------------------------------
    echo "$DUP"
    exit 1
fi

cp ALLFONTS.txt mkalias.dat
# CHARSET PXL MISC FIXED MINCHO GOTHIC
# now, pixel 10 jisx0201 and pixel 20 gothic,
#      pixel 12 jisx0201 and pixel 24 gothic does not exist (fake)
%{mkalias} Misc-Fixed Alias-Fixed Alias-Gothic Alias-Mincho - \
ISO8859-1       10 mplus_f10WEIGHT mplus_f10WEIGHT mplus_j10WEIGHT - \
ISO8859-1       12 shnm6x12a shnm6x12a shnm6x12a shnm6x12a \
ISO8859-1       14 7x14a 7x14a 7x14a 7x14a \
ISO8859-1       16 shnm8x16a shnm8x16a shnm8x16a shnm8x16a \
ISO8859-1       18 shnm9x18a shnm9x18a shnm9x18a shnm9x18a \
ISO8859-1       20 10x20rk 10x20rk - 10x20rk \
ISO8859-1       24 12x24a 12x24a - 12x24a \
JISX0201.1976-0 10 mplus_j10WEIGHT-jisx0201 mplus_j10WEIGHT-jisx0201 mplus_j10WEIGHT-jisx0201 mplus_j10WEIGHT-jisx0201 \
JISX0201.1976-0 12 shnm6x12r shnm6x12r shnm6x12r shnm6x12r \
JISX0201.1976-0 14 7x14rk 7x14rk 7x14rk 7x14rk \
JISX0201.1976-0 16 shnm8x16r shnm8x16r shnm8x16r shnm8x16r \
JISX0201.1976-0 18 shnm9x18r shnm9x18r shnm9x18r shnm9x18r \
JISX0201.1976-0 20 10x20rk 10x20rk - 10x20rk \
JISX0201.1976-0 24 12x24rk 12x24rk - 12x24rk \
JISX0208.1983-0 10 mplus_j10WEIGHT mplus_j10WEIGHT mplus_j10WEIGHT - \
JISX0208.1983-0 12 shnmk12 shnmk12 shnmk12 shnmk12min \
JISX0208.1983-0 14 shnmk14 shnmk14 shnmk14 k14 \
JISX0208.1983-0 16 shnmk16 shnmk16 shnmk16 shnmk16min \
JISX0208.1983-0 20 - - - k20 \
JISX0208.1983-0 24 - - - jiskan24 \
JISX0208.1990-0 10 mplus_j10WEIGHT mplus_j10WEIGHT mplus_j10WEIGHT - \
JISX0213.2000-1 12 warabi12-2000-1 warabi12-2000-1 warabi12-2000-1 warabi12-2000-1 \
JISX0213.2000-1 14 k14-2000-1 k14-2000-1 k14-2000-1 k14-2000-1 \
JISX0213.2000-2 14 k14-2000-2 k14-2000-2 k14-2000-2 k14-2000-2 \
JISX0213.2000-1 16 jiskan16-2000-1 jiskan16-2000-1 jiskan16-2000-1 jiskan16-2000-1 \
JISX0213.2000-2 16 jiskan16-2000-2 jiskan16-2000-2 jiskan16-2000-2 jiskan16-2000-2 \
JISX0213.2000-1 24 jiskan24-2000-1 jiskan24-2000-1 jiskan24-2000-1 jiskan24-2000-1 \
JISX0213.2000-2 24 jiskan24-2000-2 jiskan24-2000-2 jiskan24-2000-2 jiskan24-2000-2 \
JISX0213.2003-1 24 jiskan24-2003-1 jiskan24-2003-1 jiskan24-2003-1 jiskan24-2003-1 \
> fonts.alias
mkdir BDFS
for src in *.bdf; do
    bdftopcf $src | gzip -9 > ${src%.bdf}.pcf.gz && mv $src BDFS/
done
popd

%install

install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0755 -d $RPM_BUILD_ROOT%{cidmapdir}

## jisksp14
install -m 0644 -p jisksp14.pcf* $RPM_BUILD_ROOT%{_fontdir}/

## kappa20

## knm_new
for i in knmhn12x.bdf knmzn12x.bdf; do
    bdftopcf $i | gzip -9 > $RPM_BUILD_ROOT%{_fontdir}/`basename $i | sed -e 's/.bdf/.pcf.gz/'`
done

## fonts-ja
### remove an unnecessary file
rm -f fonts-ja/mplus_cursors.pcf.gz
for i in fonts-ja/*.pcf.gz; do
    install -m 0644 -p $i $RPM_BUILD_ROOT%{_fontdir}/`basename $i`
done

# for ghostscript
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{cidmapdir}/
install -m 0644 -p %{SOURCE3} $RPM_BUILD_ROOT%{cidmapdir}/
install -m 0644 -p %{SOURCE4} $RPM_BUILD_ROOT%{cidmapdir}/

# Create fonts.scale and fonts.dir
/usr/bin/mkfontdir $RPM_BUILD_ROOT%{_fontdir}
# for dummy
touch $RPM_BUILD_ROOT%{_fontdir}/encodings.dir

install -m 0644 -p fonts-ja/fonts.alias $RPM_BUILD_ROOT%{_fontdir}/

# Install catalogue symlink
install -m 0755 -d $RPM_BUILD_ROOT%{cataloguedir}
ln -sf %{_fontdir} $RPM_BUILD_ROOT%{cataloguedir}/%{fontname}
sed -i -e s,%{_datadir}/fonts/,%{_datadir}/fonts/ttf/,g %buildroot/usr/share/ghostscript/conf.d/*
# lowercase to befriend repocop tests
sed -i -e 's,\(^.*$\),\L\1,' `find %buildroot/usr/share/fonts -name fonts.alias`
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
%{_fontbasedir}/*/%{_fontstem}/*.pcf.gz

%doc doc.orig readme.kaname_bdf
%doc fonts-ja/COPYRIGHT* fonts-ja/README* fonts-ja/LICENSE* fonts-ja/ALLFONTS.txt
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/fonts.alias
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/fonts.dir
%ghost %verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/encodings.dir
%{cidmapdir}/FAPIcidfmap.ja
%{cidmapdir}/cidfmap.ja
%{cidmapdir}/CIDFnmap.ja
%{cataloguedir}/*

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080710-alt2_11
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080710-alt1_11
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080710-alt1_10
- initial release by fcimport

