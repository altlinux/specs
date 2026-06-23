%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname jaro_winkler

Name:          gem-jaro-winkler
Version:       1.6.1
Release:       alt1
Summary:       Ruby & C implementation of Jaro-Winkler distance algorithm which supports UTF-8 string
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/tonytonyjan/jaro_winkler
Vcs:           https://github.com/tonytonyjan/jaro_winkler.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake libruby-devel
%if_enabled check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 0
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names jaro_winkler,jaro-winkler
Provides:      jaro_winkler = %EVR
Provides:      gem(jaro_winkler) = 1.6.1

%description
jaro_winkler is an implementation of Jaro-Winkler distance algorithm which is
written in C extension and will fallback to pure Ruby version in platforms other
than MRI/KRI like JRuby or Rubinius. Both of C and Ruby implementation support
any kind of string encoding, such as UTF-8, EUC-JP, Big5, etc.


%if_enabled    doc
%package       -n gem-jaro-winkler-doc
Version:       1.6.1
Release:       alt1
Summary:       Ruby & C implementation of Jaro-Winkler distance algorithm which supports UTF-8 string documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jaro_winkler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jaro_winkler) = 1.6.1

%description   -n gem-jaro-winkler-doc
Ruby & C implementation of Jaro-Winkler distance algorithm which supports UTF-8
string documentation files.

jaro_winkler is an implementation of Jaro-Winkler distance algorithm which is
written in C extension and will fallback to pure Ruby version in platforms other
than MRI/KRI like JRuby or Rubinius. Both of C and Ruby implementation support
any kind of string encoding, such as UTF-8, EUC-JP, Big5, etc.

%description   -n gem-jaro-winkler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jaro_winkler.
%endif


%if_enabled    devel
%package       -n gem-jaro-winkler-devel
Version:       1.6.1
Release:       alt1
Summary:       Ruby & C implementation of Jaro-Winkler distance algorithm which supports UTF-8 string development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jaro_winkler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jaro_winkler) = 1.6.1
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 0
Conflicts:     gem(rake) >= 14

%description   -n gem-jaro-winkler-devel
Ruby & C implementation of Jaro-Winkler distance algorithm which supports UTF-8
string development package.

jaro_winkler is an implementation of Jaro-Winkler distance algorithm which is
written in C extension and will fallback to pure Ruby version in platforms other
than MRI/KRI like JRuby or Rubinius. Both of C and Ruby implementation support
any kind of string encoding, such as UTF-8, EUC-JP, Big5, etc.

%description   -n gem-jaro-winkler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jaro_winkler.
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
%doc LICENSE.txt CHANGELOG.md README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-jaro-winkler-doc
%doc LICENSE.txt CHANGELOG.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-jaro-winkler-devel
%doc LICENSE.txt CHANGELOG.md README.md
%ruby_includedir/*
%endif


%changelog
* Mon Jun 22 2026 Pavel Skrylev <majioa@altlinux.org> 1.6.1-alt1
- ^ 1.5.6 -> 1.6.1

* Thu Jul 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.5.6-alt1
- ^ 1.5.4.1 -> 1.5.6

* Sun May 08 2022 Pavel Skrylev <majioa@altlinux.org> 1.5.4.1-alt1
- ^ 1.5.4 -> 1.5.4.1

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.5.4-alt1
- ^ 1.5.3 -> 1.5.4
- ! spec tags

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.3-alt1.1
- ! spec according to changelog rules

* Mon Jun 24 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.3-alt1
- ^ v1.5.3
- ! spec

* Tue Apr 30 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.2-alt2
- remove noarch from devel package
- cleanup spec

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.2-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
