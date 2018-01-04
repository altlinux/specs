%define  pkgname em-socksify
 
Name: 	 ruby-%pkgname
Version: 0.3.2
Release: alt1
 
Summary: EventMachine SOCKSify shim: adds SOCKS support to any protocol
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/igrigorik/em-socksify
 
Packager: Andrey Cherepanov <cas@altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-test-unit ruby-tool-rdoc ruby-tool-setup
BuildRequires: ruby-eventmachine
 
%description
Dealing with SOCKS and HTTP proxies is a pain. EM-Socksify provides a
simple ship to setup and negotiation a SOCKS / HTTP connection for any
EventMachine protocol.

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
%ruby_sitelibdir/*
# For arch-specific files
#%%ruby_sitearchdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Thu Jan 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- New version.

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 0.3.1-alt1
- New version

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Initial build for ALT Linux
