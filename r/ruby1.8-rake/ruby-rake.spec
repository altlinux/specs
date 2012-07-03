%define ruby_major 1.8

Name: ruby%{ruby_major}-rake
Version: 0.8.7
Release: alt4
Summary: Ruby based make-like utility
License: MIT
Group: Development/Ruby
Url: http://rake.rubyforge.org

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: rake-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires: ruby%{ruby_major}-stdlibs rpm-build-ruby ruby%{ruby_major}-tool-rdoc ruby-tool-setup ruby%{ruby_major}-flexmock

%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies
are specified in standard Ruby syntax.

%package doc
Summary: Documentation files for rake
Group: Documentation

%description doc
Documentation files for rake

%prep
%setup -n rake-%version
%patch -p1
%update_setup_rb
rm -f rakelib/tags.rake

%build
%ruby_config
%ruby_build
%ruby_vendor -Ilib bin/rake test:all
rdoc --op html -T kilmer -t "Rake -- Ruby Make" --include install.rb MIT-LICENSE TODO CHANGES lib doc/* doc/*/* --line-numbers --inline-source --main README

%install
%ruby_install
mkdir -p %buildroot/%_man1dir
install -p -m 644 doc/rake.1.gz %buildroot/%_man1dir

# Rubygems?  We don't need no stinkin' rubygems!
%add_findreq_skiplist %ruby_sitelibdir/rake/gempackagetask.rb

%files
%_bindir/*
%ruby_sitelibdir/*
%_man1dir/*

%files doc
%doc html

%changelog
* Tue Apr 12 2011 Timur Aitov <timonbl4@altlinux.org> 0.8.7-alt4
- Rebuild for ruby1.8

* Tue Mar 22 2011 Andriy Stepanov <stanv@altlinux.ru> 0.8.7-alt3
- Rebuild with new ruby.

* Tue Jan 04 2011 Alexey I. Froloff <raorn@altlinux.org> 0.8.7-alt2
- Updated to rake-0.8.7-134-g9dad179

* Thu Jul 15 2010 Alexey I. Froloff <raorn@altlinux.org> 0.8.7-alt1
- [0.8.7]

* Wed May 06 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.4-alt1
- [0.8.4]

* Sun Mar 30 2008 Sir Raorn <raorn@altlinux.ru> 0.8.1-alt1
- [0.8.1]

* Thu Jan 24 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.7.3-alt2
- Add ruby-module-misc to requires

* Tue May 22 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.7.3-alt1
- 0.7.3 

* Thu Jul 06 2006 Sir Raorn <raorn@altlinux.ru> 0.7.1-alt1
- [0.7.1]

* Tue Mar 07 2006 Kirill A. Shutemov <kas@altlinux.ru> 0.7.0-alt2
- header in /usr/bin/rake fixed [#9195]

* Thu Feb 16 2006 Kirill A. Shutemov <kas@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Wed Aug 31 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.5.4-alt1
- Initial build for ALT Linux

