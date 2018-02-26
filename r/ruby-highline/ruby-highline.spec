# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname highline

Name: ruby-%pkgname
Version: 1.5.1
Release: alt2

Summary: HighLine is a high-level command-line IO library
Group: Development/Ruby
License: GPLv2 or Ruby
Url: http://highline.rubyforge.org/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source0: %pkgname-%version.tgz

# Automatically added by buildreq on Sat Dec 12 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
A high-level IO library that provides validation, type conversion, and more for
command-line interfaces. HighLine also includes a complete menu system that can
crank out anything from simple list selection to complete shells with just
minutes of work.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%doc CHANGELOG INSTALL LICENSE README TODO
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/HighLine

%changelog
* Mon Jan 04 2010 Igor Zubkov <icesik@altlinux.org> 1.5.1-alt2
- fix Url
- fix License

* Sat Dec 12 2009 Igor Zubkov <icesik@altlinux.org> 1.5.1-alt1
- build for Sisyphus


