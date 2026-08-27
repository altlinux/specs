%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ci_reporter_minitest

Name:          gem-ci-reporter-minitest
Version:       1.0.0
Release:       alt2
Summary:       Connects CI::Reporter to Minitest
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ci-reporter/ci_reporter_minitest
Vcs:           https://github.com/ci-reporter/ci_reporter_minitest.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bundler) >= 1.6
BuildRequires: gem(ci_reporter) >= 2.0
BuildRequires: gem(ci_reporter_test_utils) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rspec-collection_matchers) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(ci_reporter) >= 3
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency minitest >= 6.0
%ruby_alias_names ci_reporter_minitest,ci-reporter-minitest
Requires:      gem(ci_reporter) >= 2.0
Requires:      gem(minitest) >= 5.0
Conflicts:     gem(ci_reporter) >= 3
Conflicts:     gem(minitest) >= 7
Provides:      gem(ci_reporter_minitest) = 1.0.0

%description
Connects CI::Reporter to Minitest.


%if_enabled    doc
%package       -n gem-ci-reporter-minitest-doc
Version:       1.0.0
Release:       alt2
Summary:       Connects CI::Reporter to Minitest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ci_reporter_minitest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem-ci-reporter-minitest = 1.0.0-alt2
Requires:      gem(ci_reporter_minitest) = 1.0.0

%description   -n gem-ci-reporter-minitest-doc
Connects CI::Reporter to Minitest documentation files.

%description   -n gem-ci-reporter-minitest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ci_reporter_minitest.
%endif


%if_enabled    devel
%package       -n gem-ci-reporter-minitest-devel
Version:       1.0.0
Release:       alt2
Summary:       Connects CI::Reporter to Minitest development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ci_reporter_minitest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem-ci-reporter-minitest = 1.0.0-alt2
Requires:      gem(ci_reporter_minitest) = 1.0.0
Requires:      gem(bundler) >= 1.6
Requires:      gem(ci_reporter_test_utils) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rspec-collection_matchers) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rspec) >= 4

%description   -n gem-ci-reporter-minitest-devel
Connects CI::Reporter to Minitest development package.

%description   -n gem-ci-reporter-minitest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ci_reporter_minitest.
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

%if_enabled    doc
%files         -n gem-ci-reporter-minitest-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ci-reporter-minitest-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Wed Aug 19 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2
- * rebased to upstream
- ! fixed dep to minitest gem

* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
