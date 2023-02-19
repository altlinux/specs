# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname chef-api

Name:          gem-chef-api
Version:       0.10.10.5
Release:       alt0.1
Summary:       A tiny Chef API client with minimal dependencies
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef-boneyard/chef-api
Vcs:           https://github.com/chef-boneyard/chef-api.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(chefstyle) >= 0
BuildRequires: gem(rake) >= 10.1.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(chef-zero) >= 2.0.0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(github-markup) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0.4.0
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(mixlib-log) >= 1
BuildRequires: gem(mime-types) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(chef-zero) >= 16
BuildConflicts: gem(pry-stack_explorer) >= 1
BuildConflicts: gem(mixlib-log) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency pry-stack_explorer >= 0.6.1,pry-stack_explorer < 1
%ruby_use_gem_dependency chef-zero >= 15.0.12,chef-zero < 16
Requires:      gem(mixlib-log) >= 1
Requires:      gem(mime-types) >= 0
Conflicts:     gem(mixlib-log) >= 4
Provides:      gem(chef-api) = 0.10.10.5

%ruby_use_gem_version chef-api:0.10.10.5
%ruby_use_gem_version chef-infra-api:0.10.10.5

%description
A tiny Chef API client with minimal dependencies.


%package       -n gem-chef-infra-api
Version:       0.10.10.5
Release:       alt0.1
Summary:       A tiny Chef API client with minimal dependencies
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mixlib-log) >= 1
Requires:      gem(mime-types) >= 0
Conflicts:     gem(mixlib-log) >= 4
Provides:      gem(chef-infra-api) = 0.10.10.5

%description   -n gem-chef-infra-api
A tiny Chef Infra API gem.


%package       -n gem-chef-infra-api-doc
Version:       0.10.10.5
Release:       alt0.1
Summary:       A tiny Chef API client with minimal dependencies documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-infra-api
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-infra-api) = 0.10.10.5

%description   -n gem-chef-infra-api-doc
A tiny Chef API client with minimal dependencies documentation files.

A tiny Chef Infra API gem.

%description   -n gem-chef-infra-api-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-infra-api.


%package       -n gem-chef-infra-api-devel
Version:       0.10.10.5
Release:       alt0.1
Summary:       A tiny Chef API client with minimal dependencies development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-infra-api
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-infra-api) = 0.10.10.5
Requires:      gem(chefstyle) >= 0
Requires:      gem(rake) >= 10.1.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(chef-zero) >= 2.0.0
Requires:      gem(yard) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(github-markup) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry-stack_explorer) >= 0.4.0
Requires:      gem(rb-readline) >= 0
Requires:      gem(chef-api) = 0.10.10.5
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(chef-zero) >= 16
Conflicts:     gem(pry-stack_explorer) >= 1

%description   -n gem-chef-infra-api-devel
A tiny Chef API client with minimal dependencies development package.

A tiny Chef Infra API gem.

%description   -n gem-chef-infra-api-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-infra-api.


%package       -n gem-chef-api-doc
Version:       0.10.10.5
Release:       alt0.1
Summary:       A tiny Chef API client with minimal dependencies documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-api
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-api) = 0.10.10.5

%description   -n gem-chef-api-doc
A tiny Chef API client with minimal dependencies documentation files.

%description   -n gem-chef-api-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-api.


%package       -n gem-chef-api-devel
Version:       0.10.10.5
Release:       alt0.1
Summary:       A tiny Chef API client with minimal dependencies development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-api
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-api) = 0.10.10.5
Requires:      gem(chefstyle) >= 0
Requires:      gem(rake) >= 10.1.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(chef-zero) >= 2.0.0
Requires:      gem(yard) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(github-markup) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry-stack_explorer) >= 0.4.0
Requires:      gem(rb-readline) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(chef-zero) >= 16
Conflicts:     gem(pry-stack_explorer) >= 1

%description   -n gem-chef-api-devel
A tiny Chef API client with minimal dependencies development package.

%description   -n gem-chef-api-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-api.


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

%files         -n gem-chef-infra-api
%ruby_gemspecdir/chef-infra-api-0.10.10.5.gemspec
%ruby_gemslibdir/chef-infra-api-0.10.10.5

%files         -n gem-chef-infra-api-doc
%ruby_gemsdocdir/chef-infra-api-0.10.10.5

%files         -n gem-chef-infra-api-devel

%files         -n gem-chef-api-doc
%ruby_gemdocdir

%files         -n gem-chef-api-devel


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 0.10.10.5-alt0.1
- ^ 0.10.10 -> 0.10.10p5

* Thu Feb 11 2021 Pavel Skrylev <majioa@altlinux.org> 0.10.10-alt1
- + packaged gem with usage Ruby Policy 2.0
