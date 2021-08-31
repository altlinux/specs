%define        gemname minitest-hooks

Name:          gem-minitest-hooks
Version:       1.5.0
Release:       alt1
Summary:       Around and before_all/after_all/around_all hooks for Minitest
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/jeremyevans/minitest-hooks
Vcs:           https://github.com/jeremyevans/minitest-hooks.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) > 5.3 gem(minitest) < 6
BuildRequires: gem(sequel) > 4
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(minitest) > 5.3 gem(minitest) < 6
Provides:      gem(minitest-hooks) = 1.5.0


%description
minitest-hooks adds around and before_all/after_all/around_all hooks for
Minitest. This allows you do things like run each suite of specs inside a
database transaction, running each spec inside its own savepoint inside that
transaction, which can significantly speed up testing for specs that share
expensive database setup code.


%package       -n gem-minitest-hooks-doc
Version:       1.5.0
Release:       alt1
Summary:       Around and before_all/after_all/around_all hooks for Minitest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-hooks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-hooks) = 1.5.0

%description   -n gem-minitest-hooks-doc
Around and before_all/after_all/around_all hooks for Minitest documentation
files.

minitest-hooks adds around and before_all/after_all/around_all hooks for
Minitest. This allows you do things like run each suite of specs inside a
database transaction, running each spec inside its own savepoint inside that
transaction, which can significantly speed up testing for specs that share
expensive database setup code.

%description   -n gem-minitest-hooks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-hooks.


%package       -n gem-minitest-hooks-devel
Version:       1.5.0
Release:       alt1
Summary:       Around and before_all/after_all/around_all hooks for Minitest development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-hooks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-hooks) = 1.5.0
Requires:      gem(sequel) > 4
Requires:      gem(sqlite3) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-minitest-hooks-devel
Around and before_all/after_all/around_all hooks for Minitest development
package.

minitest-hooks adds around and before_all/after_all/around_all hooks for
Minitest. This allows you do things like run each suite of specs inside a
database transaction, running each spec inside its own savepoint inside that
transaction, which can significantly speed up testing for specs that share
expensive database setup code.

%description   -n gem-minitest-hooks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-hooks.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-minitest-hooks-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-minitest-hooks-devel
%doc README.rdoc


%changelog
* Sun Jul 18 2021 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- + packaged gem with Ruby Policy 2.0
