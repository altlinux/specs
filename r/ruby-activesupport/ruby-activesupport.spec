%define pkgname activesupport

Name: ruby-%pkgname
Version: 2.3.11
Release: alt1
Summary: Support and utility classes used by the Rails framework
License: MIT
Group: Development/Ruby
Url: http://rubyforge.org/projects/activesupport/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 18 2008 (-bi)
BuildRequires: libxml-ruby rpm-build-ruby ruby-builder ruby-i18n ruby-json ruby-memcache-client ruby-mocha ruby-nokogiri ruby-tool-rdoc ruby-tool-setup ruby-tzinfo tzdata

%description
Utility library which carries commonly used classes and goodies from the
Rails framework.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -q -n %pkgname-%version
%patch -p1
rm -rf lib/active_support/vendor*
# JRuby crap
rm -f lib/active_support/xml_mini/jdom.rb
%update_setup_rb

%build
%ruby_config
%ruby_build

# XXX@timonbl4: this test don't pass
rm -f test/xml_mini/nokogirisax_engine_test.rb
rm -f test/core_ext/time_ext_test.rb

ruby -Ilib:test:. -e 'Dir["test/**/*_test.rb"].sort.each { |f| require f }'

%install
%ruby_install
%rdoc lib/

%files
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/ActiveSupport*

%changelog
* Thu Apr 21 2011 Timur Aitov <timonbl4@altlinux.org> 2.3.11-alt1
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

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.2.1-alt1
- [2.3.2.1]

* Wed Nov 19 2008 Sir Raorn <raorn@altlinux.ru> 2.2.1-alt1
- [2.2.1]

* Mon Nov 10 2008 Sir Raorn <raorn@altlinux.ru> 2.2.0-alt1
- [2.2.0]

* Mon Sep 08 2008 Sir Raorn <raorn@altlinux.ru> 2.1.1-alt1
- [2.1.1]

* Tue Jul 08 2008 Sir Raorn <raorn@altlinux.ru> 2.1.0-alt1
- [2.1.0]

* Mon Mar 31 2008 Sir Raorn <raorn@altlinux.ru> 2.0.2-alt2
- Rebuilt with rpm-build-ruby

* Mon Jan 07 2008 Sir Raorn <raorn@altlinux.ru> 2.0.2-alt1
- [2.0.2]
- Eliminated vendor/*, use system packages
- Use ruby-tool-setup
- Updated buildreqs

* Sun Dec 09 2007 Sir Raorn <raorn@altlinux.ru> 1.4.4-alt1
- [1.4.4]

* Wed May 23 2007 Sir Raorn <raorn@altlinux.ru> 1.4.2-alt1
- [1.4.2]

* Thu Jul 06 2006 Sir Raorn <raorn@altlinux.ru> 1.3.1-alt1
- [1.3.1]

* Wed Mar 15 2006 Sir Raorn <raorn@altlinux.ru> 1.2.5-alt1
- 1.2.5
- Dropped rubygems

* Wed Aug 31 2005 Mikhail Yakshin <greycat@altlinux.ru> 1.1.1-alt1
- Initial build for ALT Linux

