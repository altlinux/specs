# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%define        gemname yard-sitemap

Name:          gem-yard-sitemap
Version:       1.0.1
Release:       alt1.3
Summary:       A YARD plugin to build a sitemap.xml for generated HTML documentation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lsegal/yard-sitemap
Vcs:           https://github.com/lsegal/yard-sitemap.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(yard-sitemap) = 1.0.1


%description
A YARD plugin to build a sitemap.xml for generated HTML documentation.


%package       -n gem-yard-sitemap-doc
Version:       1.0.1
Release:       alt1.3
Summary:       A YARD plugin to build a sitemap.xml for generated HTML documentation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета yard-sitemap
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(yard-sitemap) = 1.0.1

%description   -n gem-yard-sitemap-doc
A YARD plugin to build a sitemap.xml for generated HTML documentation
documentation files.

%description   -n gem-yard-sitemap-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета yard-sitemap.


%package       -n gem-yard-sitemap-devel
Version:       1.0.1
Release:       alt1.3
Summary:       A YARD plugin to build a sitemap.xml for generated HTML documentation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета yard-sitemap
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(yard-sitemap) = 1.0.1

%description   -n gem-yard-sitemap-devel
A YARD plugin to build a sitemap.xml for generated HTML documentation
development package.

%description   -n gem-yard-sitemap-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета yard-sitemap.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-yard-sitemap-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-yard-sitemap-devel
%doc README.md


%changelog
* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1.3
- ! spec

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1.2
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1.1
- fixed (!) spec according to changelog rules

* Fri Aug 02 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- added (+) packaged gem with the Ruby Policy 2.0 usage
