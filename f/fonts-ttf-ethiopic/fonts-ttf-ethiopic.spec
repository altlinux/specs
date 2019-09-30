# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:	Ethiopic TrueType fonts
Name:		fonts-ttf-ethiopic
Version:	1.0
Release:	alt1_17
License:	GPL
Group:		System/Fonts/True type
# GFZemen unicode font from
# ftp://ftp.ethiopic.org/pub/fonts/TrueType/gfzemenu.ttf
# the site seems gone now
Source0:	fonts-ttf-ethiopic.tar.bz2

BuildArch:	noarch
BuildRequires:	mkfontscale
Source44: import.info

%description
This Package provides Free Ethiopic TrueType fonts.

%prep

%setup -q -n %{name}

%install
mkdir -p %buildroot/%{_datadir}/fonts/ttf/ethiopic/
cp *.ttf %buildroot/%{_datadir}/fonts/ttf/ethiopic/

(
cd %buildroot/%{_datadir}/fonts/ttf/ethiopic/
mkfontscale > fonts.scale
cp fonts.scale fonts.dir
)

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/ttf/ethiopic \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-ethiopic:pri=50

%files
%dir %{_datadir}/fonts/ttf/ethiopic/
%{_datadir}/fonts/ttf/ethiopic/*
%_sysconfdir/X11/fontpath.d/ttf-ethiopic:pri=50





%changelog
* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_17
- new version

