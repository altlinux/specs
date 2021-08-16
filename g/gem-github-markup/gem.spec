%define        gemname github-markup

Name:          gem-github-markup
Version:       4.0.0
Release:       alt1
Summary:       The code GitHub uses to render README.markup
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/github/markup
Vcs:           https://github.com/github/markup.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 12 gem(rake) < 14
BuildRequires: gem(minitest) >= 5.4 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(github-markup) = 4.0.0


%description
This gem is used by GitHub to render any fancy markup such as Markdown, Textile,
Org-Mode, etc. Fork it and add your own!


%package       -n github-markup
Version:       4.0.0
Release:       alt1
Summary:       The code GitHub uses to render README.markup executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета github-markup
Group:         Other
BuildArch:     noarch

Requires:      gem(github-markup) = 4.0.0

%description   -n github-markup
The code GitHub uses to render README.markup executable(s).

This gem is used by GitHub to render any fancy markup such as Markdown, Textile,
Org-Mode, etc. Fork it and add your own!

%description   -n github-markup -l ru_RU.UTF-8
Исполнямка для самоцвета github-markup.


%package       -n gem-github-markup-doc
Version:       4.0.0
Release:       alt1
Summary:       The code GitHub uses to render README.markup documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета github-markup
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(github-markup) = 4.0.0

%description   -n gem-github-markup-doc
The code GitHub uses to render README.markup documentation files.

This gem is used by GitHub to render any fancy markup such as Markdown, Textile,
Org-Mode, etc. Fork it and add your own!

%description   -n gem-github-markup-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета github-markup.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md test/markups/README.asciidoc test/markups/README.asciidoc.html test/markups/README.creole test/markups/README.creole.html test/markups/README.directives.rst test/markups/README.directives.rst.html test/markups/README.hidetitle.asciidoc test/markups/README.hidetitle.asciidoc.html test/markups/README.litcoffee test/markups/README.litcoffee.html test/markups/README.markdown test/markups/README.markdown.html test/markups/README.mediawiki test/markups/README.mediawiki.html test/markups/README.noformat test/markups/README.noformat.html test/markups/README.org test/markups/README.org.html test/markups/README.pod test/markups/README.pod.html test/markups/README.rdoc test/markups/README.rdoc.html test/markups/README.rst test/markups/README.rst.html test/markups/README.rst.txt test/markups/README.rst.txt.html test/markups/README.textile test/markups/README.textile.html test/markups/README.toc.asciidoc test/markups/README.toc.asciidoc.html test/markups/README.toc.rst test/markups/README.toc.rst.html test/markups/README.txt test/markups/README.txt.html
%ruby_gemspec
%ruby_gemlibdir

%files         -n github-markup
%doc README.md test/markups/README.asciidoc test/markups/README.asciidoc.html test/markups/README.creole test/markups/README.creole.html test/markups/README.directives.rst test/markups/README.directives.rst.html test/markups/README.hidetitle.asciidoc test/markups/README.hidetitle.asciidoc.html test/markups/README.litcoffee test/markups/README.litcoffee.html test/markups/README.markdown test/markups/README.markdown.html test/markups/README.mediawiki test/markups/README.mediawiki.html test/markups/README.noformat test/markups/README.noformat.html test/markups/README.org test/markups/README.org.html test/markups/README.pod test/markups/README.pod.html test/markups/README.rdoc test/markups/README.rdoc.html test/markups/README.rst test/markups/README.rst.html test/markups/README.rst.txt test/markups/README.rst.txt.html test/markups/README.textile test/markups/README.textile.html test/markups/README.toc.asciidoc test/markups/README.toc.asciidoc.html test/markups/README.toc.rst test/markups/README.toc.rst.html test/markups/README.txt test/markups/README.txt.html
%_bindir/github-markup

%files         -n gem-github-markup-doc
%doc README.md test/markups/README.asciidoc test/markups/README.asciidoc.html test/markups/README.creole test/markups/README.creole.html test/markups/README.directives.rst test/markups/README.directives.rst.html test/markups/README.hidetitle.asciidoc test/markups/README.hidetitle.asciidoc.html test/markups/README.litcoffee test/markups/README.litcoffee.html test/markups/README.markdown test/markups/README.markdown.html test/markups/README.mediawiki test/markups/README.mediawiki.html test/markups/README.noformat test/markups/README.noformat.html test/markups/README.org test/markups/README.org.html test/markups/README.pod test/markups/README.pod.html test/markups/README.rdoc test/markups/README.rdoc.html test/markups/README.rst test/markups/README.rst.html test/markups/README.rst.txt test/markups/README.rst.txt.html test/markups/README.textile test/markups/README.textile.html test/markups/README.toc.asciidoc test/markups/README.toc.asciidoc.html test/markups/README.toc.rst test/markups/README.toc.rst.html test/markups/README.txt test/markups/README.txt.html
%ruby_gemdocdir


%changelog
* Thu Jun 03 2021 Pavel Skrylev <majioa@altlinux.org> 4.0.0-alt1
- + packaged gem with Ruby Policy 2.0
