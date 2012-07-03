# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname gettext_rails

Name: ruby-%pkgname
Version: 2.1.0
Release: alt2

Summary: Localization support for Ruby on Rails(>=2.3) by Ruby-GetText-Package
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/gettext/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Thu Oct 15 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-activerecord-sqlite3-adapter ruby-gettext_activerecord-tools ruby-locale_rails ruby-rails ruby-tool-setup

%description
gettext_rails provides the localization for Ruby on Rails-2.3 or later
using Ruby-GetText-Package.

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
cp %_datadir/rails/environments/boot.rb test/config/boot.rb

%build
%ruby_config
%ruby_build
%ruby_vendor -rgettext/tools -e GetText.create_mofiles
pushd test
unset LC_ALL LC_CTYPE LC_NUMERIC LC_TIME LC_COLLATE LC_MESSAGES
export LANG=en_US.UTF-8
%rake makemo
%rake test
popd

%install
%ruby_install

%find_lang %pkgname

%files -f %pkgname.lang
%doc README.rdoc
%ruby_sitelibdir/*
%exclude %ruby_sitelibdir/gettext_rails/tools.rb

%files tools
%doc sample
%ruby_sitelibdir/gettext_rails/tools.rb

%changelog
* Sun Jun 06 2010 Alexey I. Froloff <raorn@altlinux.org> 2.1.0-alt2
- Run tests in en_US.UTF-8 locale

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 2.1.0-alt1
- [2.1.0]

* Thu Oct 15 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.4-alt1
- Built for Sisyphus

