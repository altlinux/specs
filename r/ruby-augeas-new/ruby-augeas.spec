%define  pkgname augeas
 
Name: 	 ruby-%pkgname-new
Version: 0.6.4 
Release: alt1.3
 
Summary: A fork of ruby-augeas (bindings for augeas) with exceptions support
License: LGPL 2.1
Group:   Development/Ruby
Url:     https://github.com/dotdoom/augeas
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: libaugeas-devel
 
%description
A fork of ruby-augeas (bindings for augeas) with exceptions support.

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
%ruby_sitearchdir/*
%ruby_sitelibdir/*.rb
 
%changelog
* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.4-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.4-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.4-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Apr 07 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.4-alt1
- Initial build in Sisyphus
