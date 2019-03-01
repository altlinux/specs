%define  pkgname ffi-yajl
%def_without benchmark
 
Name: 	       ruby-%pkgname
Version:       2.3.1
Release:       alt3
Summary:       ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/chef/ffi-yajl
# VCS:         https://github.com/chef/ffi-yajl.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
 
Source:        %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rack)
BuildRequires: gem(rspec)
BuildRequires: gem(rake-compiler)
BuildRequires: gem(rake)
BuildRequires: gem(ffi)
BuildRequires: gem(libyajl2)
BuildRequires: libyajl-devel

%description
ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library.
ffi-yajl supports multiple Ruby C extension mechanisms, including both
MRI native extensions and FFI in order to be compatible with as many
Ruby implementations as possible while providing good performance where
possible.

%package doc
Summary:       Documentation files for %name
Group:         Documentation
 
BuildArch:     noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%_bindir/ffi-yajl-bench
%ruby_gemlibdir/*
%ruby_gemextdir/*
%ruby_gemspecdir/*

%files doc
%ruby_gemdocdir/*
 
%changelog
* Tue Feb 05 2019 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt3
- Use Ruby Policy 2.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt2.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt2
- Fix yajl-ruby library name.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Jun 22 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt2
- Rebuild with new %%ruby_sitearchdir location
- Optionally build benchmark tool, disabled by default

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- new version 2.3.0

* Tue Sep 22 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- New version

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux
