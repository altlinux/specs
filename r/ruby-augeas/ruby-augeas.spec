%define  pkgname augeas
 
Name: 	 ruby-%pkgname
Version: 0.6.4 
Release: alt1
 
Summary: Ruby bindings for Augeas
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
The class Augeas provides bindings to augeas [augeas.net] library.

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
* Thu Apr 06 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.4-alt1
- Initial build in Sisyphus
