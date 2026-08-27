%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname robottelo_reporter

Name:          gem-robottelo-reporter
Version:       0.1.1
Release:       alt2
Summary:       Generate tests results xml file report
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/SatelliteQE/robottelo_reporter
Vcs:           https://github.com/satelliteqe/robottelo_reporter.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(builder) >= 2.1.2
BuildRequires: gem(bundler) >= 1.16
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop-checkstyle_formatter) >= 0
BuildRequires: gem(simplecov) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(minitest) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
%ruby_alias_names robottelo_reporter,robottelo-reporter
Requires:      gem(builder) >= 2.1.2
Provides:      gem(robottelo_reporter) = 0.1.1

%description
Generate tests report output compatible with robottelo py.test output.


%if_enabled    doc
%package       -n gem-robottelo-reporter-doc
Version:       0.1.1
Release:       alt2
Summary:       Generate tests results xml file report documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета robottelo_reporter
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(robottelo_reporter) = 0.1.1

%description   -n gem-robottelo-reporter-doc
Generate tests results xml file report documentation files.

Generate tests report output compatible with robottelo py.test output.

%description   -n gem-robottelo-reporter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета robottelo_reporter.
%endif


%if_enabled    devel
%package       -n gem-robottelo-reporter-devel
Version:       0.1.1
Release:       alt2
Summary:       Generate tests results xml file report development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета robottelo_reporter
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(robottelo_reporter) = 0.1.1
Requires:      gem(bundler) >= 1.16
Requires:      gem(coveralls) >= 0
Requires:      gem(minitest) >= 5.0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop-checkstyle_formatter) >= 0
Requires:      gem(simplecov) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(minitest) >= 7

%description   -n gem-robottelo-reporter-devel
Generate tests results xml file report development package.

Generate tests report output compatible with robottelo py.test output.

%description   -n gem-robottelo-reporter-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета robottelo_reporter.
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
%doc LICENSE README.rst
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-robottelo-reporter-doc
%doc LICENSE README.rst
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-robottelo-reporter-devel
%doc LICENSE README.rst
%endif


%changelog
* Sat Aug 22 2026 Pavel Skrylev <majioa@altlinux.org> 0.1.1-alt2
- * rebased to upstream git flow

* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.1-alt1
- + packaged gem with Ruby Policy 2.0
