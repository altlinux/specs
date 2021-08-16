%define        gemname ci_reporter_test_utils

Name:          gem-ci-reporter-test-utils
Version:       0.0.4
Release:       alt1
Summary:       Test utilities for CI::Reporter
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ci-reporter/ci_reporter_test_utils
Vcs:           https://github.com/ci-reporter/ci_reporter_test_utils.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.6 gem(bundler) < 3
BuildRequires: gem(rake) >= 0 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(ci_reporter_test_utils) = 0.0.4

%description
Test utilities for CI::Reporter.


%package       -n gem-ci-reporter-test-utils-doc
Version:       0.0.4
Release:       alt1
Summary:       Test utilities for CI::Reporter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ci_reporter_test_utils
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ci_reporter_test_utils) = 0.0.4

%description   -n gem-ci-reporter-test-utils-doc
Test utilities for CI::Reporter documentation files.

%description   -n gem-ci-reporter-test-utils-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ci_reporter_test_utils.


%package       -n gem-ci-reporter-test-utils-devel
Version:       0.0.4
Release:       alt1
Summary:       Test utilities for CI::Reporter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ci_reporter_test_utils
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ci_reporter_test_utils) = 0.0.4
Requires:      gem(bundler) >= 1.6 gem(bundler) < 3
Requires:      gem(rake) >= 0 gem(rake) < 14

%description   -n gem-ci-reporter-test-utils-devel
Test utilities for CI::Reporter development package.

%description   -n gem-ci-reporter-test-utils-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ci_reporter_test_utils.


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

%files         -n gem-ci-reporter-test-utils-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ci-reporter-test-utils-devel
%doc README.md


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.4-alt1
- + packaged gem with Ruby Policy 2.0
