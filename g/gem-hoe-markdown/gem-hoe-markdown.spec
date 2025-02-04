%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hoe-markdown

Name:          gem-hoe-markdown
Version:       1.7.0
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
%if_enabled check
BuildRequires: gem(rspec) >= 3.0
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.3.0
Requires:      gem(rake) > 0
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(rspec) >= 4
Provides:      hoe-markdown = %EVR
Provides:      gem(hoe-markdown) = 1.7.0

%description
Hoe plugin with markdown helpers, for example to hyperlink github issues and
github usernames in markdown files.

Hoe::Markdown is a Hoe plugin to help manage your project's markdown files. It's
intended for gem maintainers, but the underlying library of markdown
manipulation methods might be generally useful.


%if_enabled    doc
%package       -n gem-hoe-markdown-doc
Version:       1.7.0
Release:       alt1
Summary:       Hoe (rubygem) plugin to hyperlink your markdown documentation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-markdown
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-markdown) = 1.7.0

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
%endif


%if_enabled    devel
%package       -n gem-hoe-markdown-devel
Version:       1.7.0
Release:       alt1
Summary:       Hoe (rubygem) plugin to hyperlink your markdown documentation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-markdown
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-markdown) = 1.7.0

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
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-hoe-markdown-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hoe-markdown-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%endif


%changelog
* Fri Jan 10 2025 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- ^ 1.4.0 -> 1.7.0

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- ^ 1.1.0 -> 1.4.0

* Tue Jun 9 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with usage Ruby Policy 2.0
