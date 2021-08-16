%define        gemname rb-inotify

Name:          gem-rb-inotify
Version:       0.10.1
Release:       alt1
Summary:       A thorough inotify wrapper for Ruby using FFI
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/guard/rb-inotify/
Vcs:           https://github.com/guard/rb-inotify.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ffi) >= 1.0 gem(ffi) < 2
BuildRequires: gem(rspec) >= 3.6 gem(rspec) < 4
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(concurrent-ruby) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ffi) >= 1.0 gem(ffi) < 2
Obsoletes:     ruby-rb-inotify < %EVR
Provides:      ruby-rb-inotify = %EVR
Provides:      gem(rb-inotify) = 0.10.1


%description
This is a simple wrapper over the inotify Linux kernel subsystem for monitoring
changes to files and directories. It uses the FFI gem to avoid having to
compile a C extension.


%package       -n gem-rb-inotify-doc
Version:       0.10.1
Release:       alt1
Summary:       A thorough inotify wrapper for Ruby using FFI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rb-inotify
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rb-inotify) = 0.10.1

%description   -n gem-rb-inotify-doc
A thorough inotify wrapper for Ruby using FFI documentation files.

This is a simple wrapper over the inotify Linux kernel subsystem for monitoring
changes to files and directories. It uses the FFI gem to avoid having to
compile a C extension.

%description   -n gem-rb-inotify-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rb-inotify.


%package       -n gem-rb-inotify-devel
Version:       0.10.1
Release:       alt1
Summary:       A thorough inotify wrapper for Ruby using FFI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rb-inotify
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rb-inotify) = 0.10.1
Requires:      gem(rspec) >= 3.6 gem(rspec) < 4
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(concurrent-ruby) >= 0

%description   -n gem-rb-inotify-devel
A thorough inotify wrapper for Ruby using FFI development package.

This is a simple wrapper over the inotify Linux kernel subsystem for monitoring
changes to files and directories. It uses the FFI gem to avoid having to
compile a C extension.

%description   -n gem-rb-inotify-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rb-inotify.


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

%files         -n gem-rb-inotify-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rb-inotify-devel
%doc README.md


%changelog
* Mon Jun 28 2021 Pavel Skrylev <majioa@altlinux.org> 0.10.1-alt1
- ^ 0.9.10 -> 0.10.1

* Mon Sep 03 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.10-alt2.1
- Rebuild for new Ruby autorequirements.

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.9.10-alt2
- Rebuild as ruby gem for openqa

* Thu Sep 28 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.9.10-alt1
- Initial build for Sisyphus
