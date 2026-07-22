%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dry-logic

Name:          gem-dry-logic
Version:       1.6.0
Release:       alt1
Summary:       Predicate logic with rule composition
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-logic
Vcs:           https://github.com/dry-rb/dry-logic.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(dry-core) >= 1.1
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(warning) >= 0
BuildRequires: gem(zeitwerk) >= 2.6
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(dry-core) >= 2
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.1.0
Requires:      gem(bigdecimal) >= 0
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(dry-core) >= 1.1
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(dry-core) >= 2
Conflicts:     gem(zeitwerk) >= 3
Provides:      gem(dry-logic) = 1.6.0

%description
Predicate logic with rule composition


%if_enabled    doc
%package       -n gem-dry-logic-doc
Version:       1.6.0
Release:       alt1
Summary:       Predicate logic with rule composition documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-logic
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(dry-logic) = 1.6.0

%description   -n gem-dry-logic-doc
Predicate logic with rule composition documentation files.

%description   -n gem-dry-logic-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-logic.
%endif


%if_enabled    devel
%package       -n gem-dry-logic-devel
Version:       1.6.0
Release:       alt1
Summary:       Predicate logic with rule composition development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-logic
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(dry-logic) = 1.6.0

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
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md changelog.yml
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-dry-logic-doc
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md changelog.yml
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-logic-devel
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md changelog.yml
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 1.6.0-alt1
- ^ 1.5.0 -> 1.6.0

* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- + packaged gem with Ruby Policy 2.0
