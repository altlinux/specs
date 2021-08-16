%define        gemname chef-telemetry

Name:          gem-chef-telemetry
Version:       1.0.33
Release:       alt1
Summary:       Send user actions to the Chef telemetry system
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/chef-telemetry
Vcs:           https://github.com/chef/chef-telemetry.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
BuildRequires: gem(chef-config) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
Requires:      gem(chef-config) >= 0
Provides:      gem(chef-telemetry) = 1.0.33

%description
Chef InSpec is an open-source testing framework for infrastructure with a
human- and machine-readable language for specifying compliance, security and
policy requirements. See Chef RFC-051 for further information.


%package       -n gem-chef-telemetry-doc
Version:       1.0.33
Release:       alt1
Summary:       Send user actions to the Chef telemetry system documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-telemetry
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-telemetry) = 1.0.33

%description   -n gem-chef-telemetry-doc
Send user actions to the Chef telemetry system documentation files.

Chef InSpec is an open-source testing framework for infrastructure with a
human- and machine-readable language for specifying compliance, security and
policy requirements. See Chef RFC-051 for further information.

%description   -n gem-chef-telemetry-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-telemetry.


%package       -n gem-chef-telemetry-devel
Version:       1.0.33
Release:       alt1
Summary:       Send user actions to the Chef telemetry system development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-telemetry
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-telemetry) = 1.0.33
Requires:      gem(bundler) >= 0 gem(bundler) < 3

%description   -n gem-chef-telemetry-devel
Send user actions to the Chef telemetry system development package.

Chef InSpec is an open-source testing framework for infrastructure with a
human- and machine-readable language for specifying compliance, security and
policy requirements. See Chef RFC-051 for further information.

%description   -n gem-chef-telemetry-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-telemetry.


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

%files         -n gem-chef-telemetry-doc
%ruby_gemdocdir

%files         -n gem-chef-telemetry-devel


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.33-alt1
- + packaged gem with Ruby Policy 2.0
