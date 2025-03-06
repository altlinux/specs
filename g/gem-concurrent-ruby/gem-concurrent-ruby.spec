%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname concurrent-ruby

Name:          gem-concurrent-ruby
Version:       1.3.5
Release:       alt1
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more
License:       MIT
Group:         Development/Ruby
Url:           http://www.concurrent-ruby.com
Vcs:           https://github.com/ruby-concurrency/concurrent-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Source1:       concurrent_ruby.jar
BuildRequires(pre): rpm-build-ruby
BuildRequires: fakegit
%if_enabled check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 1.0.7
BuildRequires: gem(rake-compiler-dock) >= 1.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rake-compiler-dock) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Requires:      ruby >= 2.3
Obsoletes:     ruby-concurrent-ruby < %EVR
Provides:      ruby-concurrent-ruby = %EVR
Provides:      gem(concurrent-ruby) = 1.3.5

%ruby_on_build_rake_tasks repackage:all

%description
Modern concurrency tools for Ruby. Inspired by Erlang, Clojure, Scala, Haskell,
F#, C#, Java, and classic concurrency patterns.

The design goals of this gem are:

* Be an 'unopinionated' toolbox that provides useful utilities without debating
which is better or why
* Remain free of external gem dependencies
* Stay true to the spirit of the languages providing inspiration
* But implement in a way that makes sense for Ruby
* Keep the semantics as idiomatic Ruby as possible
* Support features that make sense in Ruby
* Exclude features that don't make sense in Ruby
* Be small, lean, and loosely coupled
* Thread-safety
* Backward compatibility


%package       -n gem-concurrent-ruby-edge
Version:       0.7.2
Release:       alt1
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.3
Requires:      gem(concurrent-ruby) >= 1.3
Conflicts:     gem(concurrent-ruby) >= 2
Provides:      concurrent-ruby-edge = %EVR
Provides:      gem(concurrent-ruby-edge) = 0.7.2

%description   -n gem-concurrent-ruby-edge
These features are under active development and may change frequently. They are
expected not to keep backward compatibility (there may also lack tests and
documentation). Semantic versions will be obeyed though. Features developed in
`concurrent-ruby-edge` are expected to move to `concurrent-ruby` when final.
Please see http://concurrent-ruby.com for more information.


%if_enabled    doc
%package       -n gem-concurrent-ruby-edge-doc
Version:       0.7.2
Release:       alt1
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета concurrent-ruby-edge
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(concurrent-ruby-edge) = 0.7.2

%description   -n gem-concurrent-ruby-edge-doc
Modern concurrency tools including agents, futures, promises, thread pools,
supervisors, and more documentation files.

These features are under active development and may change frequently. They are
expected not to keep backward compatibility (there may also lack tests and
documentation). Semantic versions will be obeyed though. Features developed in
`concurrent-ruby-edge` are expected to move to `concurrent-ruby` when final.
Please see http://concurrent-ruby.com for more information.

%description   -n gem-concurrent-ruby-edge-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета concurrent-ruby-edge.
%endif


%if_enabled    devel
%package       -n gem-concurrent-ruby-edge-devel
Version:       0.7.2
Release:       alt1
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета concurrent-ruby-edge
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(concurrent-ruby-edge) = 0.7.2
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) > 1.2.4
Requires:      gem(rake-compiler-dock) >= 1.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler-dock) >= 2

%description   -n gem-concurrent-ruby-edge-devel
Modern concurrency tools including agents, futures, promises, thread pools,
supervisors, and more development package.

These features are under active development and may change frequently. They are
expected not to keep backward compatibility (there may also lack tests and
documentation). Semantic versions will be obeyed though. Features developed in
`concurrent-ruby-edge` are expected to move to `concurrent-ruby` when final.
Please see http://concurrent-ruby.com for more information.

%description   -n gem-concurrent-ruby-edge-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета concurrent-ruby-edge.
%endif


%package       -n gem-concurrent-ruby-ext
Version:       1.3.5
Release:       alt1
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more
Group:         Development/Ruby

Requires:      ruby >= 2.3
Requires:      gem(concurrent-ruby) = 1.3.5
Requires:      gem(concurrent-ruby-edge) = 0.7.2
Provides:      concurrent-ruby-ext = %EVR
Provides:      gem(concurrent-ruby-ext) = 1.3.5

%description   -n gem-concurrent-ruby-ext
C extensions to optimize the concurrent-ruby gem when running under MRI. Please
see http://concurrent-ruby.com for more information.


%if_enabled    doc
%package       -n gem-concurrent-ruby-ext-doc
Version:       1.3.5
Release:       alt1
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета concurrent-ruby-ext
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(concurrent-ruby-ext) = 1.3.5

%description   -n gem-concurrent-ruby-ext-doc
Modern concurrency tools including agents, futures, promises, thread pools,
supervisors, and more documentation files.

C extensions to optimize the concurrent-ruby gem when running under MRI. Please
see http://concurrent-ruby.com for more information.

%description   -n gem-concurrent-ruby-ext-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета concurrent-ruby-ext.
%endif


%if_enabled    devel
%package       -n gem-concurrent-ruby-ext-devel
Version:       1.3.5
Release:       alt1
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета concurrent-ruby-ext
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(concurrent-ruby-ext) = 1.3.5
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) > 1.2.4
Requires:      gem(rake-compiler-dock) >= 1.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler-dock) >= 2

%description   -n gem-concurrent-ruby-ext-devel
Modern concurrency tools including agents, futures, promises, thread pools,
supervisors, and more development package.

C extensions to optimize the concurrent-ruby gem when running under MRI. Please
see http://concurrent-ruby.com for more information.

%description   -n gem-concurrent-ruby-ext-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета concurrent-ruby-ext.
%endif


%if_enabled    doc
%package       -n gem-concurrent-ruby-doc
Version:       1.3.5
Release:       alt1
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета concurrent-ruby
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(concurrent-ruby) = 1.3.5

%description   -n gem-concurrent-ruby-doc
Modern concurrency tools including agents, futures, promises, thread pools,
supervisors, and more documentation files.

Modern concurrency tools for Ruby. Inspired by Erlang, Clojure, Scala, Haskell,
F#, C#, Java, and classic concurrency patterns.

The design goals of this gem are:

* Be an 'unopinionated' toolbox that provides useful utilities without debating
which is better or why
* Remain free of external gem dependencies
* Stay true to the spirit of the languages providing inspiration
* But implement in a way that makes sense for Ruby
* Keep the semantics as idiomatic Ruby as possible
* Support features that make sense in Ruby
* Exclude features that don't make sense in Ruby
* Be small, lean, and loosely coupled
* Thread-safety
* Backward compatibility

%description   -n gem-concurrent-ruby-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета concurrent-ruby.
%endif


%if_enabled    devel
%package       -n gem-concurrent-ruby-devel
Version:       1.3.5
Release:       alt1
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета concurrent-ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(concurrent-ruby) = 1.3.5
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) > 1.2.4
Requires:      gem(rake-compiler-dock) >= 1.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler-dock) >= 2

%description   -n gem-concurrent-ruby-devel
Modern concurrency tools including agents, futures, promises, thread pools,
supervisors, and more development package.

Modern concurrency tools for Ruby. Inspired by Erlang, Clojure, Scala, Haskell,
F#, C#, Java, and classic concurrency patterns.

The design goals of this gem are:

* Be an 'unopinionated' toolbox that provides useful utilities without debating
which is better or why
* Remain free of external gem dependencies
* Stay true to the spirit of the languages providing inspiration
* But implement in a way that makes sense for Ruby
* Keep the semantics as idiomatic Ruby as possible
* Support features that make sense in Ruby
* Exclude features that don't make sense in Ruby
* Be small, lean, and loosely coupled
* Thread-safety
* Backward compatibility

%description   -n gem-concurrent-ruby-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета concurrent-ruby.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install
# TODO: de-build-in
install -D -m644 %SOURCE1 %buildroot%ruby_gemlibdir/lib/concurrent-ruby/concurrent/concurrent_ruby.jar

%check
%ruby_test

%files
%doc CHANGELOG.md LICENSE.txt README.md CODE_OF_CONDUCT.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-concurrent-ruby-edge
%doc CHANGELOG.md LICENSE.txt README.md CODE_OF_CONDUCT.md
%ruby_gemspecdir/concurrent-ruby-edge-0.7.2.gemspec
%ruby_gemslibdir/concurrent-ruby-edge-0.7.2

%if_enabled    doc
%files         -n gem-concurrent-ruby-edge-doc
%doc CHANGELOG.md LICENSE.txt README.md CODE_OF_CONDUCT.md
%ruby_gemsdocdir/concurrent-ruby-edge-0.7.2
%endif

%if_enabled    devel
%files         -n gem-concurrent-ruby-edge-devel
%doc CHANGELOG.md LICENSE.txt README.md CODE_OF_CONDUCT.md
%endif

%files         -n gem-concurrent-ruby-ext
%doc CHANGELOG.md LICENSE.txt README.md CODE_OF_CONDUCT.md
%ruby_gemspecdir/concurrent-ruby-ext-1.3.5.gemspec
%ruby_gemslibdir/concurrent-ruby-ext-1.3.5
%ruby_gemsextdir/concurrent-ruby-ext-1.3.5

%if_enabled    doc
%files         -n gem-concurrent-ruby-ext-doc
%doc CHANGELOG.md LICENSE.txt README.md CODE_OF_CONDUCT.md
%ruby_gemsdocdir/concurrent-ruby-ext-1.3.5
%endif

%if_enabled    devel
%files         -n gem-concurrent-ruby-ext-devel
%doc CHANGELOG.md LICENSE.txt README.md CODE_OF_CONDUCT.md
%ruby_includedir/*
%endif

%if_enabled    doc
%files         -n gem-concurrent-ruby-doc
%doc CHANGELOG.md LICENSE.txt README.md CODE_OF_CONDUCT.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-concurrent-ruby-devel
%doc CHANGELOG.md LICENSE.txt README.md CODE_OF_CONDUCT.md
%endif


%changelog
* Thu Mar 06 2025 Pavel Skrylev <majioa@altlinux.org> 1.3.5-alt1
- ^ 1.2.3 -> 1.3.5

* Wed Feb 21 2024 Pavel Skrylev <majioa@altlinux.org> 1.2.3-alt1
- ^ 1.2.2 -> 1.2.3

* Tue Apr 11 2023 Pavel Skrylev <majioa@altlinux.org> 1.2.2-alt1
- ^ 1.1.9 -> 1.2.2

* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.9-alt1
- ^ 1.1.7 -> 1.1.9

* Tue Sep 15 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.7-alt2
- ^ 1.1.6 -> 1.1.7

* Tue May 12 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.6-alt2
- + java part

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.6-alt1
- ^ concurrent-ruby 1.1.5 -> 1.1.6
- ^ concurrent-ruby-ext 1.1.5 -> 1.1.6
- ^ concurrent-ruby-edge 0.5.0 -> 0.6.0
- ! spec syntax

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.5-alt1
- Bump to 1.1.5

* Mon Jan 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.4-alt1
- Bump to 1.1.4;
- Use Ruby Policy 2.0.

* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt2
- Gemify build for Sisyphus

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus
