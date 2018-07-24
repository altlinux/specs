%define pkgname paginator

Name: ruby-%pkgname
Version: 1.2.0
Release: alt1
Summary: A generic paginator object for use in any Ruby program
License: MIT/X Consortium
Group: Development/Ruby
Url: http://rubyforge.org/projects/paginator/

Source: %pkgname-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
Paginator doesn't make any assumptions as to how data is retrieved;
you just have to provide it with the total number of objects and a
way to pull a specific set of objects based on the offset and number
of objects per page.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

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
%ruby_test_unit -Ilib test/test_paginator.rb

%files
%doc README.md
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/Paginator*

%changelog
* Thu Jul 19 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt2.2
- Rebuild with new Ruby autorequirements.

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.1.1-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.1-alt2
- Rebuilt with Ruby 1.9

* Tue Sep 02 2008 Sir Raorn <raorn@altlinux.ru> 1.1.1-alt1
- [1.1.1]

* Tue Jan 08 2008 Sir Raorn <raorn@altlinux.ru> 1.1.0-alt1
- Initial build for ALT Linux

