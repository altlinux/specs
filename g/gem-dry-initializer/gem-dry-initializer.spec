%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname dry-initializer

Name:          gem-dry-initializer
Version:       3.1.1
Release:       alt1
Summary:       DSL for declaring params and options of the initializer
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-initializer
Vcs:           https://github.com/dry-rb/dry-initializer.git
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
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(dry-types) >= 0
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(active_attr) >= 0
BuildRequires: gem(anima) >= 0
BuildRequires: gem(attr_extras) >= 0
BuildRequires: gem(benchmark-ips) >= 2.5
BuildRequires: gem(concord) >= 0
BuildRequires: gem(fast_attributes) >= 0
BuildRequires: gem(kwattr) >= 0
BuildRequires: gem(ruby-prof) >= 0
BuildRequires: gem(values) >= 0
BuildRequires: gem(value_struct) >= 0
BuildRequires: gem(virtus) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(benchmark-ips) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Provides:      gem(dry-initializer) = 3.1.1


%description
DSL for declaring params and options of the initializer


%if_enabled    doc
%package       -n gem-dry-initializer-doc
Version:       3.1.1
Release:       alt1
Summary:       DSL for declaring params and options of the initializer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-initializer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dry-initializer) = 3.1.1

%description   -n gem-dry-initializer-doc
DSL for declaring params and options of the initializer documentation files.
%description   -n gem-dry-initializer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-initializer.
%endif


%if_enabled    devel
%package       -n gem-dry-initializer-devel
Version:       3.1.1
Release:       alt1
Summary:       DSL for declaring params and options of the initializer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-initializer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dry-initializer) = 3.1.1
Requires:      gem(rake) >= 12.3.3
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(warning) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rspec) >= 0
Requires:      gem(dry-types) >= 0
Requires:      gem(activesupport) >= 0
Requires:      gem(active_attr) >= 0
Requires:      gem(anima) >= 0
Requires:      gem(attr_extras) >= 0
Requires:      gem(benchmark-ips) >= 2.5
Requires:      gem(concord) >= 0
Requires:      gem(fast_attributes) >= 0
Requires:      gem(kwattr) >= 0
Requires:      gem(ruby-prof) >= 0
Requires:      gem(values) >= 0
Requires:      gem(value_struct) >= 0
Requires:      gem(virtus) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(benchmark-ips) >= 3

%description   -n gem-dry-initializer-devel
DSL for declaring params and options of the initializer development package.
%description   -n gem-dry-initializer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dry-initializer.
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
%files         -n gem-dry-initializer-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-initializer-devel
%doc README.md
%endif


%changelog
* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 3.1.1-alt1
- + packaged gem with Ruby Policy 2.0
