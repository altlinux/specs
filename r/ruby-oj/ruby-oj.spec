%define  pkgname oj
 
Name: 	 ruby-%pkgname
Version: 3.4.0
Release: alt1
 
Summary: A fast JSON parser and Object marshaller as a Ruby gem
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://www.ohler.com/oj/
 
Packager: Andrey Cherepanov <cas@altlinux.org>
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
 
%description
A fast JSON parser and Object marshaller as a Ruby gem.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
# Remove unmet to C extension
#subst 's,^require.*oj/oj.*,,' lib/oj.rb
rm -f lib/oj/active_support_helper.rb
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
#%%ruby_test_unit -Ilib:test test
 
%files
%doc README*
%ruby_sitearchdir/*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*
 
%changelog
* Fri Jan 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version.

* Mon Jan 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.10-alt1
- New version.

* Sat Oct 28 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.9-alt1
- New version

* Thu Oct 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.8-alt1
- New version

* Tue Oct 03 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.7-alt1
- New version

* Sat Sep 23 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.6-alt1
- New version

* Sat Sep 09 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.5-alt1.1
- Rebuild with Ruby 2.4.1

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.5-alt1
- New version

* Fri Aug 04 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.4-alt1
- New version

* Wed Aug 02 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.3-alt1
- New version

* Wed Jul 12 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.2-alt1
- New version

* Tue Jul 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.1-alt1
- New version

* Sun Jul 09 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- New version

* Wed Jul 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- New version

* Thu Jun 22 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.0-alt1
- New version

* Mon Jun 19 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.4-alt1
- New version

* Wed Jun 14 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.3-alt1
- New version

* Tue Jun 13 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.2-alt1
- New version

* Mon Jun 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version

* Sat Jun 03 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.11-alt1
- New version

* Fri May 19 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.9-alt1
- New version

* Wed May 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.8-alt1
- New version

* Thu May 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.7-alt1
- New version

* Mon May 08 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.6-alt1
- New version

* Thu May 04 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.5-alt1
- New version

* Tue May 02 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.4-alt1
- New version

* Fri Apr 28 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version

* Wed Apr 26 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- New version

* Tue Apr 25 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version

* Wed Mar 22 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.5-alt1
- New version

* Wed Mar 15 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.3-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.2-alt1
- New version
- Remove ActiveSupportHelper
- Rebuild with new %%ruby_sitearchdir location

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.1-alt1
- new version 2.18.1

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 2.17.4-alt1
- new version 2.17.4

* Tue Jun 02 2015 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt0.M70P.1
- Backport new version to p7 branch

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- Initial build for ALT Linux
