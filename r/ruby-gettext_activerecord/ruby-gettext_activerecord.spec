# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname gettext_activerecord

Name: ruby-%pkgname
Version: 2.1.0
Release: alt1

Summary: Localization support for ActiveRecord by Ruby-GetText-Package
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/gettext/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Wed Oct 14 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-activerecord-sqlite3-adapter ruby-builder ruby-gettext-utils ruby-tool-setup

%description
gettext_activerecord provides the localization for ActiveRecord-2.2 or
later using Ruby-GetText-Package.

%package tools
Summary: Developer modules for %name
Group: Development/Ruby
Requires: %name = %version-%release

%description tools
Developer modules for %name.

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_vendor -rgettext/tools -e GetText.create_mofiles
pushd test
%ruby_vendor -I../lib -ractive_record -rgettext_activerecord/tools -e 'GetText.create_mofiles(:mo_root => "locale")'
find . -name 'test_*.rb' -print0 |
	xargs -r0 -n 1 %ruby_test_unit -I../lib
popd

%install
%ruby_install

%find_lang %pkgname

%files -f %pkgname.lang
%doc README.rdoc
%ruby_sitelibdir/*
%exclude %ruby_sitelibdir/gettext_activerecord/parser.rb
%exclude %ruby_sitelibdir/gettext_activerecord/tools.rb

%files tools
%doc sample
%ruby_sitelibdir/gettext_activerecord/parser.rb
%ruby_sitelibdir/gettext_activerecord/tools.rb

%changelog
* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 2.1.0-alt1
- [2.1.0]

* Wed Oct 14 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.4-alt1
- Built for Sisyphus

