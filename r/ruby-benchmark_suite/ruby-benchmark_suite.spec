%define  pkgname benchmark_suite
 
Name: 	 ruby-%pkgname
Version: 1.0.0 
Release: alt1.git5bded6
 
Summary: A set of enhancements to the standard library benchmark.rb
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/evanphx/benchmark_suite
 
Packager: Andrey Cherepanov <cas@altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-test-unit ruby-tool-rdoc ruby-tool-setup
BuildRequires: ruby-benchmark-ips
 
%description
This package contains a command line tool for running multiple
benchmarks against multiple rubies. It is also uses benchmark/ips to
report iterations per second.

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
%_bindir/benchmark
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.git5bded6
- Initial build for ALT Linux
