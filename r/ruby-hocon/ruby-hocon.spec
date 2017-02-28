%define  pkgname hocon
 
Name: 	 ruby-%pkgname
Version: 1.2.4 
Release: alt1
 
Summary: This is a port of the Typesafe Config library to Ruby
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/puppetlabs/ruby-hocon
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %name-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
The library provides Ruby support for the HOCON configuration file format.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -q
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
%_bindir/hocon
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Tue Feb 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1
- Initial build in Sisyphus
