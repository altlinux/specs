%define        gemname binman

Name:          gem-binman
Version:       5.1.0.3
Release:       alt0.1
Summary:       Creates manual pages from header comments
License:       ISC
Group:         Development/Ruby
Url:           http://sunaku.github.io/binman/man/
Vcs:           https://github.com/sunaku/binman.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(md2man) >= 5.1
BuildRequires: gem(rake) >= 10.1
BuildRequires: gem(opener) >= 0.1.0
BuildConflicts: gem(md2man) >= 6
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(opener) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(opener) >= 0.1.0
Conflicts:     gem(opener) >= 1
Provides:      gem(binman) = 5.1.0.3

%ruby_use_gem_version binman:5.1.0.3

%description
binman generates manual pages from header comments in your scripts so that you
can keep your documentation and implementation together, in the same file, for
easy maintenance. But keeping them apart, in separate files, is supported too.


%package       -n binman
Version:       5.1.0.3
Release:       alt0.1
Summary:       Creates manual pages from header comments executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета binman
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(binman) = 5.1.0.3

%description   -n binman
Creates manual pages from header comments executable(s).

binman generates manual pages from header comments in your scripts so that you
can keep your documentation and implementation together, in the same file, for
easy maintenance. But keeping them apart, in separate files, is supported too.

%description   -n binman -l ru_RU.UTF-8
Исполнямка для самоцвета binman.


%package       -n gem-binman-doc
Version:       5.1.0.3
Release:       alt0.1
Summary:       Creates manual pages from header comments documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета binman
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(binman) = 5.1.0.3

%description   -n gem-binman-doc
Creates manual pages from header comments documentation files.

binman generates manual pages from header comments in your scripts so that you
can keep your documentation and implementation together, in the same file, for
easy maintenance. But keeping them apart, in separate files, is supported too.

%description   -n gem-binman-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета binman.


%package       -n gem-binman-devel
Version:       5.1.0.3
Release:       alt0.1
Summary:       Creates manual pages from header comments development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета binman
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(binman) = 5.1.0.3
Requires:      gem(md2man) >= 5.1
Requires:      gem(rake) >= 10.1
Conflicts:     gem(md2man) >= 6
Conflicts:     gem(rake) >= 14

%description   -n gem-binman-devel
Creates manual pages from header comments development package.

binman generates manual pages from header comments in your scripts so that you
can keep your documentation and implementation together, in the same file, for
easy maintenance. But keeping them apart, in separate files, is supported too.

%description   -n gem-binman-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета binman.


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

%files         -n binman
%doc README.markdown
%_bindir/binman
%_bindir/binman-help
%_bindir/binman-html
%_bindir/binman-rake
%_bindir/binman-roff
%_bindir/binman-show
%_bindir/binman-text

%files         -n gem-binman-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-binman-devel
%doc README.markdown


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 5.1.0.3-alt0.1
- ^ 5.1.0[1] -> 5.1.0[3]

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 5.1.0.1-alt0.1
- ^ 5.1.0 -> 5.1.0[.1]

* Mon Apr 29 2019 Pavel Skrylev <majioa@altlinux.org> 5.1.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
