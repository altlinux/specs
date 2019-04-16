%define  pkgname jsminc

Name:          ruby-%pkgname
Version:       2.0.0
Release:       alt2
Summary:       A fast JavaScript minifier written in C (by Douglas Crockford)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rf-/jsminc
# VCS:         https://github.com/rf-/jsminc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary. JSMinC is the original C version of JSMin, embedded in Ruby.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%changelog
* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt2
- Use Ruby Policy 2.0

* Sun Jun 10 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1.1
- Rebuild for aarch64.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
