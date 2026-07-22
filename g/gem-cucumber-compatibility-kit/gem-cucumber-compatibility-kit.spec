%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname cucumber-compatibility-kit

Name:          gem-cucumber-compatibility-kit
Version:       29.2.2
Release:       alt1
Summary:       cucumber-compatibility-kit-29.2.2
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cucumber/compatibility-kit
Vcs:           https://github.com/cucumber/compatibility-kit.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 3.13
BuildRequires: gem(rubocop) >= 1.81.0
BuildRequires: gem(rubocop-performance) >= 1.26.0
BuildRequires: gem(rubocop-rspec) >= 3.7.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.81.6,rubocop < 2
%ruby_use_gem_dependency rubocop-performance >= 1.26.0,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
Requires:      ruby >= 3.1
Requires:      rubygems >= 3.2.8
Provides:      gem(cucumber-compatibility-kit) = 29.2.2

%description
Kit to check compatibility with official cucumber ruby implementation


%if_enabled    doc
%package       -n gem-cucumber-compatibility-kit-doc
Version:       29.2.2
Release:       alt1
Summary:       cucumber-compatibility-kit-29.2.2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cucumber-compatibility-kit
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-compatibility-kit) = 29.2.2

%description   -n gem-cucumber-compatibility-kit-doc
cucumber-compatibility-kit-29.2.2 documentation files.

Kit to check compatibility with official cucumber ruby implementation

%description   -n gem-cucumber-compatibility-kit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cucumber-compatibility-kit.
%endif


%if_enabled    devel
%package       -n gem-cucumber-compatibility-kit-devel
Version:       29.2.2
Release:       alt1
Summary:       cucumber-compatibility-kit-29.2.2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cucumber-compatibility-kit
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-compatibility-kit) = 29.2.2
Requires:      gem(rspec) >= 3.13
Requires:      gem(rubocop) >= 1.81.0
Requires:      gem(rubocop-performance) >= 1.26.0
Requires:      gem(rubocop-rspec) >= 3.7.0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rspec) >= 4

%description   -n gem-cucumber-compatibility-kit-devel
cucumber-compatibility-kit-29.2.2 development package.

Kit to check compatibility with official cucumber ruby implementation

%description   -n gem-cucumber-compatibility-kit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cucumber-compatibility-kit.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-cucumber-compatibility-kit-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-cucumber-compatibility-kit-devel
%doc LICENSE README.md
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 29.2.2-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
