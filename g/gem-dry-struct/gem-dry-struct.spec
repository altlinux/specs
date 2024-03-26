%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname dry-struct

Name:          gem-dry-struct
Version:       1.6.0
Release:       alt1
Summary:       Typed structs and value objects
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-struct
Vcs:           https://github.com/dry-rb/dry-struct.git
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
BuildRequires: gem(yard) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(activerecord) >= 0
BuildRequires: gem(attrio) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(fast_attributes) >= 0
BuildRequires: gem(hotch) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(virtus) >= 0
BuildRequires: gem(dry-core) >= 1.0
BuildRequires: gem(dry-types) >= 1.7
BuildRequires: gem(ice_nine) >= 0.11
BuildRequires: gem(zeitwerk) >= 2.6
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(dry-core) >= 2
BuildConflicts: gem(dry-types) >= 2
BuildConflicts: gem(ice_nine) >= 1
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(dry-core) >= 1.0
Requires:      gem(dry-types) >= 1.7
Requires:      gem(ice_nine) >= 0.11
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(dry-core) >= 2
Conflicts:     gem(dry-types) >= 2
Conflicts:     gem(ice_nine) >= 1
Conflicts:     gem(zeitwerk) >= 3
Provides:      gem(dry-struct) = 1.6.0


%description
Typed structs and value objects


%if_enabled    doc
%package       -n gem-dry-struct-doc
Version:       1.6.0
Release:       alt1
Summary:       Typed structs and value objects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-struct
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dry-struct) = 1.6.0

%description   -n gem-dry-struct-doc
Typed structs and value objects documentation files.
%description   -n gem-dry-struct-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-struct.
%endif


%if_enabled    devel
%package       -n gem-dry-struct-devel
Version:       1.6.0
Release:       alt1
Summary:       Typed structs and value objects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-struct
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dry-struct) = 1.6.0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(warning) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(bundler) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(activerecord) >= 0
Requires:      gem(attrio) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(fast_attributes) >= 0
Requires:      gem(hotch) >= 0
Requires:      gem(sqlite3) >= 0
Requires:      gem(virtus) >= 0
Conflicts:     gem(rubocop) >= 2

%description   -n gem-dry-struct-devel
Typed structs and value objects development package.
%description   -n gem-dry-struct-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dry-struct.
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
%files         -n gem-dry-struct-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-struct-devel
%doc README.md
%endif


%changelog
* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- + packaged gem with Ruby Policy 2.0
