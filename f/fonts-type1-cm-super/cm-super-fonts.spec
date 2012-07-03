%define type1fontsdir %_datadir/fonts/type1/cm-super

Name: fonts-type1-cm-super
Version: 0.3.3
Release: alt8.qa1
Summary: Cyrillic Type 1 EC/TC and LH fonts
Group: Publishing
License: GPL

PreReq: %name-pfb = %version-%release, %name-afm = %version-%release
Obsoletes: cm-super-fonts
Provides: cm-super-fonts = %version-%release

Source: cm-super-%version.tar.bz2

BuildArch: noarch
BuildRequires: tex-common
BuildRequires: mkfontscale

%package pfb
Summary: Cyrillic Type 1 EC/TC and LH fonts in pfb format
Group: Publishing
Provides: fonts-cm-super cm-super-fonts-pfb = %version-%release
Obsoletes: fonts-cm-super cm-super-fonts
PreReq: fontconfig >= 2.4.2

%package afm
Summary: AFM metrics for Cyrillic Type 1 EC/TC and LH fonts
Group: Publishing
PreReq: %name-pfb = %version-%release
Provides: fonts-cm-super-afm cm-super-fonts-afm = %version-%release
Obsoletes: fonts-cm-super-afm cm-super-fonts-afm

%package tex
Summary: TeX support for Cyrillic Type 1 EC/TC and LH fonts
Group: Publishing
PreReq: %name-tex-dvips = %version-%release, %name-pfb = %version-%release
Provides: fonts-cm-super-tex cm-super-fonts-tex = %version-%release
Obsoletes: fonts-cm-super-tex cm-super-fonts-tex

%package tex-dvips
Summary: Encoding files for TeX support for Cyrillic Type 1 EC/TC and LH fonts
Group: Publishing
Provides: fonts-cm-super-tex-dvips cm-super-fonts-tex-dvips = %version-%release
Obsoletes: fonts-cm-super-tex-dvips cm-super-fonts-tex-dvips

%package tex-afm
Summary: AFM metrics for TeX support for Cyrillic Type 1 EC/TC and LH fonts
Group: Publishing
PreReq: %name-tex = %version-%release
Provides: fonts-cm-super-tex-afm cm-super-fonts-tex-afm = %version-%release
Obsoletes: fonts-cm-super-tex-afm cm-super-fonts-tex-afm

%description 
The cm-super package contains Type 1 fonts converted from METAFONT
fonts and covers entire EC/TC and LH fonts (Computer Modern font
families). All European and Cyrillic writings are covered. Each Type 1
font program contains ALL glyphs from the following standard LaTeX
font encodings: T1, TS1, T2A, T2B, T2C, X2, and also Adobe
StandardEncoding (583 glyphs per non-SC font and 466 glyphs per SC
font), and could be reencoded to any of these encodings using standard
dvips or pdftex facilities (the corresponding support files are 
included in %name-tex package).

%description pfb
The %name-pfb package contains Type 1 fonts in pfb format,
converted from METAFONT fonts and covers entire EC/TC and LH fonts
(Computer Modern font families).
All European and Cyrillic writings are covered. Each Type 1
font program contains ALL glyphs from the following standard LaTeX
font encodings: T1, TS1, T2A, T2B, T2C, X2, and also Adobe
StandardEncoding (583 glyphs per non-SC font and 466 glyphs per SC
font), and could be reencoded to any of these encodings using standard
dvips or pdftex facilities (the corresponding support files are 
included in %name-tex package).

%description afm
The %name-afm package contains Adobe Font Metrics for Type 1 fonts converted 
from METAFONT fonts which cover entire EC/TC and LH fonts (Computer Modern font
families). All European and Cyrillic writings are covered. Each Type 1
font program contains ALL glyphs from the following standard LaTeX
font encodings: T1, TS1, T2A, T2B, T2C, X2, and also Adobe
StandardEncoding (583 glyphs per non-SC font and 466 glyphs per SC
font), and could be reencoded to any of these encodings using standard
dvips or pdftex facilities (the corresponding support files are
included in %name-tex package).

%description tex
The %name-tex package contains TeX support files for Type 1 fonts converted 
from METAFONT fonts which cover entire EC/TC and LH fonts (Computer Modern font
families). All European and Cyrillic writings are covered. Each Type 1
font program contains ALL glyphs from the following standard LaTeX
font encodings: T1, TS1, T2A, T2B, T2C, X2, and also Adobe
StandardEncoding (583 glyphs per non-SC font and 466 glyphs per SC
font), and could be reencoded to any of these encodings using standard
dvips or pdftex facilities (the corresponding support files are also
included).

%description tex-dvips
The %name-tex package contains encoding files for Type 1 fonts converted 
from METAFONT fonts which cover entire EC/TC and LH fonts (Computer Modern font
families). All European and Cyrillic writings are covered. Each Type 1
font program contains ALL glyphs from the following standard LaTeX
font encodings: T1, TS1, T2A, T2B, T2C, X2, and also Adobe
StandardEncoding (583 glyphs per non-SC font and 466 glyphs per SC
font), and could be reencoded to any of these encodings using standard
dvips or pdftex facilities (the corresponding support files are also
included).

%description tex-afm
The %name-tex-afm package contains Adobe Font Metrics for Type 1 fonts converted 
from METAFONT fonts which cover entire EC/TC and LH fonts (Computer Modern font
families). All European and Cyrillic writings are covered. Each Type 1
font program contains ALL glyphs from the following standard LaTeX
font encodings: T1, TS1, T2A, T2B, T2C, X2, and also Adobe
StandardEncoding (583 glyphs per non-SC font and 466 glyphs per SC
font), and could be reencoded to any of these encodings using standard
dvips or pdftex facilities (the corresponding support files are
included in %name-tex package).

%prep
%setup -q -n cm-super

%install
# Directories for cm-super fonts
%__mkdir -p %buildroot/%_datadir/texmf/fonts/{type1,afm}/public
%__mkdir -p %buildroot/%_datadir/texmf/dvips/{config,base}
%__mkdir -p %buildroot/%type1fontsdir/afms
%__mkdir -p %buildroot/%_sysconfdir/tex-fonts.d

# Install cm-super fonts
%__cp pfb/* %buildroot%type1fontsdir
%__cp afm/* %buildroot%type1fontsdir/afms/
pushd %buildroot%type1fontsdir
    gunzip afms/*.gz
    cd afms
    for i in *.afm ; do
	%__ln_s afms/$i %buildroot%type1fontsdir/$i
    done	
popd    
%__ln_s %type1fontsdir %buildroot/%_datadir/texmf/fonts/type1/public/cm-super
%__ln_s %type1fontsdir/afms %buildroot/%_datadir/texmf/fonts/afm/public/cm-super

mkdir -p %buildroot/%_sysconfdir/texmf/updmap.d
mkdir -p %buildroot%_datadir/texmf/fonts/map/dvips/cm-super
mkdir -p %buildroot%_datadir/texmf/fonts/enc/dvips/cm-super
pushd dvips
    for i in *.map ; do
	echo "Map $i" >> %buildroot/%_sysconfdir/tex-fonts.d/cm-super.cfg
	echo "Map $i" >> %buildroot/%_sysconfdir/texmf/updmap.d/30-cm-super.cfg
	%__cp $i %buildroot%_datadir/texmf/dvips/config/
	   cp $i %buildroot%_datadir/texmf/fonts/map/dvips/cm-super/
    done
    %__cp *.enc %buildroot%_datadir/texmf/dvips/base/
       cp *.enc %buildroot%_datadir/texmf/fonts/enc/dvips/cm-super/
popd


mkfontscale %buildroot%type1fontsdir
ln -s fonts.scale %buildroot%type1fontsdir/fonts.dir

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../../%type1fontsdir %buildroot%_sysconfdir/X11/fontpath.d/type1-cm-super:pri=40

%post pfb
%_bindir/fc-cache %type1fontsdir ||:

%files

%files pfb
%doc README ChangeLog COPYING TODO FAQ
%_sysconfdir/X11/fontpath.d/*
%dir %type1fontsdir
%type1fontsdir/*.pfb
%type1fontsdir/fonts.dir
%type1fontsdir/fonts.scale

%files afm
%dir %type1fontsdir/afms
%type1fontsdir/*.afm
%type1fontsdir/afms/*.afm

%files tex-afm
%_datadir/texmf/fonts/afm/public/cm-super

%files tex-dvips
%_datadir/texmf/dvips/base/*
%_datadir/texmf/fonts/enc/dvips/cm-super

%files tex
%_datadir/texmf/dvips/config/*
%_datadir/texmf/fonts/type1/public/cm-super
%_sysconfdir/tex-fonts.d/cm-super.cfg
%_datadir/texmf/fonts/map/dvips/cm-super
%_sysconfdir/texmf/updmap.d/30-cm-super.cfg

%changelog
* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.3.3-alt8.qa1
- NMU (by repocop): the following fixes applied:
  * altlinux-policy-tex-obsolete-util-calls-in-post for fonts-type1-cm-super-tex
  * altlinux-policy-tex-obsolete-util-calls-in-post for fonts-type1-cm-super-tex-dvips
  * altlinux-policy-tex-obsolete-util-calls-in-post for fonts-type1-cm-super-tex-afm
  * postclean-05-filetriggers for spec file

* Thu Feb 19 2009 Grigory Batalov <bga@altlinux.ru> 0.3.3-alt8
- tetex-core requirements (post, postun) were removed as they are
  automatically calculated.
- Maps and encodings are copied to the new standard place.

* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.3.3-alt7
- rebuild with fonts policy

* Wed Nov 27 2002 AEN <aen@altlinux.ru> 0.3.3-alt6
- package renamed to cm-super-fonts and virtualized
- new package pfb
- pfb's moved to %type1fontsdir
- afm's moved to %type1fontsdir/afms, symlinks in %type1fontsdir

* Wed Nov 27 2002 Alexander Bokovoy <ab@altlinux.ru> 0.3.3-alt5
- %name-tex: fixed missed dependence on %name.
- Corrected dependencies on tetex-core.

* Mon Nov 25 2002 Alexander Bokovoy <ab@altlinux.ru> 0.3.3-alt4
- Move dvips encoding files to %name-tex-dvips (these encoding
  files are shared among other font packages as well)

* Sun Nov 24 2002 Alexander Bokovoy <ab@altlinux.ru> 0.3.3-alt3
- Fix dependency loop in fonts-cm-super-tex

* Fri Nov 22 2002 Alexander Bokovoy <ab@altlinux.ru> 0.3.3-alt2
- Fix postinstall scripts

* Thu Nov 21 2002 Alexander Bokovoy <ab@altlinux.ru> 0.3.3-alt1
- Initial packaging


