%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname dry-logic

Name:          gem-dry-logic
Version:       1.5.0
Release:       alt1
Summary:       Predicate logic with rule composition
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-logic
Vcs:           https://github.com/dry-rb/dry-logic.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
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
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(hotch) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(dry-core) >= 1.0
BuildRequires: gem(zeitwerk) >= 2.6
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(dry-core) >= 2
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(dry-core) >= 1.0
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(dry-core) >= 2
Conflicts:     gem(zeitwerk) >= 3
Provides:      gem(dry-logic) = 1.5.0


%description
Predicate logic with rule composition


%if_enabled    doc
%package       -n gem-dry-logic-doc
Version:       1.5.0
Release:       alt1
Summary:       Predicate logic with rule composition documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-logic
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dry-logic) = 1.5.0

%description   -n gem-dry-logic-doc
Predicate logic with rule composition documentation files.
%description   -n gem-dry-logic-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-logic.
%endif


%if_enabled    devel
%package       -n gem-dry-logic-devel
Version:       1.5.0
Release:       alt1
Summary:       Predicate logic with rule composition development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-logic
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dry-logic) = 1.5.0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(warning) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(bundler) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(hotch) >= 0
Requires:      gem(pry-byebug) >= 0
Conflicts:     gem(rubocop) >= 2

%description   -n gem-dry-logic-devel
Predicate logic with rule composition development package.
%description   -n gem-dry-logic-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dry-logic.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-dry-logic-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-logic-devel
%doc README.md
%endif


%changelog
* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- + packaged gem with Ruby Policy 2.0
