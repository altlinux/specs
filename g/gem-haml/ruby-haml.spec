%define        gemname haml

Name:          gem-haml
Version:       5.2.2
Release:       alt1
Summary:       HTML Abstraction Markup Language - A Markup Haiku
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/haml/haml
Vcs:           https://github.com/haml/haml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(temple) >= 0.8.0
BuildRequires: gem(tilt) >= 0
BuildRequires: gem(rails) >= 4.0.0 gem(rails) < 7
BuildRequires: gem(rbench) >= 0
BuildRequires: gem(minitest) >= 4.0 gem(minitest) < 6
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(simplecov) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency rails >= 6.1.3.2,rails < 7
Requires:      gem(temple) >= 0.8.0
Requires:      gem(tilt) >= 0
Obsoletes:     ruby-haml < %EVR
Provides:      ruby-haml = %EVR
Provides:      gem(haml) = 5.2.2


%description
Haml is a templating engine for HTML. It's designed to make it both easier and
more pleasant to write HTML documents, by eliminating redundancy, reflecting the
underlying structure that the document represents, and providing an elegant
syntax that's both powerful and easy to understand.


%package       -n haml
Version:       5.2.2
Release:       alt1
Summary:       HTML Abstraction Markup Language - A Markup Haiku executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета haml
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(haml) = 5.2.2

%description   -n haml
HTML Abstraction Markup Language - A Markup Haiku executable(s).

Haml is a templating engine for HTML. It's designed to make it both easier and
more pleasant to write HTML documents, by eliminating redundancy, reflecting the
underlying structure that the document represents, and providing an elegant
syntax that's both powerful and easy to understand.

%description   -n haml -l ru_RU.UTF-8
Исполнямка для самоцвета haml.


%package       -n gem-haml-doc
Version:       5.2.2
Release:       alt1
Summary:       HTML Abstraction Markup Language - A Markup Haiku documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета haml
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(haml) = 5.2.2

%description   -n gem-haml-doc
HTML Abstraction Markup Language - A Markup Haiku documentation files.

Haml is a templating engine for HTML. It's designed to make it both easier and
more pleasant to write HTML documents, by eliminating redundancy, reflecting the
underlying structure that the document represents, and providing an elegant
syntax that's both powerful and easy to understand.

%description   -n gem-haml-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета haml.


%package       -n gem-haml-devel
Version:       5.2.2
Release:       alt1
Summary:       HTML Abstraction Markup Language - A Markup Haiku development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета haml
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(haml) = 5.2.2
Requires:      gem(rails) >= 4.0.0 gem(rails) < 7
Requires:      gem(rbench) >= 0
Requires:      gem(minitest) >= 4.0 gem(minitest) < 6
Requires:      gem(nokogiri) >= 0
Requires:      gem(simplecov) >= 0 gem(simplecov) < 1

%description   -n gem-haml-devel
HTML Abstraction Markup Language - A Markup Haiku development package.

Haml is a templating engine for HTML. It's designed to make it both easier and
more pleasant to write HTML documents, by eliminating redundancy, reflecting the
underlying structure that the document represents, and providing an elegant
syntax that's both powerful and easy to understand.

%description   -n gem-haml-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета haml.


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

%files         -n haml
%doc README.md
%_bindir/haml

%files         -n gem-haml-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-haml-devel
%doc README.md


%changelog
* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 5.2.2-alt1
- ^ 5.1.1 -> 5.2.2

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 5.1.1-alt1
- Bump to 5.1.1
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.3-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Thu Sep 28 2017 Mikhail Gordeev <obirvalger@altlinux.org> 5.0.3-alt1
- Initial build for Sisyphus
