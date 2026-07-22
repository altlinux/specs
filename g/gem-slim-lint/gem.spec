%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname slim_lint

Name:          gem-slim-lint
Version:       0.35.0
Release:       alt1
Summary:       Slim template linting tool
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sds/slim-lint
Vcs:           https://github.com/sds/slim-lint.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(overcommit) >= 0.62.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rexml) >= 3.2
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rspec-its) >= 1.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(slim) >= 3.0
BuildConflicts: gem(overcommit) >= 1
BuildConflicts: gem(rexml) >= 4
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-its) >= 3
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(slim) >= 6.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency overcommit >= 0.70.0,overcommit < 1
%ruby_use_gem_dependency rspec-its >= 2.0.0,rspec-its < 3
%ruby_alias_names slim_lint,slim-lint
Requires:      ruby >= 3.0
Requires:      gem(rake) >= 0
Requires:      gem(rexml) >= 3.2
Requires:      gem(rubocop) >= 1.0
Requires:      gem(slim) >= 3.0
Conflicts:     gem(rexml) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(slim) >= 6.0
Provides:      gem(slim_lint) = 0.35.0

%description
Configurable tool for writing clean and consistent Slim templates


%package       -n slim-lint
Version:       0.35.0
Release:       alt1
Summary:       Slim template linting tool executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета slim_lint
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(slim_lint) = 0.35.0
Requires:      gem(rake) >= 0
Conflicts:     gem(rubocop) >= 2

%description   -n slim-lint
Slim template linting tool executable(s).

Configurable tool for writing clean and consistent Slim templates

%description   -n slim-lint -l ru_RU.UTF-8
Исполнямка для самоцвета slim_lint.


%if_enabled    doc
%package       -n gem-slim-lint-doc
Version:       0.35.0
Release:       alt1
Summary:       Slim template linting tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета slim_lint
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(slim_lint) = 0.35.0

%description   -n gem-slim-lint-doc
Slim template linting tool documentation files.

Configurable tool for writing clean and consistent Slim templates

%description   -n gem-slim-lint-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета slim_lint.
%endif


%if_enabled    devel
%package       -n gem-slim-lint-devel
Version:       0.35.0
Release:       alt1
Summary:       Slim template linting tool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета slim_lint
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(slim_lint) = 0.35.0
Requires:      gem(overcommit) >= 0.62.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rspec-its) >= 1.0
Requires:      gem(simplecov) >= 0
Conflicts:     gem(overcommit) >= 1
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-its) >= 3

%description   -n gem-slim-lint-devel
Slim template linting tool development package.

Configurable tool for writing clean and consistent Slim templates

%description   -n gem-slim-lint-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета slim_lint.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc LICENSE.md CHANGELOG.md README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n slim-lint
%doc LICENSE.md CHANGELOG.md README.md
%_bindir/slim-lint

%if_enabled    doc
%files         -n gem-slim-lint-doc
%doc LICENSE.md CHANGELOG.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-slim-lint-devel
%doc LICENSE.md CHANGELOG.md README.md
%endif


%changelog
* Wed Jul 08 2026 Alexander Burmatov <thatman@altlinux.org> 0.35.0-alt1
- ^ 0.22.1 -> 0.35.0

* Sun Sep 12 2021 Pavel Skrylev <majioa@altlinux.org> 0.22.1-alt1
- + packaged gem with Ruby Policy 2.0
