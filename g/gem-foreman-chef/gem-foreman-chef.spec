%define        gemname foreman_chef

Name:          gem-foreman-chef
Version:       0.10.0
Release:       alt1
Summary:       Plugin for Chef integration with Foreman
License:       GPL-3
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_chef
Vcs:           https://github.com/theforeman/foreman_chef.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         foreman-3.5.0.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(deface) >= 0
BuildRequires: gem(foreman-tasks) >= 0.8.0
BuildRequires: gem(sqlite3) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

Requires:      gem(deface) >= 0
Requires:      gem(foreman-tasks) >= 0.8.0
Provides:      gem(foreman_chef) = 0.10.0

%ruby_alias_names foreman_chef,foreman-chef

%description
Foreman extensions that are required for better Chef integration.


%package       -n gem-foreman-chef-doc
Version:       0.10.0
Release:       alt1
Summary:       Plugin for Chef integration with Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_chef
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_chef) = 0.10.0

%description   -n gem-foreman-chef-doc
Plugin for Chef integration with Foreman documentation files.

Foreman extensions that are required for better Chef integration.

%description   -n gem-foreman-chef-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_chef.


%package       -n gem-foreman-chef-devel
Version:       0.10.0
Release:       alt1
Summary:       Plugin for Chef integration with Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_chef
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_chef) = 0.10.0
Requires:      gem(sqlite3) >= 0

%description   -n gem-foreman-chef-devel
Plugin for Chef integration with Foreman development package.

Foreman extensions that are required for better Chef integration.

%description   -n gem-foreman-chef-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_chef.


%prep
%setup
%autopatch

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

%files         -n gem-foreman-chef-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-foreman-chef-devel
%doc README.md


%changelog
* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt1
- + packaged gem with Ruby Policy 2.0
