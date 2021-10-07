%define        gemname kramdown-parser-gfm

Name:          gem-kramdown-parser-gfm
Version:       1.0.1
Release:       alt1.1
Summary:       This is a parser for kramdown that converts Markdown documents in the GFM dialect to HTML
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/kramdown/parser-gfm
Vcs:           https://github.com/kramdown/parser-gfm.git
Packager:      Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem-rexml
BuildRequires: gem(kramdown) >= 2.0 gem(kramdown) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
Requires:      gem(kramdown) >= 2.0 gem(kramdown) < 3
Provides:      gem(kramdown-parser-gfm) = 1.0.1


%description
This is a parser for kramdown that converts Markdown documents in the GFM
dialect to HTML.


%package       -n gem-kramdown-parser-gfm-doc
Version:       1.0.1
Release:       alt1.1
Summary:       This is a parser for kramdown that converts Markdown documents in the GFM dialect to HTML documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета kramdown-parser-gfm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(kramdown-parser-gfm) = 1.0.1

%description   -n gem-kramdown-parser-gfm-doc
This is a parser for kramdown that converts Markdown documents in the GFM
dialect to HTML documentation files.

%description   -n gem-kramdown-parser-gfm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета kramdown-parser-gfm.


%package       -n gem-kramdown-parser-gfm-devel
Version:       1.0.1
Release:       alt1.1
Summary:       This is a parser for kramdown that converts Markdown documents in the GFM dialect to HTML development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета kramdown-parser-gfm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(kramdown-parser-gfm) = 1.0.1

%description   -n gem-kramdown-parser-gfm-devel
This is a parser for kramdown that converts Markdown documents in the GFM
dialect to HTML development package.

%description   -n gem-kramdown-parser-gfm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета kramdown-parser-gfm.


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

%files         -n gem-kramdown-parser-gfm-doc
%ruby_gemdocdir

%files         -n gem-kramdown-parser-gfm-devel


%changelog
* Tue Sep 14 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1.1
- ! spec

* Tue Mar 16 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 1.0.1-alt1
- initial build
