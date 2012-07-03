%define pkgname activeresource

Name: ruby-%pkgname
Version: 2.3.11
Release: alt1
Summary: Think Active Record for web resources
License: Ruby
Group: Development/Ruby
Url: http://rubyforge.org/projects/activeresource/

Requires: ruby-activesupport = %version

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 18 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-activesupport ruby-builder ruby-mocha ruby-tool-rdoc ruby-tool-setup

%description
Wraps web resources in model classes that can be manipulated
through XML over REST.

%package doc
Summary: Documentation files for %pkgname
Group: Documentation

%description doc
Documentation files for %pkgname

%prep
%setup -q -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib:test test/*_test.rb test/*/*_test.rb

%install
%ruby_install
%rdoc lib/

%files
%doc CHANGELOG README
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/ActiveResource*

%changelog
* Fri Apr 22 2011 Timur Aitov <timonbl4@altlinux.org> 2.3.11-alt1
- [2.3.11]

* Sat May 29 2010 Alexey I. Froloff <raorn@altlinux.org> 2.3.8-alt1
- [2.3.8]

* Sun Apr 25 2010 Alexey I. Froloff <raorn@altlinux.org> 2.3.5-alt3
- [2.3.5-200-g9e262de]

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 2.3.5-alt2
- [2.3.5-175-ga84e9b4]

* Sat Nov 28 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.5-alt1
- [2.3.5]

* Tue Oct 13 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.4-alt1
- [2.3.4-68-g7454d18]

* Fri Jul 24 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.3.1-alt1
- [2.3.3.1]

* Mon Jun 29 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.2.1-alt1
- [2.3.2.1]

* Wed Nov 19 2008 Sir Raorn <raorn@altlinux.ru> 2.2.1-alt1
- [2.2.1]

* Tue Nov 18 2008 Sir Raorn <raorn@altlinux.ru> 2.2.0-alt1
- [2.2.0]

* Mon Sep 08 2008 Sir Raorn <raorn@altlinux.ru> 2.1.1-alt1
- [2.1.1]

* Tue Jul 08 2008 Sir Raorn <raorn@altlinux.ru> 2.1.0-alt1
- [2.1.0]

* Wed Apr 02 2008 Sir Raorn <raorn@altlinux.ru> 2.0.2-alt2
- Rebuilt with rpm-build-ruby

* Tue Jan 08 2008 Sir Raorn <raorn@altlinux.ru> 2.0.2-alt1
- Initial build for ALT Linux

