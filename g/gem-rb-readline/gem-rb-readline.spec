%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rb-readline

Name:          gem-rb-readline
Version:       0.5.5.3
Release:       alt0.1
Summary:       Pure-Ruby Readline Implementation
License:       BSD
Group:         Development/Ruby
Url:           http://github.com/ConnorAtherton/rb-readline
Vcs:           https://github.com/connoratherton/rb-readline.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(minitest) >= 5.2
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 1.8.6
Requires:      rubygems >= 1.3.5
Provides:      gem(rb-readline) = 0.5.5.3

%ruby_use_gem_version rb-readline:0.5.5.3

%description
The readline library provides a pure Ruby implementation of the GNU readline C
library, as well as the Readline extension that ships as part of the standard
library.


%if_enabled    doc
%package       -n gem-rb-readline-doc
Version:       0.5.5.3
Release:       alt0.1
Summary:       Pure-Ruby Readline Implementation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rb-readline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rb-readline) = 0.5.5.3

%description   -n gem-rb-readline-doc
Pure-Ruby Readline Implementation documentation files.

The readline library provides a pure Ruby implementation of the GNU readline C
library, as well as the Readline extension that ships as part of the standard
library.

%description   -n gem-rb-readline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rb-readline.
%endif


%if_enabled    devel
%package       -n gem-rb-readline-devel
Version:       0.5.5.3
Release:       alt0.1
Summary:       Pure-Ruby Readline Implementation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rb-readline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rb-readline) = 0.5.5.3
Requires:      gem(minitest) >= 5.2
Requires:      gem(rake) >= 0
Conflicts:     gem(minitest) >= 6

%description   -n gem-rb-readline-devel
Pure-Ruby Readline Implementation development package.

The readline library provides a pure Ruby implementation of the GNU readline C
library, as well as the Readline extension that ships as part of the standard
library.

%description   -n gem-rb-readline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rb-readline.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rb-readline-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rb-readline-devel
%doc LICENSE README.md
%endif


%changelog
* Sun Aug 16 2026 Pavel Skrylev <majioa@altlinux.org> 0.5.5.3-alt0.1
- ^ 0.5.5 -> 0.5.5p3
- * updated to upstream git base

* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.5-alt1
- + packaged gem with Ruby Policy 2.0
