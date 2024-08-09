%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname nio4r

Name:          gem-nio4r
Version:       2.7.3
Release:       alt1
Summary:       New I/O for Ruby: Cross-platform asynchronous I/O primitives for scalable network clients and servers
License:       MIT or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/socketry/nio4r
Vcs:           https://github.com/socketry/nio4r.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-nio4r < %EVR
Provides:      ruby-nio4r = %EVR
Provides:      gem(nio4r) = 2.7.3


%description
New I/O for Ruby (nio4r): cross-platform asynchronous I/O primitives for
scalable network clients and servers. Modeled after the Java NIO API, but
simplified for ease-of-use. nio4r provides an abstract, cross-platform stateful
I/O selector API for Ruby. I/O selectors are the heart of "reactor"-based event
loops, and monitor multiple I/O objects for various types of readiness, e.g.
ready for reading or writing.


%if_enabled    doc
%package       -n gem-nio4r-doc
Version:       2.7.3
Release:       alt1
Summary:       New I/O for Ruby: Cross-platform asynchronous I/O primitives for scalable network clients and servers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета nio4r
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(nio4r) = 2.7.3
Obsoletes:     ruby-nio4r-doc
Provides:      ruby-nio4r-doc

%description   -n gem-nio4r-doc
New I/O for Ruby: Cross-platform asynchronous I/O primitives for scalable
network clients and servers documentation files.

New I/O for Ruby (nio4r): cross-platform asynchronous I/O primitives for
scalable network clients and servers. Modeled after the Java NIO API, but
simplified for ease-of-use. nio4r provides an abstract, cross-platform stateful
I/O selector API for Ruby. I/O selectors are the heart of "reactor"-based event
loops, and monitor multiple I/O objects for various types of readiness, e.g.
ready for reading or writing.

%description   -n gem-nio4r-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета nio4r.
%endif


%if_enabled    devel
%package       -n gem-nio4r-devel
Version:       2.7.3
Release:       alt1
Summary:       New I/O for Ruby: Cross-platform asynchronous I/O primitives for scalable network clients and servers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета nio4r
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(nio4r) = 2.7.3
Conflicts:     libev-devel

%description   -n gem-nio4r-devel
New I/O for Ruby: Cross-platform asynchronous I/O primitives for scalable
network clients and servers development package.

New I/O for Ruby (nio4r): cross-platform asynchronous I/O primitives for
scalable network clients and servers. Modeled after the Java NIO API, but
simplified for ease-of-use. nio4r provides an abstract, cross-platform stateful
I/O selector API for Ruby. I/O selectors are the heart of "reactor"-based event
loops, and monitor multiple I/O objects for various types of readiness, e.g.
ready for reading or writing.

%description   -n gem-nio4r-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета nio4r.
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
%doc ext/libev/README readme.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-nio4r-doc
%doc ext/libev/README readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-nio4r-devel
%doc ext/libev/README readme.md
%ruby_includedir/*
%endif


%changelog
* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 2.7.3-alt1
- ^ 2.5.8 -> 2.7.3

* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 2.5.8-alt1
- ^ 2.5.2 -> 2.5.8

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.5.2-alt1
- updated (^) 2.5.1 -> 2.5.2
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.1-alt1
- updated (^) 2.3.1 -> 2.5.1

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt2
- moved to (>) Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus
