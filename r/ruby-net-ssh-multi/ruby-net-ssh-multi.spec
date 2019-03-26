%define        pkgname net-ssh-multi
 
Name: 	       ruby-%pkgname
Version:       1.2.1
Release:       alt1
Summary:       SSH connection multiplexing: execute commands simultaneously on multiple hosts via SSH
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/net-ssh/net-ssh-multi
# VCS:         https://github.com/net-ssh/net-ssh-multi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
 
Source:        %name-%version.tar
 
BuildRequires(pre): rpm-build-ruby
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


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
 
%description   doc
Documentation files for %gemname gem.


%prep
%setup
 
%build
%gem_build
 
%install
%gem_install
 
%check
%gem_test
 
%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir
 
%changelog
* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt1
- Bump to 1.2.1
- Use Ruby Policy 2.0

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
