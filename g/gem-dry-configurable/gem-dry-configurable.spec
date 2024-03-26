%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname dry-configurable

Name:          gem-dry-configurable
Version:       1.0.2
Release:       alt1
Summary:       A mixin to add configuration functionality to your classes
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-configurable
Vcs:           https://github.com/dry-rb/dry-configurable.git
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
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(benchmark-memory) >= 0
BuildRequires: gem(memory_profiler) >= 0
BuildRequires: gem(hanami-utils) >= 0
BuildRequires: gem(hotch) >= 0
BuildRequires: gem(rspec-benchmark) >= 0
BuildRequires: gem(dry-core) >= 1.0
BuildRequires: gem(zeitwerk) >= 2.6
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(dry-core) >= 2
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(dry-core) >= 1.0
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(dry-core) >= 2
Conflicts:     gem(zeitwerk) >= 3
Provides:      gem(dry-configurable) = 1.0.2


%description
A mixin to add configuration functionality to your classes


%if_enabled    doc
%package       -n gem-dry-configurable-doc
Version:       1.0.2
Release:       alt1
Summary:       A mixin to add configuration functionality to your classes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-configurable
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dry-configurable) = 1.0.2

%description   -n gem-dry-configurable-doc
A mixin to add configuration functionality to your classes documentation files.
%description   -n gem-dry-configurable-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-configurable.
%endif


%if_enabled    devel
%package       -n gem-dry-configurable-devel
Version:       1.0.2
Release:       alt1
Summary:       A mixin to add configuration functionality to your classes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-configurable
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dry-configurable) = 1.0.2
Requires:      gem(rake) >= 12.3.3
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(warning) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(byebug) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(benchmark-memory) >= 0
Requires:      gem(memory_profiler) >= 0
Requires:      gem(hanami-utils) >= 0
Requires:      gem(hotch) >= 0
Requires:      gem(rspec-benchmark) >= 0
Conflicts:     gem(rubocop) >= 2

%description   -n gem-dry-configurable-devel
A mixin to add configuration functionality to your classes development package.
%description   -n gem-dry-configurable-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dry-configurable.
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
%files         -n gem-dry-configurable-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-configurable-devel
%doc README.md
%endif


%changelog
* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
