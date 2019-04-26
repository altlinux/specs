%define ttfdir %_datadir/fonts/ttf/google-literata

Name: fonts-ttf-google-literata
Version: 2.100
Release: alt1

Summary: Google Literata fonts for e-books
License: OFL
Group: System/Fonts/True type

Url: https://github.com/googlefonts/literata
Source: Literata-v2.100.zip

BuildArch: noarch

PreReq: fontconfig >= 2.4.2
BuildRequires: unzip

%description
This package contains Google Literata fonts
optimized for e-books and e-ink display.

%package -n fonts-ttf-google-literata-vf
Summary: Google Literata variable fonts for e-books
License: OFL
Group: System/Fonts/True type

%description -n fonts-ttf-google-literata-vf
This package contains Google Literata variable fonts for e-books.

%prep
%setup -q -c

%build

%install
mkdir -p %buildroot%ttfdir/ %buildroot%{ttfdir}-vf/
install -p -m644 ttfs/*.ttf %buildroot%ttfdir/
install -p -m644 variable/*.ttf %buildroot%{ttfdir}-vf/

%files
%doc OFL.txt
%ttfdir

%files -n fonts-ttf-google-literata-vf
%{ttfdir}-vf

%changelog
* Fri Apr 26 2019 Igor Vlasenko <viy@altlinux.ru> 2.100-alt1
- Initial build.

