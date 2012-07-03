# vim: set ft=spec: -*- rpm-spec -*-

Name: ruby-activeldap
Version: 1.2.2
Release: alt1

Summary: ruby library for object-oriented LDAP interction
Group: Development/Ruby
License: GPL

Url: http://rubyforge.org/projects/ruby-activeldap/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Wed Aug 13 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-gettext-utils ruby-tool-rdoc ruby-tool-setup

%add_findreq_skiplist %_datadir/rails/plugins/*/rails_generators/*/templates/*

%description
Ruby/ActiveLDAP is a ruby extension library which provides a clean
objected oriented interface to the Ruby/LDAP library.  It was inspired
by ActivRecord. This is not nearly as clean or as flexible as
ActiveRecord, but it is still trivial to define new objects and
manipulate them with minimal difficulty.

%package -n rails-plugin-activeldap
Summary: ActiveLdap plugin for Ruby on Rails
Group: Development/Ruby
Requires: %name = %version-%release
Provides: rails-plugin-active_ldap = %version-%release
Obsoletes: rails-plugin-active_ldap
PreReq: ruby-railties >= 2.1.0-alt2

%description -n rails-plugin-activeldap
ActiveLdap plugin for Ruby on Rails.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -q
%patch -p1
%update_setup_rb

rm -f lib/active_ldap/adapter/net_ldap*
rm -f lib/active_ldap/adapter/jndi*

%build
%ruby_config
%ruby_build
# Needs running LDAP server
#ruby test/run-test.rb

%install
%ruby_install
%rdoc lib/

mkdir -p %buildroot%_datadir/rails/plugins/activeldap
cp -dpR rails/* rails_generators/ %buildroot%_datadir/rails/plugins/activeldap

%find_lang active-ldap

%files -f active-ldap.lang
%doc CHANGES COPYING README TODO
%ruby_sitelibdir/active_ldap*
# HAK HAK HAK to make al-admin work
%exclude %ruby_sitelibdir/active_ldap/get_text/parser.rb

%files -n rails-plugin-activeldap
%_datadir/rails/plugins/activeldap

%files doc
%doc examples
%ruby_sitelibdir/active_ldap/get_text/parser.rb
%ruby_ri_sitedir/ActiveLdap

%changelog
* Thu Jul 15 2010 Alexey I. Froloff <raorn@altlinux.org> 1.2.2-alt1
- [1.2.2]

* Wed Jul 01 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.9-alt1
- [1.0.9]
- Rails plugin renamed to "activeldap"

* Wed Aug 13 2008 Sir Raorn <raorn@altlinux.ru> 1.0.1-alt1
- [1.0.1]
- RI documentation and examples moved do -doc subpackage
- Packaged Ruby on Rails plugin

* Tue Jul 11 2006 Sir Raorn <raorn@altlinux.ru> 0.7.4-alt1
- [0.7.4]
- Removed patches:
 + alt-search-scope (search scope now configurable, defaults
   to LDAP_SCOPE_ONELEVEL)

* Mon Feb 21 2005 Sir Raorn <raorn@altlinux.ru> 0.5.5-alt1
- [0.5.5]
- Document LDAP::Schema2 extension (prereq'd ruby-ldap)
- URL changed to rubyforge project page
- Set packager to ruby@packages.a.o

* Tue Jan 25 2005 Sir Raorn <raorn@altlinux.ru> 0.5.3-alt1
- [0.5.3]

* Wed Sep 15 2004 Sir Raorn <raorn@altlinux.ru> 0.1.4-alt2
- Fix search scope

* Sat Sep 11 2004 Sir Raorn <raorn@altlinux.ru> 0.1.4-alt1.1
- Rebuilt with new ruby

* Sun Sep 05 2004 Sir Raorn <raorn@altlinux.ru> 0.1.4-alt1
- Built for Sisyphus

