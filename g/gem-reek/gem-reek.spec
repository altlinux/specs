%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname reek

Name:          gem-reek
Version:       6.5.0
Release:       alt1
Summary:       Code smell detector for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/troessner/reek
Vcs:           https://github.com/troessner/reek.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby rake setup-rb
%if_enabled check
BuildRequires: gem(aruba) >= 2.3
BuildRequires: gem(codeclimate-engine-rb) >= 0.4.0
BuildRequires: gem(cucumber) >= 10.0
BuildRequires: gem(dry-schema) >= 1.13
BuildRequires: gem(logger) >= 1.6
BuildRequires: gem(parser) >= 3.3.0
BuildRequires: gem(rainbow) >= 3.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rexml) >= 3.1
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rspec-benchmark) >= 0.6.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rspec) >= 3.7.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(yard) >= 0.9.5
BuildConflicts: gem(aruba) >= 3
BuildConflicts: gem(codeclimate-engine-rb) >= 0.5
BuildConflicts: gem(cucumber) >= 12.0
BuildConflicts: gem(dry-schema) >= 2
BuildConflicts: gem(logger) >= 2
BuildConflicts: gem(parser) >= 3.4
BuildConflicts: gem(rainbow) >= 4
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rexml) >= 4
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-benchmark) >= 0.7
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      ruby >= 3.1.0
Requires:      gem(dry-schema) >= 1.13
Requires:      gem(logger) >= 1.6
Requires:      gem(parser) >= 3.3.0
Requires:      gem(rainbow) >= 3.0
Requires:      gem(rexml) >= 3.1
Conflicts:     gem(dry-schema) >= 2
Conflicts:     gem(logger) >= 2
Conflicts:     gem(parser) >= 3.4
Conflicts:     gem(rainbow) >= 4
Conflicts:     gem(rexml) >= 4
Provides:      gem(reek) = 6.5.0

%description
Reek is a tool that examines Ruby classes, modules and methods and reports any
code smells it finds.


%package       -n reek
Version:       6.5.0
Release:       alt1
Summary:       Code smell detector for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета reek
Group:         Other
BuildArch:     noarch

Requires:      gem(reek) = 6.5.0

%description   -n reek
Code smell detector for Ruby executable(s).

Reek is a tool that examines Ruby classes, modules and methods and reports any
code smells it finds.

%description   -n reek -l ru_RU.UTF-8
Исполнямка для самоцвета reek.


%if_enabled    doc
%package       -n gem-reek-doc
Version:       6.5.0
Release:       alt1
Summary:       Code smell detector for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета reek
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(reek) = 6.5.0

%description   -n gem-reek-doc
Code smell detector for Ruby documentation files.

Reek is a tool that examines Ruby classes, modules and methods and reports any
code smells it finds.

%description   -n gem-reek-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета reek.
%endif


%if_enabled    devel
%package       -n gem-reek-devel
Version:       6.5.0
Release:       alt1
Summary:       Code smell detector for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета reek
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(reek) = 6.5.0

%description   -n gem-reek-devel
Code smell detector for Ruby development package.

Reek is a tool that examines Ruby classes, modules and methods and reports any
code smells it finds.

%description   -n gem-reek-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета reek.
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
%doc CHANGELOG.md CONTRIBUTING.md License.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n reek
%doc CHANGELOG.md CONTRIBUTING.md License.txt README.md
%_bindir/code_climate_reek
%_bindir/reek

%if_enabled    doc
%files         -n gem-reek-doc
%doc CHANGELOG.md CONTRIBUTING.md License.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-reek-devel
%doc CHANGELOG.md CONTRIBUTING.md License.txt README.md
%endif


%changelog
* Mon Jun 01 2026 Pavel Skrylev <majioa@altlinux.org> 6.5.0-alt1
- ^ 6.3.0 -> 6.5.0

* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 6.3.0-alt1
- ^ 6.1.4 -> 6.3.0 (without check/devel)
- ! fixed dep to codeclimate-engine from devel to prod (closes #49788)

* Sat Dec 02 2023 Pavel Skrylev <majioa@altlinux.org> 6.1.4-alt1
- ^ 6.1.1 -> 6.1.4 without devel

* Tue Nov 01 2022 Pavel Skrylev <majioa@altlinux.org> 6.1.1-alt1
- + packaged gem with Ruby Policy 2.0
