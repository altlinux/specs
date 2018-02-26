# vim: set ft=spec: -*- rpm-spec -*-

Name: ruby-gettext
Version: 2.1.0
Release: alt2

Summary: Native Language Support Library for Ruby
Group: Development/Ruby
License: LGPL
Url: http://rubyforge.org/projects/gettext/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Obsoletes: %name-cgi
Obsoletes: %name-erb
Provides: %name-cgi = %version-%release
Provides: %name-erb = %version-%release

# Automatically added by buildreq on Wed May 06 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-locale ruby-racc-runtime ruby-rake ruby-tool-rdoc ruby-tool-setup

Source: %name-package-%version.tar
Patch: %name-%version-%release.patch

%description
Ruby GetText Package is Native Language Support Library and Tools
which modeled after GNU gettext package.

Features:
 * Simple APIs(similar GNU gettext)
 * rgettext creates po-files from ruby scripts.
   The po-file is compatible to GNU gettext.
 * rmsgfmt creates a mo-file from a po-file.

%package utils
Summary: GetText utils
Group: Development/Ruby

%description utils
GetText utils

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %name-package-%version
%patch -p1 
%update_setup_rb

%build
%ruby_config
%ruby_build
pushd test
%ruby_vendor -I../lib -e 'require "gettext/tools"; GetText.create_mofiles(:mo_root => "locale")'
find . -name 'test_*.rb' -print0 |
	xargs -r0 -n 1 %ruby_test_unit -I../lib -I./
popd

%install
%ruby_install
%rdoc lib/

%find_lang rgettext

%files
%ruby_sitelibdir/*
%exclude %ruby_sitelibdir/gettext/parser
%exclude %ruby_sitelibdir/gettext/tools
%exclude %ruby_sitelibdir/gettext/tools.rb
%exclude %ruby_sitelibdir/gettext/utils.rb
%doc README.rdoc

%files -f rgettext.lang utils
%_bindir/rgettext
%_bindir/rmsgfmt
%_bindir/rmsgmerge
%ruby_sitelibdir/gettext/parser
%ruby_sitelibdir/gettext/tools
%ruby_sitelibdir/gettext/tools.rb
%ruby_sitelibdir/gettext/utils.rb

%files doc
%doc samples ChangeLog*
%ruby_ri_sitedir/GetText*

%changelog
* Mon Mar 21 2011 Andriy Stepanov <stanv@altlinux.ru> 2.1.0-alt2
- Rebuild with new version.

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 2.1.0-alt1
- [2.1.0]

* Tue Oct 13 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.4-alt1
- [2.0.4]

* Wed May 06 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.1-alt1
- [2.0.1]

* Sun Aug 31 2008 Sir Raorn <raorn@altlinux.ru> 1.92.0-alt2
- Rebuilt wth new rpm-build-ruby

* Wed Aug 13 2008 Sir Raorn <raorn@altlinux.ru> 1.92.0-alt1
- [1.92.0]

* Sun Jul 13 2008 Sir Raorn <raorn@altlinux.ru> 1.91.0-alt1
- [1.91.0]

* Mon Mar 31 2008 Sir Raorn <raorn@altlinux.ru> 1.90.0-alt1
- [1.90.0]
- Package made noarch

* Wed Jan 23 2008 Sir Raorn <raorn@altlinux.ru> 1.10.0-alt3
- Added doc subpackage

* Sun Jan 13 2008 Sir Raorn <raorn@altlinux.ru> 1.10.0-alt2
- Split package to pieces:
 + ruby-gettext - common modules
 + utils - development utilites
 + rails - Ruby on Rails gettext support
 + cgi - CGI gettext support
 + erb - eRuby gettext support
- Removed obsolete be rmsgfmt translation
- Removed 'gettext/iconv', use 'iconv' module
- Removed win32 support

* Wed Aug 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.10.0-alt1
- 1.10.0 source tree.

* Tue May 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.9.0-alt1
- 1.9.0.

* Fri Apr 21 2006 Vital Khilko <vk@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Tue Nov 15 2005 Vital Khilko <vk@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Thu Sep 08 2005 Vital Khilko <vk@altlinux.ru> 0.6.1-alt2
- fixed locale dir

* Tue Sep 28 2004 Vital Khilko <vk@altlinux.ru> 0.5.3-alt3
- fixed locale.rb for new global variable RUBY_PLATFORM

* Mon Sep 27 2004 Vital Khilko <vk@altlinux.ru> 0.5.3-alt2
- rebuilded with new ruby

* Wed Mar 31 2004 Vital Khilko <vk@altlinux.ru> 0.5.3-alt1
- initial build for altlinux sisyphus.
- added belarusian translation
