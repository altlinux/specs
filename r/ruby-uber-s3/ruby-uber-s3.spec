%define  pkgname uber-s3
 
Name: 	 ruby-%pkgname
Version: 0.2.4 
Release: alt1
 
Summary: Ruby S3 client with synchronous and asynchronous I/O adapters
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/pressly/uber-s3
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
A simple, but very fast, S3 client for Ruby supporting synchronous
(net-http) and asynchronous (em+fibers) io.

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
* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 0.2.4-alt1
- Initial build for ALT Linux
