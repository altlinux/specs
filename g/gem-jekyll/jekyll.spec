%define        gemname jekyll

Name:          gem-jekyll
Version:       4.2.0
Release:       alt1.1
Summary:       Jekyll is a simple, blog-aware, static site generator
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jekyll/jekyll.git
Vcs:           https://github.com/jekyll/jekyll.git
Packager:      Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem-rubocop
BuildRequires: gem-sassc
BuildRequires: gem(addressable) >= 2.4 gem(addressable) < 3
BuildRequires: gem(colorator) >= 1.0 gem(colorator) < 2
BuildRequires: gem(em-websocket) >= 0.5 gem(em-websocket) < 1
BuildRequires: gem(i18n) >= 1.0 gem(i18n) < 2
BuildRequires: gem(jekyll-sass-converter) >= 2.0 gem(jekyll-sass-converter) < 3
BuildRequires: gem(jekyll-watch) >= 2.0 gem(jekyll-watch) < 3
BuildRequires: gem(kramdown) >= 2.3 gem(kramdown) < 3
BuildRequires: gem(kramdown-parser-gfm) >= 1.0 gem(kramdown-parser-gfm) < 2
BuildRequires: gem(liquid) >= 4.0 gem(liquid) < 6
BuildRequires: gem(mercenary) >= 0.4.0 gem(mercenary) < 0.5
BuildRequires: gem(pathutil) >= 0.9 gem(pathutil) < 1
BuildRequires: gem(rouge) >= 3.0 gem(rouge) < 4
BuildRequires: gem(safe_yaml) >= 1.0 gem(safe_yaml) < 2
BuildRequires: gem(terminal-table) >= 3.0 gem(terminal-table) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency terminal-table >= 3.0,terminal-table < 4
%ruby_use_gem_dependency liquid >= 5.0.1,liquid < 6
%ruby_ignore_names test-theme-symlink,test-theme,test-dependency-theme,test-theme-skinny
Requires:      gem(addressable) >= 2.4 gem(addressable) < 3
Requires:      gem(colorator) >= 1.0 gem(colorator) < 2
Requires:      gem(em-websocket) >= 0.5 gem(em-websocket) < 1
Requires:      gem(i18n) >= 1.0 gem(i18n) < 2
Requires:      gem(jekyll-sass-converter) >= 2.0 gem(jekyll-sass-converter) < 3
Requires:      gem(jekyll-watch) >= 2.0 gem(jekyll-watch) < 3
Requires:      gem(kramdown) >= 2.3 gem(kramdown) < 3
Requires:      gem(kramdown-parser-gfm) >= 1.0 gem(kramdown-parser-gfm) < 2
Requires:      gem(liquid) >= 4.0 gem(liquid) < 6
Requires:      gem(mercenary) >= 0.4.0 gem(mercenary) < 0.5
Requires:      gem(pathutil) >= 0.9 gem(pathutil) < 1
Requires:      gem(rouge) >= 3.0 gem(rouge) < 4
Requires:      gem(safe_yaml) >= 1.0 gem(safe_yaml) < 2
Requires:      gem(terminal-table) >= 3.0 gem(terminal-table) < 4
Provides:      gem(jekyll) = 4.2.0


%description
Jekyll is a simple, blog aware, static site generator.


%package       -n jekyll
Version:       4.2.0
Release:       alt1.1
Summary:       Jekyll is a simple, blog-aware, static site generator executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета jekyll
Group:         Other
BuildArch:     noarch

Requires:      gem(jekyll) = 4.2.0

%description   -n jekyll
Jekyll is a simple, blog-aware, static site generator executable(s).

Jekyll is a simple, blog aware, static site generator.

%description   -n jekyll -l ru_RU.UTF-8
Исполнямка для самоцвета jekyll.


%package       -n gem-jekyll-doc
Version:       4.2.0
Release:       alt1.1
Summary:       Jekyll is a simple, blog-aware, static site generator documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jekyll
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jekyll) = 4.2.0

%description   -n gem-jekyll-doc
Jekyll is a simple, blog-aware, static site generator documentation
files.

Jekyll is a simple, blog aware, static site generator.

%description   -n gem-jekyll-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jekyll.


%package       -n gem-jekyll-devel
Version:       4.2.0
Release:       alt1.1
Summary:       Jekyll is a simple, blog-aware, static site generator development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jekyll
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jekyll) = 4.2.0

%description   -n gem-jekyll-devel
Jekyll is a simple, blog-aware, static site generator development
package.

Jekyll is a simple, blog aware, static site generator.

%description   -n gem-jekyll-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jekyll.


%prep
%setup
#%patch -p1

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n jekyll
%doc README.markdown
%_bindir/jekyll

%files         -n gem-jekyll-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-jekyll-devel
%doc README.markdown


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 4.2.0-alt1.1
- ! spec

* Wed Mar 03 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 4.2.0-alt1
- initial build
