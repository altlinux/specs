%define  pkgname oj
 
Name: 	 ruby-%pkgname
Version: 2.8.0 
Release: alt1
 
Summary: A fast JSON parser and Object marshaller as a Ruby gem
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://www.ohler.com/oj/
 
Packager: Andrey Cherepanov <cas@altlinux.org>
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
 
%description
A fast JSON parser and Object marshaller as a Ruby gem.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
# Remove unmet to C extension
subst 's,^require.*oj/oj.*,,' lib/oj.rb
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

%files doc
%ruby_ri_sitedir/*
 
%changelog
* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- Initial build for ALT Linux
