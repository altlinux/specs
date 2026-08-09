%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dry-struct

Name:          gem-dry-struct
Version:       1.8.1
Release:       alt1
Summary:       Typed structs and value objects
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-struct
Vcs:           https://github.com/dry-rb/dry-struct.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(dry-core) >= 1.1
BuildRequires: gem(dry-monads) >= 0
BuildRequires: gem(dry-types) >= 1.8.2
BuildRequires: gem(ice_nine) >= 0.11
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(super_diff) >= 0
BuildRequires: gem(warning) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(zeitwerk) >= 2.6
BuildConflicts: gem(dry-core) >= 2
BuildConflicts: gem(dry-types) >= 2
BuildConflicts: gem(ice_nine) >= 1
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.3
Requires:      gem(dry-core) >= 1.1
Requires:      gem(dry-types) >= 1.8.2
Requires:      gem(ice_nine) >= 0.11
Requires:      gem(rake) >= 12.3.3
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(dry-core) >= 2
Conflicts:     gem(dry-types) >= 2
Conflicts:     gem(ice_nine) >= 1
Conflicts:     gem(zeitwerk) >= 3
Provides:      dry-struct = %EVR
Provides:      gem(dry-struct) = 1.8.1

%description
Typed structs and value objects


%if_enabled    doc
%package       -n gem-dry-struct-doc
Version:       1.8.1
Release:       alt1
Summary:       Typed structs and value objects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-struct
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dry-struct) = 1.8.1

%description   -n gem-dry-struct-doc
Typed structs and value objects documentation files.

%description   -n gem-dry-struct-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-struct.
%endif


%if_enabled    devel
%package       -n gem-dry-struct-devel
Version:       1.8.1
Release:       alt1
Summary:       Typed structs and value objects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-struct
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dry-struct) = 1.8.1
Requires:      gem(bundler) >= 0
Requires:      gem(dry-core) >= 1.1
Requires:      gem(dry-monads) >= 0
Requires:      gem(dry-types) >= 1.8.2
Requires:      gem(ice_nine) >= 0.11
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rexml) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(super_diff) >= 0
Requires:      gem(warning) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(dry-core) >= 2
Conflicts:     gem(dry-types) >= 2
Conflicts:     gem(ice_nine) >= 1
Conflicts:     gem(zeitwerk) >= 3

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
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir
%_logdir/%gemname

%if_enabled    doc
%files         -n gem-dry-struct-doc
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-struct-devel
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%endif


%changelog
* Sun Aug 09 2026 Pavel Skrylev <majioa@altlinux.org> 1.8.1-alt1
- ^ 1.6.0 -> 1.8.1

* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- + packaged gem with Ruby Policy 2.0
