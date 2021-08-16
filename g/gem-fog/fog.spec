%define        gemname fog

Name:          gem-fog
Version:       2.2.0
Release:       alt2.1
Summary:       The Ruby cloud services library
License:       MIT
Group:         Development/Other
Url:           http://fog.io
Vcs:           https://github.com/fog/fog.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         2.2.0.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(fog-core) >= 2.1 gem(fog-core) < 3
BuildRequires: gem(fog-json) >= 0
BuildRequires: gem(fog-xml) >= 0.1.1 gem(fog-xml) < 0.2
BuildRequires: gem(json) >= 2.0 gem(json) < 3
BuildRequires: gem(ipaddress) >= 0.5 gem(ipaddress) < 1
BuildRequires: gem(fog-aliyun) >= 0.1.0
BuildRequires: gem(fog-atmos) >= 0
BuildRequires: gem(fog-aws) >= 0.6.0
BuildRequires: gem(fog-brightbox) >= 0.4 gem(fog-brightbox) <= 2
BuildRequires: gem(fog-cloudatcost) >= 0.4 gem(fog-cloudatcost) < 1
BuildRequires: gem(fog-cloudstack) >= 0.1.0 gem(fog-cloudstack) < 0.2
BuildRequires: gem(fog-digitalocean) >= 0.3.0
BuildRequires: gem(fog-dnsimple) >= 2.1 gem(fog-dnsimple) < 3
BuildRequires: gem(fog-dynect) >= 0.0.2 gem(fog-dynect) < 1
BuildRequires: gem(fog-ecloud) >= 0.1 gem(fog-ecloud) < 1
BuildRequires: gem(fog-google) >= 1.0 gem(fog-google) < 2
BuildRequires: gem(fog-internet-archive) >= 0
BuildRequires: gem(fog-local) >= 0
BuildRequires: gem(fog-openstack) >= 0
BuildRequires: gem(fog-ovirt) >= 0
BuildRequires: gem(fog-powerdns) >= 0.1.1
BuildRequires: gem(fog-profitbricks) >= 0
BuildRequires: gem(fog-rackspace) >= 0
BuildRequires: gem(fog-radosgw) >= 0.0.2
BuildRequires: gem(fog-riakcs) >= 0
BuildRequires: gem(fog-sakuracloud) >= 0.0.4
BuildRequires: gem(fog-serverlove) >= 0
BuildRequires: gem(fog-softlayer) >= 0
BuildRequires: gem(fog-storm_on_demand) >= 0
BuildRequires: gem(fog-terremark) >= 0
BuildRequires: gem(fog-vmfusion) >= 0
BuildRequires: gem(fog-voxel) >= 0
BuildRequires: gem(fog-vsphere) >= 0.4.0
BuildRequires: gem(fog-xenserver) >= 0
BuildRequires: gem(docker-api) >= 1.13.6
BuildRequires: gem(fission) >= 0
BuildRequires: gem(mime-types) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-stub-const) >= 0
# BuildRequires: gem(opennebula) >= 5.10.5
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rbvmomi) >= 0
BuildRequires: gem(rubocop) >= 0.52.1 gem(rubocop) < 2
BuildRequires: gem(shindo) >= 0.3.4 gem(shindo) < 0.4
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(thor) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(rspec-core) >= 0
BuildRequires: gem(rspec-expectations) >= 0
BuildRequires: gem(vcr) >= 0
BuildRequires: gem(webmock) >= 1.22.2 gem(webmock) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency fog-dynect >= 0.5.0,fog-dynect < 1
%ruby_use_gem_dependency fog-brightbox >= 1.0,fog-brightbox < 2
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(fog-core) >= 2.1 gem(fog-core) < 3
Requires:      gem(fog-json) >= 0
Requires:      gem(fog-xml) >= 0.1.1 gem(fog-xml) < 0.2
Requires:      gem(json) >= 2.0 gem(json) < 3
Requires:      gem(ipaddress) >= 0.5 gem(ipaddress) < 1
Requires:      gem(fog-aliyun) >= 0.1.0
Requires:      gem(fog-atmos) >= 0
Requires:      gem(fog-aws) >= 0.6.0 gem(fog-aws) < 4
Requires:      gem(fog-brightbox) >= 0.4 gem(fog-brightbox) <= 2
Requires:      gem(fog-cloudatcost) >= 0.4 gem(fog-cloudatcost) < 1
Requires:      gem(fog-cloudstack) >= 0.1.0 gem(fog-cloudstack) < 0.2
Requires:      gem(fog-digitalocean) >= 0.3.0
Requires:      gem(fog-dnsimple) >= 2.1 gem(fog-dnsimple) < 3
Requires:      gem(fog-dynect) >= 0.0.2 gem(fog-dynect) < 1
Requires:      gem(fog-ecloud) >= 0.1 gem(fog-ecloud) < 1
Requires:      gem(fog-google) >= 1.0 gem(fog-google) < 2
Requires:      gem(fog-internet-archive) >= 0
Requires:      gem(fog-local) >= 0
Requires:      gem(fog-openstack) >= 0
Requires:      gem(fog-ovirt) >= 0
Requires:      gem(fog-powerdns) >= 0.1.1
Requires:      gem(fog-profitbricks) >= 0
Requires:      gem(fog-rackspace) >= 0
Requires:      gem(fog-radosgw) >= 0.0.2
Requires:      gem(fog-riakcs) >= 0
Requires:      gem(fog-sakuracloud) >= 0.0.4
Requires:      gem(fog-serverlove) >= 0
Requires:      gem(fog-softlayer) >= 0
Requires:      gem(fog-storm_on_demand) >= 0
Requires:      gem(fog-terremark) >= 0
Requires:      gem(fog-vmfusion) >= 0
Requires:      gem(fog-voxel) >= 0
Requires:      gem(fog-vsphere) >= 0.4.0
Requires:      gem(fog-xenserver) >= 0
Provides:      gem(fog) = 2.2.0


%description
fog is the Ruby cloud services library, top to bottom:

- Collections provide a simplified interface, making clouds easier to work with
and switch between.
- Requests allow power users to get the most out of the features of each
individual cloud.
- Mocks make testing and integrating a breeze.


%package       -n fog
Version:       2.2.0
Release:       alt2.1
Summary:       The Ruby cloud services library executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета fog
Group:         Development/Other
BuildArch:     noarch

Requires:      gem(fog) = 2.2.0

%description   -n fog
The Ruby cloud services library executable(s).

fog is the Ruby cloud services library, top to bottom:

- Collections provide a simplified interface, making clouds easier to work with
and switch between.
- Requests allow power users to get the most out of the features of each
individual cloud.
- Mocks make testing and integrating a breeze.

%description   -n fog -l ru_RU.UTF-8
Исполнямка для самоцвета fog.


%package       -n gem-fog-doc
Version:       2.2.0
Release:       alt2.1
Summary:       The Ruby cloud services library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog) = 2.2.0
Obsoletes:     fog-doc
Provides:      fog-doc

%description   -n gem-fog-doc
The Ruby cloud services library documentation files.

fog is the Ruby cloud services library, top to bottom:

- Collections provide a simplified interface, making clouds easier to work with
and switch between.
- Requests allow power users to get the most out of the features of each
individual cloud.
- Mocks make testing and integrating a breeze.

%description   -n gem-fog-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog.


%package       -n gem-fog-devel
Version:       2.2.0
Release:       alt2.1
Summary:       The Ruby cloud services library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog) = 2.2.0
Requires:      gem(docker-api) >= 1.13.6
Requires:      gem(fission) >= 0
Requires:      gem(mime-types) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-stub-const) >= 0
Requires:      gem(opennebula) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rbvmomi) >= 0
Requires:      gem(rubocop) >= 0.52.1 gem(rubocop) < 2
Requires:      gem(shindo) >= 0.3.4 gem(shindo) < 0.4
Requires:      gem(simplecov) >= 0
Requires:      gem(thor) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(rspec-core) >= 0
Requires:      gem(rspec-expectations) >= 0
Requires:      gem(vcr) >= 0
Requires:      gem(webmock) >= 1.22.2 gem(webmock) < 4
Requires:      gem(fog-brightbox) >= 1.0 gem(fog-brightbox) < 2

%description   -n gem-fog-devel
The Ruby cloud services library development package.

fog is the Ruby cloud services library, top to bottom:

- Collections provide a simplified interface, making clouds easier to work with
and switch between.
- Requests allow power users to get the most out of the features of each
individual cloud.
- Mocks make testing and integrating a breeze.

%description   -n gem-fog-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog.


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

%files         -n fog
%doc README.md
%_bindir/fog

%files         -n gem-fog-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-devel
%doc README.md


%changelog
* Fri Jul 23 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt2.1
- ! spec

* Wed Jun 17 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt2
- ! require lib when runnung the executable (closes #38607)
- ! spec tags and syntax

* Mon Jun 24 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- > Ruby Policy 2.0
- ^ 2.1.0 -> 2.2.0

* Tue Nov 13 2018 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- Bump to 2.1.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 23 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
