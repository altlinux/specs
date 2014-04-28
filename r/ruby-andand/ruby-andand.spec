%define  pkgname andand
 
Name: 	 ruby-%pkgname
Version: 1.3.1 
Release: alt1
 
Summary: andand is a method that provides guarded method invocation, analagous to the && operator in Ruby, and especially &&=
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://andand.rubyforge.org/
 
Packager: Andrey Cherepanov <cas@altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-test-unit ruby-tool-rdoc ruby-tool-setup
 
%description
andand is a method that provides guarded method invocation, analagous to
the && operator in Ruby, and especially &&=.

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
* Mon Apr 21 2014 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux
