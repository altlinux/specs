%define        pkgname ed25519

Name:          ruby-%pkgname
Version:       1.2.4
Release:       alt2
Summary:       Ruby library for the Ed25519 public-key signature system
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/crypto-rb/ed25519
# VCS:         https://github.com/crypto-rb/ed25519.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
A Ruby binding to the Ed25519 elliptic curve public-key signature system
described in RFC 8032.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-cool.io-doc
Obsoletes:     ruby-cool.io-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%package       -n gem-%pkgname-devel
Summary:       Development files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-devel
Development files for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*

%changelog
* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.4-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1
- Initial build for Sisyphus
