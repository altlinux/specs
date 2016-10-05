%define  pkgname ohai
 
Name: 	 %pkgname
Version: 8.20.0
Release: alt1
 
Summary: Ohai profiles your system and emits JSON
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/chef/ohai
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
#BuildRequires: chef-config
BuildRequires: ruby-ffi >= 1.9
BuildRequires: ruby-ffi-yajl >= 2.2
BuildRequires: ruby-ipaddress
BuildRequires: ruby-mime-types >= 2.0
BuildRequires: ruby-mixlib-cli
BuildRequires: ruby-mixlib-config >= 2.0
BuildRequires: ruby-mixlib-log
BuildRequires: ruby-mixlib-shellout >= 2.0
BuildRequires: ruby-net-dhcp
BuildRequires: ruby-systemu >= 2.6.4
BuildRequires: ruby-tool-setup
# Windows-specific requirement ruby-wmi-lite is not required
 
%description
Ohai is a tool that is used to detect attributes on a node, and then
provide these attributes to the chef-client at the start of every
chef-client run. Ohai is required by the chef-client and must be present
on a node.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%update_setup_rb
 
%build
%ruby_config
%ruby_build
 
%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
 
%check
%ruby_test_unit -Ilib:test test
 
%files
%doc README*
%_bindir/%pkgname
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Wed Oct 05 2016 Andrey Cherepanov <cas@altlinux.org> 8.20.0-alt1
- new version 8.20.0

* Mon Oct 19 2015 Andrey Cherepanov <cas@altlinux.org> 8.7.0-alt1
- New version

* Fri Jan 30 2015 Andrey Cherepanov <cas@altlinux.org> 8.0.1-alt1
- Initial build for ALT Linux
