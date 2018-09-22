Name:		geany-themes
Version:	1.24
Release:	alt1
Summary:	A collection of syntax highlighting color schemes for Geany
Group:		Development/Tools
URL:		https://github.com/geany/geany-themes

# Some of the color schemes are clearly stated as GPLv2+, some are BSD
License:	GPLv2+ and BSD

# https://github.com/geany/geany-themes/releases/download/1.24/geany-themes-1.24.tar.bz2
Source:		%{name}-%{version}.tar

Requires:	geany >= 1.24
BuildArch:	noarch

%description
Geany-Themes is a set of syntax highlighting color schemes for the Geany IDE.
Simply install this package, restart Geany and find the themes in
View->Editor->Color Schemes.

%prep
%setup

%build
# Nothing to build here. We just have to place some configuraton files into the
# proper directory..

%install
install -d %buildroot/%{_datadir}/geany/colorschemes
install -pm 644 colorschemes/*.conf %buildroot/%{_datadir}/geany/colorschemes

%files
%doc AUTHORS COPYING README.md
%_datadir/geany/colorschemes/*.conf

%changelog
* Sat Sep 22 2018 Alexey Appolonov <alexey@altlinux.org> 1.24-alt1
- Initial ALT Linux release.
