# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname dbi

Name: ruby-%pkgname
Version: 0.4.1
Release: alt1

Summary: Vendor independent interface for accessing databases, similar to Perl's DBI
Group: Development/Ruby
License: BSD
Url: http://rubyforge.org/projects/ruby-dbi/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Mon Sep 01 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
Ruby/DBI develops a database independent interface for accessing
databases - similar to Perl's DBI.

%package utils
Summary: Interactive DBI shell
Group: Databases
Requires: %name = %version-%release

%description utils
Interactive DBI shell

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

# name Class
%define ruby_dbi_subpackage() \
%package -n ruby-dbd-%1 \
Summary: %2 driver for ruby-dbi \
Group: Development/Ruby \
PreReq: %name = %version-%release \
\
%description -n ruby-dbd-%1 \
%2 driver for Ruby/DBI \
\
%files -n ruby-dbd-%1 \
%ruby_sitelibdir/dbd/%2.rb \
%ruby_sitelibdir/dbd/%1 \
%nil

%ruby_dbi_subpackage mysql Mysql
%ruby_dbi_subpackage odbc ODBC
%ruby_dbi_subpackage pg Pg
%ruby_dbi_subpackage sqlite3 SQLite3

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb
# raise LoadError, "the trace module has been removed until it actually works."
rm -f lib/dbi/trace.rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%doc ChangeLog README TODO
%ruby_sitelibdir/dbi*
%dir %ruby_sitelibdir/dbd

%files utils
%_bindir/dbi

%files doc
%doc doc/*.rdoc examples
%ruby_ri_sitedir/DBI*

%changelog
* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.4.1-alt1
- [0.4.1]
- Dropped old sqlite backend

* Sun Aug 31 2008 Sir Raorn <raorn@altlinux.ru> 0.4.0-alt1
- [0.4.0]
- DBD modules moved to separate packages

* Sat Dec 09 2006 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- 0.1.1
- updated Url:, added Packager: and BuildArch: noarch
- buildreq
- fixed /usr/local hashbang references
- added sqlite support

* Tue Oct 07 2003 Michael Shigorin <mike@altlinux.ru> 0.0.21-alt1
- 0.0.21

* Wed Aug 20 2003 Michael Shigorin <mike@altlinux.ru> 0.0.20-alt1
- 0.0.20
- rebuilt with Ruby 1.8
- added BuildRequires: ruby libruby-devel (thanks ab@!)

* Tue Jan 14 2003 Michael Shigorin <mike@altlinux.ru> 0.0.18-alt0.2
- built for ALT Linux
- somewhat based on debian package libdbi-ruby

