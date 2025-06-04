Name:    libsvgpp-devel
Version: 1.3.1
Release: alt1

Summary: C++ SVG library

License: BSL-1.0
Group:   Development/C
Url:     https://github.com/svgpp/svgpp

Packager: Grigory Ustinov <grenka@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

%description
SVG++ library can be thought of as a framework, containing parsers for various
SVG syntaxes, adapters that simplify handling of parsed data and a lot of other
utilities and helpers for the most common tasks.

%prep
%setup

%build

%install
install -m 755 -d %buildroot%_includedir
cp -R include/svgpp %buildroot%_includedir
cp -R include/exboost %buildroot%_includedir
find %buildroot/%_includedir -type f -exec chmod 0644 '{}' \;

%files
%doc LICENSE_1_0.txt *.md
%_includedir/svgpp
%_includedir/exboost

%changelog
* Tue Jun 03 2025 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
