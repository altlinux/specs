# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_disable   devel
%define        puppetname theforeman-puppetserver_foreman

Name:          puppet-theforeman-puppetserver-foreman
Version:       4.3.0
Release:       alt2
Summary:       Puppet module for managing Foreman integration in Puppetserver
License:       GPLv3
Group:         Development/Ruby
Url:           https://github.com/theforeman/puppet-puppetserver_foreman
Vcs:           git@github.com:theforeman/puppet-puppetserver_foreman.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(github_changelog_generator) >= 1.15.0
BuildRequires: gem(kafo_module_lint) >= 0
BuildRequires: gem(oauth) >= 0
BuildRequires: gem(openvox) >= 8
BuildRequires: gem(puppet-lint-spaceship_operator_without_tag-check) >= 2.0
BuildRequires: gem(puppet_metadata) >= 6.3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(voxpupuli-test) >= 14.0
BuildRequires: gem(webmock) >= 2.0
BuildConflicts: gem(puppet-blacksmith) >= 10
BuildConflicts: gem(puppet-lint-spaceship_operator_without_tag-check) >= 3
BuildConflicts: gem(puppet_metadata) >= 7
BuildConflicts: gem(voxpupuli-test) >= 15
BuildConflicts: gem(webmock) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
Requires:      puppet
Requires:      puppetserver
Obsoletes:     puppet-puppetserver-foreman < %EVR
Provides:      puppet-puppetserver-foreman = %EVR

%description
Puppet module for managing Foreman integration in Puppetserver.

The Foreman integration consists of an ENC and a report processor. This has a
configuration file. All of this can be managed by this module.

Historically this integration was part of theforeman-foreman module.


%if_enabled    devel
%package       -n puppet-theforeman-puppetserver-foreman-devel
Version:       4.3.0
Release:       alt2
Summary:       Puppet module for managing Foreman integration in Puppetserver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      puppet-theforeman-puppetserver-foreman = 4.3.0-alt2
Requires:      gem(github_changelog_generator) >= 1.15.0
Requires:      gem(kafo_module_lint) >= 0
Requires:      gem(oauth) >= 0
Requires:      gem(openvox) >= 8
Requires:      gem(puppet-blacksmith) >= 9.1
Requires:      gem(puppet-lint-spaceship_operator_without_tag-check) >= 2.0
Requires:      gem(puppet_metadata) >= 6.3
Requires:      gem(rake) >= 0
Requires:      gem(voxpupuli-test) >= 14.0
Requires:      gem(webmock) >= 2.0
Conflicts:     gem(puppet-blacksmith) >= 10
Conflicts:     gem(puppet-lint-spaceship_operator_without_tag-check) >= 3
Conflicts:     gem(puppet_metadata) >= 7
Conflicts:     gem(voxpupuli-test) >= 15
Conflicts:     gem(webmock) >= 3

%description   -n puppet-theforeman-puppetserver-foreman-devel
Puppet module for managing Foreman integration in Puppetserver.

The Foreman integration consists of an ENC and a report processor. This has a
configuration file. All of this can be managed by this module.

Historically this integration was part of theforeman-foreman module.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install
chmod a+x %buildroot%_libexecdir/%name/files/*.rb
mkdir -p %buildroot%_libexecdir/puppet-modules/
mv %buildroot%_libexecdir/%name %buildroot%_libexecdir/puppet-modules/%puppetname

%check
%ruby_test

%files
%doc README*
%_libexecdir/puppet-modules/%puppetname

%if_enabled    devel
%files         -n puppet-theforeman-puppetserver-foreman-devel
%doc README*
%endif


%changelog
* Mon Sep 07 2026 Pavel Skrylev <majioa@altlinux.org> 4.3.0-alt2
- ^ 2.2.0 -> 4.3.0
- ! fixed of old call to File.exists (closes ALT #60384)

* Wed Jan 18 2023 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt2
- * rename package
- ! fix excessive exception matcher

* Wed Jan 18 2023 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- ^ 2.0.0 -> 2.2.0
- ! exceptions for timeout

* Mon Jan 31 2022 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged puppet module with usage Ruby Policy 2.0
