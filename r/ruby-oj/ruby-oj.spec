%define  pkgname oj
 
Name: 	 ruby-%pkgname
Version: 2.18.2
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
rm -f lib/oj/active_support_helper.rb
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
%ruby_sitearchdir/*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*
 
%changelog
* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.2-alt1
- New version
- Remove ActiveSupportHelper
- Rebuild with new %%ruby_sitearchdir location

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.1-alt1
- new version 2.18.1

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 2.17.4-alt1
- new version 2.17.4

* Tue Jun 02 2015 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt0.M70P.1
- Backport new version to p7 branch

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- Initial build for ALT Linux
