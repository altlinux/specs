%define  pkgname rspec-support
 
Name: 	 ruby-%pkgname
Version: 3.7.1
Release: alt1
 
Summary: Common code needed by the other RSpec gems
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/rspec/rspec-support
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
RSpec::Support provides common functionality to RSpec::Core,
RSpec::Expectations and RSpec::Mocks. It is considered suitable for
internal use only at this time.

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
* Wed Jan 31 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt1
- New version.

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version

* Fri May 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version

* Wed Mar 08 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 3.2.2-alt1
- Initial build for ALT Linux
