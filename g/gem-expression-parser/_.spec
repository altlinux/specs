%define        gemname expression_parser

Name:          gem-expression-parser
Version:       0.9.1
Release:       alt1.1
Summary:       Math parser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/nricciar/expression_parser
Vcs:           https://github.com/nricciar/expression_parser.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         cov.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(simplecov) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names expression_parser,expression-parser
%ruby_ignore_names dummy_sass_only,dummy_sass
Provides:      gem(expression_parser) = 0.9.1


%description
Math parser based on Lukasz Wrobel's blog post.


%package       -n gem-expression-parser-doc
Version:       0.9.1
Release:       alt1.1
Summary:       Math parser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета expression_parser
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(expression_parser) = 0.9.1

%description   -n gem-expression-parser-doc
Math parser documentation files.

Math parser based on Lukasz Wrobel's blog post.

%description   -n gem-expression-parser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета expression_parser.


%package       -n gem-expression-parser-devel
Version:       0.9.1
Release:       alt1.1
Summary:       Math parser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета expression_parser
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(expression_parser) = 0.9.1
Requires:      gem(test-unit) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(simplecov) >= 0

%description   -n gem-expression-parser-devel
Math parser development package.

Math parser based on Lukasz Wrobel's blog post.

%description   -n gem-expression-parser-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета expression_parser.


%prep
%setup
%patch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-expression-parser-doc
%doc README
%ruby_gemdocdir

%files         -n gem-expression-parser-devel
%doc README


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.9.1-alt1.1
- ! spec

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
