%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname commonmarker

Name:          gem-commonmarker
Version:       0.23.10
Release:       alt1
Summary:       CommonMark parser and renderer. Written in C, wrapped in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/gjtorikian/commonmarker
Vcs:           https://github.com/gjtorikian/commonmarker.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(awesome_print) >= 0
BuildRequires: gem(json) >= 2.3
BuildRequires: gem(minitest) >= 5.6
BuildRequires: gem(minitest-focus) >= 1.1
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0.9
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-standard) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rdoc) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Provides:      gem(commonmarker) = 0.23.10


%description
A fast, safe, extensible parser for CommonMark. This wraps the official libcmark
library.


%package       -n commonmarker
Version:       0.23.10
Release:       alt1
Summary:       CommonMark parser and renderer. Written in C, wrapped in Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета commonmarker
Group:         Other
BuildArch:     noarch

Requires:      gem(commonmarker) = 0.23.10

%description   -n commonmarker
CommonMark parser and renderer. Written in C, wrapped in Ruby executable(s).

A fast, safe, extensible parser for CommonMark. This wraps the official libcmark
library.

%description   -n commonmarker -l ru_RU.UTF-8
Исполнямка для самоцвета commonmarker.


%if_enabled    doc
%package       -n gem-commonmarker-doc
Version:       0.23.10
Release:       alt1
Summary:       CommonMark parser and renderer. Written in C, wrapped in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета commonmarker
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(commonmarker) = 0.23.10

%description   -n gem-commonmarker-doc
CommonMark parser and renderer. Written in C, wrapped in Ruby documentation
files.

A fast, safe, extensible parser for CommonMark. This wraps the official libcmark
library.

%description   -n gem-commonmarker-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета commonmarker.
%endif


%if_enabled    devel
%package       -n gem-commonmarker-devel
Version:       0.23.10
Release:       alt1
Summary:       CommonMark parser and renderer. Written in C, wrapped in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета commonmarker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(commonmarker) = 0.23.10
Requires:      gem(awesome_print) >= 0
Requires:      gem(json) >= 2.3
Requires:      gem(minitest) >= 5.6
Requires:      gem(minitest-focus) >= 1.1
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0.9
Requires:      gem(rdoc) >= 6.1.1
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-standard) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(kramdown) >= 0
Requires:      gem(redcarpet) >= 0
Conflicts:     gem(json) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rdoc) >= 7

%description   -n gem-commonmarker-devel
CommonMark parser and renderer. Written in C, wrapped in Ruby development
package.

A fast, safe, extensible parser for CommonMark. This wraps the official libcmark
library.

%description   -n gem-commonmarker-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета commonmarker.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n commonmarker
%doc README.md
%_bindir/commonmarker

%if_enabled    doc
%files         -n gem-commonmarker-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-commonmarker-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Tue Jul 30 2024 Pavel Skrylev <majioa@altlinux.org> 0.23.10-alt1
- ^ 0.23.9 -> 0.23.10

* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 0.23.9-alt1
- + packaged gem with Ruby Policy 2.0
