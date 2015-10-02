%define  pkgname plist
 
Name: 	 ruby-%pkgname
Version: 3.1.0 
Release: alt1
 
Summary: All-purpose Property List manipulation library for Ruby
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/bleything/plist
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Plist is a library to manipulate Property List files, also known as
plists. It can parse plist files into native Ruby data structures as
well as generating new plist files from your Ruby objects.

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
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Mon Sep 21 2015 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version

* Tue Feb 17 2015 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt2
- Return to Sisyphus
