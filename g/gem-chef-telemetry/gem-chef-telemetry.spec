%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname chef-telemetry

Name:          gem-chef-telemetry
Version:       1.1.9
Release:       alt1
Summary:       Send user actions to the Chef telemetry system
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/chef-telemetry
Vcs:           https://github.com/chef/chef-telemetry.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(chef-config) >= 0
BuildRequires: gem(chefstyle) >= 2.2.0
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildConflicts: gem(chefstyle) >= 3
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency chefstyle >= 2.2.2,chefstyle < 3
Requires:      ruby >= 2.7
Requires:      gem(chef-config) >= 0
Requires:      gem(concurrent-ruby) >= 1.0
Conflicts:     gem(concurrent-ruby) >= 2
Provides:      gem(chef-telemetry) = 1.1.9

%description
Chef InSpec is an open-source testing framework for infrastructure with a human-
and machine-readable language for specifying compliance, security and policy
requirements. See Chef RFC-051 for further information.


%if_enabled    doc
%package       -n gem-chef-telemetry-doc
Version:       1.1.9
Release:       alt1
Summary:       Send user actions to the Chef telemetry system documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-telemetry
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-telemetry) = 1.1.9

%description   -n gem-chef-telemetry-doc
Send user actions to the Chef telemetry system documentation files.

Chef InSpec is an open-source testing framework for infrastructure with a human-
and machine-readable language for specifying compliance, security and policy
requirements. See Chef RFC-051 for further information.

%description   -n gem-chef-telemetry-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-telemetry.
%endif


%if_enabled    devel
%package       -n gem-chef-telemetry-devel
Version:       1.1.9
Release:       alt1
Summary:       Send user actions to the Chef telemetry system development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-telemetry
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-telemetry) = 1.1.9
Requires:      gem(chefstyle) >= 2.2.0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(chefstyle) >= 3
Conflicts:     gem(rspec) >= 4

%description   -n gem-chef-telemetry-devel
Send user actions to the Chef telemetry system development package.

Chef InSpec is an open-source testing framework for infrastructure with a human-
and machine-readable language for specifying compliance, security and policy
requirements. See Chef RFC-051 for further information.

%description   -n gem-chef-telemetry-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-telemetry.
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
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-chef-telemetry-doc
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-chef-telemetry-devel
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%endif


%changelog
* Wed Nov 05 2025 Pavel Skrylev <majioa@altlinux.org> 1.1.9-alt1
- ^ 1.0.33 -> 1.1.9

* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.33-alt1
- + packaged gem with Ruby Policy 2.0
