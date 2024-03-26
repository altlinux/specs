%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname dry-types

Name:          gem-dry-types
Version:       1.7.2
Release:       alt1
Summary:       Type system for Ruby supporting coercions, constraints and complex types like structs, value objects, enums etc
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-types
Vcs:           https://github.com/dry-rb/dry-types.git
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
BuildRequires: gem(yard) >= 0
BuildRequires: gem(dry-monads) >= 0
BuildRequires: gem(dry-struct) >= 0
BuildRequires: gem(attrio) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(fast_attributes) >= 0
BuildRequires: gem(hotch) >= 0
BuildRequires: gem(virtus) >= 0
BuildRequires: gem(bigdecimal) >= 3.0
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(dry-core) >= 1.0
BuildRequires: gem(dry-inflector) >= 1.0
BuildRequires: gem(dry-logic) >= 1.4
BuildRequires: gem(zeitwerk) >= 2.6
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(bigdecimal) >= 4
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(dry-core) >= 2
BuildConflicts: gem(dry-inflector) >= 2
BuildConflicts: gem(dry-logic) >= 2
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(bigdecimal) >= 3.0
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(dry-core) >= 1.0
Requires:      gem(dry-inflector) >= 1.0
Requires:      gem(dry-logic) >= 1.4
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(bigdecimal) >= 4
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(dry-core) >= 2
Conflicts:     gem(dry-inflector) >= 2
Conflicts:     gem(dry-logic) >= 2
Conflicts:     gem(zeitwerk) >= 3
Provides:      gem(dry-types) = 1.7.2


%description
Type system for Ruby supporting coercions, constraints and complex types like
structs, value objects, enums etc


%if_enabled    doc
%package       -n gem-dry-types-doc
Version:       1.7.2
Release:       alt1
Summary:       Type system for Ruby supporting coercions, constraints and complex types like structs, value objects, enums etc documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-types
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dry-types) = 1.7.2

%description   -n gem-dry-types-doc
Type system for Ruby supporting coercions, constraints and complex types like
structs, value objects, enums etc documentation files.

Type system for Ruby supporting coercions, constraints and complex types like
structs, value objects, enums etc
%description   -n gem-dry-types-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-types.
%endif


%if_enabled    devel
%package       -n gem-dry-types-devel
Version:       1.7.2
Release:       alt1
Summary:       Type system for Ruby supporting coercions, constraints and complex types like structs, value objects, enums etc development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-types
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dry-types) = 1.7.2
Requires:      gem(rake) >= 12.3.3
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(warning) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(byebug) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(dry-monads) >= 0
Requires:      gem(dry-struct) >= 0
Requires:      gem(attrio) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(fast_attributes) >= 0
Requires:      gem(hotch) >= 0
Requires:      gem(virtus) >= 0
Conflicts:     gem(rubocop) >= 2

%description   -n gem-dry-types-devel
Type system for Ruby supporting coercions, constraints and complex types like
structs, value objects, enums etc development package.

Type system for Ruby supporting coercions, constraints and complex types like
structs, value objects, enums etc
%description   -n gem-dry-types-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dry-types.
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
%files         -n gem-dry-types-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-types-devel
%doc README.md
%endif


%changelog
* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.7.2-alt1
- + packaged gem with Ruby Policy 2.0
