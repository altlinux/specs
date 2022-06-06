%define        gemname concurrent-ruby

Name:          gem-concurrent-ruby
Version:       1.1.9
Release:       alt1
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more
License:       MIT
Group:         Development/Ruby
Url:           http://www.concurrent-ruby.com
Vcs:           https://github.com/ruby-concurrency/concurrent-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source1:       concurrent_ruby.jar
Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.16.1,simplecov < 1
%ruby_use_gem_dependency timecop >= 0.9.1,timecop < 1
Obsoletes:     ruby-concurrent-ruby < %EVR
Provides:      ruby-concurrent-ruby = %EVR
Provides:      gem(concurrent-ruby) = 1.1.9

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
Version:       0.6.0
Release:       alt2.2
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(concurrent-ruby) >= 1.1.9 gem(concurrent-ruby) < 1.2
Provides:      gem(concurrent-ruby-edge) = 0.6.0

%description   -n gem-concurrent-ruby-edge
These features are under active development and may change frequently. They are
expected not to keep backward compatibility (there may also lack tests and
documentation). Semantic versions will be obeyed though. Features developed in
`concurrent-ruby-edge` are expected to move to `concurrent-ruby` when final.
Please see http://concurrent-ruby.com for more information.


%package       -n gem-concurrent-ruby-edge-doc
Version:       0.6.0
Release:       alt2.2
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета concurrent-ruby-edge
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(concurrent-ruby-edge) = 0.6.0

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


%package       -n gem-concurrent-ruby-edge-devel
Version:       0.6.0
Release:       alt2.2
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета concurrent-ruby-edge
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(concurrent-ruby-edge) = 0.6.0

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


%package       -n gem-concurrent-ruby-ext
Version:       1.1.9
Release:       alt1
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more
Group:         Development/Ruby

Requires:      gem(concurrent-ruby) = 1.1.9
Provides:      gem(concurrent-ruby-ext) = 1.1.9

%description   -n gem-concurrent-ruby-ext
C extensions to optimize the concurrent-ruby gem when running under MRI. Please
see http://concurrent-ruby.com for more information.


%package       -n gem-concurrent-ruby-ext-doc
Version:       1.1.9
Release:       alt1
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета concurrent-ruby-ext
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(concurrent-ruby-ext) = 1.1.9

%description   -n gem-concurrent-ruby-ext-doc
Modern concurrency tools including agents, futures, promises, thread pools,
supervisors, and more documentation files.

C extensions to optimize the concurrent-ruby gem when running under MRI. Please
see http://concurrent-ruby.com for more information.

%description   -n gem-concurrent-ruby-ext-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета concurrent-ruby-ext.


%package       -n gem-concurrent-ruby-ext-devel
Version:       1.1.9
Release:       alt1
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета concurrent-ruby-ext
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(concurrent-ruby-ext) = 1.1.9

%description   -n gem-concurrent-ruby-ext-devel
Modern concurrency tools including agents, futures, promises, thread pools,
supervisors, and more development package.

C extensions to optimize the concurrent-ruby gem when running under MRI. Please
see http://concurrent-ruby.com for more information.

%description   -n gem-concurrent-ruby-ext-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета concurrent-ruby-ext.


%package       -n gem-concurrent-ruby-doc
Version:       1.1.9
Release:       alt1
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета concurrent-ruby
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(concurrent-ruby) = 1.1.9

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


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install
# TODO: de-build-in
install -D -m644 %SOURCE1 %buildroot%ruby_gemlibdir/lib/concurrent-ruby/concurrent/concurrent_ruby.jar

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-concurrent-ruby-edge
%doc README.md
%ruby_gemspecdir/concurrent-ruby-edge-0.6.0.gemspec
%ruby_gemslibdir/concurrent-ruby-edge-0.6.0

%files         -n gem-concurrent-ruby-edge-doc
%doc README.md
%ruby_gemsdocdir/concurrent-ruby-edge-0.6.0

%files         -n gem-concurrent-ruby-edge-devel
%doc README.md

%files         -n gem-concurrent-ruby-ext
%doc README.md
%ruby_gemspecdir/concurrent-ruby-ext-1.1.9.gemspec
%ruby_gemslibdir/concurrent-ruby-ext-1.1.9
%ruby_gemsextdir/concurrent-ruby-ext-1.1.9

%files         -n gem-concurrent-ruby-ext-doc
%doc README.md
%ruby_gemsdocdir/concurrent-ruby-ext-1.1.9

%files         -n gem-concurrent-ruby-ext-devel
%doc README.md
%ruby_includedir/*

%files         -n gem-concurrent-ruby-doc
%doc README.md
%ruby_gemdocdir


%changelog
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
