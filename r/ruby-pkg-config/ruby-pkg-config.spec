%define  pkgname pkg-config
 
Name: 	 ruby-%pkgname
Version: 1.2.9
Release: alt1
 
Summary: pkg-config implemented by pure Ruby
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/ruby-gnome2/pkg-config
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%filter_from_requires \,^ruby(dl/import),d

%description
A pkg-config implementation by Ruby.

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
* Mon Jan 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.9-alt1
- New version.

* Thu Oct 19 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.8-alt1
- New version

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1
- New version

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.6-alt1
- New version

* Mon Aug 07 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1
- New version

* Tue May 30 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.3-alt1
- New version

* Mon May 29 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1
- New version

* Tue Apr 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version

* Fri Apr 21 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.9-alt1
- New version

* Thu Apr 20 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.8-alt1
- New version

* Mon Sep 26 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.7-alt1
- New version

* Tue Dec 04 2012 Led <led@altlinux.ru> 1.0.7-alt3.1
- Rebuilt with ruby-1.9.3-alt1

* Thu Nov 10 2011 Timur Aitov <timonbl4@altlinux.org> 1.0.7-alt3
- Repair build

* Fri Apr 29 2011 Timur Aitov <timonbl4@altlinux.org> 1.0.7-alt2
- Repair build

* Sun Jan 09 2011 Alexey I. Froloff <raorn@altlinux.org> 1.0.7-alt1
- Built for Sisyphus

