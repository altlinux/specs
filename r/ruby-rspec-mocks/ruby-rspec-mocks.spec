%define  pkgname rspec-mocks
 
Name: 	 ruby-%pkgname
Version: 3.4.0
Release: alt1
 
Summary: RSpec's 'test double' framework, with support for stubbing and mocking
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/rspec/rspec-mocks
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
rspec-mocks is a test-double framework for rspec with support for method
stubs, fakes, and message expectations on generated test-doubles and
real objects alike.

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
* Mon Jan 18 2016 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- Initial build for ALT Linux
