%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dry-schema

Name:          gem-dry-schema
Version:       1.16.0
Release:       alt1.1
Summary:       Coercion and validation for data structures
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-schema
Vcs:           https://github.com/dry-rb/dry-schema.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(dry-configurable) >= 1.0.1
BuildRequires: gem(dry-core) >= 1.1
BuildRequires: gem(dry-initializer) >= 3.2
BuildRequires: gem(dry-logic) >= 1.6
BuildRequires: gem(dry-monads) >= 0
BuildRequires: gem(dry-struct) >= 0
BuildRequires: gem(dry-types) >= 1.9.1
BuildRequires: gem(i18n) >= 0
BuildRequires: gem(json_schemer) >= 0
BuildRequires: gem(ostruct) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(super_diff) >= 0
BuildRequires: gem(transproc) >= 0
BuildRequires: gem(warning) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(zeitwerk) >= 2.6
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
Requires:      ruby >= 3.3
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(dry-configurable) >= 1.0.1
Requires:      gem(dry-core) >= 1.1
Requires:      gem(dry-initializer) >= 3.2
Requires:      gem(dry-logic) >= 1.6
Requires:      gem(dry-types) >= 1.9.1
Requires:      gem(rake) >= 12.3.3
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(dry-configurable) >= 2
Conflicts:     gem(dry-core) >= 2
Conflicts:     gem(dry-initializer) >= 4
Conflicts:     gem(dry-logic) >= 2
Conflicts:     gem(dry-types) >= 2
Conflicts:     gem(zeitwerk) >= 3
Provides:      dry-schema = %EVR
Provides:      gem(dry-schema) = 1.16.0

%description
dry-schema provides a DSL for defining schemas with keys and rules that should
be applied to values. It supports coercion, input sanitization, custom types and
localized error messages (with or without I18n gem). It's also used as the
schema engine in dry-validation.


%if_enabled    doc
%package       -n gem-dry-schema-doc
Version:       1.16.0
Release:       alt1.1
Summary:       Coercion and validation for data structures documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-schema
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dry-schema) = 1.16.0

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
Version:       1.16.0
Release:       alt1.1
Summary:       Coercion and validation for data structures development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-schema
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dry-schema) = 1.16.0
Requires:      gem(bundler) >= 0
Requires:      gem(json_schemer) >= 0
Requires:      gem(ostruct) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(super_diff) >= 0
Requires:      gem(yard) >= 0

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
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir
%_logdir/%gemname

%if_enabled    doc
%files         -n gem-dry-schema-doc
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-schema-devel
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%endif


%changelog
* Sun Aug 09 2026 Pavel Skrylev <majioa@altlinux.org> 1.16.0-alt1.1
- + added link to logged file

* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 1.16.0-alt1
- ^ 1.13.3 -> 1.16.0

* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.13.3-alt1
- + packaged gem with Ruby Policy 2.0
