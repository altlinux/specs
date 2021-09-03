%define        gemname md2man

Name:          gem-md2man
Version:       5.1.2
Release:       alt1.1
Summary:       Converts markdown into UNIX manual pages
License:       ISC
Group:         Development/Ruby
Url:           https://sunaku.github.io/md2man/man
Vcs:           https://github.com/sunaku/md2man.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(binman) >= 5.0 gem(binman) < 6
BuildRequires: gem(redcarpet) >= 3.0 gem(redcarpet) < 4
BuildRequires: gem(rouge) >= 3.0 gem(rouge) < 4
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(rake) >= 12.0 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(binman) >= 5.0 gem(binman) < 6
Requires:      gem(redcarpet) >= 3.0 gem(redcarpet) < 4
Requires:      gem(rouge) >= 3.0 gem(rouge) < 4
Provides:      gem(md2man) = 5.1.2


%description
md2man - markdown to manpage

md2man is a Ruby library and a set of command-line programs that convert
Markdown into UNIX manpages as well as HTML webpages using Redcarpet.


%package       -n md2man-utils
Version:       5.1.2
Release:       alt1.1
Summary:       Converts markdown into UNIX manual pages executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета md2man
Group:         Other
BuildArch:     noarch

Requires:      gem(md2man) = 5.1.2

%description   -n md2man-utils
Converts markdown into UNIX manual pages executable(s).

md2man - markdown to manpage

md2man is a Ruby library and a set of command-line programs that convert
Markdown into UNIX manpages as well as HTML webpages using Redcarpet.

%description   -n md2man-utils -l ru_RU.UTF-8
Исполнямка для самоцвета md2man.


%package       -n gem-md2man-doc
Version:       5.1.2
Release:       alt1.1
Summary:       Converts markdown into UNIX manual pages documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета md2man
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(md2man) = 5.1.2

%description   -n gem-md2man-doc
Converts markdown into UNIX manual pages documentation files.

md2man - markdown to manpage

md2man is a Ruby library and a set of command-line programs that convert
Markdown into UNIX manpages as well as HTML webpages using Redcarpet.

%description   -n gem-md2man-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета md2man.


%package       -n gem-md2man-devel
Version:       5.1.2
Release:       alt1.1
Summary:       Converts markdown into UNIX manual pages development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета md2man
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(md2man) = 5.1.2
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(rake) >= 12.0 gem(rake) < 14

%description   -n gem-md2man-devel
Converts markdown into UNIX manual pages development package.

md2man - markdown to manpage

md2man is a Ruby library and a set of command-line programs that convert
Markdown into UNIX manpages as well as HTML webpages using Redcarpet.

%description   -n gem-md2man-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета md2man.


%prep
%setup

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

%files         -n md2man-utils
%doc README.markdown
%_bindir/md2man-html
%_bindir/md2man-rake
%_bindir/md2man-roff

%files         -n gem-md2man-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-md2man-devel
%doc README.markdown


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 5.1.2-alt1.1
- ! spec

* Mon Apr 29 2019 Pavel Skrylev <majioa@altlinux.org> 5.1.2-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
