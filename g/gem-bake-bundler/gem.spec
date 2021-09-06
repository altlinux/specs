%define        gemname bake-bundler

Name:          gem-bake-bundler
Version:       0.3.5
Release:       alt1
Summary:       Provides recipes for bundler
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/bake-bundler
Vcs:           https://github.com/ioquatix/bake-bundler.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bake) >= 0.9 gem(bake) < 1
BuildRequires: gem(rspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(bake) >= 0.9 gem(bake) < 1
Requires:      gem(rspec) >= 0
Provides:      gem(bake-bundler) = 0.3.5


%description
Provides recipes for bundler.


%package       -n gem-bake-bundler-doc
Version:       0.3.5
Release:       alt1
Summary:       Provides recipes for bundler documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bake-bundler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bake-bundler) = 0.3.5

%description   -n gem-bake-bundler-doc
Provides recipes for bundler documentation files.

%description   -n gem-bake-bundler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bake-bundler.


%package       -n gem-bake-bundler-devel
Version:       0.3.5
Release:       alt1
Summary:       Provides recipes for bundler development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bake-bundler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bake-bundler) = 0.3.5

%description   -n gem-bake-bundler-devel
Provides recipes for bundler development package.

%description   -n gem-bake-bundler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bake-bundler.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-bake-bundler-doc
%ruby_gemdocdir

%files         -n gem-bake-bundler-devel


%changelog
* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.5-alt1
- + packaged gem with Ruby Policy 2.0
