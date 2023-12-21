%define        _unpackaged_files_terminate_build 1
%define        gemname ronn-ng

Name:          gem-ronn-ng
Version:       0.9.1
Release:       alt1
Summary:       Builds man pages from Markdown
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/apjanke/ronn-ng
Vcs:           https://github.com/apjanke/ronn-ng.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rack) >= 2.0
BuildRequires: gem(rake) >= 12.3
BuildRequires: gem(rubocop) >= 0.57.1
BuildRequires: gem(sinatra) >= 2.0
BuildRequires: gem(test-unit) >= 3.2
BuildRequires: gem(kramdown) >= 2.1
BuildRequires: gem(mustache) >= 0.7
BuildRequires: gem(nokogiri) >= 1.9
BuildConflicts: gem(sinatra) >= 3
BuildConflicts: gem(kramdown) >= 3
BuildConflicts: gem(mustache) >= 2
BuildConflicts: gem(nokogiri) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 2.2.2,rack < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
%ruby_use_gem_dependency mustache >= 1.1.1,mustache < 2
Requires:      nokogiri
Requires:      ronn
Requires:      gem(kramdown) >= 2.1
Requires:      gem(mustache) >= 0.7
Requires:      gem(nokogiri) >= 1.9
Conflicts:     gem(kramdown) >= 3
Conflicts:     gem(mustache) >= 2
Conflicts:     gem(nokogiri) >= 2
Obsoletes:     gem-ronn < %EVR
Provides:      gem-ronn = %EVR
Provides:      gem(ronn-ng) = 0.9.1


%description
Ronn-NG builds manuals in HTML and Unix man page format from Markdown.


%package       -n ronn
Version:       0.9.1
Release:       alt1
Summary:       Builds man pages from Markdown executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ronn-ng
Group:         Other
BuildArch:     noarch

Requires:      gem(ronn-ng) = 0.9.1

%description   -n ronn
Builds man pages from Markdown executable(s).

Ronn-NG builds manuals in HTML and Unix man page format from Markdown.

%description   -n ronn -l ru_RU.UTF-8
Исполнямка для самоцвета ronn-ng.


%package       -n gem-ronn-ng-doc
Version:       0.9.1
Release:       alt1
Summary:       Builds man pages from Markdown documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ronn-ng
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ronn-ng) = 0.9.1

%description   -n gem-ronn-ng-doc
Builds man pages from Markdown documentation files.

Ronn-NG builds manuals in HTML and Unix man page format from Markdown.

%description   -n gem-ronn-ng-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ronn-ng.


%package       -n gem-ronn-ng-devel
Version:       0.9.1
Release:       alt1
Summary:       Builds man pages from Markdown development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ronn-ng
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ronn-ng) = 0.9.1
Requires:      gem(rack) >= 2.0
Requires:      gem(rake) >= 12.3
Requires:      gem(rubocop) >= 0.57.1
Requires:      gem(sinatra) >= 2.0
Requires:      gem(test-unit) >= 3.2
Conflicts:     gem(sinatra) >= 3

%description   -n gem-ronn-ng-devel
Builds man pages from Markdown development package.

Ronn-NG builds manuals in HTML and Unix man page format from Markdown.

%description   -n gem-ronn-ng-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ronn-ng.


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

%files         -n ronn
%doc README.md
%_bindir/ronn
%_mandir/*.xz

%files         -n gem-ronn-ng-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ronn-ng-devel
%doc README.md


%changelog
* Tue Dec 19 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.1-alt1
- + packaged gem with Ruby Policy 2.0 updating ronn executable (closes #48853)
