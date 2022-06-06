%define        gemname puppet-resource_api

Name:          gem-puppet-resource-api
Version:       1.8.14
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
BuildRequires: gem(hocon) >= 1.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names puppet-resource_api,puppet-resource-api
Requires:      gem(hocon) >= 1.0
Provides:      gem(puppet-resource_api) = 1.8.14


%description
This is an implementation of the Resource API specification.

Find a working example of a new-style providers in the Palo Alto Firewall
module:

* Type
* Base provider
* Actual provider with validation and xml processing
* New unit tests for 100% coverage.


%package       -n gem-puppet-resource-api-doc
Version:       1.8.14
Release:       alt1
Summary:       This library provides a simple way to write new native resources for puppet documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puppet-resource_api
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(puppet-resource_api) = 1.8.14

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
Version:       1.8.14
Release:       alt1
Summary:       This library provides a simple way to write new native resources for puppet development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puppet-resource_api
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puppet-resource_api) = 1.8.14

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
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 1.8.14-alt1
- ^ 1.8.13 -> 1.8.14

* Wed May 6 2020 Pavel Skrylev <majioa@altlinux.org> 1.8.13-alt1
- + packaged gem with usage Ruby Policy 2.0
