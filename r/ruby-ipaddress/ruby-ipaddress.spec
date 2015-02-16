%define  pkgname ipaddress
 
Name: 	 ruby-%pkgname
Version: 0.8.0 
Release: alt1
 
Summary: A library to handle IP (both IPv4 and IPv6) addresses for Ruby
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/bluemonk/ipaddress
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
IPAddress is a Ruby library designed to make the use of IPv4 and IPv6
addresses simple, powerful and enjoyable. It provides a complete set of
methods to handle IP addresses for any need, from simple scripting to
full network design.

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
#ruby_test_unit -Ilib:test test
 
%files
%doc README*
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt1
- Initial build for ALT Linux
- Disable tests
