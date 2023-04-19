%define        _unpackaged_files_terminate_build 1
%define        gemname fast_gettext

Name:          gem-fast-gettext
Version:       2.3.0
Release:       alt1
Summary:       GetText but 3.5 x faster, 560 x less memory, simple, clean namespace (7 vs 34) and threadsafe
License:       MIT or Ruby
Group:         Development/Ruby
Url:           https://github.com/grosser/fast_gettext
Vcs:           https://github.com/grosser/fast_gettext.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(activerecord) >= 0
BuildRequires: gem(i18n) >= 0
BuildRequires: gem(bump) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-packaging) >= 0
BuildRequires: gem(single_cov) >= 0
BuildRequires: gem(forking_test_runner) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names fast_gettext,fast-gettext
Obsoletes:     ruby-fast_gettext < %EVR
Provides:      ruby-fast_gettext = %EVR
Provides:      gem(fast_gettext) = 2.3.0


%description
GetText but 3.5 x faster, 560 x less memory, simple, clean namespace (7 vs 34)
and threadsafe!

It supports multiple backends (.mo, .po, .yml files, Database(ActiveRecord + any
other), Chain, Loggers) and can easily be extended.


%package       -n gem-fast-gettext-doc
Version:       2.3.0
Release:       alt1
Summary:       GetText but 3.5 x faster, 560 x less memory, simple, clean namespace (7 vs 34) and threadsafe documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fast_gettext
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fast_gettext) = 2.3.0

%description   -n gem-fast-gettext-doc
GetText but 3.5 x faster, 560 x less memory, simple, clean namespace (7 vs 34)
and threadsafe documentation files.

GetText but 3.5 x faster, 560 x less memory, simple, clean namespace (7 vs 34)
and threadsafe!

It supports multiple backends (.mo, .po, .yml files, Database(ActiveRecord + any
other), Chain, Loggers) and can easily be extended.

%description   -n gem-fast-gettext-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fast_gettext.


%package       -n gem-fast-gettext-devel
Version:       2.3.0
Release:       alt1
Summary:       GetText but 3.5 x faster, 560 x less memory, simple, clean namespace (7 vs 34) and threadsafe development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fast_gettext
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fast_gettext) = 2.3.0
Requires:      gem(rake) >= 0
Requires:      gem(sqlite3) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(activerecord) >= 0
Requires:      gem(i18n) >= 0
Requires:      gem(bump) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-packaging) >= 0
Requires:      gem(single_cov) >= 0
Requires:      gem(forking_test_runner) >= 0

%description   -n gem-fast-gettext-devel
GetText but 3.5 x faster, 560 x less memory, simple, clean namespace (7 vs 34)
and threadsafe development package.

GetText but 3.5 x faster, 560 x less memory, simple, clean namespace (7 vs 34)
and threadsafe!

It supports multiple backends (.mo, .po, .yml files, Database(ActiveRecord + any
other), Chain, Loggers) and can easily be extended.

%description   -n gem-fast-gettext-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fast_gettext.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc Readme.md lib/fast_gettext/vendor/README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-fast-gettext-doc
%doc Readme.md lib/fast_gettext/vendor/README.rdoc
%ruby_gemdocdir

%files         -n gem-fast-gettext-devel
%doc Readme.md lib/fast_gettext/vendor/README.rdoc


%changelog
* Thu Apr 13 2023 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- ^ 2.2.0 -> 2.3.0

* Sat Jan 21 2023 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- ^ 2.0.3 -> 2.2.0

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.3-alt1
- ^ 1.8.0 -> 2.0.3

* Wed May 13 2020 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt2
- ! spec tags
- ! .gear/rules
- * license

* Thu Feb 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- ^ 1.7.0 -> 1.8.0
- > Ruby Policy 2.0

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- Bump to 1.7.0.

* Thu Sep 20 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt3.1
- Rebuild for new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt3
- Fix package as gem.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2.1
- Rebuild with Ruby 2.5.0

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2
- Rebuild with Ruby 2.4.2

* Fri May 19 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build in Sisyphus
