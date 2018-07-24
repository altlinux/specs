%define  pkgname mixlib-shellout
 
Name: 	 ruby-%pkgname
Version: 2.4.0
Release: alt1
 
Summary: mixin library for subprocess management, output collection
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/chef/mixlib-shellout
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Provides a simplified interface to shelling out yet still collecting
both standard out and standard error and providing full control over
environment, working directory, uid, gid, etc.

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
%rubygem_specdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux
