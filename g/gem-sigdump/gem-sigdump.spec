%define        gemname sigdump

Name:          gem-sigdump
Version:       0.2.4.6
Release:       alt0.1
Summary:       Use signal to show stacktrace of a Ruby process without restarting it
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/frsyuki/sigdump/
Vcs:           https://github.com/frsyuki/sigdump.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0.9.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-sigdump < %EVR
Provides:      ruby-sigdump = %EVR
Provides:      gem(sigdump) = 0.2.4.6

%ruby_use_gem_version sigdump:0.2.4.6

%description
In short: SIGQUIT of Java VM for Ruby.

Server applications (like Rails apps) cause performance problems, deadlock or
memory swapping from time to time. But it's difficult to reproduce such kind of
problems. sigdump makes it possible to get information from a running process
without restarting. Just sending SIGCONT signal will dump backtrace and memory
profile to /tmp/sigdump-<pid>.log file.

sigdump dumps following information (see also Sample output):

* Backtrace of all threads
* Number of allocated objects per class
* GC profiler reports if GC profiler is enabled (GC::Profiler.enable is
called)
* Stacktrace of Java threads for each Ruby threads if the runtime is JRuby


%package       -n gem-sigdump-doc
Version:       0.2.4.6
Release:       alt0.1
Summary:       Use signal to show stacktrace of a Ruby process without restarting it documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sigdump
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sigdump) = 0.2.4.6

%description   -n gem-sigdump-doc
Use signal to show stacktrace of a Ruby process without restarting it
documentation files.

In short: SIGQUIT of Java VM for Ruby.

Server applications (like Rails apps) cause performance problems, deadlock or
memory swapping from time to time. But it's difficult to reproduce such kind of
problems. sigdump makes it possible to get information from a running process
without restarting. Just sending SIGCONT signal will dump backtrace and memory
profile to /tmp/sigdump-<pid>.log file.

sigdump dumps following information (see also Sample output):

* Backtrace of all threads
* Number of allocated objects per class
* GC profiler reports if GC profiler is enabled (GC::Profiler.enable is
called)
* Stacktrace of Java threads for each Ruby threads if the runtime is JRuby

%description   -n gem-sigdump-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sigdump.


%package       -n gem-sigdump-devel
Version:       0.2.4.6
Release:       alt0.1
Summary:       Use signal to show stacktrace of a Ruby process without restarting it development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sigdump
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sigdump) = 0.2.4.6
Requires:      gem(rake) >= 0.9.2

%description   -n gem-sigdump-devel
Use signal to show stacktrace of a Ruby process without restarting it
development package.

In short: SIGQUIT of Java VM for Ruby.

Server applications (like Rails apps) cause performance problems, deadlock or
memory swapping from time to time. But it's difficult to reproduce such kind of
problems. sigdump makes it possible to get information from a running process
without restarting. Just sending SIGCONT signal will dump backtrace and memory
profile to /tmp/sigdump-<pid>.log file.

sigdump dumps following information (see also Sample output):

* Backtrace of all threads
* Number of allocated objects per class
* GC profiler reports if GC profiler is enabled (GC::Profiler.enable is
called)
* Stacktrace of Java threads for each Ruby threads if the runtime is JRuby

%description   -n gem-sigdump-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sigdump.


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

%files         -n gem-sigdump-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sigdump-devel
%doc README.md


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 0.2.4.6-alt0.1
- ^ 0.2.4 -> 0.2.4p6

* Sun Sep 30 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.4-alt1
- Initial build for Sisyphus
