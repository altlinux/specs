# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname mongrel

Name: ruby-%pkgname
Version: 1.1.5
Release: alt8

Summary: Simple Fast Mostly Ruby Web Server
Group: Development/Ruby
License: MIT
Url: http://rubyforge.org/projects/mongrel/

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Wed Aug 27 2008 (-bi)
BuildRequires: /proc libruby-devel ruby-daemons ruby-gem_plugin ruby-test-unit ruby-tool-setup ragel

%description
Mongrel is a small library that provides a very fast HTTP 1.1
server for Ruby web applications.  It is not particular to any
framework, and is intended to be just enough to get a web
application running behind a more complete and robust web
server.


%package doc
Summary: Documentation files for %name
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation files for %name.


%prep
%setup -q -n %pkgname-%version
%patch -p1
%update_setup_rb


%build
%ruby_config
## 58 tests, 445 assertions, 3 failures, 0 errors, 0 pendings, 0 omissions, 0 notifications
#pushd ext/http11
#ragel -G2 -o http11_parser.c http11_parser.rl
#popd
%ruby_build


%install
%ruby_install
%rdoc lib/


%check
%ruby_test_unit -Ilib:ext/http11 test


%files
%doc CHANGELOG README TODO
%_bindir/*
%ruby_sitelibdir/*
%ruby_sitearchdir/*


%files doc
%doc examples
%ruby_ri_sitedir/Mongrel*


%changelog
* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt8
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt7
- Rebuild with Ruby 2.3.1

* Wed Mar 19 2014 Led <led@altlinux.ru> 1.1.5-alt6.3
- Rebuilt with ruby-2.0.0-alt1

* Fri Mar 14 2014 Led <led@altlinux.ru> 1.1.5-alt6.2
- fixed Group for doc subpackage
- disabled test_more_web_server and test_deflate for ruby >= 2.0

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.1.5-alt6.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Nov 29 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.5-alt6
- Fix build with Ruby 1.9.2

* Sat Jun 05 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.5-alt5
- Fix cookies processing (once more)

* Sun May 02 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.5-alt4
- Fix cookies processing

* Fri Nov 20 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.5-alt3
- Fixed :prefix setting for new Rails API

* Fri May 15 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.5-alt2
- Rebuilt with Ruby 1.9

* Wed Aug 27 2008 Sir Raorn <raorn@altlinux.ru> 1.1.5-alt1
- Built for Sisyphus
