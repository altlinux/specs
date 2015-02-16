%define  pkgname mixlib-log
 
Name: 	 ruby-%pkgname
Version: 1.4.0 
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
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- Initial build for ALT Linux
