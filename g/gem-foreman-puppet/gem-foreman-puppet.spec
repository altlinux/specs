%define        gemname foreman_puppet

Name:          gem-foreman-puppet
Version:       4.0.3
Release:       alt1.1
Summary:       Add Puppet features to Foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_puppet
Vcs:           https://github.com/theforeman/foreman_puppet.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       public.tar
Patch:         lost_method.patch
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names foreman_puppet,foreman-puppet
Provides:      gem(foreman_puppet) = 4.0.3


%description
Allow assigning Puppet environments and classes to the Foreman Hosts.


%package       -n gem-foreman-puppet-doc
Version:       4.0.3
Release:       alt1.1
Summary:       Add Puppet features to Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_puppet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_puppet) = 4.0.3

%description   -n gem-foreman-puppet-doc
Add Puppet features to Foreman documentation files.

Allow assigning Puppet environments and classes to the Foreman Hosts.

%description   -n gem-foreman-puppet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_puppet.


%package       -n gem-foreman-puppet-devel
Version:       4.0.3
Release:       alt1.1
Summary:       Add Puppet features to Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_puppet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_puppet) = 4.0.3

%description   -n gem-foreman-puppet-devel
Add Puppet features to Foreman development package.

Allow assigning Puppet environments and classes to the Foreman Hosts.

%description   -n gem-foreman-puppet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_puppet.


%prep
%setup
%setup -a 1

%build
%ruby_build

%install
%ruby_install
install -d %buildroot%_datadir/foreman
cp -rp public %buildroot%_datadir/foreman

%check
%ruby_test

%files
%doc README.md webpack/__mocks__/foremanReact/readme.md
%ruby_gemspec
%ruby_gemlibdir
%_datadir/foreman/public

%files         -n gem-foreman-puppet-doc
%doc README.md webpack/__mocks__/foremanReact/readme.md
%ruby_gemdocdir

%files         -n gem-foreman-puppet-devel
%doc README.md webpack/__mocks__/foremanReact/readme.md


%changelog
* Fri Nov 11 2022 Pavel Skrylev <majioa@altlinux.org> 4.0.3-alt1.1
- ! fixed www data paths to store

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 4.0.3-alt1
- ^ 2.0.0 -> 4.0.3

* Sat Nov 20 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
