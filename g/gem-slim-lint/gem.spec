%define        gemname slim_lint

Name:          gem-slim-lint
Version:       0.22.1
Release:       alt1
Summary:       Slim template linting tool
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sds/slim-lint
Vcs:           https://github.com/sds/slim-lint.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rubocop) >= 0.78.0 gem(rubocop) < 2
BuildRequires: gem(slim) >= 3.0 gem(slim) < 5.0
BuildRequires: gem(pry) >= 0.13 gem(pry) < 1
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rspec-its) >= 1.0 gem(rspec-its) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(rubocop) >= 0.78.0 gem(rubocop) < 2
Requires:      gem(slim) >= 3.0 gem(slim) < 5.0
Provides:      gem(slim_lint) = 0.22.1


%description
Configurable tool for writing clean and consistent Slim templates


%package       -n slim-lint
Version:       0.22.1
Release:       alt1
Summary:       Slim template linting tool executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета slim_lint
Group:         Other
BuildArch:     noarch

Requires:      gem(slim_lint) = 0.22.1

%description   -n slim-lint
Slim template linting tool executable(s).

Configurable tool for writing clean and consistent Slim templates

%description   -n slim-lint -l ru_RU.UTF-8
Исполнямка для самоцвета slim_lint.


%package       -n gem-slim-lint-doc
Version:       0.22.1
Release:       alt1
Summary:       Slim template linting tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета slim_lint
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(slim_lint) = 0.22.1

%description   -n gem-slim-lint-doc
Slim template linting tool documentation files.

Configurable tool for writing clean and consistent Slim templates

%description   -n gem-slim-lint-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета slim_lint.


%package       -n gem-slim-lint-devel
Version:       0.22.1
Release:       alt1
Summary:       Slim template linting tool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета slim_lint
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(slim_lint) = 0.22.1
Requires:      gem(pry) >= 0.13 gem(pry) < 1
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(rspec-its) >= 1.0 gem(rspec-its) < 2

%description   -n gem-slim-lint-devel
Slim template linting tool development package.

Configurable tool for writing clean and consistent Slim templates

%description   -n gem-slim-lint-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета slim_lint.


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

%files         -n slim-lint
%_bindir/slim-lint

%files         -n gem-slim-lint-doc
%ruby_gemdocdir

%files         -n gem-slim-lint-devel


%changelog
* Sun Sep 12 2021 Pavel Skrylev <majioa@altlinux.org> 0.22.1-alt1
- + packaged gem with Ruby Policy 2.0
