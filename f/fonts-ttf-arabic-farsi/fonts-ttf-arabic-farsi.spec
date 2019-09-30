# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define name_orig farsifonts
%define fontdir	fonts/ttf/arabic/farsi

Name:		fonts-ttf-arabic-farsi
Summary:	Arabic TrueType fonts
Version:	0.4
Release:	alt1_16
License:	GPL
Group:		System/Fonts/True type
Source:		http://www.farsiweb.info/font/%{name_orig}-%{version}.tar.bz2
URL:		http://www.farsiweb.info
BuildArch:	noarch
BuildRequires:	mkfontscale
Provides:	fonts-ttf-arabic
Source44: import.info

%description
This Package provides Free Arabic TrueType fonts donated under the GPL license
by farsiweb.info.

%prep
%setup -n %name_orig-%version -q

%build

%install
mkdir -p %buildroot/%_datadir/%fontdir
cp *.ttf %buildroot/%_datadir/%fontdir

pushd %buildroot/%_datadir/%fontdir
mkfontscale
cp fonts.scale fonts.dir
popd

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/%fontdir \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-arabic-farsi:pri=50

%files
%doc COPYING NEWS *.txt
%dir %_datadir/%{fontdir}
%_datadir/%{fontdir}/*
%_sysconfdir/X11/fontpath.d/ttf-arabic-farsi:pri=50






%changelog
* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_16
- new version

