%define        _unpackaged_files_terminate_build 1
%define        gemname puppet-resource_api

Name:          gem-puppet-resource-api
Version:       1.9.0
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
%if_with check
BuildRequires: gem(CFPropertyList) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(simplecov-console) >= 0
BuildRequires: gem(puppetlabs_spec_helper) >= 3.0
BuildRequires: gem(rspec-puppet) >= 0
BuildRequires: gem(codecov) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(license_finder) >= 0
BuildRequires: gem(rubocop) >= 0.57.0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(github_changelog_generator) >= 1.15
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(ffi) >= 0
BuildRequires: gem(puppet) >= 0
BuildRequires: gem(hocon) >= 1.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(puppetlabs_spec_helper) >= 8
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(github_changelog_generator) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency puppetlabs_spec_helper >= 7.0.2,puppetlabs_spec_helper < 8
%ruby_alias_names puppet-resource_api,puppet-resource-api
Requires:      gem(hocon) >= 1.0
Provides:      gem(puppet-resource_api) = 1.9.0


%description
This is an implementation of the Resource API specification.

Find a working example of a new-style providers in the Palo Alto Firewall
module:

* Type
* Base provider
* Actual provider with validation and xml processing
* New unit tests for 100% coverage.


%package       -n gem-puppet-resource-api-doc
Version:       1.9.0
Release:       alt1
Summary:       This library provides a simple way to write new native resources for puppet documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puppet-resource_api
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(puppet-resource_api) = 1.9.0

%description   -n gem-puppet-resource-api-doc
This library provides a simple way to write new native resources for puppet
documentation files.

This is an implementation of the Resource API specification.

Find a working example of a new-style providers in the Palo Alto Firewall
module:

* Type
* Base provider
* Actual provider with validation and xml processing
* New unit tests for 100% coverage.

%description   -n gem-puppet-resource-api-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puppet-resource_api.


%package       -n gem-puppet-resource-api-devel
Version:       1.9.0
Release:       alt1
Summary:       This library provides a simple way to write new native resources for puppet development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puppet-resource_api
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puppet-resource_api) = 1.9.0
Requires:      gem(CFPropertyList) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(simplecov-console) >= 0
Requires:      gem(puppetlabs_spec_helper) >= 3.0
Requires:      gem(rspec-puppet) >= 0
Requires:      gem(codecov) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(license_finder) >= 0
Requires:      gem(rubocop) >= 0.57.0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(github_changelog_generator) >= 1.15
Requires:      gem(pry-byebug) >= 0
Requires:      gem(ffi) >= 0
Requires:      gem(puppet) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(puppetlabs_spec_helper) >= 8
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(github_changelog_generator) >= 2

%description   -n gem-puppet-resource-api-devel
This library provides a simple way to write new native resources for puppet
development package.

This is an implementation of the Resource API specification.

Find a working example of a new-style providers in the Palo Alto Firewall
module:

* Type
* Base provider
* Actual provider with validation and xml processing
* New unit tests for 100% coverage.

%description   -n gem-puppet-resource-api-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета puppet-resource_api.


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

%files         -n gem-puppet-resource-api-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-puppet-resource-api-devel
%doc README.md


%changelog
* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 1.9.0-alt1
- ^ 1.8.14 -> 1.9.0

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 1.8.14-alt1
- ^ 1.8.13 -> 1.8.14

* Wed May 6 2020 Pavel Skrylev <majioa@altlinux.org> 1.8.13-alt1
- + packaged gem with usage Ruby Policy 2.0
