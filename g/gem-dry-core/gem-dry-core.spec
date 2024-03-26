%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dry-core

Name:          gem-dry-core
Version:       1.0.1
Release:       alt1
Summary:       A toolset of small support modules used throughout the dry-rb ecosystem
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-core
Vcs:           https://github.com/dry-rb/dry-core.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(warning) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(dry-inflector) >= 1.0.0
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(zeitwerk) >= 2.6
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(inflecto) >= 2
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(zeitwerk) >= 3
Provides:      gem(dry-core) = 1.0.1


%description
A toolset of small support modules used throughout the dry-rb ecosystem


%if_enabled    doc
%package       -n gem-dry-core-doc
Version:       1.0.1
Release:       alt1
Summary:       A toolset of small support modules used throughout the dry-rb ecosystem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dry-core) = 1.0.1

%description   -n gem-dry-core-doc
A toolset of small support modules used throughout the dry-rb ecosystem
documentation files.
%description   -n gem-dry-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-core.
%endif


%if_enabled    devel
%package       -n gem-dry-core-devel
Version:       1.0.1
Release:       alt1
Summary:       A toolset of small support modules used throughout the dry-rb ecosystem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dry-core) = 1.0.1
Requires:      gem(rake) >= 12.3.3
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(warning) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(byebug) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(activesupport) >= 0
Requires:      gem(dry-inflector) >= 1.0.0
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(dry-inflector) >= 2

%description   -n gem-dry-core-devel
A toolset of small support modules used throughout the dry-rb ecosystem
development package.
%description   -n gem-dry-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dry-core.
%endif


%prep
%setup
%autopatch

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

%if_enabled    doc
%files         -n gem-dry-core-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-core-devel
%doc README.md
%endif


%changelog
* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
