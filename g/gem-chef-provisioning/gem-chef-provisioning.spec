%define        gemname chef-provisioning

Name:          gem-chef-provisioning
Version:       2.7.7
Release:       alt1.3
Summary:       A library for creating machines and infrastructures idempotently in Chef
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/chef-provisioning
Vcs:           https://github.com/chef/chef-provisioning.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(ohai) >= 0
BuildRequires: gem(chef) >= 0
BuildRequires: gem(chefstyle) >= 0.10.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(net-ssh) >= 2.9
BuildRequires: gem(net-scp) >= 1.0
BuildRequires: gem(net-ssh-gateway) > 1.2
BuildRequires: gem(inifile) >= 2.0.2
BuildRequires: gem(cheffish) >= 4.0
BuildRequires: gem(winrm) >= 2.0
BuildRequires: gem(winrm-fs) >= 1.0
BuildRequires: gem(winrm-elevated) >= 1.0
BuildRequires: gem(mixlib-install) >= 1.0
BuildConflicts: gem(chefstyle) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(net-ssh) >= 7
BuildConflicts: gem(net-scp) >= 4
BuildConflicts: gem(net-ssh-gateway) >= 3.0
BuildConflicts: gem(cheffish) >= 18
BuildConflicts: gem(winrm) >= 3
BuildConflicts: gem(winrm-fs) >= 2
BuildConflicts: gem(winrm-elevated) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency net-ssh >= 6.1.0,net-ssh < 7
%ruby_use_gem_dependency net-scp >= 3.0.0,net-scp < 4
%ruby_use_gem_dependency chefstyle >= 2.2.2,chefstyle < 3
%ruby_use_gem_dependency cheffish >= 17.1.4,cheffish < 18
Requires:      gem(net-ssh) >= 2.9
Requires:      gem(net-scp) >= 1.0
Requires:      gem(net-ssh-gateway) > 1.2
Requires:      gem(inifile) >= 2.0.2
Requires:      gem(cheffish) >= 4.0
Requires:      gem(winrm) >= 2.0
Requires:      gem(winrm-fs) >= 1.0
Requires:      gem(winrm-elevated) >= 1.0
Requires:      gem(mixlib-install) >= 1.0
Conflicts:     gem(net-ssh) >= 7
Conflicts:     gem(net-scp) >= 4
Conflicts:     gem(net-ssh-gateway) >= 3.0
Conflicts:     gem(cheffish) >= 18
Conflicts:     gem(winrm) >= 3
Conflicts:     gem(winrm-fs) >= 2
Conflicts:     gem(winrm-elevated) >= 2
Obsoletes:     ruby-chef-provisioning < %EVR
Provides:      ruby-chef-provisioning = %EVR
Provides:      gem(chef-provisioning) = 2.7.7


%description
Chef Provisioning is a Cookbook and Recipe based approach for managing your
infrastructure. Users can codify their infrastructure and use Chef to converge
their infrastructure to the desired state. It has a plugin model (called
Drivers) to manage different infrastructures, including AWS, Azure and
Fog.

Chef Provisioning is maintained according to the Chef Maintenance Policy.


%package       -n gem-chef-provisioning-doc
Version:       2.7.7
Release:       alt1.3
Summary:       A library for creating machines and infrastructures idempotently in Chef documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-provisioning
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-provisioning) = 2.7.7

%description   -n gem-chef-provisioning-doc
A library for creating machines and infrastructures idempotently in Chef
documentation files.

Chef Provisioning is a Cookbook and Recipe based approach for managing your
infrastructure. Users can codify their infrastructure and use Chef to converge
their infrastructure to the desired state. It has a plugin model (called
Drivers) to manage different infrastructures, including AWS, Azure and
Fog.

Chef Provisioning is maintained according to the Chef Maintenance Policy.

%description   -n gem-chef-provisioning-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-provisioning.


%package       -n gem-chef-provisioning-devel
Version:       2.7.7
Release:       alt1.3
Summary:       A library for creating machines and infrastructures idempotently in Chef development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-provisioning
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-provisioning) = 2.7.7
Requires:      gem(ohai) >= 0
Requires:      gem(chef) >= 0
Requires:      gem(chefstyle) >= 0.10.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(simplecov) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry-stack_explorer) >= 0
Conflicts:     gem(chefstyle) >= 3
Conflicts:     gem(rspec) >= 4

%description   -n gem-chef-provisioning-devel
A library for creating machines and infrastructures idempotently in Chef
development package.

Chef Provisioning is a Cookbook and Recipe based approach for managing your
infrastructure. Users can codify their infrastructure and use Chef to converge
their infrastructure to the desired state. It has a plugin model (called
Drivers) to manage different infrastructures, including AWS, Azure and
Fog.

Chef Provisioning is maintained according to the Chef Maintenance Policy.

%description   -n gem-chef-provisioning-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-provisioning.


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

%files         -n gem-chef-provisioning-doc
%ruby_gemdocdir

%files         -n gem-chef-provisioning-devel


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 2.7.7-alt1.3
- ! of closing build deps under check condition

* Mon Jul 13 2020 Pavel Skrylev <majioa@altlinux.org> 2.7.7-alt1.2
- ! spec syntax and deps

* Fri Jul 10 2020 Pavel Skrylev <majioa@altlinux.org> 2.7.7-alt1.1
- ! spec deps and syntax

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.7.7-alt1
- updated (^) 2.7.6 -> 2.7.7
- fixed (!) spec

* Tue Sep 17 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.6-alt1.1
- fixed (!) spec
- fixed (!) gem dependency

* Tue Feb 19 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.6-alt1
- updated (^) 2.7.1 -> 2.7.6
- used (>) Ruby Policy 2.0

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.1-alt1
- Initial build for Sisyphus
