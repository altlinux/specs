%define        gemname hoe-gemspec

Name:          gem-hoe-gemspec
Version:       1.0.0.1
Release:       alt1
Summary:       Generate a prerelease gemspec based on a Hoe spec
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/flavorjones/hoe-gemspec
Vcs:           https://github.com/flavorjones/hoe-gemspec.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.11 gem(minitest) < 6
BuildRequires: gem(hoe-git) >= 0
BuildRequires: gem(hoe-bundler) >= 0
BuildRequires: gem(concourse) >= 0.23 gem(concourse) < 1
BuildRequires: gem(hoe) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(hoe-gemspec) = 1.0.0.1

%ruby_use_gem_version hoe-gemspec:1.0.0.1

%description
Generate a prerelease gemspec based on a Hoe spec.


%package       -n gem-hoe-gemspec-doc
Version:       1.0.0.1
Release:       alt1
Summary:       Generate a prerelease gemspec based on a Hoe spec documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-gemspec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-gemspec) = 1.0.0.1

%description   -n gem-hoe-gemspec-doc
Generate a prerelease gemspec based on a Hoe spec documentation files.

%description   -n gem-hoe-gemspec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-gemspec.


%package       -n gem-hoe-gemspec-devel
Version:       1.0.0.1
Release:       alt1
Summary:       Generate a prerelease gemspec based on a Hoe spec development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-gemspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-gemspec) = 1.0.0.1
Requires:      gem(minitest) >= 5.11 gem(minitest) < 6
Requires:      gem(hoe-git) >= 0
Requires:      gem(hoe-bundler) >= 0
Requires:      gem(concourse) >= 0.23 gem(concourse) < 1
Requires:      gem(hoe) >= 0

%description   -n gem-hoe-gemspec-devel
Generate a prerelease gemspec based on a Hoe spec development package.

%description   -n gem-hoe-gemspec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-gemspec.


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

%files         -n gem-hoe-gemspec-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hoe-gemspec-devel
%doc README.md


%changelog
* Sun Apr 17 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.0.1-alt1
- + packaged gem with Ruby Policy 2.0
