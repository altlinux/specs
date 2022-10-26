%define        gemname foreman_setup

Name:          gem-foreman-setup
Version:       8.0.1
Release:       alt1
Summary:       Helps set up Foreman for provisioning
License:       GPL-3
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_setup
Vcs:           https://github.com/theforeman/foreman_setup.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names foreman_setup,foreman-setup
Provides:      gem(foreman_setup) = 8.0.1


%description
Plugin for Foreman that helps set up provisioning.


%package       -n gem-foreman-setup-doc
Version:       8.0.1
Release:       alt1
Summary:       Helps set up Foreman for provisioning documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_setup
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_setup) = 8.0.1

%description   -n gem-foreman-setup-doc
Helps set up Foreman for provisioning documentation files.

Plugin for Foreman that helps set up provisioning.

%description   -n gem-foreman-setup-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_setup.


%package       -n gem-foreman-setup-devel
Version:       8.0.1
Release:       alt1
Summary:       Helps set up Foreman for provisioning development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_setup
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_setup) = 8.0.1

%description   -n gem-foreman-setup-devel
Helps set up Foreman for provisioning development package.

Plugin for Foreman that helps set up provisioning.

%description   -n gem-foreman-setup-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_setup.


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

%files         -n gem-foreman-setup-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-foreman-setup-devel
%doc README.md


%changelog
* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 8.0.1-alt1
- ^ 7.0.0 -> 8.0.1

* Sun Nov 21 2021 Pavel Skrylev <majioa@altlinux.org> 7.0.0-alt1
- + packaged gem with Ruby Policy 2.0
