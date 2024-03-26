%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname dry-schema

Name:          gem-dry-schema
Version:       1.13.3
Release:       alt1
Summary:       Coercion and validation for data structures
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-schema
Vcs:           https://github.com/dry-rb/dry-schema.git
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
BuildRequires: gem(dry-monads) >= 0
BuildRequires: gem(dry-struct) >= 0
BuildRequires: gem(i18n) >= 1.8.2
BuildRequires: gem(json-schema) >= 0
BuildRequires: gem(transproc) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(actionpack) >= 0
BuildRequires: gem(activemodel) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(hotch) >= 0
BuildRequires: gem(virtus) >= 0
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(dry-configurable) >= 1.0.1
BuildRequires: gem(dry-core) >= 1.0
BuildRequires: gem(dry-initializer) >= 3.0
BuildRequires: gem(dry-logic) >= 1.4
BuildRequires: gem(dry-types) >= 1.7
BuildRequires: gem(zeitwerk) >= 2.6
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(dry-configurable) >= 2
BuildConflicts: gem(dry-core) >= 2
BuildConflicts: gem(dry-initializer) >= 4
BuildConflicts: gem(dry-logic) >= 2
BuildConflicts: gem(dry-types) >= 2
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency i18n >= 1.10.0,i18n < 2
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(dry-configurable) >= 1.0.1
Requires:      gem(dry-core) >= 1.0
Requires:      gem(dry-initializer) >= 3.0
Requires:      gem(dry-logic) >= 1.4
Requires:      gem(dry-types) >= 1.7
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(dry-configurable) >= 2
Conflicts:     gem(dry-core) >= 2
Conflicts:     gem(dry-initializer) >= 4
Conflicts:     gem(dry-logic) >= 2
Conflicts:     gem(dry-types) >= 2
Conflicts:     gem(zeitwerk) >= 3
Provides:      gem(dry-schema) = 1.13.3


%description
dry-schema provides a DSL for defining schemas with keys and rules that should
be applied to values. It supports coercion, input sanitization, custom types and
localized error messages (with or without I18n gem). It's also used as the
schema engine in dry-validation.


%if_enabled    doc
%package       -n gem-dry-schema-doc
Version:       1.13.3
Release:       alt1
Summary:       Coercion and validation for data structures documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-schema
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dry-schema) = 1.13.3

%description   -n gem-dry-schema-doc
Coercion and validation for data structures documentation files.

dry-schema provides a DSL for defining schemas with keys and rules that should
be applied to values. It supports coercion, input sanitization, custom types and
localized error messages (with or without I18n gem). It's also used as the
schema engine in dry-validation.


%description   -n gem-dry-schema-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-schema.
%endif


%if_enabled    devel
%package       -n gem-dry-schema-devel
Version:       1.13.3
Release:       alt1
Summary:       Coercion and validation for data structures development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-schema
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dry-schema) = 1.13.3
Requires:      gem(rake) >= 12.3.3
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(warning) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(byebug) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(dry-monads) >= 0
Requires:      gem(dry-struct) >= 0
Requires:      gem(i18n) >= 1.8.2
Requires:      gem(json-schema) >= 0
Requires:      gem(transproc) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(actionpack) >= 0
Requires:      gem(activemodel) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(hotch) >= 0
Requires:      gem(virtus) >= 0
Conflicts:     gem(rubocop) >= 2

%description   -n gem-dry-schema-devel
Coercion and validation for data structures development package.

dry-schema provides a DSL for defining schemas with keys and rules that should
be applied to values. It supports coercion, input sanitization, custom types and
localized error messages (with or without I18n gem). It's also used as the
schema engine in dry-validation.


%description   -n gem-dry-schema-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dry-schema.
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
%files         -n gem-dry-schema-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-schema-devel
%doc README.md
%endif


%changelog
* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.13.3-alt1
- + packaged gem with Ruby Policy 2.0
