%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dry-monads

Name:          gem-dry-monads
Version:       1.10.0
Release:       alt1
Summary:       Common monads for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-monads
Vcs:           https://github.com/dry-rb/dry-monads.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(debug_inspector) >= 0
BuildRequires: gem(dry-core) >= 1.1
BuildRequires: gem(dry-types) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(super_diff) >= 0
BuildRequires: gem(warning) >= 0
BuildRequires: gem(zeitwerk) >= 2.6
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(dry-core) >= 2
BuildConflicts: gem(rdoc) >= 8.0
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.3
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(dry-core) >= 1.1
Requires:      gem(rake) >= 12.3.3
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(dry-core) >= 2
Conflicts:     gem(rdoc) >= 8.0
Conflicts:     gem(zeitwerk) >= 3
Provides:      dry-monads = %EVR
Provides:      gem(dry-monads) = 1.10.0

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
Version:       1.10.0
Release:       alt1
Summary:       Common monads for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-monads
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dry-monads) = 1.10.0

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
Version:       1.10.0
Release:       alt1
Summary:       Common monads for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-monads
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dry-monads) = 1.10.0
Requires:      gem(bundler) >= 0
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(debug_inspector) >= 0
Requires:      gem(dry-core) >= 1.1
Requires:      gem(dry-types) >= 0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rexml) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(super_diff) >= 0
Requires:      gem(warning) >= 0
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(dry-core) >= 2
Conflicts:     gem(rdoc) >= 8.0
Conflicts:     gem(zeitwerk) >= 3

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
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir
%_logdir/%gemname

%if_enabled    doc
%files         -n gem-dry-monads-doc
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-monads-devel
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%endif


%changelog
* Sun Aug 09 2026 Pavel Skrylev <majioa@altlinux.org> 1.10.0-alt1
- ^ 1.6.0 -> 1.10.0

* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- + packaged gem with Ruby Policy 2.0
