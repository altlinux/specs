# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary: Tifinagh TTF font(s)
Name: fonts-ttf-tifinagh
Version: 1.0
Release: alt1_13
License: Free use and distribution
Group: System/Fonts/True type
Source0: hapaxber.ttf
Source1: inventaire-des-oeils.pdf
BuildArch:	noarch
BuildRequires:	ttmkfdir
Source44: import.info

%description
This package contains fonts for the Tifinagh script,
as encoded in unicode.

%prep
%setup -cT %{name}-%{version}
cp %{SOURCE1} .

cat << EOF > README.txt
The "Hapax Berbère" font was used as the reference font for
the proposal of inclusion of tifinagh script into Unicode BMP;
its autor, Patrick Andries hapax(at)iquebec.com, kindly released
as freely usable and distributable.

The PDF file inventaire-des-oeils.pdf gives the list of all the glyphs
in the font (there are various glyph variants and ligatures on private
use area too)
EOF

%install
install -D %{SOURCE0} %buildroot/%{_datadir}/fonts/ttf/tifinagh/hapaxber.ttf

%post
touch %{_datadir}/fonts/ttf

%files
%doc inventaire-des-oeils.pdf
%doc README.txt
%dir %{_datadir}/fonts/ttf/tifinagh
%{_datadir}/fonts/ttf/tifinagh/*.ttf


%changelog
* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_13
- new version

