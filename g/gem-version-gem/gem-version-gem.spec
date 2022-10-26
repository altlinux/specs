%define        gemname version_gem

Name:          gem-version-gem
Version:       1.1.1
Release:       alt1
Summary:       Enhance your VERSION! Sugar for Version modules
License:       MIT
Group:         Development/Ruby
Url:           https://gitlab.com/oauth-xx/version_gem
Vcs:           https://gitlab.com/oauth-xx/version_gem/-/tree/v1.1.1.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rubocop-lts) >= 8.0.2 gem(rubocop-lts) < 23
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(rubocop-performance) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 22.0.1,rubocop-lts < 23
Provides:      gem(version_gem) = 1.1.1


%description
Versions are good. Versions are cool. Versions will win.


%package       -n gem-version-gem-doc
Version:       1.1.1
Release:       alt1
Summary:       Enhance your VERSION! Sugar for Version modules documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета version_gem
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(version_gem) = 1.1.1

%description   -n gem-version-gem-doc
Enhance your VERSION! Sugar for Version modules documentation files.

Versions are good. Versions are cool. Versions will win.

%description   -n gem-version-gem-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета version_gem.


%package       -n gem-version-gem-devel
Version:       1.1.1
Release:       alt1
Summary:       Enhance your VERSION! Sugar for Version modules development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета version_gem
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(version_gem) = 1.1.1
Requires:      gem(rspec) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rubocop-lts) >= 8.0.2 gem(rubocop-lts) < 23
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(rubocop-performance) >= 0

%description   -n gem-version-gem-devel
Enhance your VERSION! Sugar for Version modules development package.

Versions are good. Versions are cool. Versions will win.

%description   -n gem-version-gem-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета version_gem.


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

%files         -n gem-version-gem-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-version-gem-devel
%doc README.md


%changelog
* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with Ruby Policy 2.0
