%define        gemname em-synchrony

Name:          gem-em-synchrony
Version:       1.0.6
Release:       alt2
Summary:       Fiber aware EventMachine clients and convenience classes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/igrigorik/em-synchrony
Vcs:           https://github.com/igrigorik/em-synchrony.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(eventmachine) >= 1.0.0.beta.1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(eventmachine) >= 1.0.0.beta.1
Obsoletes:     ruby-em-synchrony < %EVR
Provides:      ruby-em-synchrony = %EVR
Provides:      gem(em-synchrony) = 1.0.6


%description
Collection of convenience classes and primitives to help untangle evented code,
plus a number of patched EM clients to make them Fiber aware. To learn more,
please see: Untangling Evented Code with Ruby Fibers.

* Fiber aware ConnectionPool with sync/async query support
* Fiber aware Iterator to allow concurrency control & mixing of sync/async
* Fiber aware async inline support: turns any async function into sync
* Fiber aware Multi-request interface for any callback enabled clients
* Fiber aware TCPSocket replacement, powered by EventMachine
* Fiber aware Thread, Mutex, ConditionVariable clases
* Fiber aware sleep, defer, system


%package       -n gem-em-synchrony-doc
Version:       1.0.6
Release:       alt2
Summary:       Fiber aware EventMachine clients and convenience classes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета em-synchrony
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(em-synchrony) = 1.0.6

%description   -n gem-em-synchrony-doc
Fiber aware EventMachine clients and convenience classes documentation
files.

Collection of convenience classes and primitives to help untangle evented code,
plus a number of patched EM clients to make them Fiber aware. To learn more,
please see: Untangling Evented Code with Ruby Fibers.

* Fiber aware ConnectionPool with sync/async query support
* Fiber aware Iterator to allow concurrency control & mixing of sync/async
* Fiber aware async inline support: turns any async function into sync
* Fiber aware Multi-request interface for any callback enabled clients
* Fiber aware TCPSocket replacement, powered by EventMachine
* Fiber aware Thread, Mutex, ConditionVariable clases
* Fiber aware sleep, defer, system

%description   -n gem-em-synchrony-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета em-synchrony.


%package       -n gem-em-synchrony-devel
Version:       1.0.6
Release:       alt2
Summary:       Fiber aware EventMachine clients and convenience classes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета em-synchrony
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(em-synchrony) = 1.0.6

%description   -n gem-em-synchrony-devel
Fiber aware EventMachine clients and convenience classes development
package.

Collection of convenience classes and primitives to help untangle evented code,
plus a number of patched EM clients to make them Fiber aware. To learn more,
please see: Untangling Evented Code with Ruby Fibers.

* Fiber aware ConnectionPool with sync/async query support
* Fiber aware Iterator to allow concurrency control & mixing of sync/async
* Fiber aware async inline support: turns any async function into sync
* Fiber aware Multi-request interface for any callback enabled clients
* Fiber aware TCPSocket replacement, powered by EventMachine
* Fiber aware Thread, Mutex, ConditionVariable clases
* Fiber aware sleep, defer, system

%description   -n gem-em-synchrony-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета em-synchrony.


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

%files         -n gem-em-synchrony-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-em-synchrony-devel
%doc README.md


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.6-alt2
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.6-alt1.1
- Rebuild with new Ruby autorequirements.

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.6-alt1
- new version 1.0.6

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- new version 1.0.5

* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- Initial build for ALT Linux
