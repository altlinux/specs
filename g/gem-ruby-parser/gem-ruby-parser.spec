%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ruby_parser

Name:          gem-ruby-parser
Version:       3.21.1
Release:       alt1
Summary:       ruby_parser (RP) is a ruby parser written in pure ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/ruby_parser
Vcs:           https://github.com/seattlerb/ruby_parser.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: unifdef
BuildRequires: gem(rake) >= 10
BuildRequires: gem(oedipus_lex) >= 2.6
BuildRequires: gem(hoe) >= 0
BuildConflicts: gem(rake) >= 15
BuildConflicts: gem(oedipus_lex) >= 3
%if_enabled check
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(sexp_processor) >= 4.16
BuildRequires: gem(racc) >= 1.5
BuildConflicts: gem(sexp_processor) >= 5
BuildConflicts: gem(racc) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names ruby_parser,ruby-parser
Requires:      gem(sexp_processor) >= 4.16
Requires:      gem(racc) >= 1.5
Conflicts:     gem(sexp_processor) >= 5
Conflicts:     gem(racc) >= 2
Provides:      gem(ruby_parser) = 3.21.1

%ruby_on_build_rake_tasks generate

%description
ruby_parser (RP) is a ruby parser written in pure ruby (utilizing racc-which
does by default use a C extension). RP's output is the same as ParseTree's
output: s-expressions using ruby's arrays and base types.


%package       -n ruby-parser
Version:       3.21.1
Release:       alt1
Summary:       ruby_parser (RP) is a ruby parser written in pure ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ruby_parser
Group:         Other
BuildArch:     noarch

Requires:      gem(ruby_parser) = 3.21.1

%description   -n ruby-parser
ruby_parser (RP) is a ruby parser written in pure ruby
executable(s).

ruby_parser (RP) is a ruby parser written in pure ruby (utilizing racc-which
does by default use a C extension). RP's output is the same as ParseTree's
output: s-expressions using ruby's arrays and base types.

%description   -n ruby-parser -l ru_RU.UTF-8
Исполнямка для самоцвета ruby_parser.


%if_enabled    doc
%package       -n gem-ruby-parser-doc
Version:       3.21.1
Release:       alt1
Summary:       ruby_parser (RP) is a ruby parser written in pure ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby_parser
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby_parser) = 3.21.1

%description   -n gem-ruby-parser-doc
ruby_parser (RP) is a ruby parser written in pure ruby documentation
files.

ruby_parser (RP) is a ruby parser written in pure ruby (utilizing racc-which
does by default use a C extension). RP's output is the same as ParseTree's
output: s-expressions using ruby's arrays and base types.

%description   -n gem-ruby-parser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby_parser.
%endif


%if_enabled    devel
%package       -n gem-ruby-parser-devel
Version:       3.21.1
Release:       alt1
Summary:       ruby_parser (RP) is a ruby parser written in pure ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby_parser
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby_parser) = 3.21.1
Requires:      gem(rdoc) >= 4.0
Requires:      gem(rake) >= 10
Requires:      gem(oedipus_lex) >= 2.6
Requires:      gem(hoe) >= 0
Conflicts:     gem(rake) >= 15
Conflicts:     gem(oedipus_lex) >= 3

%description   -n gem-ruby-parser-devel
ruby_parser (RP) is a ruby parser written in pure ruby development
package.

ruby_parser (RP) is a ruby parser written in pure ruby (utilizing racc-which
does by default use a C extension). RP's output is the same as ParseTree's
output: s-expressions using ruby's arrays and base types.

%description   -n gem-ruby-parser-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby_parser.
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

%files         -n ruby-parser
%doc README.rdoc
%_bindir/ruby_parse
%_bindir/ruby_parse_extract_error

%if_enabled    doc
%files         -n gem-ruby-parser-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ruby-parser-devel
%doc README.rdoc
%endif


%changelog
* Tue Jul 30 2024 Pavel Skrylev <majioa@altlinux.org> 3.21.1-alt1
- ^ 3.21.0 -> 3.21.1

* Tue Jun 04 2024 Pavel Skrylev <majioa@altlinux.org> 3.21.0-alt1
- ^ 3.19.1 -> 3.21.0

* Wed Apr 06 2022 Pavel Skrylev <majioa@altlinux.org> 3.19.1-alt1
- ^ 3.15.0 -> 3.19.1

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 3.15.0-alt1.1
- ! out of compilation error due to spec typo
- + proper build dep to racc executable

* Sun Nov 22 2020 Pavel Skrylev <majioa@altlinux.org> 3.15.0-alt1
- ^ 3.14.2 -> 3.15.0

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 3.14.2-alt0.1
- updated (^) 3.13.1 -> 3.14.2
- fixed (!) spec

* Wed Sep 18 2019 Pavel Skrylev <majioa@altlinux.org> 3.13.1-alt2
- fixed (!) ref to v3.13.1

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.13.1-alt1
- updated (^) 3.13.0 -> 3.13.1
- fixed (!) spec

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 3.13.0-alt1
- added (+) using setup gem's dependency detection
- updated (^) 3.12.0 -> 3.13.0

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 3.12.0-alt1
- updated (^) 3.11.0 -> 3.12.0
- used (>) Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.0-alt1
- Initial build for Sisyphus
