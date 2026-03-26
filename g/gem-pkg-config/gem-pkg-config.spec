%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname pkg-config

Name:          gem-pkg-config
Version:       1.6.5
Release:       alt1
Summary:       pkg-config implemented by pure Ruby
License:       LGPLv2+
Group:         Development/Ruby
Url:           https://github.com/ruby-gnome2/pkg-config
Vcs:           https://github.com/ruby-gnome2/pkg-config.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-pkg-config < %EVR
Provides:      ruby-pkg-config = %EVR
Provides:      gem(pkg-config) = 1.6.5

%description
pkg-config can be used in your extconf.rb to properly detect need libraries for
compiling Ruby native extensions


%if_enabled    doc
%package       -n gem-pkg-config-doc
Version:       1.6.5
Release:       alt1
Summary:       pkg-config implemented by pure Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pkg-config
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(pkg-config) = 1.6.5

%description   -n gem-pkg-config-doc
pkg-config implemented by pure Ruby documentation files.

pkg-config can be used in your extconf.rb to properly detect need libraries for
compiling Ruby native extensions

%description   -n gem-pkg-config-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pkg-config.
%endif


%if_enabled    devel
%package       -n gem-pkg-config-devel
Version:       1.6.5
Release:       alt1
Summary:       pkg-config implemented by pure Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pkg-config
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(pkg-config) = 1.6.5
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-pkg-config-devel
pkg-config implemented by pure Ruby development package.

pkg-config can be used in your extconf.rb to properly detect need libraries for
compiling Ruby native extensions

%description   -n gem-pkg-config-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pkg-config.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-pkg-config-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-pkg-config-devel
%doc README.rdoc
%endif


%changelog
* Wed Mar 25 2026 Pavel Skrylev <majioa@altlinux.org> 1.6.5-alt1
- ^ 1.4.1 -> 1.6.5

* Sat Jun 13 2020 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- ^ 1.3.7 -> 1.4.1

* Tue Mar 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.7-alt1
- ^ 1.3.3 -> 1.3.7

* Fri Feb 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.3-alt1
- > Ruby Policy 2.0
- ^ 1.3.1 -> 1.3.3

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Sat Apr 28 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- New version.

* Tue Apr 10 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version.

* Mon Jan 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.9-alt1
- New version.

* Thu Oct 19 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.8-alt1
- New version

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1
- New version

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.6-alt1
- New version

* Mon Aug 07 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1
- New version

* Tue May 30 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.3-alt1
- New version

* Mon May 29 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1
- New version

* Tue Apr 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version

* Fri Apr 21 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.9-alt1
- New version

* Thu Apr 20 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.8-alt1
- New version

* Mon Sep 26 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.7-alt1
- New version

* Tue Dec 04 2012 Led <led@altlinux.ru> 1.0.7-alt3.1
- Rebuilt with ruby-1.9.3-alt1

* Thu Nov 10 2011 Timur Aitov <timonbl4@altlinux.org> 1.0.7-alt3
- Repair build

* Fri Apr 29 2011 Timur Aitov <timonbl4@altlinux.org> 1.0.7-alt2
- Repair build

* Sun Jan 09 2011 Alexey I. Froloff <raorn@altlinux.org> 1.0.7-alt1
- Built for Sisyphus
