%define ruby_major 1.8
%define pkgname actionmailer

Name: ruby%{ruby_major}-%pkgname
Version: 2.3.11
Release: alt2
Summary: Service layer for easy email delivery and testing
License: MIT
Group: Development/Ruby
Url: http://rubyforge.org/projects/actionmailer/

Requires: ruby%{ruby_major}-activesupport = %version

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 18 2008 (-bi)
BuildRequires: ruby%{ruby_major} rpm-build-ruby ruby%{ruby_major}-actionpack ruby%{ruby_major}-mocha ruby%{ruby_major}-text-format ruby%{ruby_major}-tmail ruby%{ruby_major}-tool-rdoc ruby-tool-setup

%description
Makes it trivial to test and deliver emails sent from a single service layer.

%package doc
Summary: Documentation files for %pkgname
Group: Documentation

%description doc
Documentation files for %pkgname

%prep
%setup -n %pkgname-%version
%patch -p1
rm -rf lib/action_mailer/vendor*
%update_setup_rb

%build
%ruby_config
%ruby_build
for t in test/*_test.rb; do
%ruby_test_unit -Ilib:test "$t"
done

%install
%ruby_install
%rdoc lib/

%files
%doc CHANGELOG README
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/Action*

%changelog
* Thu Apr 28 2011 Timur Aitov <timonbl4@altlinux.org> 2.3.11-alt2
- Rebuild for ruby1.8

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

* Tue Apr 01 2008 Sir Raorn <raorn@altlinux.ru> 2.0.2-alt2
- Rebuilt with rpm-build-ruby

* Tue Jan 08 2008 Sir Raorn <raorn@altlinux.ru> 2.0.2-alt1
- [2.0.2]

* Sun Dec 09 2007 Sir Raorn <raorn@altlinux.ru> 1.3.6-alt1
- [1.3.6]

* Wed May 23 2007 Sir Raorn <raorn@altlinux.ru> 1.3.3-alt1
- [1.3.3]

* Fri Aug 11 2006 Sir Raorn <raorn@altlinux.ru> 1.2.5-alt1
- [1.2.5]

* Thu Jul 06 2006 Sir Raorn <raorn@altlinux.ru> 1.2.3-alt1
- [1.2.3]

* Wed Mar 15 2006 Sir Raorn <raorn@altlinux.ru> 1.1.5-alt1
- [1.1.5]
- Dropped rubygems

* Wed Aug 31 2005 Mikhail Yakshin <greycat@altlinux.ru> 1.0.1-alt1
- Initial build for ALT Linux

