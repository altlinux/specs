%define        gemname concourse

Name:          gem-concourse
Version:       0.40.0
Release:       alt1
Summary:       Provide Rake tasks to ease management of Concourse pipelines
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/flavorjones/concourse-gem
Vcs:           https://github.com/flavorjones/concourse-gem.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(term-ansicolor) >= 0
BuildRequires: gem(bundler) >= 2.1.4 gem(bundler) < 3
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(term-ansicolor) >= 0
Obsoletes:     ruby-concourse < %EVR
Provides:      ruby-concourse = %EVR
Provides:      gem(concourse) = 0.40.0


%description
The concourse gem provides rake tasks to help you manage Concourse CI pipelines,
jobs, and workers, to assist in running tasks with fly execute, and even run a
local ephemeral deployment of Concourse on your development machine.

If you're not familiar with Concourse CI, you can read up on it at
https://concourse-ci.org


%package       -n gem-concourse-doc
Version:       0.40.0
Release:       alt1
Summary:       Provide Rake tasks to ease management of Concourse pipelines
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета concourse
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(concourse) = 0.40.0

%description   -n gem-concourse-doc
Provide Rake tasks to ease management of Concourse pipelines. See
https://concourse.ci/ to learn about Concourse documentation files.

The concourse gem provides rake tasks to help you manage Concourse CI pipelines,
jobs, and workers, to assist in running tasks with fly execute, and even run a
local ephemeral deployment of Concourse on your development machine.

If you're not familiar with Concourse CI, you can read up on it at
https://concourse-ci.org

%description   -n gem-concourse-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета concourse.


%package       -n gem-concourse-devel
Version:       0.40.0
Release:       alt1
Summary:       Provide Rake tasks to ease management of Concourse pipelines
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета concourse
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(concourse) = 0.40.0
Requires:      gem(bundler) >= 2.1.4 gem(bundler) < 3
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-concourse-devel
Provide Rake tasks to ease management of Concourse pipelines. See
https://concourse.ci/ to learn about Concourse development package.

The concourse gem provides rake tasks to help you manage Concourse CI pipelines,
jobs, and workers, to assist in running tasks with fly execute, and even run a
local ephemeral deployment of Concourse on your development machine.

If you're not familiar with Concourse CI, you can read up on it at
https://concourse-ci.org

%description   -n gem-concourse-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета concourse.


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

%files         -n gem-concourse-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-concourse-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.40.0-alt1
- ^ 0.26.0 -> 0.40.0

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 0.26.0-alt1
- Bump to 0.26.0.
- Use Ruby Policy 2.0.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1
- New version.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 0.18.0-alt1
- Initial build for Sisyphus
