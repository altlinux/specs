# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname ruby-gpgme

Name: %pkgname
Version: 1.0.6
Release: alt1

Summary: Ruby interface to GnuPG Made Easy
Group: Development/Ruby
License: LGPLv2.1+
Url: http://rubyforge.org/projects/ruby-gpgme/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Sat Dec 27 2008 (-bi)
BuildRequires: libgpgme-devel libruby-devel

%description
Ruby interface to GnuPG Made Easy (GPGME).

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1

%build
%ruby_configure
%make_build

%install
%makeinstall_std
%rdoc *.c lib/

%files
%doc README
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%files doc
%doc examples
%ruby_ri_sitedir/GPGME*

%changelog
* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.6-alt1
- [1.0.6]
- License changed to LGPLv2.1+

* Sat Dec 27 2008 Sir Raorn <raorn@altlinux.ru> 1.0.1-alt1
- [1.0.1]

* Tue Aug 31 2004 Sir Raorn <raorn@altlinux.ru> 0.2-alt1
- Built for Sisyphus

