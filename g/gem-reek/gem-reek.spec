%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname reek

Name:          gem-reek
Version:       6.3.0
Release:       alt1
Summary:       Code smell detector for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/troessner/reek
Vcs:           https://github.com/troessner/reek.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         move-codeclimate-engine-to-prod.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(aruba) >= 2.1
BuildRequires: gem(bigdecimal) >= 2.0.0
BuildRequires: gem(codeclimate-engine-rb) >= 0.4.0
BuildRequires: gem(cucumber) >= 9.0
BuildRequires: gem(kramdown) >= 2.1
BuildRequires: gem(kramdown-parser-gfm) >= 1.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rspec-benchmark) >= 0.6.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(yard) >= 0.9.5
BuildRequires: gem(redcarpet) >= 3.4
BuildRequires: gem(pry) >= 0.13.1
BuildRequires: gem(dry-schema) >= 1.13.0
BuildRequires: gem(parser) >= 3.3.0
BuildRequires: gem(rainbow) >= 2.0
BuildRequires: gem(rexml) >= 3.1
BuildConflicts: gem(aruba) >= 3
BuildConflicts: gem(bigdecimal) >= 4.0
BuildConflicts: gem(codeclimate-engine-rb) >= 0.5
BuildConflicts: gem(cucumber) >= 10
BuildConflicts: gem(kramdown) >= 3
BuildConflicts: gem(kramdown-parser-gfm) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-benchmark) >= 0.7
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(redcarpet) >= 4
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(dry-schema) >= 1.14
BuildConflicts: gem(parser) >= 3.4
BuildConflicts: gem(rainbow) >= 4
BuildConflicts: gem(rexml) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      gem(dry-schema) >= 1.13.0
Requires:      gem(parser) >= 3.3.0
Requires:      gem(rainbow) >= 2.0
Requires:      gem(rexml) >= 3.1
Requires:      gem(codeclimate-engine-rb) >= 0.4.0
Conflicts:     gem(dry-schema) >= 1.14
Conflicts:     gem(parser) >= 3.4
Conflicts:     gem(rainbow) >= 4
Conflicts:     gem(rexml) >= 4
Conflicts:     gem(codeclimate-engine-rb) >= 0.5
Provides:      gem(reek) = 6.3.0


%description
Reek is a tool that examines Ruby classes, modules and methods and reports any
code smells it finds.


%package       -n reek
Version:       6.3.0
Release:       alt1
Summary:       Code smell detector for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета reek
Group:         Other
BuildArch:     noarch

Requires:      gem(reek) = 6.3.0

%description   -n reek
Code smell detector for Ruby executable(s).

Reek is a tool that examines Ruby classes, modules and methods and reports any
code smells it finds.
%description   -n reek -l ru_RU.UTF-8
Исполнямка для самоцвета reek.


%if_enabled    doc
%package       -n gem-reek-doc
Version:       6.3.0
Release:       alt1
Summary:       Code smell detector for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета reek
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(reek) = 6.3.0

%description   -n gem-reek-doc
Code smell detector for Ruby documentation files.

Reek is a tool that examines Ruby classes, modules and methods and reports any
code smells it finds.
%description   -n gem-reek-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета reek.
%endif


%if_enabled    devel
%package       -n gem-reek-devel
Version:       6.3.0
Release:       alt1
Summary:       Code smell detector for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета reek
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(reek) = 6.3.0
Requires:      gem(aruba) >= 2.1
Requires:      gem(bigdecimal) >= 2.0.0
Requires:      gem(cucumber) >= 9.0
Requires:      gem(kramdown) >= 2.1
Requires:      gem(kramdown-parser-gfm) >= 1.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rspec-benchmark) >= 0.6.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(yard) >= 0.9.5
Requires:      gem(redcarpet) >= 3.4
Requires:      gem(pry) >= 0.13.1
Conflicts:     gem(aruba) >= 3
Conflicts:     gem(bigdecimal) >= 4.0
Conflicts:     gem(cucumber) >= 10
Conflicts:     gem(kramdown) >= 3
Conflicts:     gem(kramdown-parser-gfm) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-benchmark) >= 0.7
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rspec) >= 3
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(yard) >= 1
Conflicts:     gem(redcarpet) >= 4
Conflicts:     gem(pry) >= 1

%description   -n gem-reek-devel
Code smell detector for Ruby development package.

Reek is a tool that examines Ruby classes, modules and methods and reports any
code smells it finds.
%description   -n gem-reek-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета reek.
%endif


%prep
%setup
%autopatch

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

%files         -n reek
%doc README.md
%_bindir/code_climate_reek
%_bindir/reek

%if_enabled    doc
%files         -n gem-reek-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-reek-devel
%doc README.md
%endif


%changelog
* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 6.3.0-alt1
- ^ 6.1.4 -> 6.3.0 (without check/devel)
- ! fixed dep to codeclimate-engine from devel to prod (closes #49788)

* Sat Dec 02 2023 Pavel Skrylev <majioa@altlinux.org> 6.1.4-alt1
- ^ 6.1.1 -> 6.1.4 without devel

* Tue Nov 01 2022 Pavel Skrylev <majioa@altlinux.org> 6.1.1-alt1
- + packaged gem with Ruby Policy 2.0
