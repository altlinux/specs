%define        gemname foreman_puppet

Name:          gem-foreman-puppet
Version:       2.0.0
Release:       alt1
Summary:       Add Puppet features to Foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_puppet
Vcs:           https://github.com/theforeman/foreman_puppet.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         lost_method.patch
BuildRequires(pre): rpm-build-ruby
%ruby_alias_names foreman_puppet,foreman-puppet
%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(foreman_puppet) = 2.0.0


%description
Allow assigning Puppet environments and classes to the Foreman Hosts.


%package       -n gem-foreman-puppet-doc
Version:       2.0.0
Release:       alt1
Summary:       Add Puppet features to Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_puppet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_puppet) = 2.0.0

%description   -n gem-foreman-puppet-doc
Add Puppet features to Foreman documentation files.

Allow assigning Puppet environments and classes to the Foreman Hosts.

%description   -n gem-foreman-puppet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_puppet.


%prep
%setup
%patch

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

%files         -n gem-foreman-puppet-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Sat Nov 20 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
