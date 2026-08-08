%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dry-validation

Name:          gem-dry-validation
Version:       1.11.1
Release:       alt1.1
Summary:       Validation library
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-validation
Vcs:           https://github.com/dry-rb/dry-validation.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(dry-core) >= 1.1
BuildRequires: gem(dry-initializer) >= 3.2
BuildRequires: gem(dry-monads) >= 0
BuildRequires: gem(dry-schema) >= 1.14
BuildRequires: gem(i18n) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(warning) >= 0
BuildRequires: gem(zeitwerk) >= 2.6
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(dry-core) >= 2
BuildConflicts: gem(dry-initializer) >= 4
BuildConflicts: gem(dry-schema) >= 2
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.1
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(dry-core) >= 1.1
Requires:      gem(dry-initializer) >= 3.2
Requires:      gem(dry-schema) >= 1.14
Requires:      gem(rake) >= 12.3.3
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(dry-core) >= 2
Conflicts:     gem(dry-initializer) >= 4
Conflicts:     gem(dry-schema) >= 2
Conflicts:     gem(zeitwerk) >= 3
Provides:      gem(dry-validation) = 1.11.1

%description
Validation library


%if_enabled    doc
%package       -n gem-dry-validation-doc
Version:       1.11.1
Release:       alt1.1
Summary:       Validation library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-validation
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(dry-validation) = 1.11.1

%description   -n gem-dry-validation-doc
Validation library documentation files.

%description   -n gem-dry-validation-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-validation.
%endif


%if_enabled    devel
%package       -n gem-dry-validation-devel
Version:       1.11.1
Release:       alt1.1
Summary:       Validation library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-validation
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(dry-validation) = 1.11.1
Requires:      gem(dry-monads) >= 0
Requires:      gem(i18n) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(warning) >= 0

%description   -n gem-dry-validation-devel
Validation library development package.

%description   -n gem-dry-validation-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dry-validation.
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
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md changelog.yml
%ruby_gemspec
%ruby_gemlibdir
%_logdir/%gemname

%if_enabled    doc
%files         -n gem-dry-validation-doc
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md changelog.yml
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-validation-devel
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md changelog.yml
%endif


%changelog
* Sun Aug 09 2026 Pavel Skrylev <majioa@altlinux.org> 1.11.1-alt1.1
- + added log folder

* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 1.11.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
