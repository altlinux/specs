%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname guard-cucumber

Name:          gem-guard-cucumber
Version:       3.0.0
Release:       alt2
Summary:       Guard plugin for Cucumber
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/guard/guard-cucumber
Vcs:           https://github.com/guard/guard-cucumber.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.6
BuildRequires: gem(cucumber) >= 3.1
BuildRequires: gem(guard-bundler) >= 2.0.0
BuildRequires: gem(guard-compat) >= 1.0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(guard-rubocop) >= 0
BuildRequires: gem(nenv) >= 0.1
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(rspec) >= 3.1
BuildRequires: gem(rubocop) >= 0.39.0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(guard-bundler) >= 4
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency guard-bundler >= 3.1.0,guard-bundler < 4
%ruby_use_gem_dependency rubocop >= 1.81.6,rubocop < 2
Requires:      rubygems >= 1.3.6
Requires:      gem(cucumber) >= 3.1
Requires:      gem(nenv) >= 0.1
Provides:      gem(guard-cucumber) = 3.0.0

%description
Guard::Cucumber automatically run your features (much like autotest)


%if_enabled    doc
%package       -n gem-guard-cucumber-doc
Version:       3.0.0
Release:       alt2
Summary:       Guard plugin for Cucumber documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета guard-cucumber
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(guard-cucumber) = 3.0.0

%description   -n gem-guard-cucumber-doc
Guard plugin for Cucumber documentation files.

Guard::Cucumber automatically run your features (much like autotest)

%description   -n gem-guard-cucumber-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета guard-cucumber.
%endif


%if_enabled    devel
%package       -n gem-guard-cucumber-devel
Version:       3.0.0
Release:       alt2
Summary:       Guard plugin for Cucumber development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета guard-cucumber
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(guard-cucumber) = 3.0.0
Requires:      gem(bundler) >= 1.6
Requires:      gem(guard-bundler) >= 2.0.0
Requires:      gem(guard-compat) >= 1.0
Requires:      gem(guard-rspec) >= 0
Requires:      gem(guard-rubocop) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(rspec) >= 3.1
Requires:      gem(rubocop) >= 0.39.0
Requires:      gem(yard) >= 0
Conflicts:     gem(guard-bundler) >= 4
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-guard-cucumber-devel
Guard plugin for Cucumber development package.

Guard::Cucumber automatically run your features (much like autotest)

%description   -n gem-guard-cucumber-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета guard-cucumber.
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
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-guard-cucumber-doc
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-guard-cucumber-devel
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%endif


%changelog
* Tue Jul 07 2026 Alexander Burmatov <thatman@altlinux.org> 3.0.0-alt2
- enable check

* Tue Jul 07 2026 Alexander Burmatov <thatman@altlinux.org> 3.0.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
