%define        gemname mdl

Name:          gem-mdl
Version:       0.11.0
Release:       alt1
Summary:       Markdown lint tool
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/markdownlint/markdownlint
Vcs:           https://github.com/markdownlint/markdownlint.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(kramdown) >= 2.3 gem(kramdown) < 3
BuildRequires: gem(kramdown-parser-gfm) >= 1.1 gem(kramdown-parser-gfm) < 2
BuildRequires: gem(mixlib-cli) >= 2.1.1 gem(mixlib-cli) < 3
BuildRequires: gem(mixlib-config) >= 2.2.1 gem(mixlib-config) < 4
BuildRequires: gem(mixlib-shellout) >= 0
BuildRequires: gem(bundler) >= 1.12 gem(bundler) < 3
BuildRequires: gem(minitest) >= 5.9 gem(minitest) < 6
BuildRequires: gem(pry) >= 0.10 gem(pry) < 1
BuildRequires: gem(rake) >= 11.2 gem(rake) < 14
BuildRequires: gem(rubocop) >= 0.49.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(kramdown) >= 2.3 gem(kramdown) < 3
Requires:      gem(kramdown-parser-gfm) >= 1.1 gem(kramdown-parser-gfm) < 2
Requires:      gem(mixlib-cli) >= 2.1.1 gem(mixlib-cli) < 3
Requires:      gem(mixlib-config) >= 2.2.1 gem(mixlib-config) < 4
Requires:      gem(mixlib-shellout) >= 0
Provides:      gem(mdl) = 0.11.0


%description
Style checker/lint tool for markdown files


%package       -n mdl
Version:       0.11.0
Release:       alt1
Summary:       Markdown lint tool executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета mdl
Group:         Other
BuildArch:     noarch

Requires:      gem(mdl) = 0.11.0

%description   -n mdl
Markdown lint tool executable(s).

Style checker/lint tool for markdown files

%description   -n mdl -l ru_RU.UTF-8
Исполнямка для самоцвета mdl.


%package       -n gem-mdl-doc
Version:       0.11.0
Release:       alt1
Summary:       Markdown lint tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mdl
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mdl) = 0.11.0

%description   -n gem-mdl-doc
Markdown lint tool documentation files.

Style checker/lint tool for markdown files

%description   -n gem-mdl-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mdl.


%package       -n gem-mdl-devel
Version:       0.11.0
Release:       alt1
Summary:       Markdown lint tool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mdl
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mdl) = 0.11.0
Requires:      gem(bundler) >= 1.12 gem(bundler) < 3
Requires:      gem(minitest) >= 5.9 gem(minitest) < 6
Requires:      gem(pry) >= 0.10 gem(pry) < 1
Requires:      gem(rake) >= 11.2 gem(rake) < 14
Requires:      gem(rubocop) >= 0.49.0

%description   -n gem-mdl-devel
Markdown lint tool development package.

Style checker/lint tool for markdown files

%description   -n gem-mdl-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mdl.


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

%files         -n mdl
%_bindir/mdl

%files         -n gem-mdl-doc
%ruby_gemdocdir

%files         -n gem-mdl-devel


%changelog
* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.11.0-alt1
- + packaged gem with Ruby Policy 2.0
