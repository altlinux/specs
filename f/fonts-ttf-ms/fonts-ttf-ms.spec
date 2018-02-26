%define fname ms

Name: fonts-ttf-ms
Version: 1.0
Release: alt4

Summary: Unicode True Type fonts from MS
Summary (ru_RU.UTF-8): Unicode True Type шрифты от Микрософт 
License: free to use, but restricted (see EULA)
Group: System/Fonts/True type
Url: http://telia.dl.sourceforge.net/sourceforge/corefonts

Source0: ms_eula.htm
Source1: arial32.exe
Source2: arialb32.exe
Source3: times32.exe
Source4: courie32.exe
Source5: andale32.exe
Source6: comic32.exe
Source7: georgi32.exe
Source8: impact32.exe
Source9: trebuc32.exe
Source10: verdan32.exe
Source11: webdin32.exe
Source12: wd97vwr32.exe

BuildArch: noarch

PreReq: fontconfig >= 2.4.2 cabextract >= 0.6
BuildRequires: rpm-build-fonts >= 0.3
BuildRequires: cabextract >= 0.6

Obsoletes: ms-ttf ms-fonts-ttf
Provides: ms-ttf ms-fonts-ttf

%description
A set of Unicode True Type fonts from MS

%description -l ru_RU.UTF-8
Набор Unicode True Type шрифтов от Микрософт.

%prep
%setup -T -c %name-%version
cp %SOURCE0 .
cp %SOURCE1 .
cp %SOURCE2 .
cp %SOURCE3 .
cp %SOURCE4 .
cp %SOURCE5 .
cp %SOURCE6 .
cp %SOURCE7 .
cp %SOURCE8 .
cp %SOURCE9 .
cp %SOURCE10 .
cp %SOURCE11 .
cp %SOURCE12 .

%build
for i in *32.exe ; do
	%_bindir/cabextract -L $i >/dev/null 2>&1
done
%_bindir/cabextract -L viewer1.cab >/dev/null 2>&1

%install
%ttf_fonts_install %fname
install -m644 *32.exe %buildroot%__currentfontsdir
# add ghost for ttf files
%__subst "s|\(.*ttf\)\$|%%ghost \1|g" %fname.files

%post
cd %__currentfontsdir
for i in *32.exe ; do
	%_bindir/cabextract -L $i >/dev/null 2>&1
done
%_bindir/cabextract -L viewer1.cab >/dev/null 2>&1
find ! -name \*.ttf -a ! -name fonts.\* -delete ||:

%files  -f %fname.files
%doc ms_eula.htm
%__currentfontsdir/*.exe

%changelog
* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt4
- use rpm-build-fonts
- cleanup spec, build in separate dir
- remove create links, mkscale from post script

* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt3
- fixed trigger logic

* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt2
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath
- use redistributable word 97 viewer as source for tahoma.ttf

* Thu Jan 04 2007 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- /usr/share/fonts/default/TrueType-ms -> /usr/share/fonts/ttf/ms
- package name changed

* Mon Jul 11 2005 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt13
- link to encodings.dir removed, no longer requires freetype

* Thu Dec 16 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt12
- link to encodings.dir fixed

* Wed Feb 18 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt11
- %postun script fix

* Fri Jan 30 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt10
- ttf permissions fix

* Wed Jan 28 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt9
- Directory removal and encodings.dir symlink fixes

* Tue Jan 27 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt8
- DLLs removed

* Thu Sep 04 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt7
- Full set of MS fonts (andale32.exe, comic32.exe, georgi32.exe, impact32.exe, trebuc32.exe, verdan32.exe, webdin32.exe)

* Wed Aug 27 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt6
- Changed dir
- Cleanups (removed obsolete gnome-font-install and xftcache calls, fontconfig)
- Requirements fixed
- Translation
- Renamed to ms-fonts-ttf

* Mon Oct 07 2002 AEN <aen@altlinux.ru> 1.0-alt5
- fc-cache & gnome-font install added in %post

* Wed Sep 25 2002 AEN <aen@altlinux.ru> 1.0-alt4
- built with cabextract-0.6

* Wed Sep 25 2002 AEN <aen@altlinux.ru> 1.0-alt3
- build rpm with fonts

* Thu Nov 01 2001 Sergey Vlasov <vsu@altlinux.ru> 1.0-alt2
- convert file names to lower case

* Mon Jul 16 2001 AEN <aen@logic.ru> 1.0-alt1
- build for Sisyphus
