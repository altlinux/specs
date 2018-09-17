%define  pkgname mixlib-log
 
Name: 	 ruby-%pkgname
Version: 2.0.7
Release: alt1
 
Summary: A simple class based Log mechanism, similar to Merb and Chef, that you can mix in to your project
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/chef/mixlib-log
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Mixlib::Log provides a mixin for enabling a class based logger object,
a-la Merb, Chef, and Nanite.

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
* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.7-alt1
- New version.

* Fri Aug 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt1
- New version.
- Package as gem.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.4-alt1
- New version.

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- Initial build for ALT Linux
