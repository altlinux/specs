%define        gemname ci_reporter

Name:          gem-ci-reporter
Version:       2.0.0
Release:       alt1
Summary:       Connects Ruby test frameworks to CI systems via JUnit reports
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ci-reporter/ci_reporter
Vcs:           https://github.com/ci-reporter/ci_reporter.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(builder) >= 2.1.2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Requires:      gem(builder) >= 2.1.2
Provides:      gem(ci_reporter) = 2.0.0


%description
CI::Reporter is an add-on to Ruby testing frameworks that allows you to generate
XML reports of your test runs. The resulting files can be read by a continuous
integration system that understands Ant's JUnit report format.


%package       -n gem-ci-reporter-doc
Version:       2.0.0
Release:       alt1
Summary:       Connects Ruby test frameworks to CI systems via JUnit reports documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ci_reporter
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ci_reporter) = 2.0.0

%description   -n gem-ci-reporter-doc
Connects Ruby test frameworks to CI systems via JUnit reports documentation
files.

CI::Reporter is an add-on to Ruby testing frameworks that allows you to generate
XML reports of your test runs. The resulting files can be read by a continuous
integration system that understands Ant's JUnit report format.

%description   -n gem-ci-reporter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ci_reporter.


%package       -n gem-ci-reporter-devel
Version:       2.0.0
Release:       alt1
Summary:       Connects Ruby test frameworks to CI systems via JUnit reports development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ci_reporter
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ci_reporter) = 2.0.0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-ci-reporter-devel
Connects Ruby test frameworks to CI systems via JUnit reports development
package.

CI::Reporter is an add-on to Ruby testing frameworks that allows you to generate
XML reports of your test runs. The resulting files can be read by a continuous
integration system that understands Ant's JUnit report format.

%description   -n gem-ci-reporter-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ci_reporter.


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

%files         -n gem-ci-reporter-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ci-reporter-devel
%doc README.md


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
