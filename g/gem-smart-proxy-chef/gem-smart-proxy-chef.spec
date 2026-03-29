# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname smart_proxy_chef

Name:          gem-smart-proxy-chef
Version:       0.2.0
Release:       alt1.2
Summary:       Chef support for Foreman Smart-Proxy
License:       GPLv3
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_chef
Vcs:           https://github.com/theforeman/smart_proxy_chef.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.7
BuildRequires: gem(chef-api) >= 0
BuildRequires: gem(mocha) >= 1
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rake) >= 10
BuildRequires: gem(smart_proxy) >= 0
BuildRequires: gem(test-unit) >= 2
BuildRequires: gem(webmock) >= 1
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(rack-test) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(webmock) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 2.7.1,mocha < 3
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
%ruby_use_gem_dependency rack-test >= 2.0.0,rack-test < 3
%ruby_alias_names smart_proxy_chef,smart-proxy-chef
Requires:      gem(chef-api) >= 0
Provides:      smart_proxy_chef = %EVR
Provides:      gem(smart_proxy_chef) = 0.2.0

%description
Chef support for Foreman Smart-Proxy.


%if_enabled    doc
%package       -n gem-smart-proxy-chef-doc
Version:       0.2.0
Release:       alt1.2
Summary:       Chef support for Foreman Smart-Proxy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета smart_proxy_chef
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(smart_proxy_chef) = 0.2.0

%description   -n gem-smart-proxy-chef-doc
Chef support for Foreman Smart-Proxy documentation files.

%description   -n gem-smart-proxy-chef-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета smart_proxy_chef.
%endif


%if_enabled    devel
%package       -n gem-smart-proxy-chef-devel
Version:       0.2.0
Release:       alt1.2
Summary:       Chef support for Foreman Smart-Proxy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета smart_proxy_chef
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(smart_proxy_chef) = 0.2.0
Requires:      gem(bundler) >= 1.7
Requires:      gem(mocha) >= 1
Requires:      gem(rack-test) >= 0
Requires:      gem(rake) >= 10
Requires:      gem(smart_proxy) >= 0
Requires:      gem(test-unit) >= 2
Requires:      gem(webmock) >= 1
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(rack-test) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(test-unit) >= 4
Conflicts:     gem(webmock) >= 4

%description   -n gem-smart-proxy-chef-devel
Chef support for Foreman Smart-Proxy development package.

%description   -n gem-smart-proxy-chef-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета smart_proxy_chef.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-smart-proxy-chef-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-smart-proxy-chef-devel
%doc LICENSE README.md
%endif


%changelog
* Sun Mar 29 2026 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1.2
- * rebased to upstream
- ! rewrote spec with explicit deps

* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1.1
- ! closes build deps under check condition

* Thu Feb 11 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with usage Ruby Policy 2.0
