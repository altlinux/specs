%define        gemname cheffish

Name:          gem-cheffish
Version:       17.1.4
Release:       alt1
Summary:       Resources and tools for testing and interacting with Chef and Chef Server
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/cheffish
Vcs:           https://github.com/chef/cheffish.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(chefstyle) >= 2.0.8 gem(chefstyle) < 3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(chef-zero) >= 14.0
BuildRequires: gem(chef-utils) >= 17.0
BuildRequires: gem(net-ssh) >= 0
BuildRequires: gem(chefstyle) >= 2.0.8 gem(chefstyle) < 3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(chef-zero) >= 14.0
BuildRequires: gem(chef-utils) >= 17.0
BuildRequires: gem(net-ssh) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency chefstyle >= 2.2.2,chefstyle < 3
Requires:      gem(chef-zero) >= 14.0
Requires:      gem(chef-utils) >= 17.0
Requires:      gem(net-ssh) >= 0
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR
Provides:      gem(cheffish) = 17.1.4


%description
This library provides a variety of convergent resources for interacting with the
Chef Server; along the way, it happens to provide some very useful and
sophisticated ways of running Chef resources as recipes in RSpec examples.


%package       -n gem-cheffish-doc
Version:       17.1.4
Release:       alt1
Summary:       Resources and tools for testing and interacting with Chef and Chef Server documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cheffish
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(cheffish) = 17.1.4

%description   -n gem-cheffish-doc
Resources and tools for testing and interacting with Chef and Chef Server
documentation files.

This library provides a variety of convergent resources for interacting with the
Chef Server; along the way, it happens to provide some very useful and
sophisticated ways of running Chef resources as recipes in RSpec examples.

%description   -n gem-cheffish-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cheffish.


%package       -n gem-cheffish-devel
Version:       17.1.4
Release:       alt1
Summary:       Resources and tools for testing and interacting with Chef and Chef Server development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cheffish
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cheffish) = 17.1.4
Requires:      gem(chefstyle) >= 2.0.8 gem(chefstyle) < 3
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-cheffish-devel
Resources and tools for testing and interacting with Chef and Chef Server
development package.

This library provides a variety of convergent resources for interacting with the
Chef Server; along the way, it happens to provide some very useful and
sophisticated ways of running Chef resources as recipes in RSpec examples.

%description   -n gem-cheffish-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cheffish.


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

%files         -n gem-cheffish-doc
%ruby_gemdocdir

%files         -n gem-cheffish-devel


%changelog
* Thu Oct 27 2022 Pavel Skrylev <majioa@altlinux.org> 17.1.4-alt1
- ^ 16.0.3 -> 17.1.4

* Mon Jul 13 2020 Pavel Skrylev <majioa@altlinux.org> 16.0.3-alt1
- ^ 14.0.9 -> 16.0.3
- ! spec tags and syntax

* Mon Apr 08 2019 Pavel Skrylev <majioa@altlinux.org> 14.0.9-alt1
- ^ 14.0.1 -> 14.0.9
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.1-alt1
- Initial build for Sisyphus
