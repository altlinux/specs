%define  pkgname rspec-puppet
 
Name: 	 ruby-%pkgname
Version: 0.1.6 
Release: alt1
 
Summary: RSpec tests for your Puppet manifests
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/puppetlabs/rspec-puppet
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
Patch0:  fix-import-rspec.patch
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-rspec-core
BuildRequires: ruby-spec_helper
BuildRequires: ruby-tool-setup
 
%description
RSpec tests for your Puppet manifests & modules.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%patch0 -p1
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
%_bindir/*
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Wed Dec 23 2015 Andrey Cherepanov <cas@altlinux.org> 0.1.6-alt1
- Initial build for ALT Linux
