Name: 	 chef-zero
Version: 14.0.1
Release: alt1
 
Summary: Self-contained, easy-setup, fast-start in-memory Chef server for testing and solo setup purposes
License: Apache 2.0
Group:   Development/Ruby
Url:     http://www.opscode.com/
# VCS:   https://github.com/chef/chef-zero

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %name-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: ruby-mixlib-log
BuildRequires: ruby-hashie
BuildRequires: ruby-uuidtools
BuildRequires: ruby-ffi-yajl
 
Requires: ruby-rack-handler-webrick

%description
rubyzip is a ruby module for reading and writing zip files.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup
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
%doc CHANGELOG.md LICENSE README.md
%_bindir/chef-zero
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Mon Feb 19 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.1-alt1
- New version.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 13.1.0-alt1.1
- Rebuild with Ruby 2.4.1

* Tue Jul 18 2017 Andrey Cherepanov <cas@altlinux.org> 13.1.0-alt1
- New version

* Tue Apr 04 2017 Andrey Cherepanov <cas@altlinux.org> 13.0.0-alt1
- New version

* Wed Mar 29 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.2-alt1
- New version

* Tue Mar 21 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- new version 5.2.0

* Wed Oct 05 2016 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- new version 5.1.0

* Fri Aug 21 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.3-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- New version

* Tue Feb 17 2015 Andrey Cherepanov <cas@altlinux.org> 4.0-alt1
- Initial build for ALT Linux
