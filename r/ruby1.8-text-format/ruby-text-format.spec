%define ruby_major 1.8
%define pkgname text-format

Name: ruby%{ruby_major}-%pkgname
Version: 1.0.0
Release: alt4
Summary: Text::Format formats fixed-width text nicely.
License: Ruby
Group: Development/Ruby
Url: http://rubyforge.org/projects/text-format/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 02 2008 (-bi)
BuildRequires: ruby%{ruby_major} rpm-build-ruby ruby%{ruby_major}-stdlibs ruby%{ruby_major}-tool-rdoc ruby-tool-setup

%description
Text::Format is provides the ability to nicely format fixed-width text with
knowledge of the writeable space (number of columns), margins, and indentation
settings.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb
rm -f pre-setup.rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib tests/tc_*.rb

%install
%ruby_install
%rdoc lib/

%files
%doc Changelog README ToDo
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/Text*

%changelog
* Thu Apr 28 2011 Timur Aitov <timonbl4@altlinux.org> 1.0.0-alt4
- Rebuild for ruby1.8

* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.0-alt3
- Rebuilt with Ruby 1.9

* Wed Apr 02 2008 Sir Raorn <raorn@altlinux.ru> 1.0.0-alt2
- Rebuilt with rpm-build-ruby

* Tue Jan 08 2008 Sir Raorn <raorn@altlinux.ru> 1.0.0-alt1
- Initial build for ALT Linux

