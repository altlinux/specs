%define ruby_major 1.8
%define pkgname rails

Name: ruby%{ruby_major}-%pkgname
Version: 2.3.11
Release: alt2
Summary: Web-application framework with template engine, control-flow layer, and ORM.
License: MIT
Group: Development/Ruby
Url: http://www.rubyonrails.org

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: railties-%version.tar
Patch: railties-%version-%release.patch

BuildArch: noarch

Requires: ruby%{ruby_major}-railties = %version-%release
Requires: ruby%{ruby_major}-rake >= 0.7.2

# Indirect dependencies
Requires: ruby%{ruby_major}(rack/handler/webrick) ruby%{ruby_major}-tool-irb

# Automatically added by buildreq on Wed Jul 09 2008 (-bi)
BuildRequires: ruby%{ruby_major} rpm-build-ruby ruby%{ruby_major}-actionmailer ruby%{ruby_major}-i18n ruby%{ruby_major}-mocha ruby%{ruby_major}-fcgi ruby%{ruby_major}-rack-handler-fastcgi

# Do not process eruby templates
%add_findreq_skiplist %ruby_sitelibdir/rails_generator/generators/components/*/templates/*
# It only requires "modules", which belongs to application root
%add_findreq_skiplist %ruby_sitelibdir/console_*.rb
%add_findreq_skiplist %ruby_sitelibdir/commands/about.rb
%add_findreq_skiplist %ruby_sitelibdir/commands/performance/request.rb
# Used only by tasks/gems.rake
%add_findreq_skiplist %ruby_sitelibdir/rails/gem_builder.rb
# Templates
%add_findreq_skiplist %_datadir/%pkgname/configs/*
%add_findreq_skiplist %_datadir/%pkgname/dispatches/*
%add_findreq_skiplist %_datadir/%pkgname/doc/*
%add_findreq_skiplist %_datadir/%pkgname/environments/*
%add_findreq_skiplist %_datadir/%pkgname/helpers/*
%add_findreq_skiplist %_datadir/%pkgname/html/*

%description
Rails is a framework for building web-application using CGI, FCGI,
mod_ruby, or WEBrick on top of either MySQL, PostgreSQL, SQLite, DB2,
SQL Server, or Oracle with eRuby- or Builder-based templates.

This package contains development tools.

%package -n ruby%{ruby_major}-railties
Summary: Gluing the Engine to the Rails
Group: Development/Ruby
Requires: ruby%{ruby_major}-activesupport = %version
Requires: ruby%{ruby_major}-activerecord = %version
Requires: ruby%{ruby_major}-actionpack = %version
Requires: ruby%{ruby_major}-actionmailer = %version
Requires: ruby%{ruby_major}-activeresource = %version

%description -n ruby%{ruby_major}-railties
Rails is a framework for building web-application using CGI, FCGI,
mod_ruby, or WEBrick on top of either MySQL, PostgreSQL, SQLite, DB2,
SQL Server, or Oracle with eRuby- or Builder-based templates.

This package contains railties module.

%prep
%setup -q -n railties-%version
%patch -p1
find . -type f -print0 |
	xargs -r0 sed -i 's,/usr/local/bin/ruby,%_bindir/ruby,' --

%build
# Uses rubygems
rm -f test/gem_dependency_test.rb
# Not compatible with test-unit 2.x
rm -f test/backtrace_cleaner_test.rb
find test -type f -name '*_test.rb' -print0 |
	xargs -r0 -n1 ruby -Ilib:test

%install
mkdir -p %buildroot{%_bindir,%_datadir/%pkgname/plugins,%ruby_sitelibdir}
cp -rp lib/* %buildroot%ruby_sitelibdir
cp -rp bin builtin configs dispatches doc environments helpers html \
	fresh_rakefile README \
	%buildroot%_datadir/%pkgname
install -p -m755 bin/rails %buildroot%_bindir/rails
cat <<EOF > %buildroot%ruby_sitelibdir/railties_path.rb
RAILTIES_PATH = "%_datadir/%pkgname"
EOF
#rdoc lib/

%files
%_bindir/*
%_datadir/%pkgname
%exclude %_datadir/%pkgname/plugins
%ruby_sitelibdir/commands*
%ruby_sitelibdir/tasks*
%ruby_sitelibdir/console_*.rb
%ruby_sitelibdir/*_server.rb
%ruby_sitelibdir/rails_generator*

%files -n ruby%{ruby_major}-railties
%dir %_datadir/%pkgname
%dir %_datadir/%pkgname/plugins
%ruby_sitelibdir/*
%exclude %ruby_sitelibdir/commands*
%exclude %ruby_sitelibdir/tasks*
%exclude %ruby_sitelibdir/console_*.rb
%exclude %ruby_sitelibdir/*_server.rb
%exclude %ruby_sitelibdir/rails_generator*

%changelog
* Thu Apr 28 2011 Timur Aitov <timonbl4@altlinux.org> 2.3.11-alt2
- Rebuild for ruby1.8

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

* Sun Nov 08 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.4-alt2
- config.gem now works with system modules

* Tue Oct 13 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.4-alt1
- [2.3.4-68-g7454d18]
- Do not throw errors if rubygems installed and loaded in the middle of
  initialization process (closes: #2107)

* Sun Jul 26 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.3.1-alt3
- Reworked anti-gems patch again to fix initializer

* Sat Jul 25 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.3.1-alt2
- Fix initializer bailing out when gems disabled

* Fri Jul 24 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.3.1-alt1
- [2.3.3.1]

* Tue Jun 30 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.2.1-alt1
- [2.3.2.1]

* Wed Nov 19 2008 Sir Raorn <raorn@altlinux.ru> 2.2.1-alt1
- [2.2.1]

* Wed Nov 19 2008 Sir Raorn <raorn@altlinux.ru> 2.2.0-alt1
- [2.2.0]

* Tue Sep 09 2008 Sir Raorn <raorn@altlinux.ru> 2.1.1-alt1
- [2.1.1]

* Fri Aug 29 2008 Sir Raorn <raorn@altlinux.ru> 2.1.0-alt3
- Added mongrel (old-style) support

* Sun Jul 13 2008 Sir Raorn <raorn@altlinux.ru> 2.1.0-alt2
- Also load plugins from /usr/share/rails/plugins (init.rb and
  about.yml placeholders)
- Fixed couple of warnings

* Tue Jul 08 2008 Sir Raorn <raorn@altlinux.ru> 2.1.0-alt1
- [2.1.0]
- rails_generator modules moved from railties to rails package

* Wed Apr 02 2008 Sir Raorn <raorn@altlinux.ru> 2.0.2-alt2
- Rebuilt with rpm-build-ruby
- Default database set to sqlite3

* Tue Jan 08 2008 Sir Raorn <raorn@altlinux.ru> 2.0.2-alt1.1
- Fix default database regression

* Tue Jan 08 2008 Sir Raorn <raorn@altlinux.ru> 2.0.2-alt1
- [2.0.2]

* Sun Dec 09 2007 Sir Raorn <raorn@altlinux.ru> 1.2.6-alt1
- [1.2.6]

* Wed May 23 2007 Sir Raorn <raorn@altlinux.ru> 1.2.3-alt1
- [1.2.3]
- Moved ruby modules to ruby-railties package

* Fri Aug 11 2006 Sir Raorn <raorn@altlinux.ru> 1.1.6-alt1
- [1.1.6]

* Tue Jul 11 2006 Sir Raorn <raorn@altlinux.ru> 1.1.4-alt2
- Use builtins form RAILTIES_PATH, not "../..../../"

* Thu Jul 06 2006 Sir Raorn <raorn@altlinux.ru> 1.1.4-alt1
- [1.1.4]

* Wed Mar 15 2006 Sir Raorn <raorn@altlinux.ru> 1.0.0-alt1
- [1.0.1]
- Dropped rubygems

* Wed Aug 31 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.13.1-alt1
- Initial build for ALT Linux

