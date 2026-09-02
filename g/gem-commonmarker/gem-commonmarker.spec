%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname commonmarker

Name:          gem-commonmarker
Version:       2.10.0
Release:       alt1
Summary:       CommonMark parser and renderer. Written in C, wrapped in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/gjtorikian/commonmarker
Vcs:           https://github.com/gjtorikian/commonmarker.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake libruby-devel
%if_enabled check
BuildRequires: gem(amazing_print) >= 0
BuildRequires: gem(debug) >= 0
BuildRequires: gem(minitest) >= 5.6
BuildRequires: gem(minitest-focus) >= 1.1
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 1.1.2
BuildRequires: gem(rb_sys) >= 0.9
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rb_sys) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.6
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Requires:      ruby >= 3.2
Requires:      gem(rb_sys) >= 0.9
Conflicts:     ruby >= 5
Conflicts:     gem(rb_sys) >= 1
Provides:      gem(commonmarker) = 2.10.0

%description
A fast, safe, extensible parser for CommonMark. This wraps the official libcmark
library.


%if_enabled    doc
%package       -n gem-commonmarker-doc
Version:       2.10.0
Release:       alt1
Summary:       CommonMark parser and renderer. Written in C, wrapped in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета commonmarker
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(commonmarker) = 2.10.0

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
Version:       2.10.0
Release:       alt1
Summary:       CommonMark parser and renderer. Written in C, wrapped in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета commonmarker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(commonmarker) = 2.10.0
Requires:      gem(amazing_print) >= 0
Requires:      gem(debug) >= 0

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
%doc LICENSE.txt README.md CHANGELOG.md CODE_OF_CONDUCT.txt
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-commonmarker-doc
%doc LICENSE.txt README.md CHANGELOG.md CODE_OF_CONDUCT.txt
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-commonmarker-devel
%doc LICENSE.txt README.md CHANGELOG.md CODE_OF_CONDUCT.txt
%endif


%changelog
* Tue Sep 01 2026 Pavel Skrylev <majioa@altlinux.org> 2.10.0-alt1
- ^ 0.23.10 -> 2.10.0

* Tue Jul 30 2024 Pavel Skrylev <majioa@altlinux.org> 0.23.10-alt1
- ^ 0.23.9 -> 0.23.10

* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 0.23.9-alt1
- + packaged gem with Ruby Policy 2.0
