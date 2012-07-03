%define pkgname paginator

Name: ruby-%pkgname
Version: 1.1.1
Release: alt2
Summary: A generic paginator object for use in any Ruby program
License: MIT/X Consortium
Group: Development/Ruby
Url: http://rubyforge.org/projects/paginator/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Jan 08 2008 (-bi)
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
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib test/test_paginator.rb

%install
%ruby_install
%rdoc lib/

%files
%doc History.txt README.txt
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/Paginator*

%changelog
* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.1-alt2
- Rebuilt with Ruby 1.9

* Tue Sep 02 2008 Sir Raorn <raorn@altlinux.ru> 1.1.1-alt1
- [1.1.1]

* Tue Jan 08 2008 Sir Raorn <raorn@altlinux.ru> 1.1.0-alt1
- Initial build for ALT Linux

