
Name:    chef
Version: 12.6.0
Release: alt1

Summary: Clients for the chef systems integration framework
Group:   Networking/Other
License: Apache-2.0
URL:     https://www.chef.io/
# VCS:   https://github.com/opscode/chef.git

Packager:  Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

# Filter automatic requirements
%filter_from_requires /^ruby(\(win32\|windows\|wmi-lite\).*)/d;/^python2.7(yum)/d

Source:  %name-%version.tar
Source1: chef-client.init
Source2: chef-client.service
Source3: chef-client.default
Source4: chef-client.rb

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: chef-zero >= 4.2.2
BuildRequires: erubis >= 2.7
#BuildRequires: ohai >= 8.6
BuildRequires: ohai
BuildRequires: ruby-activesupport
BuildRequires: ruby-diff-lcs >= 1.2.4
BuildRequires: ruby-highline >= 1.6.9
BuildRequires: ruby-mixlib-cli >= 1.4
BuildRequires: ruby-mixlib-log >= 1.3
BuildRequires: ruby-mixlib-authentication >= 1.3
BuildRequires: ruby-mixlib-shellout >= 2.0.0
BuildRequires: ruby-net-ssh >= 2.6
BuildRequires: ruby-net-ssh-multi >= 1.1
BuildRequires: ruby-plist >= 3.1.0
BuildRequires: ruby-proxifier >= 1.0
BuildRequires: ruby-rack
BuildRequires: ruby-rest-client
BuildRequires: ruby-rspec-core ruby-rspec-expectations ruby-rspec-mocks
BuildRequires: ruby-syslog-logger >= 1.6.0
BuildRequires: ruby-ucf
BuildRequires: ruby-ffi-yajl >= 2.2

Requires: chef-config
Requires: ruby-highline

%description
Chef is a systems integration framework and configuration management
library written in Ruby. Chef provides a Ruby library and API that can
be used to bring the benefits of configuration management to an entire
infrastructure.

Chef can be run as a client (chef-client) to a server, or run as a
standalone tool (chef-solo). Configuration recipes are written in a pure
Ruby DSL.

This package contains the chef-client, chef-solo and knife binaries as
well as the chef library.

%package config
Summary:   Chef's default configuration and config loading
Group:     Development/Ruby
BuildArch: noarch

%description config
Chef's default configuration and config loading.

%package doc
Summary:   Documentation for %name
Group:     Development/Documentation
Requires:  %name = %version-%release
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup
%update_setup_rb
pushd chef-config
%update_setup_rb
popd

%build
%ruby_config
%ruby_build
pushd chef-config
%ruby_config
%ruby_build
popd

%install
%ruby_install
%rdoc lib/
pushd chef-config
%ruby_install
%rdoc lib/
popd

# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

# Install init scripts
install -Dm 0755 %SOURCE1 %buildroot%_initdir/chef-client
install -Dm 0644 %SOURCE2 %buildroot%_unitdir/chef-client.service
install -Dm 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/chef-client
install -Dm 0640 %SOURCE4 %buildroot%_sysconfdir/chef/client.rb

mkdir -p %buildroot%_var/log/chef
mkdir -p %buildroot%_var/lib/chef
mkdir -p %buildroot%_var/cache/chef
mkdir -p %buildroot/run/chef
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot%_man8dir
cp distro/common/man/man1/*.1 %buildroot%_man1dir/
cp distro/common/man/man8/*.8 %buildroot%_man8dir/


%check
%ruby_test_unit -Ilib:test test

%files
%doc *.md LICENSE NOTICE
%_bindir/*
%_initdir/chef-client
%_unitdir/chef-client.service
%_sysconfdir/sysconfig/chef-client
%config(noreplace) %attr(0640, root, _chef) %_sysconfdir/chef/client.rb
%dir %attr(0750, root, _chef) %_sysconfdir/chef
%dir %attr(0750, _chef, _chef) %_var/log/chef
%dir %attr(0750, _chef, _chef) %_var/lib/chef
%dir %attr(0750, _chef, _chef) %_var/cache/chef
%ruby_sitelibdir/*
%exclude %ruby_sitelibdir/chef-config/*
%_man1dir/*
%_man8dir/*

%files config
%ruby_sitelibdir/chef-config/*

%files doc
%ruby_ri_sitedir/*

%pre
getent group _chef  >/dev/null || groupadd -r _chef
getent passwd _chef >/dev/null || useradd  -r -g _chef -d %_var/lib/chef -s /sbin/nologin -c "Opscode Chef Daemon" _chef

%changelog
* Mon Jan 18 2016 Andrey Cherepanov <cas@altlinux.org> 12.6.0-alt1
- New version

* Mon Oct 19 2015 Andrey Cherepanov <cas@altlinux.org> 12.5.1-alt1
- New version
- Package chef-config as separate package (need ro build ohai)

* Fri Oct 02 2015 Andrey Cherepanov <cas@altlinux.org> 12.4.4-alt1
- New version

* Sun Sep 20 2015 Andrey Cherepanov <cas@altlinux.org> 12.4.2-alt1
- New version
- Check for component versions according chef.gemspec

* Mon Aug 03 2015 Andrey Cherepanov <cas@altlinux.org> 12.4.1-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 12.3.0-alt1
- New version

* Sat Jan 24 2015 Andrey Cherepanov <cas@altlinux.org> 12.0.6-alt1
- Initial build in Sisyphus

