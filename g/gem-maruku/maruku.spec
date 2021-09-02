%define        gemname maruku

Name:          gem-maruku
Version:       0.7.3
Release:       alt2.1
Summary:       A pure-Ruby Markdown-superset interpreter
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bhollis/maruku
Vcs:           https://github.com/bhollis/maruku.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(maruku) = 0.7.3


%description
Maruku is a Markdown-superset interpreter.

Maruku implements:

* The original Markdown syntax.
* All the improvements in PHP Markdown Extra.
* A new meta-data syntax.


%package       -n maruku
Version:       0.7.3
Release:       alt2.1
Summary:       A pure-Ruby Markdown-superset interpreter executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета maruku
Group:         Other
BuildArch:     noarch

Requires:      gem(maruku) = 0.7.3

%description   -n maruku
A pure-Ruby Markdown-superset interpreter executable(s).

Maruku is a Markdown-superset interpreter.

Maruku implements:

* The original Markdown syntax.
* All the improvements in PHP Markdown Extra.
* A new meta-data syntax.

%description   -n maruku -l ru_RU.UTF-8
Исполнямка для самоцвета maruku.


%package       -n gem-maruku-doc
Version:       0.7.3
Release:       alt2.1
Summary:       A pure-Ruby Markdown-superset interpreter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета maruku
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(maruku) = 0.7.3
Obsoletes:     maruku-doc
Provides:      maruku-doc

%description   -n gem-maruku-doc
A pure-Ruby Markdown-superset interpreter documentation files.

Maruku is a Markdown-superset interpreter.

Maruku implements:

* The original Markdown syntax.
* All the improvements in PHP Markdown Extra.
* A new meta-data syntax.

%description   -n gem-maruku-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета maruku.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n maruku
%_bindir/maruku
%_bindir/marutex

%files         -n gem-maruku-doc
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt2.1
- ! spec

* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1
- Initial build for Sisyphus
