%define        gemname terminal-table

Name:          gem-terminal-table
Version:       3.0.1
Release:       alt1
Summary:       Simple, feature rich ascii table generation library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/tj/terminal-table
Vcs:           https://github.com/tj/terminal-table.git
Packager:      Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 2 gem(bundler) < 3
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(term-ansicolor) >= 0
BuildRequires: gem(pry) >= 0 gem(pry) < 1
BuildRequires: gem(unicode-display_width) >= 1.1.1 gem(unicode-display_width) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(unicode-display_width) >= 1.1.1 gem(unicode-display_width) < 3
Provides:      gem(terminal-table) = 3.0.1


%description
Terminal Table is a fast and simple, yet feature rich table generator written
in Ruby. It supports ASCII and Unicode formatted tables.


%package       -n gem-terminal-table-doc
Version:       3.0.1
Release:       alt1
Summary:       Simple, feature rich ascii table generation library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета terminal-table
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(terminal-table) = 3.0.1

%description   -n gem-terminal-table-doc
Simple, feature rich ascii table generation library documentation
files.

Terminal Table is a fast and simple, yet feature rich table generator written
in Ruby. It supports ASCII and Unicode formatted tables.

%description   -n gem-terminal-table-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета terminal-table.


%package       -n gem-terminal-table-devel
Version:       3.0.1
Release:       alt1
Summary:       Simple, feature rich ascii table generation library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета terminal-table
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(terminal-table) = 3.0.1
Requires:      gem(bundler) >= 2 gem(bundler) < 3
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(term-ansicolor) >= 0
Requires:      gem(pry) >= 0 gem(pry) < 1

%description   -n gem-terminal-table-devel
Simple, feature rich ascii table generation library development
package.

Terminal Table is a fast and simple, yet feature rich table generator written
in Ruby. It supports ASCII and Unicode formatted tables.

%description   -n gem-terminal-table-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета terminal-table.


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

%files         -n gem-terminal-table-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-terminal-table-devel
%doc README.md


%changelog
* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- ^ 3.0.0 -> 3.0.1

* Tue Mar 16 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 3.0.0-alt1
- initial build
