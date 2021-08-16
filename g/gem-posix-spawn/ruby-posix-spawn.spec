%define        gemname posix-spawn

Name:          gem-posix-spawn
Version:       0.3.15
Release:       alt1
Summary:       Ruby process spawning library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rtomayko/posix-spawn
Vcs:           https://github.com/rtomayko/posix-spawn.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake-compiler) >= 0.7.6 gem(rake-compiler) < 2
BuildRequires: gem(minitest) >= 4 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Obsoletes:     ruby-posix-spawn < %EVR
Provides:      ruby-posix-spawn = %EVR
Provides:      gem(posix-spawn) = 0.3.15


%description
Ruby process spawning library.

fork(2) calls slow down as the parent process uses more memory due to the need
to copy page tables. In many common uses of fork(), where it is followed by one
of the exec family of functions to spawn child processes (Kernel#system,
IO::popen, Process::spawn, etc.), it's possible to remove this overhead by using
special process spawning interfaces (posix_spawn(), vfork(), etc.)

The posix-spawn library aims to implement a subset of the Ruby 1.9
Process::spawn interface in a way that takes advantage of fast process spawning
interfaces when available and provides sane fallbacks on systems that do not.


%package       -n posix-spawn-benchmark
Version:       0.3.15
Release:       alt1
Summary:       Ruby process spawning library executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета posix-spawn
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(posix-spawn) = 0.3.15

%description   -n posix-spawn-benchmark
Ruby process spawning library executable(s).

fork(2) calls slow down as the parent process uses more memory due to the need
to copy page tables. In many common uses of fork(), where it is followed by one
of the exec family of functions to spawn child processes (Kernel#system,
IO::popen, Process::spawn, etc.), it's possible to remove this overhead by using
special process spawning interfaces (posix_spawn(), vfork(), etc.)

The posix-spawn library aims to implement a subset of the Ruby 1.9
Process::spawn interface in a way that takes advantage of fast process spawning
interfaces when available and provides sane fallbacks on systems that do not.

%description   -n posix-spawn-benchmark -l ru_RU.UTF-8
Исполнямка для самоцвета posix-spawn.


%package       -n gem-posix-spawn-doc
Version:       0.3.15
Release:       alt1
Summary:       Ruby process spawning library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета posix-spawn
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(posix-spawn) = 0.3.15

%description   -n gem-posix-spawn-doc
Ruby process spawning library documentation files.

fork(2) calls slow down as the parent process uses more memory due to the need
to copy page tables. In many common uses of fork(), where it is followed by one
of the exec family of functions to spawn child processes (Kernel#system,
IO::popen, Process::spawn, etc.), it's possible to remove this overhead by using
special process spawning interfaces (posix_spawn(), vfork(), etc.)

The posix-spawn library aims to implement a subset of the Ruby 1.9
Process::spawn interface in a way that takes advantage of fast process spawning
interfaces when available and provides sane fallbacks on systems that do not.

%description   -n gem-posix-spawn-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета posix-spawn.


%package       -n gem-posix-spawn-devel
Version:       0.3.15
Release:       alt1
Summary:       Ruby process spawning library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета posix-spawn
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(posix-spawn) = 0.3.15
Requires:      gem(rake-compiler) >= 0.7.6 gem(rake-compiler) < 2
Requires:      gem(minitest) >= 4 gem(minitest) < 6

%description   -n gem-posix-spawn-devel
Ruby process spawning library development package.

fork(2) calls slow down as the parent process uses more memory due to the need
to copy page tables. In many common uses of fork(), where it is followed by one
of the exec family of functions to spawn child processes (Kernel#system,
IO::popen, Process::spawn, etc.), it's possible to remove this overhead by using
special process spawning interfaces (posix_spawn(), vfork(), etc.)

The posix-spawn library aims to implement a subset of the Ruby 1.9
Process::spawn interface in a way that takes advantage of fast process spawning
interfaces when available and provides sane fallbacks on systems that do not.

%description   -n gem-posix-spawn-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета posix-spawn.


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
%ruby_gemextdir

%files         -n posix-spawn-benchmark
%doc README.md
%_bindir/posix-spawn-benchmark

%files         -n gem-posix-spawn-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-posix-spawn-devel
%doc README.md


%changelog
* Mon Jun 28 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.15-alt1
- ^ 0.3.13 -> 0.3.15

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.3.13-alt2.3
- fixed (!) spec

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.3.13-alt2.2
- fixed (!) spec according to changelog rules

* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 0.3.13-alt2.1
- fixed (!) spec

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.3.13-alt2
- used (>) Ruby Policy 2.0

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.13-alt1
- Initial build for Sisyphus
