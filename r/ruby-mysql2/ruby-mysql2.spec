%define  pkgname mysql2
 
Name: 	 ruby-%pkgname
Version: 0.4.10
Release: alt1
 
Summary: A modern, simple and very fast Mysql library for Ruby - binding to libmysql
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/brianmario/mysql2
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel ruby-test-unit ruby-tool-rdoc
BuildRequires: libmysqlclient-devel

%filter_from_requires \,^ruby(Win32API),d

%description
The Mysql2 gem is meant to serve the extremely common use-case of
connecting, querying and iterating on results. Some database libraries
out there serve as direct 1:1 mappings of the already complex C APIs
available. This one is not.

It also forces the use of UTF-8 [or binary] for the connection [and all
strings in 1.9, unless Encoding.default_internal is set then it will
convert from UTF-8 to that encoding] and uses encoding-aware MySQL API
calls where it can.

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
%ruby_config -- --without-mysql-rpath
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
%ruby_sitearchdir/*
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Wed Nov 15 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.10-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1.1
- Rebuild with Ruby 2.4.1

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1
- New version

* Tue Jul 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.8-alt1
- New version

* Wed Jul 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.7-alt1
- New version

* Thu May 04 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.6-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.5-alt2
- Rebuild with new %%ruby_sitearchdir location

* Wed Mar 08 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.5-alt1
- New version

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 0.4.4-alt2
- Rebuild with Ruby 2.3.1

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 0.4.4-alt1
- New version

* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 0.3.18-alt1
- Initial build for ALT Linux
