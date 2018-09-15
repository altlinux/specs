%define  pkgname net-ssh-multi
 
Name: 	 ruby-%pkgname
Version: 1.2.0 
Release: alt1.4
 
Summary: SSH connection multiplexing: execute commands simultaneously on multiple hosts via SSH
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/net-ssh/net-ssh-multi
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: ruby-mocha
BuildRequires: ruby-net-ssh
BuildRequires: ruby-net-ssh-gateway
 
%description
Net::SSH::Multi is a library for controlling multiple Net::SSH
connections via a single interface. It exposes an API similar to that of
Net::SSH::Connection::Session and Net::SSH::Connection::Channel, making
it simpler to adapt programs designed for single connections to be used
with multiple connections.

This library is particularly useful for automating repetitive tasks that
must be performed on multiple machines. It executes the commands in
parallel, and allows commands to be executed on subsets of servers
(defined by groups).

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
#%%ruby_test_unit -Ilib:test test
 
%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*
 
%changelog
* Wed Sep 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1.4
- Rebuild for new Ruby autorequirements.
- Disable tests.

* Thu Jul 05 2018 Dmitry Terekhin <jqt4@altlinux.org> 1.2.0-alt1.3
- Tests disabled because is need an build for mipsel

* Wed Jul 04 2018 Dmitry Terekhin <jqt4@altlinux.org> 1.2.0-alt1.2
- Add BuildRequires for mipsel

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1.1
- Rebuild with Ruby 2.4.1

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Initial build for ALT Linux
