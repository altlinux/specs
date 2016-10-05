%define  pkgname em-synchrony
 
Name: 	 ruby-%pkgname
Version: 1.0.5
Release: alt1
 
Summary: Fiber aware EventMachine clients and convenience classes
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/igrigorik/em-synchrony
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Collection of convenience classes and primitives to help untangle
evented code, plus a number of patched EM clients to make them Fiber
aware. To learn more, please see: Untangling Evented Code with Ruby
Fibers.

* Fiber aware ConnectionPool with sync/async query support
* Fiber aware Iterator to allow concurrency control & mixing of
  sync/async
* Fiber aware async inline support: turns any async function into sync
* Fiber aware Multi-request interface for any callback enabled clients
* Fiber aware TCPSocket replacement, powered by EventMachine
* Fiber aware Thread, Mutex, ConditionVariable clases
* Fiber aware sleep, defer, system

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
rm -rf lib/active_record
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
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- new version 1.0.5

* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- Initial build for ALT Linux
