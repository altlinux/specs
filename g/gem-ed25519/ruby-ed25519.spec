%define        gemname ed25519

Name:          gem-ed25519
Version:       1.3.0
Release:       alt1
Summary:       Ruby library for the Ed25519 public-key signature system
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/crypto-rb/ed25519
Vcs:           https://github.com/crypto-rb/ed25519.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-ed25519 < %EVR
Provides:      ruby-ed25519 = %EVR
Provides:      gem(ed25519) = 1.3.0


%description
A Ruby binding to the Ed25519 elliptic curve public-key signature system
described in RFC 8032.


%package       -n gem-ed25519-doc
Version:       1.3.0
Release:       alt1
Summary:       Ruby library for the Ed25519 public-key signature system documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ed25519
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ed25519) = 1.3.0

%description   -n gem-ed25519-doc
Ruby library for the Ed25519 public-key signature system documentation files.

A Ruby binding to the Ed25519 elliptic curve public-key signature system
described in RFC 8032.

%description   -n gem-ed25519-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ed25519.


%package       -n gem-ed25519-devel
Version:       1.3.0
Release:       alt1
Summary:       Ruby library for the Ed25519 public-key signature system development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ed25519
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ed25519) = 1.3.0
Requires:      gem(bundler) >= 0

%description   -n gem-ed25519-devel
Ruby library for the Ed25519 public-key signature system development package.

A Ruby binding to the Ed25519 elliptic curve public-key signature system
described in RFC 8032.

%description   -n gem-ed25519-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ed25519.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-ed25519-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ed25519-devel
%doc README.md
%ruby_includedir/*


%changelog
* Fri Mar 11 2022 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- ^ 1.2.4 -> 1.3.0

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.4-alt3
- ! spec tags and syntax

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.4-alt2
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1
- Initial build for Sisyphus
