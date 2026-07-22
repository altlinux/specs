%define        _unpackaged_files_terminate_build 1
%def_disable    check
%def_enable    doc
%def_enable    devel
%define        gemname nenv

Name:          gem-nenv
Version:       0.3.0
Release:       alt1
Summary:       Convenience wrapper for Ruby's ENV
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/e2/nenv
Vcs:           https://github.com/e2/nenv.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.7
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(guard-rspec) >= 4.5
BuildRequires: gem(guard-rubocop) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rspec) >= 3.1
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(guard-rspec) >= 5
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.5.9,bundler < 3
%ruby_use_gem_dependency rake >= 13.3.1,rake < 14
Provides:      gem(nenv) = 0.3.0

%description
Using ENV is like using raw SQL statements in your code. We all know how that
ends...


%if_enabled    doc
%package       -n gem-nenv-doc
Version:       0.3.0
Release:       alt1
Summary:       Convenience wrapper for Ruby's ENV documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета nenv
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(nenv) = 0.3.0

%description   -n gem-nenv-doc
Convenience wrapper for Ruby's ENV documentation files.

Using ENV is like using raw SQL statements in your code. We all know how that
ends...

%description   -n gem-nenv-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета nenv.
%endif


%if_enabled    devel
%package       -n gem-nenv-devel
Version:       0.3.0
Release:       alt1
Summary:       Convenience wrapper for Ruby's ENV development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета nenv
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(nenv) = 0.3.0
Requires:      gem(bundler) >= 1.7
Requires:      gem(coveralls) >= 0
Requires:      gem(guard-rspec) >= 4.5
Requires:      gem(guard-rubocop) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 10.0
Requires:      gem(rspec) >= 3.1
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(guard-rspec) >= 5
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-nenv-devel
Convenience wrapper for Ruby's ENV development package.

Using ENV is like using raw SQL statements in your code. We all know how that
ends...

%description   -n gem-nenv-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета nenv.
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-nenv-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-nenv-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Tue Jul 07 2026 Alexander Burmatov <thatman@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
