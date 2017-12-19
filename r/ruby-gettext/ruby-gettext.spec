Name:    ruby-gettext
Version: 3.2.6
Release: alt1

Summary: Native Language Support Library for Ruby
Group:   Development/Ruby
License: Ruby or LGPLv3+
Url: http://ruby-gettext.github.io/

BuildArch: noarch

Obsoletes: %name-cgi
Obsoletes: %name-erb
Provides: %name-cgi = %version-%release
Provides: %name-erb = %version-%release

BuildRequires: rpm-build-ruby ruby-locale ruby-racc-runtime ruby-rake ruby-tool-rdoc ruby-tool-setup
BuildRequires: ruby-test-unit

Requires: ruby-text

Source: gettext-%version.tar
Patch1: alt-gemspec.patch

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
%setup
%patch1 -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
# Install gemspec
export rbVersion=`ruby -e "puts RbConfig::CONFIG[\"ruby_version\"]"`
install -Dm 0644 gettext.gemspec %buildroot%ruby_libdir/gems/$rbVersion/specifications/gettext.gemspec
%rdoc lib/

%find_lang rgettext

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,Object/identify_comment-i.ri,cache.ri,created.rid}

# Install additional documentation
install -d %buildroot%_defaultdocdir/%name-doc-%version
cp -a samples ChangeLog* %buildroot%_defaultdocdir/%name-doc-%version

%check
%if %(rpmvercmp %version 2.0) < 0
cd test
%ruby_vendor -I../lib -e 'require "gettext/tools"; GetText.create_mofiles(:mo_root => "locale")'
find . -name 'test_*.rb' -print0 | xargs -r0 -n 1 %ruby_test_unit -I../lib -I./
%endif

%files
%doc README.md
%ruby_sitelibdir/*
%exclude %ruby_sitelibdir/gettext/tools
%exclude %ruby_sitelibdir/gettext/tools.rb
%ruby_libdir/gems/*/specifications/*.gemspec

%files -f rgettext.lang utils
%_bindir/*
%ruby_sitelibdir/gettext/tools
%ruby_sitelibdir/gettext/tools.rb

%files doc
%doc samples ChangeLog*
%ruby_ri_sitedir/GetText*

%changelog
* Tue Dec 19 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.6-alt1
- New version.

* Fri Dec 15 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.5-alt1
- New version.

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.4-alt2
- Rebuild with Ruby 2.4.2

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.4-alt1
- New version

* Sat Jun 24 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- New version

* Fri May 19 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.2-alt1
- New version
- Fix project homepage, license and cleanup spec
- Package as gem

* Fri Mar 14 2014 Led <led@altlinux.ru> 2.1.0-alt2.qa1.2
- fixed build without system iconv module
- remove using deprecated 'all_load_paths'
- disable %%check for ruby >= 2.0
- iconv.rb: set encoding UTF-8

* Sun Dec 09 2012 Led <led@altlinux.ru> 2.1.0-alt2.qa1.1
- Rebuilt with ruby-1.9.3-alt1
- fixed BuildRequires

* Mon Aug 27 2012 Repocop Q. A. Robot <repocop@altlinux.org> 2.1.0-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * backup-file-in-package for ruby-gettext-doc

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
