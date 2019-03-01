%define        pkgname zoom

Name:          ruby-%pkgname
Version:       0.5.0
Release:       alt1
Summary:       Ruby binding to the Z39.50 Object-Orientation Model (ZOOM)
Group:         Development/Ruby
License:       LGPL
Url:           https://github.com/bricestacey/ruby-zoom
# VCS:         https://github.com/bricestacey/ruby-zoom.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:        %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: libyaz-devel ruby-test-unit zlib-devel libgcrypt-devel

%description
Ruby/ZOOM provides a Ruby binding to the Z39.50 Object-Orientation Model
(ZOOM), an abstract object-oriented programming interface to a subset of the
services specified by the Z39.50 standard, also known as the international
standard ISO 23950.

This software is based (and therefore depends) on YAZ, a free-software
implementation of the Z39.50/SRW/SRU standards, but could be easily ported to
any ZOOM compliant implementation.


%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %name


%package       devel
Summary:       Headers for %name
Group:         Development/Ruby
BuildArch:     noarch

%description   devel
%summary.

%prep
%setup -n %pkgname-%version

%build
%gem_build

%install
%gem_install

%files
%ruby_gemspec
%ruby_gemslibdir
%ruby_gemsextdir

%files doc
%ruby_gemsdocdir

%files devel
%ruby_includedir/*

%changelog
* Thu Feb 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- Bump to 0.5;
- Use Ruby Policy 2.0.

* Fri Apr 29 2011 Timur Aitov <timonbl4@altlinux.org> 0.4.1-alt3
- Repair build

* Sun Sep 26 2010 Alexey I. Froloff <raorn@altlinux.org> 0.4.1-alt2
- Rebuilt with Ruby 1.9.2

* Sun May 10 2009 Alexey I. Froloff <raorn@altlinux.org> 0.4.1-alt1
- Built for Sisyphus

