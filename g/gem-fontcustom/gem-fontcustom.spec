%define pkgname fontcustom

Name: gem-%pkgname
Version: 2.0.0
Release: alt1

Summary: custom icon webfonts from the comfort of the command line
License: MIT
Group: Development/Ruby
Url: https://github.com/FontCustom/fontcustom
Vcs: https://salsa.debian.org/debian/fontcustom

BuildArch: noarch

Source: %pkgname-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel

Requires: fontforge
Requires: woff2
Requires: sfnt2woff-zopfli
Requires: gem-json
Requires: gem-thor
Requires: gem-listen

%description
Generate cross-browser icon fonts and supporting files
(@font-face CSS, etc.) from a collection of SVGs.

%prep
%setup -n %pkgname-%version
%patch -p1

%build
%ruby_build
rm -rfv debian

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md LICENSES.txt README.md
%_bindir/fontcustom
%ruby_gemspec
%ruby_gemlibdir

%changelog
* Sat Nov 22 2025 Nikolay Strelkov <snk@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
