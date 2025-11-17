%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname foreman_puppet

Name:          gem-foreman-puppet
Version:       9.0.0
Release:       alt1
Summary:       Add Puppet features to Foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_puppet
Vcs:           https://github.com/theforeman/foreman_puppet.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source1:       .public.tar
Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(theforeman-rubocop) >= 0.1.1
BuildConflicts: gem(theforeman-rubocop) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency theforeman-rubocop >= 0.1.2,theforeman-rubocop < 1
%ruby_alias_names foreman_puppet,foreman-puppet
Requires:      ruby >= 2.7
Conflicts:     ruby >= 4
Provides:      gem(foreman_puppet) = 9.0.0

%description
Allow assigning Puppet environments and classes to the Foreman Hosts.


%if_enabled    doc
%package       -n gem-foreman-puppet-doc
Version:       9.0.0
Release:       alt1
Summary:       Add Puppet features to Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_puppet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_puppet) = 9.0.0

%description   -n gem-foreman-puppet-doc
Add Puppet features to Foreman documentation files.

Allow assigning Puppet environments and classes to the Foreman Hosts.

%description   -n gem-foreman-puppet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_puppet.
%endif


%if_enabled    devel
%package       -n gem-foreman-puppet-devel
Version:       9.0.0
Release:       alt1
Summary:       Add Puppet features to Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_puppet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_puppet) = 9.0.0

%description   -n gem-foreman-puppet-devel
Add Puppet features to Foreman development package.

Allow assigning Puppet environments and classes to the Foreman Hosts.

%description   -n gem-foreman-puppet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_puppet.
%endif


%prep
%setup -a 1

%build
%ruby_build

%install
%ruby_install
install -d %buildroot%_datadir/foreman
cp -rp .public %buildroot%_datadir/foreman/public

%check
%ruby_test

%files
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir
%_datadir/foreman/public

%if_enabled    doc
%files         -n gem-foreman-puppet-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-foreman-puppet-devel
%doc LICENSE README.md
%endif


%changelog
* Wed Oct 22 2025 Pavel Skrylev <majioa@altlinux.org> 9.0.0-alt1
- ^ 8.0.0p4 -> 9.0.0

* Fri Oct 04 2024 Pavel Skrylev <majioa@altlinux.org> 8.0.0.4-alt0.1
- ^ 4.0.3 -> 8.0.0p4

* Thu Apr 06 2023 Pavel Skrylev <majioa@altlinux.org> 4.0.3-alt1.2
- ! public webpack

* Fri Nov 11 2022 Pavel Skrylev <majioa@altlinux.org> 4.0.3-alt1.1
- ! fixed www data paths to store

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 4.0.3-alt1
- ^ 2.0.0 -> 4.0.3

* Sat Nov 20 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
