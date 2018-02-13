%define  pkgname ohai
 
Name: 	 %pkgname
Version: 14.0.2
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
BuildRequires: ruby-ipaddr_extensions
BuildRequires: ruby-sigar
BuildRequires: ruby-tool-setup

%filter_from_requires \,^ruby(\(win32\|wmi\),d

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
* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.2-alt1
- New version.

* Wed Jan 31 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.1-alt1
- New version.

* Thu Jan 11 2018 Andrey Cherepanov <cas@altlinux.org> 13.7.1-alt1
- New version.

* Wed Dec 06 2017 Andrey Cherepanov <cas@altlinux.org> 13.7.0-alt1
- New version.

* Wed Oct 25 2017 Andrey Cherepanov <cas@altlinux.org> 13.6.0-alt1
- New version

* Fri Sep 29 2017 Andrey Cherepanov <cas@altlinux.org> 13.5.0-alt1
- New version

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 13.4.0-alt1
- New version

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 13.3.0-alt1
- New version

* Sat Jul 01 2017 Andrey Cherepanov <cas@altlinux.org> 13.2.0-alt1
- New version

* Sat May 13 2017 Andrey Cherepanov <cas@altlinux.org> 13.1.0-alt1
- New version

* Thu Apr 13 2017 Andrey Cherepanov <cas@altlinux.org> 13.0.1-alt1
- New version

* Fri Apr 07 2017 Andrey Cherepanov <cas@altlinux.org> 13.0.0-alt1
- New version

* Wed Mar 08 2017 Andrey Cherepanov <cas@altlinux.org> 8.23.0-alt1
- new version 8.23.0

* Wed Oct 05 2016 Andrey Cherepanov <cas@altlinux.org> 8.20.0-alt1
- new version 8.20.0

* Mon Oct 19 2015 Andrey Cherepanov <cas@altlinux.org> 8.7.0-alt1
- New version

* Fri Jan 30 2015 Andrey Cherepanov <cas@altlinux.org> 8.0.1-alt1
- Initial build for ALT Linux
