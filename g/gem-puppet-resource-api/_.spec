# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname puppet-resource-api
%define        gemname puppet-resource_api

Name:          gem-%pkgname
Version:       1.8.13
Release:       alt1
Summary:       This library provides a simple way to write new native resources for puppet
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/puppet-resource_api
Vcs:           https://github.com/puppetlabs/puppet-resource_api.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
This is an implementation of the Resource API specification.

Find a working example of a new-style providers in the Palo Alto Firewall
module:

* Type
* Base provider
* Actual provider with validation and xml processing
* New unit tests for 100% coverage.


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
%ruby_build --ignore=test_module

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


%changelog
* Wed May 6 2020 Pavel Skrylev <majioa@altlinux.org> 1.8.13-alt1
- + packaged gem with usage Ruby Policy 2.0
