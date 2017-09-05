%define  pkgname systemu
 
Name: 	 ruby-%pkgname
Version: 2.6.5 
Release: alt1.1
 
Summary: Univeral capture of stdout and stderr and handling of child process pid for windows, *nix, etc.
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/ahoward/systemu
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
Patch:   remove-obsoleted-thread.patch
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(jruby)$/d

%description
Universal capture of stdout and stderr and handling of child process pid
for windows, *nix, etc.

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
 
%check
%ruby_test_unit -Ilib:test test
 
%files
%doc README*
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Sat Sep 09 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt1
- New version from https://rubygems.org/gems/systemu/versions/2.6.5

* Mon Oct 19 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.4-alt1
- Initial build for ALT Linux
