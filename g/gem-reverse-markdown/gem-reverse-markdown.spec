%define        gemname reverse_markdown

Name:          gem-reverse-markdown
Version:       2.1.1
Release:       alt1.1
Summary:       Convert html code into markdown
License:       WTFPL
Group:         Development/Ruby
Url:           http://github.com/xijo/reverse_markdown
Vcs:           https://github.com/xijo/reverse_markdown.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(codeclimate-test-reporter) >= 0
BuildRequires: gem(nokogiri) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names reverse_markdown,reverse-markdown
Requires:      gem(nokogiri) >= 0
Provides:      gem(reverse_markdown) = 2.1.1


%description
Map simple html back into markdown, e.g. if you want to import existing html
data in your application.


%package       -n reverse-markdown
Version:       2.1.1
Release:       alt1.1
Summary:       Convert html code into markdown executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета reverse_markdown
Group:         Other
BuildArch:     noarch

Requires:      gem(reverse_markdown) = 2.1.1

%description   -n reverse-markdown
Convert html code into markdown executable(s).

Map simple html back into markdown, e.g. if you want to import existing html
data in your application.

%description   -n reverse-markdown -l ru_RU.UTF-8
Исполнямка для самоцвета reverse_markdown.


%package       -n gem-reverse-markdown-doc
Version:       2.1.1
Release:       alt1.1
Summary:       Convert html code into markdown documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета reverse_markdown
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(reverse_markdown) = 2.1.1

%description   -n gem-reverse-markdown-doc
Convert html code into markdown documentation files.

Map simple html back into markdown, e.g. if you want to import existing html
data in your application.

%description   -n gem-reverse-markdown-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета reverse_markdown.


%package       -n gem-reverse-markdown-devel
Version:       2.1.1
Release:       alt1.1
Summary:       Convert html code into markdown development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета reverse_markdown
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(reverse_markdown) = 2.1.1
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(kramdown) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(codeclimate-test-reporter) >= 0

%description   -n gem-reverse-markdown-devel
Convert html code into markdown development package.

Map simple html back into markdown, e.g. if you want to import existing html
data in your application.

%description   -n gem-reverse-markdown-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета reverse_markdown.


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

%files         -n reverse-markdown
%doc README.md
%_bindir/reverse_markdown

%files         -n gem-reverse-markdown-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-reverse-markdown-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1.1
- ! closes build req under the check condition

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- + packaged gem with Ruby Policy 2.0
