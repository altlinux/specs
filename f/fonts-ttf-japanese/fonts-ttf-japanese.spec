Epoch: 1
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define src_version 20121001
%define src_name    umeplus-fonts

Summary:	Japanese TrueType fonts
Name:		fonts-ttf-japanese
Version:	0.%{src_version}
Release:	alt1_6
License:	Distributable
URL:		http://www.geocities.jp/ep3797/modified_fonts_01.html
Group:		System/Fonts/True type
Source0:	http://downloads.sourceforge.net/mdk-ut/%{src_name}-%{src_version}.tar.lzma
Source3:	cidinst.japanese
Source4:	cidunin.japanese

BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	ttmkfdir
Obsoletes:	xtt-fonts
Provides:	xtt-fonts
Source44: import.info

%description
This Package provides Free Japanese TrueType fonts (umeplus-gothic, 
umeplus-p-gothic)

%description -l ru_RU.UTF-8
Пакет предоставляет японские TrueType шрифты. 

%prep
%setup -q -n %{src_name}-%{src_version}

%install
mkdir -p %buildroot/%{_datadir}/fonts/TTF/japanese
install -m 644 *.ttf %buildroot/%{_datadir}/fonts/TTF/japanese

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/japanese \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-japanese:pri=50

%files
%doc ChangeLog README
%doc docs-*/

%dir %_datadir/fonts/TTF/japanese/
%_datadir/fonts/TTF/japanese/*.ttf
%_sysconfdir/X11/fontpath.d/ttf-japanese:pri=50




%changelog
* Wed Dec 06 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.20121001-alt1_6
- added umeplus fonts from mageia

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt10
- dropped original Wadalab font kit as Sazanami fonts succeed it.
- made a virtual compat package

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt9
- replaced Kochi fonts with Sazanami fonts

* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt8
- rebuild with fonts policy
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Mon Jul 11 2005 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt7
- link to encodings.dir removed, no longer requires freetype

* Thu Dec 16 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt6
- link to encodings.dir fixed

* Sat Jun 26 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt5
- %postun script fix

* Wed Feb 18 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt4
- %postun script fix

* Wed Sep 03 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt3
- CID support fixed

* Sun Aug 24 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt2
- Changed dir
- Cleanups

* Wed May 07 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt1.1
- added CID support (japanese support for ghostscript )

* Wed Nov 27 2002 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build
