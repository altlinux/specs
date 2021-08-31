%define        gemname rb-kqueue

Name:          gem-rb-kqueue
Version:       0.2.5
Release:       alt2
Summary:       An FFI wrapper for kqueue
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mat813/rb-kqueue
Vcs:           https://github.com/mat813/rb-kqueue.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ffi) >= 0.5.0
BuildRequires: gem(yard) >= 0.4.0
BuildRequires: gem(rspec) >= 3.3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ffi) >= 0.5.0
Obsoletes:     ruby-rb-kqueue < %EVR
Provides:      ruby-rb-kqueue = %EVR
Provides:      gem(rb-kqueue) = 0.2.5


%description
This is a simple wrapper over the kqueue BSD event notification interface
(supported on FreeBSD, NetBSD, OpenBSD, and Darwin). It uses the FFI gem to
avoid having to compile a C extension.


%package       -n gem-rb-kqueue-doc
Version:       0.2.5
Release:       alt2
Summary:       An FFI wrapper for kqueue documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rb-kqueue
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rb-kqueue) = 0.2.5

%description   -n gem-rb-kqueue-doc
An FFI wrapper for kqueue documentation files.

This is a simple wrapper over the kqueue BSD event notification interface
(supported on FreeBSD, NetBSD, OpenBSD, and Darwin). It uses the FFI gem to
avoid having to compile a C extension.


%description   -n gem-rb-kqueue-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rb-kqueue.


%package       -n gem-rb-kqueue-devel
Version:       0.2.5
Release:       alt2
Summary:       An FFI wrapper for kqueue development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rb-kqueue
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rb-kqueue) = 0.2.5
Requires:      gem(yard) >= 0.4.0
Requires:      gem(rspec) >= 3.3.0 gem(rspec) < 4

%description   -n gem-rb-kqueue-devel
An FFI wrapper for kqueue development package.

This is a simple wrapper over the kqueue BSD event notification interface
(supported on FreeBSD, NetBSD, OpenBSD, and Darwin). It uses the FFI gem to
avoid having to compile a C extension.

%description   -n gem-rb-kqueue-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rb-kqueue.


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

%files         -n gem-rb-kqueue-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rb-kqueue-devel
%doc README.md


%changelog
* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.5-alt2
- ! spec

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.5-alt1.1
- Rebuild for new Ruby autorequirements.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus
