# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname chef-api

Name:          gem-%pkgname
Version:       0.10.10
Release:       alt1
Summary:       A tiny Chef API client with minimal dependencies
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef-boneyard/chef-api
Vcs:           https://github.com/chef-boneyard/chef-api.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.


%package       -n gem-chef-infra-api
Summary:       A tiny Chef Infra API
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-chef-infra-api
A tiny Chef Infra API gem.


%package       -n gem-chef-infra-api-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-chef-infra-api-doc
Documentation files for %gemname gem.

%description   -n gem-chef-infra-api-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%files         -n gem-chef-infra-api
%doc README*
%ruby_gemspecdir/chef-infra-api-%version.gemspec
%ruby_gemslibdir/chef-infra-api-%version

%files         -n gem-chef-infra-api-doc
%ruby_gemsdocdir/chef-infra-api-%version


%changelog
* Thu Feb 11 2021 Pavel Skrylev <majioa@altlinux.org> 0.10.10-alt1
- + packaged gem with usage Ruby Policy 2.0
