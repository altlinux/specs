%define        gemname cairo

Name:          gem-cairo
Version:       1.17.8
Release:       alt1.2
Summary:       ruby bindings for cairo
License:       Ruby or GPL-2.0-or-later
Group:         Development/Ruby
Url:           https://rcairo.github.io/
Vcs:           https://github.com/rcairo/rcairo.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libcairo-devel
BuildRequires: glib2-devel
BuildRequires: libpixman-devel
BuildRequires: xorg-glproto-devel
BuildRequires: xorg-dri2proto-devel
BuildRequires: libXau-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXext-devel
BuildRequires: libXdamage-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libpcre-devel
BuildRequires: libuuid-devel
BuildRequires: libffi-devel
BuildRequires: bzlib-devel
BuildRequires: libossp-uuid-dce-devel
BuildRequires: libdrm-devel
BuildRequires: libbrotli-devel
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(xshmfence)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: gem(native-package-installer) >= 1.0.3
BuildRequires: gem(pkg-config) >= 1.2.2
BuildRequires: gem(red-colors) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(packnga) >= 0
BuildRequires: gem(poppler) >= 3.1.1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(native-package-installer) >= 1.0.3
Requires:      gem(pkg-config) >= 1.2.2
Requires:      gem(red-colors) >= 0
Obsoletes:     ruby-rcairo < 1.7.0
Provides:      ruby-rcairo = 1.17.8
Provides:      gem(cairo) = 1.17.8


%description
Ruby bindings for cairo // cairo extension for Ruby.


%package       -n gem-cairo-doc
Version:       1.17.8
Release:       alt1
Summary:       ruby bindings for cairo documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cairo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(cairo) = 1.17.8

%description   -n gem-cairo-doc
ruby bindings for cairo documentation files.

Ruby bindings for cairo // cairo extension for Ruby.

%description   -n gem-cairo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cairo.


%package       -n gem-cairo-devel
Version:       1.17.8
Release:       alt1
Summary:       ruby bindings for cairo development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cairo
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cairo) = 1.17.8
Requires:      gem(bundler) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(packnga) >= 0
Requires:      gem(poppler) >= 3.1.1
Requires:      libcairo-devel
Requires:      glib2-devel
Requires:      libpixman-devel
Requires:      xorg-glproto-devel
Requires:      xorg-dri2proto-devel
Requires:      libXau-devel
Requires:      libXdmcp-devel
Requires:      libXext-devel
Requires:      libXdamage-devel
Requires:      libXxf86vm-devel
Requires:      libpcre-devel
Requires:      libuuid-devel
Requires:      libffi-devel
Requires:      bzlib-devel
Requires:      libossp-uuid-dce-devel
Requires:      libdrm-devel
Requires:      pkgconfig(expat)
Requires:      pkgconfig(harfbuzz)
Requires:      pkgconfig(xshmfence)
Requires:      pkgconfig(libpcre2-8)
Obsoletes:     rcairo-devel < 1.7.0
Provides:      rcairo-devel = 1.17.8


%description   -n gem-cairo-devel
ruby bindings for cairo development package.

Ruby bindings for cairo // cairo extension for Ruby.

%description   -n gem-cairo-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cairo.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-cairo-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-cairo-devel
%doc README.rdoc
%ruby_gemincludedir/*


%changelog
* Thu Dec 22 2022 Valery Inozemtsev <shrek@altlinux.ru> 1.17.8-alt1.2
- rebuild with gem(poppler)

* Thu Dec 22 2022 Valery Inozemtsev <shrek@altlinux.ru> 1.17.8-alt1.1
- rebuild without gem(poppler)

* Mon Sep 26 2022 Pavel Skrylev <majioa@altlinux.org> 1.17.8-alt1
- ^ 1.17.5 -> 1.17.8

* Tue Jun 28 2022 Pavel Skrylev <majioa@altlinux.org> 1.17.5-alt1.1
- !dep to gem poppler

* Sat Apr 24 2021 Pavel Skrylev <majioa@altlinux.org> 1.17.5-alt1
- ^ 1.16.5 -> 1.17.5

* Tue May 26 2020 Pavel Skrylev <majioa@altlinux.org> 1.16.5-alt1.1
- + lost build require dep to "libbrotli-devel"

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 1.16.5-alt1
- ^ 1.16.4 -> 1.16.5
- ! spec tags and syntax

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 1.16.4-alt1.1
- ! spec

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 1.16.4-alt1
- ^ 1.16.2 -> 1.16.4

* Tue Mar 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.16.2-alt3
- ! require devel lib on build

* Tue Mar 05 2019 Pavel Skrylev <majioa@altlinux.org> 1.16.2-alt2
- > Ruby Policy 2.0

* Sat Jan 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.16.2-alt1
- 1.10 -> 1.16.2
- * placement library files into gem folder

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
