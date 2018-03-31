%define  pkgname sigar
 
Name: 	 ruby-%pkgname
Version: 0.7.3
Release: alt1.4
 
Summary: System Information Gatherer And Reporter
License: Apache 2.0
Group:   Development/Ruby
Url:     https://rubygems.org/gems/sigar
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
 
Source:  %pkgname-%version.tar
Patch1:  %pkgname-disable-inline.patch
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel ruby-test-unit ruby-tool-rdoc
 
%description
System Information Gatherer And Reporter.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%patch1 -p1
%update_setup_rb
 
%build
%ruby_config
%ruby_build
%rake

%install
%makeinstall_std -C bindings/ruby
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
 
%files
%doc README*
%ruby_sitearchdir/*.so
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1.1
- Rebuild with Ruby 2.4.1

* Wed Mar 08 2017 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1
- Initial build in Sisyphus
