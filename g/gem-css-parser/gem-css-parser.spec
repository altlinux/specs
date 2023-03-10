# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%define        gemname css_parser

Name:          gem-css-parser
Version:       1.14.0
Release:       alt1
Summary:       Ruby CSS Parser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/premailer/css_parser
Vcs:           https://github.com/premailer/css_parser.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(bump) >= 0
BuildRequires: gem(maxitest) >= 0
BuildRequires: gem(memory_profiler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 1.8
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(addressable) >= 0
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names css_parser,css-parser
Requires:      gem(addressable) >= 0
Obsoletes:     ruby-css_parser < %EVR
Provides:      ruby-css_parser = %EVR
Provides:      gem(css_parser) = 1.14.0


%description
Load, parse and cascade CSS rule sets in Ruby.


%package       -n gem-css-parser-doc
Version:       1.14.0
Release:       alt1
Summary:       Ruby CSS Parser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета css_parser
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(css_parser) = 1.14.0

%description   -n gem-css-parser-doc
Ruby CSS Parser documentation files.

Load, parse and cascade CSS rule sets in Ruby.

%description   -n gem-css-parser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета css_parser.


%package       -n gem-css-parser-devel
Version:       1.14.0
Release:       alt1
Summary:       Ruby CSS Parser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета css_parser
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(css_parser) = 1.14.0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(bump) >= 0
Requires:      gem(maxitest) >= 0
Requires:      gem(memory_profiler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 1.8
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(webrick) >= 0
Conflicts:     gem(rubocop) >= 2

%description   -n gem-css-parser-devel
Ruby CSS Parser development package.

Load, parse and cascade CSS rule sets in Ruby.

%description   -n gem-css-parser-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета css_parser.


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

%files         -n gem-css-parser-doc
%ruby_gemdocdir

%files         -n gem-css-parser-devel


%changelog
* Fri Mar 10 2023 Pavel Skrylev <majioa@altlinux.org> 1.14.0-alt1
- ^ 1.7.1 -> 1.14.0

* Thu Dec 24 2020 Pavel Skrylev <majioa@altlinux.org> 1.7.1-alt1
- ^ 1.7.0 -> 1.7.1
- * policify name

* Wed Jul 24 2019 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- > Ruby Policy 2.0
- ^ 1.6.0 -> 1.7.0

* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- Initial gemified build for Sisyphus
