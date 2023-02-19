%define        gemname codeclimate-test-reporter

Name:          gem-codeclimate-test-reporter
Version:       1.0.9
Release:       alt1.1
Summary:       Uploads Ruby test coverage data to Code Climate
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/codeclimate/ruby-test-reporter
Vcs:           https://github.com/codeclimate/ruby-test-reporter.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(webmock) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(simplecov) >= 0.17
Provides:      gem(codeclimate-test-reporter) = 1.0.9


%description
Collects test coverage data from your Ruby test suite and sends it to Code
Climate's hosted, automated code review service. Based on SimpleCov.


%package       -n codeclimate-test-reporter
Version:       1.0.9
Release:       alt1.1
Summary:       Uploads Ruby test coverage data to Code Climate executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета codeclimate-test-reporter
Group:         Other
BuildArch:     noarch

Requires:      gem(codeclimate-test-reporter) = 1.0.9

%description   -n codeclimate-test-reporter
Uploads Ruby test coverage data to Code Climate executable(s).

Collects test coverage data from your Ruby test suite and sends it to Code
Climate's hosted, automated code review service. Based on SimpleCov.

%description   -n codeclimate-test-reporter -l ru_RU.UTF-8
Исполнямка для самоцвета codeclimate-test-reporter.


%package       -n gem-codeclimate-test-reporter-doc
Version:       1.0.9
Release:       alt1.1
Summary:       Uploads Ruby test coverage data to Code Climate documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета codeclimate-test-reporter
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(codeclimate-test-reporter) = 1.0.9

%description   -n gem-codeclimate-test-reporter-doc
Uploads Ruby test coverage data to Code Climate documentation files.

Collects test coverage data from your Ruby test suite and sends it to Code
Climate's hosted, automated code review service. Based on SimpleCov.

%description   -n gem-codeclimate-test-reporter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета codeclimate-test-reporter.


%package       -n gem-codeclimate-test-reporter-devel
Version:       1.0.9
Release:       alt1.1
Summary:       Uploads Ruby test coverage data to Code Climate development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета codeclimate-test-reporter
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(codeclimate-test-reporter) = 1.0.9
Requires:      gem(bundler) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(webmock) >= 0

%description   -n gem-codeclimate-test-reporter-devel
Uploads Ruby test coverage data to Code Climate development package.

Collects test coverage data from your Ruby test suite and sends it to Code
Climate's hosted, automated code review service. Based on SimpleCov.

%description   -n gem-codeclimate-test-reporter-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета codeclimate-test-reporter.


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

%files         -n codeclimate-test-reporter
%doc README.md
%_bindir/cc-tddium-post-worker
%_bindir/codeclimate-test-reporter

%files         -n gem-codeclimate-test-reporter-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-codeclimate-test-reporter-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.9-alt1.1
- ! deps gem in spec

* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.9-alt1
- + packaged gem with Ruby Policy 2.0
