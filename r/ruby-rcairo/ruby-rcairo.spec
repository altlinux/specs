# vim: set ft=spec: -*- rpm-spec -*-

%define     pkgname cairo

Name:       ruby-r%pkgname
Version:    1.16.2
Release:    alt1

Summary:    ruby bindings for cairo
Group:      Development/Ruby
License:    GPLv2
Url:        http://cairographics.org/rcairo
# VCS:      https://github.com/rcairo/rcairo.git
Provides:   rcairo = %version-%release
Obsoletes:  rcairo < 1.7.0

Source: %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(native-package-installer) >= 1.0.3 ruby-pkg-config >= 1.2.2 
BuildRequires: libcairo-devel
BuildRequires: glib2-devel libpixman-devel xorg-glproto-devel xorg-dri2proto-devel libXau-devel libXdmcp-devel libXext-devel libXdamage-devel libXxf86vm-devel libpcre-devel libuuid-devel libossp-uuid-dce-devel libdrm-devel
BuildRequires: pkgconfig(expat) pkgconfig(harfbuzz) pkgconfig(xshmfence)

%description
Ruby bindings for cairo // cairo extension for Ruby.

%package devel
Summary: Development files for %name
Group: Development/Ruby
Requires: %name = %version-%release
PreReq: libruby-devel
Obsoletes: rcairo-devel < 1.7.0
Provides: rcairo-devel = %version-%release
# due to #include <cairo.h>
Requires: libcairo-devel

%description devel
Ruby bindings for cairo // cairo extension for Ruby.

This package contains development files.

%package doc
Summary: Documentation for Nokogiri
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation for Nokogiri.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config -- --use-system-libraries
%ruby_build

%install
%ruby_install
%rdoc lib/
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
mkdir -p %buildroot%rubygem_gemdir/%pkgname-%version/lib/ %buildroot%rubygem_extdir/%pkgname-%version/
find %buildroot%ruby_sitelibdir/ -type f -name "*.so" -exec mv {} %buildroot%rubygem_extdir/%pkgname-%version/ \;
touch %buildroot%rubygem_extdir/%pkgname-%version/gem.build_complete
mv %buildroot%ruby_sitelibdir/* %buildroot%rubygem_gemdir/%pkgname-%version/lib/

%files
%doc AUTHORS NEWS README.rdoc
%rubygem_gemdir/*
%rubygem_extdir/*
%rubygem_specdir/*

%files devel
%doc samples
#%_includedir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sat Jan 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.16.2-alt1
- Bump to 1.16.2.
- Place library files into gem folder.

* Thu Mar 13 2014 Led <led@altlinux.ru> 1.10.0-alt4.3
- updated BuildRequires

* Mon Oct 07 2013 Led <led@altlinux.ru> 1.10.0-alt4.2
- fixed BuildRequires

* Tue Dec 04 2012 Led <led@altlinux.ru> 1.10.0-alt4.1
- Rebuilt with ruby-1.9.3-alt1
- updated BuildRequires

* Thu May 17 2012 Michael Shigorin <mike@altlinux.org> 1.10.0-alt4
- fixed FTBFS by updating BR:

* Sat May 14 2011 Dmitry V. Levin <ldv@altlinux.org> 1.10.0-alt3
- ruby-rcairo-devel: Added libcairo-devel to requirements.
- Updated build dependencies.
- Rebuilt with libcairo-1.10.2-alt7.

* Tue May 03 2011 Timur Aitov <timonbl4@altlinux.org> 1.10.0-alt2
- Repair build

* Sun Jan 09 2011 Alexey I. Froloff <raorn@altlinux.org> 1.10.0-alt1
- [1.10.0]

* Thu Jul 15 2010 Alexey I. Froloff <raorn@altlinux.org> 1.8.1-alt1
- [1.8.1]

* Sat May 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1.8.0-alt3
- Rebuild with new ruby

* Fri Dec 12 2008 Kirill A. Shutemov <kas@altlinux.org> 1.8.0-alt2
- Update BuildRequires

* Fri Oct 03 2008 Sir Raorn <raorn@altlinux.ru> 1.8.0-alt1
- [1.8.0]

* Tue Sep 02 2008 Sir Raorn <raorn@altlinux.ru> 1.7.0-alt1
- [1.7.0]
- Package renamed to ruby-rcairo

* Sun Mar 30 2008 Sir Raorn <raorn@altlinux.ru> 1.5.1-alt1
- [1.5.1]

* Thu Jan 25 2007 Sir Raorn <raorn@altlinux.ru> 1.2.0-alt1
- Built for Sisyphus

