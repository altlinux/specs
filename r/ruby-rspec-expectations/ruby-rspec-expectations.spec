%define  pkgname rspec-expectations
 
Name: 	 ruby-%pkgname
Version: 3.4.0 
Release: alt1
 
Summary: Provides a readable API to express expected outcomes of a code example
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/rspec/rspec-expectations
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: ruby-rspec-support
 
%description
RSpec::Expectations lets you express expected outcomes on an object in
an example.

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
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Sat Dec 26 2015 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- Initial build for ALT Linux
