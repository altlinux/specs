%define  pkgname benchmark-ips
 
Name: 	 ruby-%pkgname
Version: 1.2.0 
Release: alt1.gite47e416
 
Summary: A iterations per second enhancement to Benchmark
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/evanphx/benchmark-ips
 
Packager: Andrey Cherepanov <cas@altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-test-unit ruby-tool-rdoc ruby-tool-setup
 
%description
Benchmark/ips benchmarks a blocks iterations/second. For short snippets
of code, ips automatically figures out how many times to run the code to
get interesting data. No more guessing at random iteration counts.

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
%_bindir/benchmark_ips
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1.gite47e416
- Initial build for ALT Linux
