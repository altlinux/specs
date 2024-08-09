%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname cool.io

Name:          gem-cool-io
Version:       1.8.1
Release:       alt1
Summary:       Simple evented I/O for Ruby (but please check out Celluloid::IO instead)
License:       MIT
Group:         Development/Ruby
Url:           https://coolio.github.io/
Vcs:           https://github.com/tarcieri/cool.io.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake-compiler) >= 1.0
BuildRequires: gem(rake-compiler-dock) >= 1.0
BuildRequires: gem(rspec) >= 2.13.0
BuildRequires: gem(rdoc) >= 3.6.0
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rake-compiler-dock) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names cool.io,cool-io
Obsoletes:     ruby-cool.io < %EVR
Provides:      ruby-cool.io = %EVR
Provides:      gem(cool.io) = 1.8.1


%description
Cool.io is an event library for Ruby, built on the libev event library, which
provides a cross-platform interface to high performance system calls. This
includes the epoll system call for Linux, the kqueue system call for BSDs and OS
X, and the completion ports interface for Solaris.

Cool.io also binds asynchronous wrappers to Ruby's core socket classes so you
can use them in conjunction with Cool.io to build asynchronous event-driven
applications.


%if_enabled    doc
%package       -n gem-cool-io-doc
Version:       1.8.1
Release:       alt1
Summary:       Simple evented I/O for Ruby (but please check out Celluloid::IO instead) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cool.io
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(cool.io) = 1.8.1

%description   -n gem-cool-io-doc
Simple evented I/O for Ruby (but please check out Celluloid::IO instead)
documentation files.

Cool.io is an event library for Ruby, built on the libev event library, which
provides a cross-platform interface to high performance system calls. This
includes the epoll system call for Linux, the kqueue system call for BSDs and OS
X, and the completion ports interface for Solaris.

Cool.io also binds asynchronous wrappers to Ruby's core socket classes so you
can use them in conjunction with Cool.io to build asynchronous event-driven
applications.

%description   -n gem-cool-io-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cool.io.
%endif


%if_enabled    devel
%package       -n gem-cool-io-devel
Version:       1.8.1
Release:       alt1
Summary:       Simple evented I/O for Ruby (but please check out Celluloid::IO instead) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cool.io
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cool.io) = 1.8.1
Requires:      gem(rake-compiler) >= 1.0
Requires:      gem(rake-compiler-dock) >= 1.0
Requires:      gem(rspec) >= 2.13.0
Requires:      gem(rdoc) >= 3.6.0
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rake-compiler-dock) >= 2
Conflicts:     libev-devel

%description   -n gem-cool-io-devel
Simple evented I/O for Ruby (but please check out Celluloid::IO instead)
development package.

Cool.io is an event library for Ruby, built on the libev event library, which
provides a cross-platform interface to high performance system calls. This
includes the epoll system call for Linux, the kqueue system call for BSDs and OS
X, and the completion ports interface for Solaris.

Cool.io also binds asynchronous wrappers to Ruby's core socket classes so you
can use them in conjunction with Cool.io to build asynchronous event-driven
applications.

%description   -n gem-cool-io-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cool.io.
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
%doc README.md ext/libev/README ext/libev/README.embed
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-cool-io-doc
%doc README.md ext/libev/README ext/libev/README.embed
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-cool-io-devel
%doc README.md ext/libev/README ext/libev/README.embed
%ruby_includedir/*
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.8.1-alt1
- ^ 1.7.1 -> 1.8.1

* Fri Oct 08 2021 Pavel Skrylev <majioa@altlinux.org> 1.7.1-alt1
- ^ 1.6.0 -> 1.7.1

* Mon May 25 2020 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1.1
- + proper conflict dep to libev-devel

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- ^ 1.5.4 -> 1.6.0
- ! spec syntax and tags

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.4-alt1
- > Ruby Policy 2.0
- ^ 1.5.3 -> 1.5.4

* Sat Sep 29 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.3-alt1
- Initial build for Sisyphus
