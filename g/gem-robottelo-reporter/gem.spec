%define        gemname robottelo_reporter

Name:          gem-robottelo-reporter
Version:       0.1.1
Release:       alt1
Summary:       Generate tests results xml file report
License:       Apache 2.0
Group:         Development/Ruby
Url:           https://github.com/SatelliteQE/robottelo_reporter
Vcs:           https://github.com/satelliteqe/robottelo_reporter.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(builder) >= 2.1.2
BuildRequires: gem(bundler) >= 1.16 gem(bundler) < 3
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      gem(builder) >= 2.1.2
Provides:      gem(robottelo_reporter) = 0.1.1


%description
Generate tests report output compatible with robottelo py.test output.


%package       -n gem-robottelo-reporter-doc
Version:       0.1.1
Release:       alt1
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


%package       -n gem-robottelo-reporter-devel
Version:       0.1.1
Release:       alt1
Summary:       Generate tests results xml file report development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета robottelo_reporter
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(robottelo_reporter) = 0.1.1
Requires:      gem(bundler) >= 1.16 gem(bundler) < 3
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6

%description   -n gem-robottelo-reporter-devel
Generate tests results xml file report development package.

Generate tests report output compatible with robottelo py.test output.

%description   -n gem-robottelo-reporter-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета robottelo_reporter.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rst
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-robottelo-reporter-doc
%doc README.rst
%ruby_gemdocdir

%files         -n gem-robottelo-reporter-devel
%doc README.rst


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.1-alt1
- + packaged gem with Ruby Policy 2.0
