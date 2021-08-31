%define        gemname citrus

Name:          gem-citrus
Version:       3.0.2
Release:       alt2
Summary:       Parsing Expressions for Ruby
License:       MIT or Ruby
Group:         Development/Ruby
Url:           https://github.com/mjackson/citrus
Vcs:           https://github.com/mjackson/citrus.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-citrus < %EVR
Provides:      ruby-citrus = %EVR
Provides:      gem(citrus) = 3.0.2


%description
Citrus is a compact and powerful parsing library for Ruby that combines the
elegance and expressiveness of the language with the simplicity and power of
parsing expressions.


%package       -n gem-citrus-doc
Version:       3.0.2
Release:       alt2
Summary:       Parsing Expressions for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета citrus
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(citrus) = 3.0.2

%description   -n gem-citrus-doc
Parsing Expressions for Ruby documentation files.

Citrus is a compact and powerful parsing library for Ruby that combines the
elegance and expressiveness of the language with the simplicity and power of
parsing expressions.

%description   -n gem-citrus-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета citrus.


%package       -n gem-citrus-devel
Version:       3.0.2
Release:       alt2
Summary:       Parsing Expressions for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета citrus
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(citrus) = 3.0.2
Requires:      gem(rake) >= 0

%description   -n gem-citrus-devel
Parsing Expressions for Ruby development package.

Citrus is a compact and powerful parsing library for Ruby that combines the
elegance and expressiveness of the language with the simplicity and power of
parsing expressions.

%description   -n gem-citrus-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета citrus.


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

%files         -n gem-citrus-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-citrus-devel
%doc README.md


%changelog
* Tue Jun 29 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.2-alt2
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Apr 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- Initial build for Sisyphus
