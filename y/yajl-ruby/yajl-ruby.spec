# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname yajl-ruby

Name: %pkgname
Version: 1.3.0
Release: alt1

Summary: YAJL C Bindings for Ruby
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/yajl-ruby/

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Sun Apr 11 2010 (-bi)
BuildRequires: libruby-devel ruby-tool-setup

%description
This package is a C binding to the excellent YAJL JSON parsing and
generation library.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %name.

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
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%files
%doc README.md CHANGELOG.md
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt2
- Rebuild with Ruby 2.3.1

* Thu Oct 01 2015 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- New version

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.7.5-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.7.5-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 0.7.5-alt1
- Built for Sisyphus
