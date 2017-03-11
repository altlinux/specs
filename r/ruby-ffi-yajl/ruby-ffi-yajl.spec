%define  pkgname ffi-yajl
%def_without benchmark
 
Name: 	 ruby-%pkgname
Version: 2.3.0
Release: alt2
 
Summary: ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/chef/ffi-yajl
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
 
Source:  %pkgname-%version.tar
Patch:   use-system-yajl-without-wrapper.patch  

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: ruby-ffi
BuildRequires: ruby-mime-types
BuildRequires: yajl-ruby
BuildRequires: libyajl-devel

%filter_from_requires /^ruby(active_support)/d

%description
ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library.
ffi-yajl supports multiple Ruby C extension mechanisms, including both
MRI native extensions and FFI in order to be compatible with as many
Ruby implementations as possible while providing good performance where
possible.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb
 
%build
%ruby_config
%ruby_build
 
%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
%if_without benchmark
rm -rf %buildroot%_bindir/ffi-yajl-bench %buildroot%ruby_sitelibdir/ffi_yajl/benchmark*
%endif
 
%check
%ruby_test_unit -Ilib:test test
 
%files
%doc README*
%if_with benchmark
%_bindir/ffi-yajl-bench
%endif
%ruby_sitearchdir/*
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt2
- Rebuild with new %%ruby_sitearchdir location
- Optionally build benchmark tool, disabled by default

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- new version 2.3.0

* Tue Sep 22 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- New version

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux
