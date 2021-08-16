%define        gemname fog-digitalocean

Name:          gem-fog-digitalocean
Version:       0.4.0
Release:       alt1.1
Summary:       Fog for DigitalOcean Platform
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-digitalocean
Vcs:           https://github.com/fog/fog-digitalocean.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(shindo) >= 0
BuildRequires: gem(rubyzip) >= 0
BuildRequires: gem(mime-types) >= 0
BuildRequires: gem(mime-types-data) >= 0
BuildRequires: gem(rubocop) >= 0.58.2 gem(rubocop) < 2
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fog-json) >= 0
BuildRequires: gem(fog-xml) >= 0
BuildRequires: gem(ipaddress) >= 0.5

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(fog-core) >= 0
Requires:      gem(fog-json) >= 0
Requires:      gem(fog-xml) >= 0
Requires:      gem(ipaddress) >= 0.5
Obsoletes:     ruby-fog-digitalocean < %EVR
Provides:      ruby-fog-digitalocean = %EVR
Provides:      gem(fog-digitalocean) = 0.4.0


%description
This is the plugin Gem to talk to Digitalocean clouds via fog.


%package       -n gem-fog-digitalocean-doc
Version:       0.4.0
Release:       alt1.1
Summary:       Fog for DigitalOcean Platform documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-digitalocean
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-digitalocean) = 0.4.0

%description   -n gem-fog-digitalocean-doc
Fog for DigitalOcean Platform documentation files.

This is the plugin Gem to talk to Digitalocean clouds via fog.

%description   -n gem-fog-digitalocean-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-digitalocean.


%package       -n gem-fog-digitalocean-devel
Version:       0.4.0
Release:       alt1.1
Summary:       Fog for DigitalOcean Platform development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-digitalocean
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-digitalocean) = 0.4.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(shindo) >= 0
Requires:      gem(rubyzip) >= 0
Requires:      gem(mime-types) >= 0
Requires:      gem(mime-types-data) >= 0
Requires:      gem(rubocop) >= 0.58.2 gem(rubocop) < 2

%description   -n gem-fog-digitalocean-devel
Fog for DigitalOcean Platform development package.

This is the plugin Gem to talk to Digitalocean clouds via fog.

%description   -n gem-fog-digitalocean-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-digitalocean.


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

%files         -n gem-fog-digitalocean-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-digitalocean-devel
%doc README.md


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1.1
- ! spec

* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- Bump to 0.4.0
- Use Ruby Policy 2.0

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
