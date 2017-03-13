%define  pkgname hiera
 
Name: 	 ruby-%pkgname
Version: 3.3.1
Release: alt1
 
Summary: A simple pluggable Hierarchical Database
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://projects.puppetlabs.com/projects/hiera/
 
Packager: Andrey Cherepanov <cas@altlinux.org>
BuildArch: noarch
 
Provides: %pkgname = %version-%release

Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%filter_from_requires \,^ruby(win32/dir),d

%description
A simple pluggable Hierarchical Database.

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
%_bindir/%pkgname
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Mon Mar 13 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.1-alt1
- New version

* Wed Mar 01 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- New version
- Remove autoreq on win32/dir

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.2-alt1
- new version 3.2.2

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 3.2.0-alt1
- New version

* Wed Apr 23 2014 Andrey Cherepanov <cas@altlinux.org> 1.3.2-alt1
- Initial build for ALT Linux
