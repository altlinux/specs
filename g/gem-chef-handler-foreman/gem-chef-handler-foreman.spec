%define        gemname chef_handler_foreman

Name:          gem-chef-handler-foreman
Version:       0.2.1
Release:       alt1
Summary:       This gem adds chef handlers so your chef-client can upload attributes (facts) and reports to Foreman
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/theforeman/chef-handler-foreman
Vcs:           https://github.com/theforeman/chef-handler-foreman.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(chef_handler_foreman) = 0.2.1

%ruby_alias_names chef_handler_foreman,chef-handler-foreman

%description
Chef handlers to integrate with foreman


%package       -n gem-chef-handler-foreman-doc
Version:       0.2.1
Release:       alt1
Summary:       This gem adds chef handlers so your chef-client can upload attributes (facts) and reports to Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef_handler_foreman
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef_handler_foreman) = 0.2.1

%description   -n gem-chef-handler-foreman-doc
This gem adds chef handlers so your chef-client can upload attributes (facts)
and reports to Foreman documentation files.

Chef handlers to integrate with foreman

%description   -n gem-chef-handler-foreman-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef_handler_foreman.


%package       -n gem-chef-handler-foreman-devel
Version:       0.2.1
Release:       alt1
Summary:       This gem adds chef handlers so your chef-client can upload attributes (facts) and reports to Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef_handler_foreman
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef_handler_foreman) = 0.2.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-chef-handler-foreman-devel
This gem adds chef handlers so your chef-client can upload attributes (facts)
and reports to Foreman development package.

Chef handlers to integrate with foreman

%description   -n gem-chef-handler-foreman-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef_handler_foreman.


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

%files         -n gem-chef-handler-foreman-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-chef-handler-foreman-devel
%doc README.md


%changelog
* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- + packaged gem with Ruby Policy 2.0
