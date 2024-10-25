%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rexical

Name:          gem-rexical
Version:       1.0.8
Release:       alt1
Summary:       Lexical scanner generator for ruby
License:       LGPL-2.1-only
Group:         Development/Ruby
Url:           https://github.com/tenderlove/rexical
Vcs:           https://github.com/tenderlove/rexical.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(getoptlong) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(getoptlong) >= 0
Obsoletes:     ruby-rexical < %EVR
Provides:      ruby-rexical = %EVR
Provides:      gem(rexical) = 1.0.8


%description
Rexical is a lexical scanner generator. It is written in Ruby itself, and
generates Ruby program. It is designed for use with Racc.


%package       -n rexical
Version:       1.0.8
Release:       alt1
Summary:       Lexical scanner generator for ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rexical
Group:         Other
BuildArch:     noarch

Requires:      gem(rexical) = 1.0.8
Conflicts:     rex

%description   -n rexical
Lexical scanner generator for ruby executable(s).

Rexical is a lexical scanner generator. It is written in Ruby itself, and
generates Ruby program. It is designed for use with Racc.

%description   -n rexical -l ru_RU.UTF-8
Исполнямка для самоцвета rexical.


%if_enabled    doc
%package       -n gem-rexical-doc
Version:       1.0.8
Release:       alt1
Summary:       Lexical scanner generator for ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rexical
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rexical) = 1.0.8

%description   -n gem-rexical-doc
Lexical scanner generator for ruby documentation files.

Rexical is a lexical scanner generator. It is written in Ruby itself, and
generates Ruby program. It is designed for use with Racc.

%description   -n gem-rexical-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rexical.
%endif


%if_enabled    devel
%package       -n gem-rexical-devel
Version:       1.0.8
Release:       alt1
Summary:       Lexical scanner generator for ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rexical
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rexical) = 1.0.8
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rubocop) >= 0

%description   -n gem-rexical-devel
Lexical scanner generator for ruby development package.

Rexical is a lexical scanner generator. It is written in Ruby itself, and
generates Ruby program. It is designed for use with Racc.

%description   -n gem-rexical-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rexical.
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
%doc README.ja README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n rexical
%doc README.ja README.rdoc
%_bindir/rex

%if_enabled    doc
%files         -n gem-rexical-doc
%doc README.ja README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rexical-devel
%doc README.ja README.rdoc
%endif


%changelog
* Wed Oct 23 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.8-alt1
- ^ 1.0.7 -> 1.0.8
- * relicensed

* Wed May 27 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt1.3
- ! spec and syntax
- * relicensed

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt1.2
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt1.1
- fixed (!) spec according to changelog rules

* Mon Aug 12 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt1
- updated (^) 1.0.5.gitd8af06b89 -> 1.0.7
- fixed (!) spec
- fixed (!) rename executable rex to rex.rb

* Mon Feb 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt4.gitd8af06b89
- Use Ruby Policy 2.0;
- Use latest git commit.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt3.1
- Rebuild with new Ruby autorequirements.

* Thu Dec 13 2012 Led <led@altlinux.ru> 1.0.5-alt3
- rename %%_bindir/rex -> %%_bindir/rexical for avoid file conflict
  with (R)?ex (rex package)
- fixed BuildRequires

* Fri Nov 30 2012 Led <led@altlinux.ru> 1.0.5-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Thu Mar 24 2011 Andriy Stepanov <stanv@altlinux.ru> 1.0.5-alt2
- Pick off rubygems.

* Thu Mar 24 2011 Andriy Stepanov <stanv@altlinux.ru> 1.0.5-alt1
- [1.0.5]
