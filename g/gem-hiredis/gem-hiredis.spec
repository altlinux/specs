%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hiredis

Name:          gem-hiredis
Version:       0.6.3.14.1
Release:       alt0.1
Summary:       Ruby wrapper for hiredis
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           http://github.com/redis/hiredis-rb
Vcs:           https://github.com/redis/hiredis-rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake libruby-devel
BuildRequires: pkgconfig(hiredis)
%if_enabled check
BuildRequires: gem(minitest) >= 5.5.1
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0.7.1
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(rake-compiler) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 6.0
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Obsoletes:     ruby-hiredis < %EVR
Provides:      ruby-hiredis = %EVR
Provides:      gem(hiredis) = 0.6.3.14.1

%ruby_use_gem_version hiredis:0.6.3.14.1

%description
Ruby extension that wraps hiredis. Both the synchronous connection API and a
separate protocol reader are supported. It is primarily intended to speed up
parsing multi bulk replies.


%if_enabled    doc
%package       -n gem-hiredis-doc
Version:       0.6.3.14.1
Release:       alt0.1
Summary:       Ruby wrapper for hiredis documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hiredis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hiredis) = 0.6.3.14.1

%description   -n gem-hiredis-doc
Ruby wrapper for hiredis documentation files.

Ruby extension that wraps hiredis. Both the synchronous connection API and a
separate protocol reader are supported. It is primarily intended to speed up
parsing multi bulk replies.

%description   -n gem-hiredis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hiredis.
%endif


%if_enabled    devel
%package       -n gem-hiredis-devel
Version:       0.6.3.14.1
Release:       alt0.1
Summary:       Ruby wrapper for hiredis development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hiredis
Group:         Development/Ruby
BuildArch:     noarch

Requires:      pkgconfig(hiredis)
Requires:      gem(hiredis) = 0.6.3.14.1
Requires:      gem(minitest) >= 5.5.1
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0.7.1
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(rake-compiler) >= 2

%description   -n gem-hiredis-devel
Ruby wrapper for hiredis development package.

Ruby extension that wraps hiredis. Both the synchronous connection API and a
separate protocol reader are supported. It is primarily intended to speed up
parsing multi bulk replies.

%description   -n gem-hiredis-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hiredis.
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
%doc COPYING CHANGELOG.md README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-hiredis-doc
%doc COPYING CHANGELOG.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hiredis-devel
%doc COPYING CHANGELOG.md README.md
%ruby_includedir/*
%endif


%changelog
* Wed Aug 19 2026 Pavel Skrylev <majioa@altlinux.org> 0.6.3.14.1-alt0.1
- ^ 0.6.3[2] -> 0.6.3p14.1

* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.3.2-alt0.1
- ^ 0.6.3[1] -> 0.6.3[2]

* Wed Apr 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.3.1-alt0.1
- ^ 0.6.3 -> 0.6.3[1]

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 0.6.3-alt2
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.3-alt1
- > Ruby Policy 2.0
- > source from github
- ^ 0.6.1 -> 0.6.3

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1.1
- Rebuild with Ruby 2.5.0

* Sat Oct 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus
