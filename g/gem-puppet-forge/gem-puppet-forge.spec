%define        gemname puppet_forge

Name:          gem-puppet-forge
Version:       3.0.0
Release:       alt1
Summary:       Ruby client for the Puppet Forge API
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/forge-ruby
Vcs:           https://github.com/puppetlabs/forge-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(faraday) >= 1.3 gem(faraday) < 2
BuildRequires: gem(faraday_middleware) >= 1.0 gem(faraday_middleware) < 2
BuildRequires: gem(semantic_puppet) >= 1.0 gem(semantic_puppet) < 2
BuildRequires: gem(minitar) >= 0
BuildRequires: gem(gettext-setup) >= 0.11 gem(gettext-setup) <= 2
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(simplecov) >= 0 gem(simplecov) < 1
BuildRequires: gem(cane) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(pry-byebug) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency gettext-setup ~> 1.0
%ruby_alias_names puppet_forge,puppet-forge
Requires:      gem(faraday) >= 1.3 gem(faraday) < 2
Requires:      gem(faraday_middleware) >= 1.0 gem(faraday_middleware) < 2
Requires:      gem(semantic_puppet) >= 1.0 gem(semantic_puppet) < 2
Requires:      gem(minitar) >= 0
Requires:      gem(gettext-setup) >= 0.11 gem(gettext-setup) <= 2
Provides:      gem(puppet_forge) = 3.0.0


%description
Access and manipulate the Puppet Forge API from Ruby.

Tools that can be used to access Forge API information on Modules, Users, and
Releases. As well as download, unpack, and install Releases to a directory.


%package       -n gem-puppet-forge-doc
Version:       3.0.0
Release:       alt1
Summary:       Ruby client for the Puppet Forge API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puppet_forge
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(puppet_forge) = 3.0.0

%description   -n gem-puppet-forge-doc
Ruby client for the Puppet Forge API documentation files.

Access and manipulate the Puppet Forge API from Ruby.

Tools that can be used to access Forge API information on Modules, Users, and
Releases. As well as download, unpack, and install Releases to a directory.

%description   -n gem-puppet-forge-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puppet_forge.


%package       -n gem-puppet-forge-devel
Version:       3.0.0
Release:       alt1
Summary:       Ruby client for the Puppet Forge API development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puppet_forge
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puppet_forge) = 3.0.0
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(simplecov) >= 0 gem(simplecov) < 1
Requires:      gem(cane) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(gettext-setup) >= 1.0 gem(gettext-setup) < 2

%description   -n gem-puppet-forge-devel
Ruby client for the Puppet Forge API development package.

Access and manipulate the Puppet Forge API from Ruby.

Tools that can be used to access Forge API information on Modules, Users, and
Releases. As well as download, unpack, and install Releases to a directory.

%description   -n gem-puppet-forge-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета puppet_forge.


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

%files         -n gem-puppet-forge-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-puppet-forge-devel
%doc README.md


%changelog
* Fri Jul 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 2.3.4 -> 3.0.0

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 2.3.4-alt1
- ^ 2.2.9 -> 2.3.4

* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.9-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
