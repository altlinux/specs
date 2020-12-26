# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:	OpenDesktop.Org.tw Font -- Simplified and Traditional Chinese and Japanese Ming and Kai Face
Name:		fonts-ttf-chinese-opendesktop
Version:	1.6.100
Release:	alt1_12
# Extracted from ftp://opensource.nchc.org.tw/odp/others/fc17/SRPMS/opendesktop-fonts-1.6.100-1.fc17.src.rpm
Source0:	opendesktop-fonts-%{version}.tar.bz2
URL:		http://www.opendesktop.org.tw/
License:	Arphic Public License
Group:		System/Fonts/True type
BuildArch:	noarch
BuildRequires: 	fontconfig
Requires(post): mkfontdir, mkfontscale
Requires(postun): mkfontdir, mkfontscale
Obsoletes:	fonts-ttf-chinese-compat
Provides:	fonts-ttf-chinese-compat = %{version}-%{release}

Source1:	69-odofonts.conf
Source2:	80-odohei.conf
Source3:	80-odokai.conf
Source4:	80-odosung.conf
Source44: import.info

%description
OpenDesktop.Org.tw Font -- Simplified and Traditional Chinese and Japanese
Ming and Kai Face, based on Chinese and Japanese TTF Fonts donated by
Arphic company.

%package -n fonts-ttf-default-zh_TW
Summary: Virtual package providing default zh_TW fonts
Group: System/Fonts/True type
Requires: %{name} = %{version}

%description -n fonts-ttf-default-zh_TW
This package provides default TrueType font for zh_TW locale.

%prep
%setup -q -n opendesktop-fonts-%{version} 
sed -i s,/usr/share/fonts/opendesktop/TrueType,/usr/share/fonts/ttf/chinese-opendesktop, *map.zh_??

%install
install -d %{buildroot}/%{_datadir}/fonts/ttf/chinese-opendesktop/
install -m 644 odosung.ttc %{buildroot}/%{_datadir}/fonts/ttf/chinese-opendesktop/
install -m 644 odokai.ttf %{buildroot}/%{_datadir}/fonts/ttf/chinese-opendesktop/
install -m 644 odohei.ttf %{buildroot}/%{_datadir}/fonts/ttf/chinese-opendesktop/

install -d %{buildroot}%{_datadir}/fontconfig/conf.avail/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/fontconfig/conf.avail/
install -m 644 80-odofonts-original.conf %{buildroot}%{_datadir}/fontconfig/conf.avail/
install -m 644 80-odofonts-simulate-MS-simplified-chinese.conf %{buildroot}%{_datadir}/fontconfig/conf.avail/
install -m 644 80-odofonts-simulate-MS-traditional-chinese.conf %{buildroot}%{_datadir}/fontconfig/conf.avail/
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/fontconfig/conf.avail/
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/fontconfig/conf.avail/
install -m 644 %{SOURCE4} %{buildroot}%{_datadir}/fontconfig/conf.avail/

# for ghostscript
install -d %{buildroot}/%{_datadir}/ghostscript/conf.d/
install -m 0644 FAPIcidfmap.zh_TW %{buildroot}/%{_datadir}/ghostscript/conf.d/
install -m 0644 FAPIcidfmap.zh_CN %{buildroot}/%{_datadir}/ghostscript/conf.d/
install -m 0644 cidfmap.zh_TW %{buildroot}/%{_datadir}/ghostscript/conf.d/
install -m 0644 cidfmap.zh_CN %{buildroot}/%{_datadir}/ghostscript/conf.d/
install -m 0644 CIDFnmap.zh_TW %{buildroot}/%{_datadir}/ghostscript/conf.d/
install -m 0644 CIDFnmap.zh_CN %{buildroot}/%{_datadir}/ghostscript/conf.d/

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/ttf/chinese-opendesktop \
    %{buildroot}%_sysconfdir/X11/fontpath.d/chinese-opendesktop:pri=50

%post
[ -x %{_bindir}/mkfontdir ] && %{_bindir}/mkfontdir %{_datadir}/fonts/ttf/chinese-opendesktop
[ -x %{_bindir}/mkfontscale ] && %{_bindir}/mkfontscale %{_datadir}/fonts/ttf/chinese-opendesktop

%postun
if [ "$1" = "0" ]; then
  [ -x %{_bindir}/mkfontdir ] && %{_bindir}/mkfontdir %{_datadir}/fonts/ttf/chinese-opendesktop
  [ -x %{_bindir}/mkfontscale ] && %{_bindir}/mkfontscale %{_datadir}/fonts/ttf/chinese-opendesktop
fi

%files
%doc Changelog Changelog.zh_TW AUTHORS COPYRIGHT license
%dir %{_datadir}/fonts/ttf/chinese-opendesktop/
%{_datadir}/fonts/ttf/chinese-opendesktop/*.ttf
%{_datadir}/fonts/ttf/chinese-opendesktop/*.ttc
%{_sysconfdir}/X11/fontpath.d/chinese-opendesktop:pri=50
%{_datadir}/fontconfig/conf.avail/*
%{_datadir}/ghostscript/conf.d/*

%changelog
* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 1.6.100-alt1_12
- update by mgaimport

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.6.100-alt1_11
- update by mgaimport

* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.100-alt1_8
- new version

