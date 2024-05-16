%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname pandoc-ruby

Name:          gem-pandoc-ruby
Version:       2.1.10
Release:       alt1
Summary:       PandocRuby
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/xwmx/pandoc-ruby
Vcs:           https://github.com/xwmx/pandoc-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rubocop) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(pandoc-ruby) = 2.1.10
Requires:      pandoc


%description
PandocRuby is a wrapper for Pandoc, a Haskell library with command line tools
for converting one markup format to another.

Pandoc can convert documents from a variety of formats including markdown,
reStructuredText, textile, HTML, DocBook, LaTeX, and MediaWiki markup to a
variety of other formats, including markdown, reStructuredText, HTML, LaTeX,
ConTeXt, PDF, RTF, DocBook XML, OpenDocument XML, ODT, GNU Texinfo, MediaWiki
markup, groff man pages, HTML slide shows, EPUB, Microsoft Word docx, and more.


%if_enabled    doc
%package       -n gem-pandoc-ruby-doc
Version:       2.1.10
Release:       alt1
Summary:       PandocRuby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pandoc-ruby
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pandoc-ruby) = 2.1.10

%description   -n gem-pandoc-ruby-doc
PandocRuby documentation files.

PandocRuby is a wrapper for Pandoc, a Haskell library with command line tools
for converting one markup format to another.

Pandoc can convert documents from a variety of formats including markdown,
reStructuredText, textile, HTML, DocBook, LaTeX, and MediaWiki markup to a
variety of other formats, including markdown, reStructuredText, HTML, LaTeX,
ConTeXt, PDF, RTF, DocBook XML, OpenDocument XML, ODT, GNU Texinfo, MediaWiki
markup, groff man pages, HTML slide shows, EPUB, Microsoft Word docx, and more.

%description   -n gem-pandoc-ruby-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pandoc-ruby.
%endif


%if_enabled    devel
%package       -n gem-pandoc-ruby-devel
Version:       2.1.10
Release:       alt1
Summary:       PandocRuby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pandoc-ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pandoc-ruby) = 2.1.10
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(rubocop) >= 0

%description   -n gem-pandoc-ruby-devel
PandocRuby development package.

PandocRuby is a wrapper for Pandoc, a Haskell library with command line tools
for converting one markup format to another.

Pandoc can convert documents from a variety of formats including markdown,
reStructuredText, textile, HTML, DocBook, LaTeX, and MediaWiki markup to a
variety of other formats, including markdown, reStructuredText, HTML, LaTeX,
ConTeXt, PDF, RTF, DocBook XML, OpenDocument XML, ODT, GNU Texinfo, MediaWiki
markup, groff man pages, HTML slide shows, EPUB, Microsoft Word docx, and more.

%description   -n gem-pandoc-ruby-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pandoc-ruby.
%endif


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

%if_enabled    doc
%files         -n gem-pandoc-ruby-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-pandoc-ruby-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 2.1.10-alt1
- + packaged gem with Ruby Policy 2.0
