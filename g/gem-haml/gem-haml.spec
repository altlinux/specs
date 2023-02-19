%define        gemname haml

Name:          gem-haml
Version:       6.1.1
Release:       alt1
Summary:       HTML Abstraction Markup Language - A Markup Haiku
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/haml/haml
Vcs:           https://github.com/haml/haml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(benchmark_driver) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(coffee-script) >= 0
BuildRequires: gem(erubi) >= 0
BuildRequires: gem(less) >= 0
BuildRequires: gem(minitest-reporters) >= 1.1
BuildRequires: gem(rails) >= 4.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(sass) >= 0
BuildRequires: gem(slim) >= 0
BuildRequires: gem(string_template) >= 0
BuildRequires: gem(unindent) >= 0
BuildRequires: gem(benchmark-ips) = 2.3.0
BuildRequires: gem(maxitest) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(stackprof) >= 0
BuildRequires: gem(temple) >= 0.8.2
BuildRequires: gem(thor) >= 0
BuildRequires: gem(tilt) >= 0
BuildConflicts: gem(minitest-reporters) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(temple) >= 0.8.2
Requires:      gem(thor) >= 0
Requires:      gem(tilt) >= 0
Obsoletes:     ruby-haml < %EVR
Provides:      ruby-haml = %EVR
Provides:      gem(haml) = 6.1.1


%description
Haml is a templating engine for HTML. It's designed to make it both easier and
more pleasant to write HTML documents, by eliminating redundancy, reflecting the
underlying structure that the document represents, and providing an elegant
syntax that's both powerful and easy to understand.


%package       -n haml
Version:       6.1.1
Release:       alt1
Summary:       HTML Abstraction Markup Language - A Markup Haiku executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета haml
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(haml) = 6.1.1

%description   -n haml
HTML Abstraction Markup Language - A Markup Haiku executable(s).

Haml is a templating engine for HTML. It's designed to make it both easier and
more pleasant to write HTML documents, by eliminating redundancy, reflecting the
underlying structure that the document represents, and providing an elegant
syntax that's both powerful and easy to understand.

%description   -n haml -l ru_RU.UTF-8
Исполнямка для самоцвета haml.


%package       -n gem-haml-doc
Version:       6.1.1
Release:       alt1
Summary:       HTML Abstraction Markup Language - A Markup Haiku documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета haml
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(haml) = 6.1.1

%description   -n gem-haml-doc
HTML Abstraction Markup Language - A Markup Haiku documentation files.

Haml is a templating engine for HTML. It's designed to make it both easier and
more pleasant to write HTML documents, by eliminating redundancy, reflecting the
underlying structure that the document represents, and providing an elegant
syntax that's both powerful and easy to understand.

%description   -n gem-haml-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета haml.


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

%files         -n haml
%doc README.md
%_bindir/haml

%files         -n gem-haml-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 6.1.1-alt1
- ^ 5.2.2 -> 6.1.1 (no devel)

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
