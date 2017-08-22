%define  pkgname rr
 
Name: 	 ruby-%pkgname
Version: 1.2.1
Release: alt1
 
Summary: RR is a test double framework that features a rich selection of double techniques and a terse syntax
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/rr/rr
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
RR is a test double framework for Ruby that features a rich selection of double techniques and a terse syntax.

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
* Tue Aug 22 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- Initial build for ALT Linux
