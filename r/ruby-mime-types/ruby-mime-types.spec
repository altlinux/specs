# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname mime-types

Name: ruby-%pkgname
Version: 1.18
Release: alt1

Summary: Manages a MIME Content-Type database that will return the Content-Type for a given filename
Group: Development/Ruby
License: Ruby/Perl/GPLv2+
Url: https://github.com/halostatue/mime-types/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source0: %pkgname-%version.tar.gz

# Automatically added by buildreq on Wed Apr 18 2012 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
MIME::Types for Ruby originally based on and synchronized with MIME::Types for
Perl by Mark Overmeer, copy right 2001 - 2009. As of version 1.15, the data
format for the MIME::Type list has changed and the synchronization will no
longer happen.

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

rm -f %buildroot%ruby_ri_sitedir/cache.ri
rm -f %buildroot%ruby_ri_sitedir/created.rid

%files
%doc *.rdoc
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/MIME

%changelog
* Wed Apr 18 2012 Igor Zubkov <icesik@altlinux.org> 1.18-alt1
- 1.16 -> 1.18
- Fix repocop warning

* Sat Dec 12 2009 Igor Zubkov <icesik@altlinux.org> 1.16-alt1
- build for Sisyphus



