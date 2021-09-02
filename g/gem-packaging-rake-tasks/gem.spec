%define        gemname packaging_rake_tasks

Name:          gem-packaging-rake-tasks
Version:       1.5.0
Release:       alt1
Summary:       Rake tasks providing tasks to package project in git and integration with build service
License:       LGPL-2.1
Group:         Development/Ruby
Url:           https://github.com/openSUSE/packaging_rake_tasks
Vcs:           https://github.com/opensuse/packaging_rake_tasks.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rake) >= 0
Provides:      gem(packaging_rake_tasks) = 1.5.0


%description
Rake tasks to allow easy packaging ruby projects in git for Build Service or
other packaging service


%package       -n gem-packaging-rake-tasks-doc
Version:       1.5.0
Release:       alt1
Summary:       Rake tasks providing tasks to package project in git and integration with build service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета packaging_rake_tasks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(packaging_rake_tasks) = 1.5.0

%description   -n gem-packaging-rake-tasks-doc
Rake tasks providing tasks to package project in git and integration with build
service documentation files.

Rake tasks to allow easy packaging ruby projects in git for Build Service or
other packaging service

%description   -n gem-packaging-rake-tasks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета packaging_rake_tasks.


%package       -n gem-packaging-rake-tasks-devel
Version:       1.5.0
Release:       alt1
Summary:       Rake tasks providing tasks to package project in git and integration with build service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета packaging_rake_tasks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(packaging_rake_tasks) = 1.5.0

%description   -n gem-packaging-rake-tasks-devel
Rake tasks providing tasks to package project in git and integration with build
service development package.

Rake tasks to allow easy packaging ruby projects in git for Build Service or
other packaging service

%description   -n gem-packaging-rake-tasks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета packaging_rake_tasks.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-packaging-rake-tasks-doc
%ruby_gemdocdir

%files         -n gem-packaging-rake-tasks-devel


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- + packaged gem with Ruby Policy 2.0
