# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define name_orig	ae_fonts
%define fontdir	fonts/ttf/arabic/arabeyes

Name:		fonts-ttf-arabic-arabeyes
Summary:	Arabic TrueType fonts
Version:	2.0
Release:	alt1_12
License:	GPLv2+
Group:		System/Fonts/True type
Source:		http://prdownloads.sourceforge.net/arabeyes/%{name_orig}_%{version}.tar.bz2
URL:		http://www.arabeyes.org/project.php?proj=Khotot
BuildArch:	noarch
Buildrequires: 	mkfontscale
Provides:	fonts-ttf-arabic
Source44: import.info

%description
This Package provides Free Arabic TrueType fonts donated under the GPL license
by arabeyes.org.

%prep
%setup -n %{name_orig}_%version -q

%build

%install
mkdir -p %buildroot/%_datadir/%fontdir
cp */*.ttf %buildroot/%_datadir/%fontdir

pushd %buildroot/%_datadir/%fontdir
mkfontscale
cp fonts.scale fonts.dir
popd

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/%fontdir \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-arabic-arabeyes:pri=50

%post
touch %{_datadir}/fonts/ttf

%files
%doc README ChangeLog
%dir %_datadir/%fontdir
%_datadir/%fontdir/*
%_sysconfdir/X11/fontpath.d/ttf-arabic-arabeyes:pri=50





%changelog
* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_12
- new version

