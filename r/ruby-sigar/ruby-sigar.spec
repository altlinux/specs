%define  pkgname sigar
 
Name: 	 ruby-%pkgname
Version: 0.7.3
Release: alt1
 
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
* Wed Mar 08 2017 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1
- Initial build in Sisyphus
