# vim: set ft=spec: -*- rpm-spec -*-

Name: ruby-dbus
Version: 0.2.12
Release: alt1

Summary: Ruby D-BUS library
Group: Development/Ruby
License: LGPLv2.1
Url: https://trac.luon.net/ruby-dbus/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %name-%version.tgz

BuildArch: noarch

# Automatically added by buildreq on Sun Mar 14 2010 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
Ruby D-Bus provides an implementation of the D-Bus protocol such that
the D-Bus system can be used in the Ruby programming language.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %name.

%prep
%setup -q
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

%rdoc lib/

%files
%doc ChangeLog NEWS README
%ruby_sitelibdir/dbus*

%files doc
%ruby_ri_sitedir/DBus*

%changelog
* Sun Mar 14 2010 Igor Zubkov <icesik@altlinux.org> 0.2.12-alt1
- 0.2.11 -> 0.2.12

* Sat Dec 19 2009 Igor Zubkov <icesik@altlinux.org> 0.2.11-alt1
- 0.2.10 -> 0.2.11

* Sat Oct 31 2009 Igor Zubkov <icesik@altlinux.org> 0.2.10-alt1
- 0.2.1 -> 0.2.10

* Wed Oct 14 2009 Igor Zubkov <icesik@altlinux.org> 0.2.1-alt2
- update setup.rb

* Sat Aug 08 2009 Igor Zubkov <icesik@altlinux.org> 0.2.1-alt1
- build


