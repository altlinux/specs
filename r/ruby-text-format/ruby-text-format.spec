%define pkgname text-format

Name: ruby-%pkgname
Version: 1.0.0
Release: alt3.1
Summary: Text::Format formats fixed-width text nicely.
License: Ruby
Group: Development/Ruby
Url: http://rubyforge.org/projects/text-format/

Source: %pkgname-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 02 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

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
* Tue Dec 04 2012 Led <led@altlinux.ru> 1.0.0-alt3.1
- Rebuilt with ruby-1.9.3-alt1

* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.0-alt3
- Rebuilt with Ruby 1.9

* Wed Apr 02 2008 Sir Raorn <raorn@altlinux.ru> 1.0.0-alt2
- Rebuilt with rpm-build-ruby

* Tue Jan 08 2008 Sir Raorn <raorn@altlinux.ru> 1.0.0-alt1
- Initial build for ALT Linux

