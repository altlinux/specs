%define        gemname foreman_setup

Name:          gem-foreman-setup
Version:       7.0.0
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
%ruby_alias_names foreman_setup,foreman-setup
%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(foreman_setup) = 7.0.0


%description
Plugin for Foreman that helps set up provisioning.


%package       -n gem-foreman-setup-doc
Version:       7.0.0
Release:       alt1
Summary:       Helps set up Foreman for provisioning documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_setup
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_setup) = 7.0.0

%description   -n gem-foreman-setup-doc
Helps set up Foreman for provisioning documentation files.

Plugin for Foreman that helps set up provisioning.

%description   -n gem-foreman-setup-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_setup.


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


%changelog
* Sun Nov 21 2021 Pavel Skrylev <majioa@altlinux.org> 7.0.0-alt1
- + packaged gem with Ruby Policy 2.0
