%define        gemname celluloid

Name:          gem-celluloid
Version:       0.18.0
Release:       alt1
Summary:       Actor-based concurrent object framework for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/celluloid/celluloid
Vcs:           https://github.com/celluloid/celluloid.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(pry) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(coveralls) >= 0.8
BuildRequires: gem(rspec) >= 3 gem(rspec) < 4
BuildRequires: gem(rspec-retry) >= 0.5 gem(rspec-retry) < 1
BuildRequires: gem(rubocop) >= 0.58.2 gem(rubocop) < 2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(timers) >= 4 gem(timers) < 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(timers) >= 4 gem(timers) < 5
Provides:      gem(celluloid) = 0.18.0


%description
Celluloid enables people to build concurrent programs out of concurrent objects
just as easily as they build sequential programs out of sequential objects


%package       -n gem-celluloid-doc
Version:       0.18.0
Release:       alt1
Summary:       Actor-based concurrent object framework for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета celluloid
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(celluloid) = 0.18.0

%description   -n gem-celluloid-doc
Actor-based concurrent object framework for Ruby documentation files.

Celluloid enables people to build concurrent programs out of concurrent objects
just as easily as they build sequential programs out of sequential objects

%description   -n gem-celluloid-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета celluloid.


%package       -n gem-celluloid-devel
Version:       0.18.0
Release:       alt1
Summary:       Actor-based concurrent object framework for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета celluloid
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(celluloid) = 0.18.0
Requires:      gem(pry) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(coveralls) >= 0.8
Requires:      gem(rspec) >= 3 gem(rspec) < 4
Requires:      gem(rspec-retry) >= 0.5 gem(rspec-retry) < 1
Requires:      gem(rubocop) >= 0.58.2 gem(rubocop) < 2
Requires:      gem(rake) >= 0

%description   -n gem-celluloid-devel
Actor-based concurrent object framework for Ruby development package.

Celluloid enables people to build concurrent programs out of concurrent objects
just as easily as they build sequential programs out of sequential objects

%description   -n gem-celluloid-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета celluloid.


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

%files         -n gem-celluloid-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-celluloid-devel
%doc README.md


%changelog
* Tue Nov 01 2022 Pavel Skrylev <majioa@altlinux.org> 0.18.0-alt1
- + packaged gem with Ruby Policy 2.0
