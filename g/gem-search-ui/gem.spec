%define        gemname search_ui

Name:          gem-search-ui
Version:       0.0.1
Release:       alt1
Summary:       Library to provide a user interface for searching in a console
License:       MIT
Group:         Development/Ruby
Url:           http://flori.github.com/search_ui
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(gem_hadar) >= 1.11.0 gem(gem_hadar) < 2
BuildRequires: gem(simplecov) >= 0.0 gem(simplecov) < 1
BuildRequires: gem(tins) >= 1.0 gem(tins) < 2
BuildRequires: gem(term-ansicolor) >= 1.0 gem(term-ansicolor) < 2
BuildRequires: gem(amatch) >= 0.0 gem(amatch) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency gem_hadar >= 1.12.0,gem_hadar < 2
Requires:      gem(tins) >= 1.0 gem(tins) < 2
Requires:      gem(term-ansicolor) >= 1.0 gem(term-ansicolor) < 2
Requires:      gem(amatch) >= 0.0 gem(amatch) < 1
Provides:      gem(search_ui) = 0.0.1


%description
This library allows a user to search an array of objects interactively in the
console by matching the pattern a user inputs to an array of objects and pick
one of the remaining objects.


%package       -n search-it
Version:       0.0.1
Release:       alt1
Summary:       Library to provide a user interface for searching in a console executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета search_ui
Group:         Other
BuildArch:     noarch

Requires:      gem(search_ui) = 0.0.1

%description   -n search-it
Library to provide a user interface for searching in a console
executable(s).

This library allows a user to search an array of objects interactively in the
console by matching the pattern a user inputs to an array of objects and pick
one of the remaining objects.

%description   -n search-it -l ru_RU.UTF-8
Исполнямка для самоцвета search_ui.


%package       -n gem-search-ui-doc
Version:       0.0.1
Release:       alt1
Summary:       Library to provide a user interface for searching in a console documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета search_ui
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(search_ui) = 0.0.1

%description   -n gem-search-ui-doc
Library to provide a user interface for searching in a console documentation
files.

This library allows a user to search an array of objects interactively in the
console by matching the pattern a user inputs to an array of objects and pick
one of the remaining objects.

%description   -n gem-search-ui-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета search_ui.


%package       -n gem-search-ui-devel
Version:       0.0.1
Release:       alt1
Summary:       Library to provide a user interface for searching in a console development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета search_ui
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(search_ui) = 0.0.1
Requires:      gem(gem_hadar) >= 1.11.0 gem(gem_hadar) < 2
Requires:      gem(simplecov) >= 0.0 gem(simplecov) < 1

%description   -n gem-search-ui-devel
Library to provide a user interface for searching in a console development
package.

This library allows a user to search an array of objects interactively in the
console by matching the pattern a user inputs to an array of objects and pick
one of the remaining objects.

%description   -n gem-search-ui-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета search_ui.


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

%files         -n search-it
%doc README.md
%_bindir/search_it

%files         -n gem-search-ui-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-search-ui-devel
%doc README.md


%changelog
* Wed Jul 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt1
- + packaged gem with Ruby Policy 2.0
