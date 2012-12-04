# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname uuidtools

Name: ruby-%pkgname
Version: 2.1.0
Release: alt1.1

Summary: A simple universally unique ID generation library
Group: Development/Ruby
License: MIT/Ruby
Url: http://github.com/sporkmonger/uuidtools

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Mon Apr 26 2010 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
UUIDTools was designed to be a simple library for generating any
of the various types of UUIDs.  It conforms to RFC 4122 whenever
possible.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%doc README
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/UUIDTools*

%changelog
* Tue Dec 04 2012 Led <led@altlinux.ru> 2.1.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Apr 26 2010 Alexey I. Froloff <raorn@altlinux.org> 2.1.0-alt1
- Built for Sisyphus

