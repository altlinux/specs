%define        gemname foreman_templates

Name:          gem-foreman-templates
Version:       9.1.0
Release:       alt1
Summary:       Template-syncing engine for Foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_templates
Vcs:           https://github.com/theforeman/foreman_templates.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(diffy) >= 0
BuildRequires: gem(git) >= 0
BuildRequires: gem(rake) >= 0 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(diffy) >= 0
Requires:      gem(git) >= 0
Provides:      gem(foreman_templates) = 9.1.0


%description
Engine to synchronise provisioning templates from GitHub


%package       -n gem-foreman-templates-doc
Version:       9.1.0
Release:       alt1
Summary:       Template-syncing engine for Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_templates
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_templates) = 9.1.0

%description   -n gem-foreman-templates-doc
Template-syncing engine for Foreman documentation files.

Engine to synchronise provisioning templates from GitHub

%description   -n gem-foreman-templates-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_templates.


%package       -n gem-foreman-templates-devel
Version:       9.1.0
Release:       alt1
Summary:       Template-syncing engine for Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_templates
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_templates) = 9.1.0
Requires:      gem(rake) >= 0 gem(rake) < 14

%description   -n gem-foreman-templates-devel
Template-syncing engine for Foreman development package.

Engine to synchronise provisioning templates from GitHub

%description   -n gem-foreman-templates-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_templates.


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

%files         -n gem-foreman-templates-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-foreman-templates-devel
%doc README.md


%changelog
* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 9.1.0-alt1
- + packaged gem with Ruby Policy 2.0
