%define fname bdb

Name: ruby-%fname
Version: 0.6.5
Release: alt3

Summary: Ruby interface to Berkeley DB
Group: Development/Ruby
License: GPL
Url: http://moulon.inra.fr/ruby/bdb.html

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %fname-%version.tar
Patch: %fname-%version-%release.patch

# Automatically added by buildreq on Sat Sep 13 2008 (-bi)
BuildRequires: libdb4-devel libruby-devel ruby-module-etc ruby-module-test-unit

%description
Ruby interface to Berkeley DB, distributed by Sleepycat.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %fname-%version
%patch -p1

%build
%ruby_configure
%make_build
#for t in tests/*.rb; do
#ruby tests/*.rb
#done

%install
%make_install DESTDIR=%buildroot install
%rdoc docs/*rb

%files
%doc Changes README.en
%ruby_sitearchdir/*

%files doc
%doc examples
%ruby_ri_sitedir/BDB*

%changelog
* Mon Nov 29 2010 Alexey I. Froloff <raorn@altlinux.org> 0.6.5-alt3
- Fix build woth Ruby 1.9.2

* Tue Jun 30 2009 Alexey I. Froloff <raorn@altlinux.org> 0.6.5-alt2
- Rebuilt with Ruby 1.9

* Sat Sep 13 2008 Sir Raorn <raorn@altlinux.ru> 0.6.5-alt1
- [0.6.5]
- Built with db4.7

* Sat Mar 29 2008 Sir Raorn <raorn@altlinux.ru> 0.6.2-alt1
- Package takeover by Team RUBY
- [0.6.2]
- Dropped summary/description translations
- Packages RI documentation and examples

* Wed Sep 27 2006 Michael Shigorin <mike@altlinux.org> 0.5.9-alt1
- 0.5.9
- package takeover
- uk_UA summary/description (yeah, I know specspo would be better)

* Sat Mar 25 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.5.8-alt0.1.1
- Rebuilt with libdb4.4.

* Sun Jan 08 2006 Michael Shigorin <mike@altlinux.org> 0.5.8-alt0.1
- NMU: 0.5.8
- updated BuildRequires (libdb4.2-devel no more)

* Mon Feb 16 2004 Alexander Bokovoy <ab@altlinux.ru> 0.5.0-alt1
- 0.5.0
- Rebuild against libdb4.2 and Ruby 1.8.1

* Sun Jul 06 2003 Alexander Bokovoy <ab@altlinux.ru> 0.4.4-alt2
- Rebuild with Ruby 1.8-alt3

* Sun Jun 29 2003 Alexander Bokovoy <ab@altlinux.ru> 0.4.4-alt1
- 0.4.4
- Rebuild with Ruby 1.8-alt1

* Fri Jan 17 2003 Rider <rider@altlinux.ru> 0.3.8-alt1
- first build for ALT Linux

