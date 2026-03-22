%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname puppet-resource_api

Name:          gem-puppet-resource-api
Version:       2.0.0
Release:       alt1
Summary:       This library provides a simple way to write new native resources for puppet
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/puppet-resource_api
Vcs:           https://github.com/puppetlabs/puppet-resource_api.git
Packager:      Baltix Maintainers Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(ffi) >= 1.15.5
BuildRequires: gem(github_changelog_generator) >= 1.15
BuildRequires: gem(hocon) >= 1.0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(puppet) >= 0
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(github_changelog_generator) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency ffi >= 1.17.0,ffi < 2
%ruby_alias_names puppet-resource_api,puppet-resource-api
Requires:      gem(hocon) >= 1.0
Provides:      gem(puppet-resource_api) = 2.0.0

%description
This is an implementation of the Resource API specification.

Find a working example of a new-style providers in the Palo Alto Firewall
module:

* Type
* Base provider
* Actual provider with validation and xml processing
* New unit tests for 100% coverage.


%if_enabled    doc
%package       -n gem-puppet-resource-api-doc
Version:       2.0.0
Release:       alt1
Summary:       This library provides a simple way to write new native resources for puppet documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puppet-resource_api
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(puppet-resource_api) = 2.0.0

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
%endif


%if_enabled    devel
%package       -n gem-puppet-resource-api-devel
Version:       2.0.0
Release:       alt1
Summary:       This library provides a simple way to write new native resources for puppet development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puppet-resource_api
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(puppet-resource_api) = 2.0.0
Requires:      gem(ffi) >= 1.15.5
Requires:      gem(github_changelog_generator) >= 1.15
Requires:      gem(hocon) >= 1.0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(puppet) >= 0
Conflicts:     gem(ffi) >= 2
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
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md HISTORY.md contrib
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-puppet-resource-api-doc
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md HISTORY.md contrib
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-puppet-resource-api-devel
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md HISTORY.md contrib
%endif


%changelog
* Sun Mar 22 2026 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- ^ 1.9.0 -> 2.0.0

* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 1.9.0-alt1
- ^ 1.8.14 -> 1.9.0

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 1.8.14-alt1
- ^ 1.8.13 -> 1.8.14

* Wed May 6 2020 Pavel Skrylev <majioa@altlinux.org> 1.8.13-alt1
- + packaged gem with usage Ruby Policy 2.0
