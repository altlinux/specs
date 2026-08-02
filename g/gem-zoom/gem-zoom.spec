%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    devel
%define        gemname zoom

Name:          gem-zoom
Version:       0.5.0.2
Release:       alt0.1
Summary:       Ruby binding to the Z39.50 Object-Orientation Model (ZOOM)
License:       LGPLv2.1
Group:         Development/Ruby
Url:           https://github.com/bricestacey/ruby-zoom
Vcs:           https://github.com/bricestacey/ruby-zoom.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake libruby-devel
BuildRequires: libyaz-devel
BuildRequires: zlib-devel
BuildRequires: libgcrypt-devel
BuildRequires: libstemmer-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-zoom < %EVR
Provides:      ruby-zoom = %EVR
Provides:      gem(zoom) = 0.5.0.2

%ruby_use_gem_version zoom:%version

%description
Ruby/ZOOM provides a Ruby binding to the Z39.50 Object-Orientation Model (ZOOM),
an abstract object-oriented programming interface to a subset of the services
specified by the Z39.50 standard, also known as the international standard ISO
23950.

This software is based (and therefore depends) on YAZ, a free-software
implementation of the Z39.50/SRW/SRU standards, but could be easily ported to
any ZOOM compliant implementation.


%if_enabled    devel
%package       -n gem-zoom-devel
Version:       0.5.0.2
Release:       alt0.1
Summary:       Ruby binding to the Z39.50 Object-Orientation Model (ZOOM) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета zoom
Group:         Development/Ruby
BuildArch:     noarch

Requires:      libyaz-devel
Requires:      zlib-devel
Requires:      libgcrypt-devel
Requires:      gem(zoom) = 0.5.0.2

%description   -n gem-zoom-devel
Ruby binding to the Z39.50 Object-Orientation Model (ZOOM) development
package.

Ruby/ZOOM provides a Ruby binding to the Z39.50 Object-Orientation Model (ZOOM),
an abstract object-oriented programming interface to a subset of the services
specified by the Z39.50 standard, also known as the international standard ISO
23950.

This software is based (and therefore depends) on YAZ, a free-software
implementation of the Z39.50/SRW/SRU standards, but could be easily ported to
any ZOOM compliant implementation.

%description   -n gem-zoom-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета zoom.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc ChangeLog README.md LICENSE
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    devel
%files         -n gem-zoom-devel
%doc ChangeLog README.md LICENSE
%ruby_includedir/*
%endif


%changelog
* Sat Aug 01 2026 Pavel Skrylev <majioa@altlinux.org> 0.5.0.2-alt0.1
- ^ 0.5.0 -> 0.5.0p2

* Mon Oct 11 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt3.2
- ! spec

* Wed Apr 15 2020 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt3.1
- + proper buildarch for devel package

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt3
- ! spec tags

* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt2
- Fix build

* Thu Feb 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- Bump to 0.5;
- Use Ruby Policy 2.0.

* Fri Apr 29 2011 Timur Aitov <timonbl4@altlinux.org> 0.4.1-alt3
- Repair build

* Sun Sep 26 2010 Alexey I. Froloff <raorn@altlinux.org> 0.4.1-alt2
- Rebuilt with Ruby 1.9.2

* Sun May 10 2009 Alexey I. Froloff <raorn@altlinux.org> 0.4.1-alt1
- Built for Sisyphus
