%define        gemname strings

Name:          gem-strings
Version:       0.2.1
Release:       alt1
Summary:       A set of useful functions for transforming strings
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/piotrmurach/strings
Vcs:           https://github.com/piotrmurach/strings.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(strings-ansi) >= 0.2 gem(strings-ansi) < 1
BuildRequires: gem(unicode_utils) >= 1.4 gem(unicode_utils) < 2
BuildRequires: gem(unicode-display_width) >= 1.5 gem(unicode-display_width) < 3.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(strings-ansi) >= 0.2 gem(strings-ansi) < 1
Requires:      gem(unicode_utils) >= 1.4 gem(unicode_utils) < 2
Requires:      gem(unicode-display_width) >= 1.5 gem(unicode-display_width) < 3.0
Provides:      gem(strings) = 0.2.1


%description
The Strings is a set of useful functions such as fold, truncate, wrap, and many
more for transforming strings.


%package       -n gem-strings-doc
Version:       0.2.1
Release:       alt1
Summary:       A set of useful functions for transforming strings documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета strings
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(strings) = 0.2.1

%description   -n gem-strings-doc
A set of useful functions for transforming strings documentation files.

The Strings is a set of useful functions such as fold, truncate, wrap, and many
more for transforming strings.

%description   -n gem-strings-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета strings.


%package       -n gem-strings-devel
Version:       0.2.1
Release:       alt1
Summary:       A set of useful functions for transforming strings development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета strings
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(strings) = 0.2.1
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-strings-devel
A set of useful functions for transforming strings development package.

The Strings is a set of useful functions such as fold, truncate, wrap, and many
more for transforming strings.

%description   -n gem-strings-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета strings.


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

%files         -n gem-strings-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-strings-devel
%doc README.md


%changelog
* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- ^ 0.2.0 -> 0.2.1

* Tue Sep 08 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- ^ 0.1.6 -> 0.2.0
- ! spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.6-alt1
- ^ 0.1.5 -> 0.1.6
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- + packaged gem with usage Ruby Policy 2.0
