%define        gemname ci_reporter_minitest

Name:          gem-ci-reporter-minitest
Version:       1.0.0
Release:       alt1
Summary:       Connects CI::Reporter to Minitest
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ci-reporter/ci_reporter_minitest
Vcs:           https://github.com/ci-reporter/ci_reporter_minitest.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(ci_reporter) >= 2.0 gem(ci_reporter) < 3
BuildRequires: gem(bundler) >= 1.6 gem(bundler) < 3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rspec-collection_matchers) >= 0
BuildRequires: gem(ci_reporter_test_utils) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(ci_reporter) >= 2.0 gem(ci_reporter) < 3
Provides:      gem(ci_reporter_minitest) = 1.0.0

%description
Connects CI::Reporter to Minitest.


%package       -n gem-ci-reporter-minitest-doc
Version:       1.0.0
Release:       alt1
Summary:       Connects CI::Reporter to Minitest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ci_reporter_minitest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ci_reporter_minitest) = 1.0.0

%description   -n gem-ci-reporter-minitest-doc
Connects CI::Reporter to Minitest documentation files.

%description   -n gem-ci-reporter-minitest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ci_reporter_minitest.


%package       -n gem-ci-reporter-minitest-devel
Version:       1.0.0
Release:       alt1
Summary:       Connects CI::Reporter to Minitest development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ci_reporter_minitest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ci_reporter_minitest) = 1.0.0
Requires:      gem(bundler) >= 1.6 gem(bundler) < 3
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(rspec-collection_matchers) >= 0
Requires:      gem(ci_reporter_test_utils) >= 0

%description   -n gem-ci-reporter-minitest-devel
Connects CI::Reporter to Minitest development package.

%description   -n gem-ci-reporter-minitest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ci_reporter_minitest.


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

%files         -n gem-ci-reporter-minitest-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ci-reporter-minitest-devel
%doc README.md


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
