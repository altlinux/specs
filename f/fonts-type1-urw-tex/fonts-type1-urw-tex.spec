%define fontsbase public/urwcyr
%define texpackname urwcyr

Name: fonts-type1-urw-tex
Version: 2.0
Release: alt8
Packager: Grigory Batalov <bga@altlinux.org>

Summary: Using cyrillic URW fonts in TeX.
License: GPL
Group: Publishing
Url: none

BuildArch: noarch

Source: %name-%version.tar
Patch0: urw-tex-%version-alt.patch
Patch1: urw-tex-%version-path.patch

Requires: urw-fonts = %version
AutoReq: yes, nosymlinks
Requires: fonts-type1-urw fonts-type1-cm-super-tex-dvips
Provides: urw-tex = %version
Obsoletes: urw-tex <= %version

# Automatically added by buildreq on Tue Oct 13 2009
BuildRequires: fonts-type1-cm-super-tex-dvips
BuildRequires: texlive-base-bin texlive-font-utils
BuildRequires(pre): rpm-build-texmf

%package doc
Summary: TeX and LaTeX samples for usage of URW fonts in TeX
Group: Publishing
Requires: %name = %version-%release
Provides: urw-tex-doc = %version
Obsoletes: urw-tex-doc <= %version

%package afm
Summary: AFM metrics for URW fonts in TeX
Group: Publishing
Requires: %name = %version-%release
AutoReq: yes, nosymlinks
Requires: fonts-type1-urw
Provides: urw-tex-afm = %version
Obsoletes: urw-tex-afm <= %version

%description
A bunch of links, metrics and styles to easily use cyrillized URW Type1 fonts
in TeX. For styles see %_texmfmain/tex/latex/urwcyr; most probably, you'll
have to insert "\usepackage{urwcyr}" into your LaTeX document preamble.

%description afm
AFM metrics for URW fonts in TeX

%description doc
TeX and LaTeX samples for usage of URW fonts in TeX

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
./build.sh
pushd dvips/config
mv -f urw-cm-super-t1.map urw-t1.map
mv -f urw-cm-super-t2a.map urw-t2a.map
popd
pushd dvipdfm/config
mv * ../
cd ..
rm -rf config
popd
pushd tex/latex/urwcyr
	for fd in ot1*.fd; do
		cp $fd $(echo $fd|sed -e "s/^o//")
	done
	sed -i -e "s/[oO]\([tT]1\)/\1/" t1*.fd
popd

%install

mkdir -p %buildroot%_texmfmain
cp -Rd * %buildroot%_texmfmain/

mkdir -p %buildroot%_sysconfdir/tex-fonts.d
echo "Map urw-t1.map" > %buildroot%_sysconfdir/tex-fonts.d/urw-tex.cfg
echo "Map urw-t2a.map" >> %buildroot%_sysconfdir/tex-fonts.d/urw-tex.cfg

mkdir -p %buildroot/%_sysconfdir/texmf/updmap.d
echo "Map urw-t1.map" > %buildroot/%_sysconfdir/texmf/updmap.d/30-urw.cfg
echo "Map urw-t2a.map" >> %buildroot/%_sysconfdir/texmf/updmap.d/30-urw.cfg

mkdir -p %buildroot%_texmfmain/fonts/map/dvips/urw
cp dvips/config/*.map %buildroot%_texmfmain/fonts/map/dvips/urw/
mkdir -p %buildroot%_texmfmain/fonts/map/dvipdf/urw
cp dvipdfm/*.map %buildroot%_texmfmain/fonts/map/dvipdf/urw/

%files afm
%dir %_texmfmain/fonts/afm/%fontsbase
%_texmfmain/fonts/afm/%fontsbase/*

%files doc
%dir %_texmfmain/doc/%texpackname
%_texmfmain/doc/%texpackname/*

%files
%_sysconfdir/tex-fonts.d/urw-tex.cfg
%_sysconfdir/texmf/updmap.d/30-urw.cfg
%_texmfmain/dvipdfm/*
%_texmfmain/dvips/config/*
%dir %_texmfmain/fonts/tfm/%fontsbase
%_texmfmain/fonts/tfm/%fontsbase/*
%dir %_texmfmain/fonts/type1/%fontsbase
%_texmfmain/fonts/type1/%fontsbase/*
%dir %_texmfmain/tex/latex/urwcyr
%_texmfmain/tex/latex/urwcyr/*
%_texmfmain/fonts/map/dvips/urw
%_texmfmain/fonts/map/dvipdf/urw
%doc readme-motygin
%doc problem
%doc license-motygin
%doc README
%doc LICENSE

%changelog
* Wed Oct 14 2009 Grigory Batalov <bga@altlinux.ru> 2.0-alt8
- Rename to fonts-type1-urw-tex according to TeXPolicy.
- Rebuild with texlive.

* Fri Jan 23 2009 Eugene Ostapets <eostapets@altlinux.ru> 2.0-alt7
- fix broken symlinks to /usr/share/fonts/default/Type1/*
- close #12990

* Sat May 1 2004 Viktor S. Grishchenko <gritzko@altlinux.ru> 2.0-alt6
- T1 family description patch by Yurix <yurix@altlinux.org>

* Fri Jan 17 2003 Alexander Bokovoy <ab@altlinux.ru> 2.0-alt5
- Rebuild against tetex-2.0-alt0.8 since dvipdfm is now part
  of tetex-core and its texmf subtree changed a structure

* Mon Nov 25 2002 Alexander Bokovoy <ab@altlinux.ru> 2.0-alt4
- Rebuild against tetex-2.0
- Split on subpackages

* Sun Jun 10 2002 Viktor S. Grichenko <gritzko@ural.ru> 2.0-alt3
- Merged (+ perl generation script)

* Fri Jun 07 2002 Alexander Bokovoy <ab@altlinux.ru> 2.0-alt2
- Changed to confirm ALT Linux packaging policy
- Added pdftex support

* Sat Jun 01 2002 Viktor S. Grichenko <gritzko@ural.ru> 0.1-1vsg
- spec file created

