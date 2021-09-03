%define        gemname hoe-markdown

Name:          gem-hoe-markdown
Version:       1.4.0
Release:       alt1
Summary:       Hoe (rubygem) plugin to hyperlink your markdown documentation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/flavorjones/hoe-markdown
Vcs:           https://github.com/flavorjones/hoe-markdown.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) > 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(rake) > 0
Provides:      gem(hoe-markdown) = 1.4.0


%description
Hoe plugin with markdown helpers, for example to hyperlink github issues and
github usernames in markdown files.

Hoe::Markdown is a Hoe plugin to help manage your project's markdown files. It's
intended for gem maintainers, but the underlying library of markdown
manipulation methods might be generally useful.


%package       -n gem-hoe-markdown-doc
Version:       1.4.0
Release:       alt1
Summary:       Hoe (rubygem) plugin to hyperlink your markdown documentation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-markdown
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-markdown) = 1.4.0

%description   -n gem-hoe-markdown-doc
Hoe (rubygem) plugin to hyperlink your markdown documentation documentation
files.

Hoe plugin with markdown helpers, for example to hyperlink github issues and
github usernames in markdown files.

Hoe::Markdown is a Hoe plugin to help manage your project's markdown files. It's
intended for gem maintainers, but the underlying library of markdown
manipulation methods might be generally useful.

%description   -n gem-hoe-markdown-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-markdown.


%package       -n gem-hoe-markdown-devel
Version:       1.4.0
Release:       alt1
Summary:       Hoe (rubygem) plugin to hyperlink your markdown documentation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-markdown
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-markdown) = 1.4.0

%description   -n gem-hoe-markdown-devel
Hoe (rubygem) plugin to hyperlink your markdown documentation development
package.

Hoe plugin with markdown helpers, for example to hyperlink github issues and
github usernames in markdown files.

Hoe::Markdown is a Hoe plugin to help manage your project's markdown files. It's
intended for gem maintainers, but the underlying library of markdown
manipulation methods might be generally useful.

%description   -n gem-hoe-markdown-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-markdown.


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

%files         -n gem-hoe-markdown-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hoe-markdown-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- ^ 1.1.0 -> 1.4.0

* Tue Jun 9 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with usage Ruby Policy 2.0
