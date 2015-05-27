%define  pkgname omnibus-software
 
Name: 	 %pkgname
Version: 4.0.0 
Release: alt1.gita5aef20
 
Summary: Collection of shared software descriptions, for use by any Omnibus project that needs them
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/chef/omnibus-software.git
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: omnibus

%description
Collection of shared software descriptions, for use by any Omnibus
project that needs them.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
# s/mac_os_x_mavericks? method does not support in ruby-chef-sugar-3.1.0
subst 's/mac_os_x_mavericks?/mac_os_x?/' config/software/bzip2.rb
%update_setup_rb
 
%build
%ruby_config
%ruby_build
 
%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

# Copy software definition
mkdir -p %buildroot%_libexecdir/%name
cp -a config %buildroot%_libexecdir/%name
 
%check
%ruby_test_unit -Ilib:test test
 
%files
%doc README*
%ruby_sitelibdir/*
%_libexecdir/%name

%files doc
%ruby_ri_sitedir/*
 
%changelog
* Wed May 27 2015 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1.gita5aef20
- Initial build for ALT Linux
