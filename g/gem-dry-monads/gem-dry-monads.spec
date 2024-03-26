%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dry-monads

Name:          gem-dry-monads
Version:       1.6.0
Release:       alt1
Summary:       Common monads for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-monads
Vcs:           https://github.com/dry-rb/dry-monads.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(warning) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(yard-junk) >= 0
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(dry-core) >= 1.0
BuildRequires: gem(zeitwerk) >= 2.6
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(dry-core) >= 2
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(dry-core) >= 1.0
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(dry-core) >= 2
Conflicts:     gem(zeitwerk) >= 3
Provides:      gem(dry-monads) = 1.6.0


%description
dry-monads is a set of common monads for Ruby. Monads provide an elegant way of
handling errors, exceptions and chaining functions so that the code is much more
understandable and has all the error handling, without all the ifs and elses.
The gem was inspired by the Kleisli gem.

What is a monad, anyway? Simply, a monoid in the category of endofunctors. The
term comes from category theory and some believe monads are tough to understand
or explain. It's hard to say why people think so because you certainly don't
need to know category theory for using them, just like you don't need it for,
say, using functions.


%if_enabled    doc
%package       -n gem-dry-monads-doc
Version:       1.6.0
Release:       alt1
Summary:       Common monads for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-monads
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dry-monads) = 1.6.0

%description   -n gem-dry-monads-doc
Common monads for Ruby documentation files.

dry-monads is a set of common monads for Ruby. Monads provide an elegant way of
handling errors, exceptions and chaining functions so that the code is much more
understandable and has all the error handling, without all the ifs and elses.
The gem was inspired by the Kleisli gem.

What is a monad, anyway? Simply, a monoid in the category of endofunctors. The
term comes from category theory and some believe monads are tough to understand
or explain. It's hard to say why people think so because you certainly don't
need to know category theory for using them, just like you don't need it for,
say, using functions.

%description   -n gem-dry-monads-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-monads.
%endif


%if_enabled    devel
%package       -n gem-dry-monads-devel
Version:       1.6.0
Release:       alt1
Summary:       Common monads for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-monads
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dry-monads) = 1.6.0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(warning) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(bundler) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(yard-junk) >= 0
Conflicts:     gem(rubocop) >= 2

%description   -n gem-dry-monads-devel
Common monads for Ruby development package.

dry-monads is a set of common monads for Ruby. Monads provide an elegant way of
handling errors, exceptions and chaining functions so that the code is much more
understandable and has all the error handling, without all the ifs and elses.
The gem was inspired by the Kleisli gem.

What is a monad, anyway? Simply, a monoid in the category of endofunctors. The
term comes from category theory and some believe monads are tough to understand
or explain. It's hard to say why people think so because you certainly don't
need to know category theory for using them, just like you don't need it for,
say, using functions.

%description   -n gem-dry-monads-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dry-monads.
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
%files         -n gem-dry-monads-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-monads-devel
%doc README.md
%endif


%changelog
* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- + packaged gem with Ruby Policy 2.0
