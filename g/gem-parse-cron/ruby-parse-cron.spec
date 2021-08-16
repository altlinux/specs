%define        gemname parse-cron

Name:          gem-parse-cron
Version:       0.1.4
Release:       alt2
Summary:       Parse crontab syntax to determine scheduled run times
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/siebertm/parse-cron
Vcs:           https://github.com/siebertm/parse-cron.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libruby-devel
BuildRequires: gem(rspec) >= 2.6.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Obsoletes:     ruby-parse-cron < %EVR
Provides:      ruby-parse-cron = %EVR
Provides:      gem(parse-cron) = 0.1.4


%description
Parse crontab syntax to determine scheduled run times. The goal of this gem is
to parse a crontab timing specification and determine when the job should be
run. It is not a scheduler, it does not run the jobs.


%package       -n gem-parse-cron-doc
Version:       0.1.4
Release:       alt2
Summary:       Parse crontab syntax to determine scheduled run times documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета parse-cron
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(parse-cron) = 0.1.4

%description   -n gem-parse-cron-doc
Parse crontab syntax to determine scheduled run times documentation
files.

Parse crontab syntax to determine scheduled run times. The goal of this gem is
to parse a crontab timing specification and determine when the job should be
run. It is not a scheduler, it does not run the jobs.

%description   -n gem-parse-cron-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета parse-cron.


%package       -n gem-parse-cron-devel
Version:       0.1.4
Release:       alt2
Summary:       Parse crontab syntax to determine scheduled run times development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета parse-cron
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(parse-cron) = 0.1.4
Requires:      gem(rspec) >= 2.6.0 gem(rspec) < 4

%description   -n gem-parse-cron-devel
Parse crontab syntax to determine scheduled run times development
package.

Parse crontab syntax to determine scheduled run times. The goal of this gem is
to parse a crontab timing specification and determine when the job should be
run. It is not a scheduler, it does not run the jobs.

%description   -n gem-parse-cron-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета parse-cron.


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

%files         -n gem-parse-cron-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-parse-cron-devel
%doc README.md


%changelog
* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.4-alt2
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Sep 01 2017 Alexey Shabalin <shaba@altlinux.ru> 0.1.4-alt1
- Initial build in Sisyphus
