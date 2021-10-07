%define        gemname stringex

Name:          gem-stringex
Version:       2.8.5
Release:       alt1
Summary:       Some [hopefully] useful extensions to Ruby's String class
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/rsl/stringex
Vcs:           https://github.com/rsl/stringex.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
# BuildRequires: gem(jeweler) >= 2.3.7
# BuildRequires: gem(travis-lint) >= 1.7.0
BuildRequires: gem(RedCloth) >= 4.2.9
BuildRequires: gem(sqlite3) >= 1.3.10
BuildRequires: gem(test-unit) >= 3.0.9 gem(test-unit) < 4
BuildRequires: gem(activerecord) >= 5.1.4
BuildRequires: gem(i18n) >= 0.7.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(stringex) = 2.8.5


%description
Some [hopefully] useful extensions to Ruby's String class. Stringex is made up
of three libraries: ActsAsUrl [permalink solution with better character
translation], Unidecoder [Unicode to ASCII transliteration], and
StringExtensions [miscellaneous helper methods for the String class].


%package       -n gem-stringex-doc
Version:       2.8.5
Release:       alt1
Summary:       Some [hopefully] useful extensions to Ruby's String class documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета stringex
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(stringex) = 2.8.5

%description   -n gem-stringex-doc
Some [hopefully] useful extensions to Ruby's String class documentation
files.

Some [hopefully] useful extensions to Ruby's String class. Stringex is made up
of three libraries: ActsAsUrl [permalink solution with better character
translation], Unidecoder [Unicode to ASCII transliteration], and
StringExtensions [miscellaneous helper methods for the String class].

%description   -n gem-stringex-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета stringex.


%package       -n gem-stringex-devel
Version:       2.8.5
Release:       alt1
Summary:       Some [hopefully] useful extensions to Ruby's String class development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета stringex
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(stringex) = 2.8.5
# Requires:      gem(jeweler) >= 2.3.7
# Requires:      gem(travis-lint) >= 1.7.0
Requires:      gem(RedCloth) >= 4.2.9
Requires:      gem(sqlite3) >= 1.3.10
Requires:      gem(test-unit) >= 3.0.9 gem(test-unit) < 4
Requires:      gem(activerecord) >= 5.1.4
Requires:      gem(i18n) >= 0.7.0

%description   -n gem-stringex-devel
Some [hopefully] useful extensions to Ruby's String class development
package.

Some [hopefully] useful extensions to Ruby's String class. Stringex is made up
of three libraries: ActsAsUrl [permalink solution with better character
translation], Unidecoder [Unicode to ASCII transliteration], and
StringExtensions [miscellaneous helper methods for the String class].

%description   -n gem-stringex-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета stringex.


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

%files         -n gem-stringex-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-stringex-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.8.5-alt1
- + packaged gem with Ruby Policy 2.0
