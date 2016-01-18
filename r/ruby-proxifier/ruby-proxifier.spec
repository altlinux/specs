%define  pkgname proxifier
 
Name: 	 ruby-%pkgname
Version: 1.0.3 
Release: alt1
 
Summary: Proxifier adds support for HTTP or SOCKS proxies and lets you force TCPSocket to use proxies
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/samuelkadolph/ruby-proxifier
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
This gem was created for 2 purposes.

First is to enable ruby programmers to use HTTP or SOCKS proxies
interchangeably when using TCPSockets. Either manually with
Proxifier::Proxy#open or by require "proxifier/env".

The second purpose is to use ruby code that doesn't use proxies for
users that have to use proxies.  The pruby and pirb executables are
simple wrappers for their respective ruby executables that support
proxies from environment variables.

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
%_bindir/*
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Tue Jan 19 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- Initial build for ALT Linux
