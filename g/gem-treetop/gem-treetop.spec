%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname treetop

Name:          gem-treetop
Epoch:         1
Version:       1.6.14
Release:       alt1
Summary:       A Ruby-based text parsing and interpretation DSL
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cjheath/treetop
Vcs:           https://github.com/cjheath/treetop.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(activesupport) >= 4
BuildRequires: gem(i18n) >= 1.0
BuildRequires: gem(polyglot) >= 0.3
BuildRequires: gem(rake) >= 11
BuildRequires: gem(rr) >= 3.0
BuildRequires: gem(rspec) >= 3
BuildConflicts: gem(i18n) >= 2
BuildConflicts: gem(polyglot) >= 1
BuildConflicts: gem(rr) >= 4
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(polyglot) >= 0.3
Conflicts:     gem(polyglot) >= 1
Obsoletes:     ruby-treetop < %EVR
Provides:      ruby-treetop = %EVR
Provides:      gem(treetop) = 1.6.14

%description
Treetop is a language for describing languages. Combining the elegance of Ruby
with cutting-edge parsing expression grammars, it helps you analyze syntax with
revolutionary ease.


%package       -n tt
Version:       1.6.14
Release:       alt1
Summary:       A Ruby-based text parsing and interpretation DSL executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета treetop
Group:         Other
BuildArch:     noarch

Requires:      gem(treetop) = 1.6.14

%description   -n tt
A Ruby-based text parsing and interpretation DSL executable(s).

Treetop is a language for describing languages. Combining the elegance of Ruby
with cutting-edge parsing expression grammars, it helps you analyze syntax with
revolutionary ease.

%description   -n tt -l ru_RU.UTF-8
Исполнямка для самоцвета treetop.


%if_enabled    doc
%package       -n gem-treetop-doc
Version:       1.6.14
Release:       alt1
Summary:       A Ruby-based text parsing and interpretation DSL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета treetop
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(treetop) = 1.6.14

%description   -n gem-treetop-doc
A Ruby-based text parsing and interpretation DSL documentation files.

Treetop is a language for describing languages. Combining the elegance of Ruby
with cutting-edge parsing expression grammars, it helps you analyze syntax with
revolutionary ease.

%description   -n gem-treetop-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета treetop.
%endif


%if_enabled    devel
%package       -n gem-treetop-devel
Version:       1.6.14
Release:       alt1
Summary:       A Ruby-based text parsing and interpretation DSL development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета treetop
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(treetop) = 1.6.14
Requires:      gem(activesupport) >= 4
Requires:      gem(i18n) >= 1.0
Requires:      gem(rake) >= 11
Requires:      gem(rr) >= 3.0
Requires:      gem(rspec) >= 3
Conflicts:     gem(i18n) >= 2
Conflicts:     gem(rr) >= 4
Conflicts:     gem(rspec) >= 4

%description   -n gem-treetop-devel
A Ruby-based text parsing and interpretation DSL development package.

Treetop is a language for describing languages. Combining the elegance of Ruby
with cutting-edge parsing expression grammars, it helps you analyze syntax with
revolutionary ease.

%description   -n gem-treetop-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета treetop.
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
%doc History.txt LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n tt
%doc History.txt LICENSE README.md
%_bindir/tt
%_mandir/tt*xz

%if_enabled    doc
%files         -n gem-treetop-doc
%doc History.txt LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-treetop-devel
%doc History.txt LICENSE README.md
%endif


%changelog
* Sun Jan 26 2025 Pavel Skrylev <majioa@altlinux.org> 1:1.6.14-alt1
- ^ 1.6.11 -> 1.6.14

* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 1:1.6.11-alt1
- ^ 1.6.10 -> 1.6.11

* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 1:1.6.10-alt2
- > Ruby Policy 2.0
- ^ 1.6.8 -> 1.6.10

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt1.1.1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.10-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Apr 03 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.10-alt1
- New version.

* Mon Aug 21 2017 Andrey Cherepanov <cas@altlinux.org> 1.6.8-alt1
- New version

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.6.5-alt1
- New version

* Wed Apr 23 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt1
- Initial build for ALT Linux
