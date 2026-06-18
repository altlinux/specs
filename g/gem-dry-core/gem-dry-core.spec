%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dry-core

Name:          gem-dry-core
Version:       1.2.0
Release:       alt1
Summary:       A toolset of small support modules used throughout the dry-rb ecosystem
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-core
Vcs:           https://github.com/dry-rb/dry-core.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(dry-inflector) >= 0
BuildRequires: gem(dry-logic) >= 0
BuildRequires: gem(dry-types) >= 0
BuildRequires: gem(logger) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(warning) >= 0
BuildRequires: gem(zeitwerk) >= 2.6
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.3
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(logger) >= 0
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(zeitwerk) >= 3
Provides:      gem(dry-core) = 1.2.0

%description
A toolset of small support modules used throughout the dry-rb ecosystem


%if_enabled    doc
%package       -n gem-dry-core-doc
Version:       1.2.0
Release:       alt1
Summary:       A toolset of small support modules used throughout the dry-rb ecosystem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dry-core) = 1.2.0

%description   -n gem-dry-core-doc
A toolset of small support modules used throughout the dry-rb ecosystem
documentation files.

%description   -n gem-dry-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-core.
%endif


%if_enabled    devel
%package       -n gem-dry-core-devel
Version:       1.2.0
Release:       alt1
Summary:       A toolset of small support modules used throughout the dry-rb ecosystem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dry-core) = 1.2.0
Requires:      gem(activesupport) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(dry-inflector) >= 0
Requires:      gem(dry-logic) >= 0
Requires:      gem(dry-types) >= 0
Requires:      gem(logger) >= 0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rexml) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(warning) >= 0
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(zeitwerk) >= 3

%description   -n gem-dry-core-devel
A toolset of small support modules used throughout the dry-rb ecosystem
development package.

%description   -n gem-dry-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dry-core.
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
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-dry-core-doc
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-core-devel
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt
%endif


%changelog
* Thu Jun 18 2026 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- ^ 1.0.1 -> 1.2.0

* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
