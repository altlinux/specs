%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dry-types

Name:          gem-dry-types
Version:       1.9.1
Release:       alt1
Summary:       Type system for Ruby supporting coercions, constraints and complex types like structs, value objects, enums etc
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-types
Vcs:           https://github.com/dry-rb/dry-types.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bigdecimal) >= 3.0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(dry-core) >= 1.0
BuildRequires: gem(dry-inflector) >= 1.0
BuildRequires: gem(dry-logic) >= 1.4
BuildRequires: gem(dry-monads) >= 0
BuildRequires: gem(dry-struct) >= 0
BuildRequires: gem(lefthook) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(warning) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(zeitwerk) >= 2.6
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(dry-core) >= 2
BuildConflicts: gem(dry-inflector) >= 2
BuildConflicts: gem(dry-logic) >= 2
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.2
Requires:      gem(bigdecimal) >= 3.0
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(dry-core) >= 1.0
Requires:      gem(dry-inflector) >= 1.0
Requires:      gem(dry-logic) >= 1.4
Requires:      gem(rake) >= 12.3.3
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(dry-core) >= 2
Conflicts:     gem(dry-inflector) >= 2
Conflicts:     gem(dry-logic) >= 2
Conflicts:     gem(zeitwerk) >= 3
Provides:      gem(dry-types) = 1.9.1

%description
Type system for Ruby supporting coercions, constraints and complex types like
structs, value objects, enums etc


%if_enabled    doc
%package       -n gem-dry-types-doc
Version:       1.9.1
Release:       alt1
Summary:       Type system for Ruby supporting coercions, constraints and complex types like structs, value objects, enums etc documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-types
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(dry-types) = 1.9.1

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
Version:       1.9.1
Release:       alt1
Summary:       Type system for Ruby supporting coercions, constraints and complex types like structs, value objects, enums etc development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-types
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(dry-types) = 1.9.1
Requires:      gem(bundler) >= 0
Requires:      gem(lefthook) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(yard) >= 0

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
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-dry-types-doc
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-types-devel
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 1.9.1-alt1
- ^ 1.7.2 -> 1.9.1

* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.7.2-alt1
- + packaged gem with Ruby Policy 2.0
