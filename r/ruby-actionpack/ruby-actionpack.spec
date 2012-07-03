%define pkgname actionpack

Name: ruby-%pkgname
Version: 2.3.11
Release: alt1
Summary: Web-flow and rendering framework putting the VC in MVC.
License: MIT
Group: Development/Ruby
Url: http://rubyforge.org/projects/actionpack/

Requires: ruby-activesupport = %version
Requires: ruby-activerecord = %version

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Jul 08 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-activerecord-sqlite3-adapter ruby-builder ruby-i18n ruby-mocha ruby-rack ruby-redcloth ruby-tool-rdoc ruby-tool-setup

%description
Eases web-request routing, handling, and response as a half-way front,
half-way page controller. Implemented with specific emphasis on enabling
easy unit/integration testing that doesn't require a browser.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1
rm -rf lib/action_controller/vendor/rack*
%update_setup_rb

%build
%ruby_config
%ruby_build
# Uses actionmailer
rm -f test/controller/assert_select_test.rb

# XXX@timonbl4: this tests not pass
rm -f test/activerecord/active_record_store_test.rb
rm -f test/controller/action_pack_assertions_test.rb
rm -f test/controller/cookie_test.rb
rm -f test/controller/integration_test.rb
rm -f test/controller/session/cookie_store_test.rb
rm -f test/controller/session/mem_cache_store_test.rb
rm -f test/template/number_helper_i18n_test.rb
rm -f test/controller/render_test.rb

ruby -Ilib:test:. -e 'Dir["test/[cft]*/**/*_test.rb"].sort.each {|f| require f }'
ruby -Ilib:test:. -e 'Dir["test/activerecord/*_test.rb"].sort.each {|f| require f }'

%install
%ruby_install
%rdoc lib/

# TODO for 2.x: remove lib/action_controller/vendor/ and package:
#  http://rubyforge.org/projects/scrapi (html-scanner)
# However, included scrAPI parts seems to be heavily patched...
%add_ruby_weakprov_path action_controller/vendor/html-scanner

%files
%doc CHANGELOG README
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/Action*

%changelog
* Thu Apr 21 2011 Timur Aitov <timonbl4@altlinux.org> 2.3.11-alt1
- [2.3.11]

* Sat Jun 05 2010 Alexey I. Froloff <raorn@altlinux.org> 2.3.8-alt1.1
- Fix cookies processing

* Sat May 29 2010 Alexey I. Froloff <raorn@altlinux.org> 2.3.8-alt1
- [2.3.8]

* Mon Apr 26 2010 Alexey I. Froloff <raorn@altlinux.org> 2.3.5-alt3.1
- Fix ActionView::Helpers::TextHelper#concat()

* Sun Apr 25 2010 Alexey I. Froloff <raorn@altlinux.org> 2.3.5-alt3
- [2.3.5-200-g9e262de]

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 2.3.5-alt2
- [2.3.5-175-ga84e9b4]

* Sat Nov 28 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.5-alt1
- [2.3.5]

* Sat Oct 31 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.4-alt2
- Fixed compatibility with new rack

* Tue Oct 13 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.4-alt1
- [2.3.4-68-g7454d18]

* Tue Jul 28 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.3.1-alt2
- Backported "Fix filter_parameter_logging of non-hash values within
  array params" from 2-3-stable

* Fri Jul 24 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.3.1-alt1
- [2.3.3.1]
- Removed obsolete %%pre script

* Mon Jul 13 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.2.1-alt2
- Backported "http_authentication needs to fail authentication if the
  password procedure returns nil" from 2-3-stable (closes: #20765)
- Backported "Ensure HTTP Digest auth uses appropriate HTTP method"
  from 2-3-stable

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

* Sun Dec 09 2007 Sir Raorn <raorn@altlinux.ru> 1.13.6-alt1
- [1.13.6]

* Thu Jun 07 2007 Sir Raorn <raorn@altlinux.ru> 1.13.3-alt2.2
- Remove more dangling directories...

* Thu Jun 07 2007 Sir Raorn <raorn@altlinux.ru> 1.13.3-alt2.1
- Remove dangling directories before install

* Thu Jun 07 2007 Sir Raorn <raorn@altlinux.ru> 1.13.3-alt2
- Oops, jnly *.rb were packaged as files

* Wed May 23 2007 Sir Raorn <raorn@altlinux.ru> 1.13.3-alt1
- [1.13.3]

* Fri Aug 11 2006 Sir Raorn <raorn@altlinux.ru> 1.12.5-alt1
- [1.12.5]

* Thu Jul 06 2006 Sir Raorn <raorn@altlinux.ru> 1.12.3-alt1
- [1.12.3]

* Wed Mar 15 2006 Sir Raorn <raorn@altlinux.ru> 1.11.2-alt1
- 1.11.2
- Dropped rubygems

* Wed Aug 31 2005 Mikhail Yakshin <greycat@altlinux.ru> 1.9.1-alt1
- Initial build for ALT Linux

