%define  pkgname net-dhcp
 
Name: 	 ruby-%pkgname
Version: 1.3.2 
Release: alt1
 
Summary: Net::DHCP library for ruby, originally written by etd
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/mjtko/net-dhcp-ruby
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
The aim of Net::DHCP is to provide a set of classes to low level handle
the DHCP protocol (rfc2131, rfc2132, etc.). With Net::DHCP you will be
able to craft custom DHCP packages and have access to all the fields
defined for the protocol.

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
%_bindir/%pkgname
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.2-alt1
- Initial build for ALT Linux
