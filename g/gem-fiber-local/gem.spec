%define        gemname fiber-local

Name:          gem-fiber-local
Version:       1.0.0
Release:       alt1
Summary:       Provides a class-level mixin to make fiber local state easy
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/fiber-local
Vcs:           https://github.com/socketry/fiber-local.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(fiber-local) = 1.0.0

%description
A module to simplify fiber-local state.


%package       -n gem-fiber-local-doc
Version:       1.0.0
Release:       alt1
Summary:       Provides a class-level mixin to make fiber local state easy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fiber-local
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fiber-local) = 1.0.0

%description   -n gem-fiber-local-doc
Provides a class-level mixin to make fiber local state easy documentation files.

A module to simplify fiber-local state.

%description   -n gem-fiber-local-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fiber-local.


%package       -n gem-fiber-local-devel
Version:       1.0.0
Release:       alt1
Summary:       Provides a class-level mixin to make fiber local state easy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fiber-local
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fiber-local) = 1.0.0
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-fiber-local-devel
Provides a class-level mixin to make fiber local state easy development package.

A module to simplify fiber-local state.

%description   -n gem-fiber-local-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fiber-local.


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

%files         -n gem-fiber-local-doc
%ruby_gemdocdir

%files         -n gem-fiber-local-devel


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
