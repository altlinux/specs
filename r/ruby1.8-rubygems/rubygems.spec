# vim: set ft=spec: -*- rpm-spec -*-

%define ruby_major 1.8

Name: ruby%{ruby_major}-rubygems
Version: 1.6.2
Release: alt1

Summary: A package management framework for the Ruby programming language
License: Ruby's
Group: Development/Ruby
Url: http://www.rubygems.org/

BuildArch: noarch

# By ruby(fileutils) and brain-damaged exception handling
Requires: ruby%{ruby_major}(etc)

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

# Automatically added by buildreq on Fri Feb 06 2009 (-bi)
BuildRequires: ruby%{ruby_major}-stdlibs rpm-build-ruby libruby%{ruby_major}-devel ruby%{ruby_major}-builder ruby%{ruby_major}-minitest ruby%{ruby_major}-rake

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
RubyGems is a package management framework for the Ruby programming language.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%set_ruby_req_method relaxed
%setup
%patch -p1
# Useless crap
rm -f lib/gauntlet_rubygems.rb

%build
for i in test/rubygems/test*.rb; do
  ruby -I%_builddir/%name-%version/lib:%_builddir/%name-%version/test "$i"	# (?) include path must begin with '/'
done

%install
ruby setup.rb --destdir=%buildroot --no-rdoc --no-ri --vendor
%rdoc lib/

%files
%ruby_sitelibdir/*
%_bindir/*

%files doc
%ruby_ri_sitedir/Gem*

%changelog
* Wed Apr 13 2011 Timur Aitov <timonbl4@altlinux.org> 1.6.2-alt1
- Build rubygems 1.6.2 for ruby1.8

* Wed Aug 04 2010 Alexey I. Froloff <raorn@altlinux.org> 1.3.7-alt1
- [1.3.7]

* Sun Feb 14 2010 Alexey I. Froloff <raorn@altlinux.org> 1.3.5-alt1
- [1.3.5]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 1.3.4-alt1
- [1.3.4]

* Sat May 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1.3.3-alt1
- [1.3.3]

* Fri Feb 06 2009 Sir Raorn <raorn@altlinux.ru> 1.3.1-alt1
- [1.3.1]

* Tue Sep 09 2008 Sir Raorn <raorn@altlinux.ru> 1.2.0-alt1
- [1.2.0]
- Fix error message when loading rubygems in vendor-specific mode

* Sun Mar 30 2008 Sir Raorn <raorn@altlinux.ru> 1.1.0-alt1
- [1.1.0]
- Prohibit rubygems usage if running in vendor-specific mode

* Wed Jan 16 2008 Sir Raorn <raorn@altlinux.ru> 1.0.1-alt1
- [1.0.1]
- All gems are moved to /usr/local/lib/ruby/gems/RUBY_VERSION,
  /usr/local/share and /usr/local/bin, please reinstall all
  installed gems
- Packaged RI documentation

* Fri Jan 12 2007 Sir Raorn <raorn@altlinux.ru> 0.9.0-alt1
- 0.9.0
- Do not package rpm macros
- Packaged gems directory structure and "sources" gem

* Tue Aug 30 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.8.11-alt1
- 0.8.11
- New wrapping of build system for ALT in rpm macro
- Removed obsolete patches

* Wed Jul 07 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.6.1-alt2
- Patch to add --prefix option (Kirill A. Shutemov)
- Add rpm macros

* Wed Jun 02 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.6.1-alt1
- First build for ALT Project 

