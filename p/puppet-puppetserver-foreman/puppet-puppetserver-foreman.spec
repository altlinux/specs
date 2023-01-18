# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname puppetserver-foreman

Name:          puppet-%pkgname
Version:       2.2.0
Release:       alt1
Summary:       Puppet module for managing Foreman integration in Puppetserver
License:       GPLv3
Group:         Development/Ruby
Url:           https://github.com/theforeman/puppet-foreman
Vcs:           https://github.com/theforeman/puppet-foreman.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         exceptions.patch
BuildRequires(pre): rpm-build-ruby

Requires:      puppet
Requires:      puppetserver

%description
Puppet module for managing Foreman integration in Puppetserver.

The Foreman integration consists of an ENC and a report processor. This has a
configuration file. All of this can be managed by this module.

Historically this integration was part of theforeman-foreman module.


%prep
%setup
%autopatch -p1

%build
%ruby_build --use=%name --srclibdirs=

%install
%ruby_install
chmod a+x %buildroot%_libexecdir/%name/files/*.rb
mkdir -p %buildroot%_libexecdir/puppet-modules/
mv %buildroot%_libexecdir/%name %buildroot%_libexecdir/puppet-modules/%pkgname

%check
%ruby_test

%files
%doc README*
%_libexecdir/puppet-modules/%pkgname


%changelog
* Wed Jan 18 2023 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- ^ 2.0.0 -> 2.2.0
- ! exceptions for timeout

* Mon Jan 31 2022 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged puppet module with usage Ruby Policy 2.0
