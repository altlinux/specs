%define  pkgname spec_helper
 
Name: 	 ruby-%pkgname
Version: 1.0.1 
Release: alt1
 
Summary: A set of shared spec helpers specific to Puppetlabs projects
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/puppetlabs/puppetlabs_spec_helper
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
#BuildRequires: ruby-rspec-puppet
BuildRequires: ruby-rspec-expectations
BuildRequires: ruby-puppet-lint
BuildRequires: ruby-puppet-syntax
BuildRequires: ruby-mocha
 
%description
This repository is meant to provide a single source of truth for how to
initialize different Puppet versions for spec testing.

The common use case is a module such as stdlib that works with many
versions of Puppet. The stdlib module should require the spec helper in
this repository, which will in turn automatically figure out the version
of Puppet being tested against and perform version specific
initialization.

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
rm -f %buildroot%ruby_sitelibdir/puppetlabs_spec_helper/module_spec_helper.rb
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
* Tue Dec 22 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial build for ALT Linux (without rspec-puppet support to prevent
  circular dependencies)
