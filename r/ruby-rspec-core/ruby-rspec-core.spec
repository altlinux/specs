%define  pkgname rspec-core
 
Name: 	 ruby-%pkgname
Version: 3.7.1
Release: alt1
 
Summary: RSpec runner and formatters
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/rspec/rspec-core
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
rspec-core provides the structure for writing executable examples of how
your code should behave, and an rspec command with tools to constrain
which examples get run and tailor the output.

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
install -Dm 0755 exe/rspec %buildroot%_bindir/rspec
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
 
%check
%ruby_test_unit -Ilib:test test
 
%files
%doc README*
%_bindir/rspec
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Thu Jan 04 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt1
- New version.

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Jun 01 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version
- Package rspec executable

* Mon Jan 18 2016 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- Initial build for ALT Linux
