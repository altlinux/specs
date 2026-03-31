%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname cheffish

Name:          gem-cheffish
Version:       17.1.8
Release:       alt1
Summary:       Resources and tools for testing and interacting with Chef and Chef Server
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/cheffish
Vcs:           https://github.com/chef/cheffish.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(chef) >= 0
BuildRequires: gem(chef-utils) >= 17.0
BuildRequires: gem(chef-zero) >= 14.0
BuildRequires: gem(logger) >= 1.6
BuildRequires: gem(net-ssh) >= 0
BuildRequires: gem(ohai) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(syslog) >= 0
BuildConflicts: gem(logger) >= 2
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency logger >= 1.7,logger < 2
Requires:      ruby >= 3.1
Requires:      gem(chef-utils) >= 17.0
Requires:      gem(chef-zero) >= 14.0
Requires:      gem(logger) >= 1.6
Requires:      gem(net-ssh) >= 0
Conflicts:     gem(logger) >= 2
Obsoletes:     ruby-cheffish < %EVR
Provides:      ruby-cheffish = %EVR
Provides:      gem(cheffish) = 17.1.8

%description
This library provides a variety of convergent resources for interacting with the
Chef Server; along the way, it happens to provide some very useful and
sophisticated ways of running Chef resources as recipes in RSpec examples.


%if_enabled    doc
%package       -n gem-cheffish-doc
Version:       17.1.8
Release:       alt1
Summary:       Resources and tools for testing and interacting with Chef and Chef Server documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cheffish
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cheffish) = 17.1.8

%description   -n gem-cheffish-doc
Resources and tools for testing and interacting with Chef and Chef Server
documentation files.

This library provides a variety of convergent resources for interacting with the
Chef Server; along the way, it happens to provide some very useful and
sophisticated ways of running Chef resources as recipes in RSpec examples.

%description   -n gem-cheffish-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cheffish.
%endif


%if_enabled    devel
%package       -n gem-cheffish-devel
Version:       17.1.8
Release:       alt1
Summary:       Resources and tools for testing and interacting with Chef and Chef Server development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cheffish
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cheffish) = 17.1.8
Requires:      gem(chef) >= 0
Requires:      gem(chef-utils) >= 17.0
Requires:      gem(chef-zero) >= 14.0
Requires:      gem(logger) >= 1.6
Requires:      gem(net-ssh) >= 0
Requires:      gem(ohai) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(syslog) >= 0
Conflicts:     gem(logger) >= 2
Conflicts:     gem(rspec) >= 4

%description   -n gem-cheffish-devel
Resources and tools for testing and interacting with Chef and Chef Server
development package.

This library provides a variety of convergent resources for interacting with the
Chef Server; along the way, it happens to provide some very useful and
sophisticated ways of running Chef resources as recipes in RSpec examples.

%description   -n gem-cheffish-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cheffish.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-cheffish-doc
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-cheffish-devel
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md README.md
%endif


%changelog
* Tue Mar 31 2026 Pavel Skrylev <majioa@altlinux.org> 17.1.8-alt1
- ^ 17.1.4 -> 17.1.8

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
