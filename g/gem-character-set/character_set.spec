%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname character_set

Name:          gem-character-set
Version:       1.8.0
Release:       alt1
Summary:       Build, read, write and compare sets of Unicode codepoints
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jaynetics/character_set
Vcs:           https://github.com/jaynetics/character_set.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(benchmark-ips) >= 2.7
BuildRequires: gem(get_process_mem) >= 0.2.3
BuildRequires: gem(gouteur) >= 1.0.0
BuildRequires: gem(rake) >= 13.1
BuildRequires: gem(rake-compiler) >= 1.1
BuildRequires: gem(range_compressor) >= 1.0
BuildRequires: gem(regexp_parser) >= 2.9
BuildRequires: gem(regexp_property_values) >= 1.5
BuildRequires: gem(rspec) >= 3.8
BuildRequires: gem(rubocop) >= 1.59
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(warning) >= 1.3
BuildConflicts: gem(benchmark-ips) >= 3
BuildConflicts: gem(get_process_mem) >= 0.3
BuildConflicts: gem(gouteur) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(range_compressor) >= 2
BuildConflicts: gem(regexp_parser) >= 3
BuildConflicts: gem(regexp_property_values) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(warning) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names character_set,character-set
%ruby_use_gem_dependency gouteur >= 1.1.0,gouteur < 2
Requires:      ruby >= 2.1.0
Provides:      gem(character_set) = 1.8.0

%description
Build, read, write and compare sets of Unicode codepoints.


%if_enabled    doc
%package       -n gem-character-set-doc
Version:       1.8.0
Release:       alt1
Summary:       Build, read, write and compare sets of Unicode codepoints documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета character_set
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(character_set) = 1.8.0

%description   -n gem-character-set-doc
Build, read, write and compare sets of Unicode codepoints documentation files.

%description   -n gem-character-set-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета character_set.
%endif


%if_enabled    devel
%package       -n gem-character-set-devel
Version:       1.8.0
Release:       alt1
Summary:       Build, read, write and compare sets of Unicode codepoints development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета character_set
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(character_set) = 1.8.0
Requires:      gem(benchmark-ips) >= 2.7
Requires:      gem(get_process_mem) >= 0.2.3
Requires:      gem(gouteur) >= 1.0.0
Requires:      gem(rake) >= 13.1
Requires:      gem(rake-compiler) >= 1.1
Requires:      gem(range_compressor) >= 1.0
Requires:      gem(regexp_parser) >= 2.9
Requires:      gem(regexp_property_values) >= 1.5
Requires:      gem(rspec) >= 3.8
Requires:      gem(rubocop) >= 1.59
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(warning) >= 1.3
Conflicts:     gem(benchmark-ips) >= 3
Conflicts:     gem(get_process_mem) >= 0.3
Conflicts:     gem(gouteur) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(range_compressor) >= 2
Conflicts:     gem(regexp_parser) >= 3
Conflicts:     gem(regexp_property_values) >= 2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(warning) >= 2

%description   -n gem-character-set-devel
Build, read, write and compare sets of Unicode codepoints development package.

%description   -n gem-character-set-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета character_set.
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
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-character-set-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-character-set-devel
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_includedir/*
%endif


%changelog
* Thu Oct 30 2025 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
