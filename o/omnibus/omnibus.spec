%define  pkgname omnibus
 
Name: 	 %pkgname
Version: 5.6.12
Release: alt1
 
Summary: Easily create full-stack installers for your Ruby project across a variety of platforms
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/chef/omnibus.git
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
# Use omnibus-software definitions
Patch1:  omnibus-use-omnibus-software.patch
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Easily create full-stack installers for your Ruby project across a
variety of platforms.

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
 
%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
 
%check
%ruby_test_unit -Ilib:test test
 
%files
%doc README*
%_bindir/%name
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 5.6.12-alt1
- New version.

* Thu Apr 05 2018 Andrey Cherepanov <cas@altlinux.org> 5.6.10-alt1
- New version.

* Mon Jun 26 2017 Andrey Cherepanov <cas@altlinux.org> 5.6.1-alt1
- New version

* Thu May 21 2015 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- Initial build for ALT Linux
