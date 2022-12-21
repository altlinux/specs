%define        gemname scoped_search

Name:          gem-scoped-search
Version:       4.1.10
Release:       alt1.1
Summary:       Easily search you ActiveRecord models with a simple query language that converts to SQL
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/wvanbergen/scoped_search
Vcs:           https://github.com/wvanbergen/scoped_search.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(activerecord) >= 4.2.0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rake) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names scoped_search,scoped-search
Requires:      gem(activerecord) >= 4.2.0
Obsoletes:     ruby-scoped_search < %EVR
Provides:      ruby-scoped_search = %EVR
Provides:      gem(scoped_search) = 4.1.10


%description
The scoped_search gem makes it easy to search your ActiveRecord models.
Searching is performed using a query string, which should be passed to the
named_scope search_for. Based on a definition in what fields to look, it will
build query conditions and return those as a named scope.

Scoped search is great if you want to offer a simple yet powerful search box to
your users and build a query based on the search string they enter. It comes
with a built-in search syntax auto-completer and a value auto-completer. It also
comes with a set of helpers that makes it easy to create a clean web UI with
sorting and an ajax auto-completer.


%package       -n gem-scoped-search-doc
Version:       4.1.10
Release:       alt1.1
Summary:       Easily search you ActiveRecord models with a simple query language that converts to SQL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета scoped_search
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(scoped_search) = 4.1.10

%description   -n gem-scoped-search-doc
Easily search you ActiveRecord models with a simple query language that converts
to SQL documentation files.

The scoped_search gem makes it easy to search your ActiveRecord models.
Searching is performed using a query string, which should be passed to the
named_scope search_for. Based on a definition in what fields to look, it will
build query conditions and return those as a named scope.

Scoped search is great if you want to offer a simple yet powerful search box to
your users and build a query based on the search string they enter. It comes
with a built-in search syntax auto-completer and a value auto-completer. It also
comes with a set of helpers that makes it easy to create a clean web UI with
sorting and an ajax auto-completer.

%description   -n gem-scoped-search-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета scoped_search.


%package       -n gem-scoped-search-devel
Version:       4.1.10
Release:       alt1.1
Summary:       Easily search you ActiveRecord models with a simple query language that converts to SQL development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета scoped_search
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(scoped_search) = 4.1.10
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(rake) >= 0

%description   -n gem-scoped-search-devel
Easily search you ActiveRecord models with a simple query language that converts
to SQL development package.

The scoped_search gem makes it easy to search your ActiveRecord models.
Searching is performed using a query string, which should be passed to the
named_scope search_for. Based on a definition in what fields to look, it will
build query conditions and return those as a named scope.

Scoped search is great if you want to offer a simple yet powerful search box to
your users and build a query based on the search string they enter. It comes
with a built-in search syntax auto-completer and a value auto-completer. It also
comes with a set of helpers that makes it easy to create a clean web UI with
sorting and an ajax auto-completer.

%description   -n gem-scoped-search-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета scoped_search.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-scoped-search-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-scoped-search-devel
%doc README.rdoc


%changelog
* Thu Dec 15 2022 Pavel Skrylev <majioa@altlinux.org> 4.1.10-alt1.1
- !closes build requires under check condition

* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 4.1.10-alt1
- ^ 4.1.9 -> 4.1.10

* Wed Dec 16 2020 Pavel Skrylev <majioa@altlinux.org> 4.1.9-alt1
- ^ 4.1.7 -> 4.1.9
- ! spec

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 4.1.7-alt1.1
- * policify name
- ! spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 4.1.7-alt1
- ^ 4.1.5 -> 4.1.7
- > Ruby Policy 2.0

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.5-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.4-alt1
- New version.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.3-alt1
- Initial build for Sisyphus
