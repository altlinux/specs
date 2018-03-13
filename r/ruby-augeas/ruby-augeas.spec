%define  pkgname augeas
 
Name: 	 ruby-%pkgname
Version: 0.5.0
Release: alt2.3
Epoch:   1
 
Summary: Provides bindings for augeas
License: LGPL 2.1
Group:   Development/Ruby
Url:     http://augeas.net
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
 
Source:  %name-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: libaugeas-devel

Conflicts: ruby-augeas-new

%description
Provides bindings for augeas.

%prep
%setup
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
%doc AUTHORS README*
%ruby_sitearchdir/*
%ruby_sitelibdir/*.rb
 
%changelog
* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2.1
- Rebuild with Ruby 2.4.1

* Fri Apr 07 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2
- Use original gem in Sisyphus (ALT #33345)

* Fri Apr 07 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.4-alt1
- Initial build in Sisyphus
