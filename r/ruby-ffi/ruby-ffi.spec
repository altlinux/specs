# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname ffi

Name: ruby-%pkgname
Version: 0.6.3
Release: alt1

Summary: Ruby foreign function interface
Group: Development/Ruby
License: BSD
Url: http://rubyforge.org/projects/ffi/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Sun Jun 28 2009 (-bi)
BuildRequires: libffi-devel libruby-devel ruby-tool-setup

%description
A Ruby foreign function interface.

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
%doc README.rdoc
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%files doc
%ruby_ri_sitedir/FFI*

%changelog
* Fri Aug 13 2010 Kirill A. Shutemov <kas@altlinux.org> 0.6.3-alt1
- 0.6.3
- Rebuild with new libffi

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.3.5-alt1
- Built for Sisyphus

