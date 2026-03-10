# vim: set ft=spec: -*- rpm-spec -*-

%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname stomp

Name:          gem-stomp
Version:       1.4.10
Release:       alt1
Summary:       Ruby client for the Stomp messaging protocol
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/stompgem/stomp
Vcs:           https://github.com/stompgem/stomp.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 2.14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Obsoletes:     ruby-stomp < %EVR
Provides:      ruby-stomp = %EVR
Provides:      gem(stomp) = 1.4.10

%description
Ruby client for the Stomp messaging protocol.


%package       -n stomp
Version:       1.4.10
Release:       alt1
Summary:       Ruby client for the Stomp messaging protocol executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета stomp
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(stomp) = 1.4.10

%description   -n stomp
Ruby client for the Stomp messaging protocol executable(s).

%description   -n stomp -l ru_RU.UTF-8
Исполнямка для самоцвета stomp.


%if_enabled    doc
%package       -n gem-stomp-doc
Version:       1.4.10
Release:       alt1
Summary:       Ruby client for the Stomp messaging protocol documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета stomp
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(stomp) = 1.4.10

%description   -n gem-stomp-doc
Ruby client for the Stomp messaging protocol documentation files.

%description   -n gem-stomp-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета stomp.
%endif


%if_enabled    devel
%package       -n gem-stomp-devel
Version:       1.4.10
Release:       alt1
Summary:       Ruby client for the Stomp messaging protocol development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета stomp
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(stomp) = 1.4.10
Requires:      gem(rspec) >= 2.14

%description   -n gem-stomp-devel
Ruby client for the Stomp messaging protocol development package.

%description   -n gem-stomp-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета stomp.
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
%doc CHANGELOG.md CONTRIBUTORS.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n stomp
%doc CHANGELOG.md CONTRIBUTORS.md LICENSE README.md
%_bindir/catstomp
%_bindir/stompcat

%if_enabled    doc
%files         -n gem-stomp-doc
%doc CHANGELOG.md CONTRIBUTORS.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-stomp-devel
%doc CHANGELOG.md CONTRIBUTORS.md LICENSE README.md
%endif


%changelog
* Tue Mar 10 2026 Pavel Skrylev <majioa@altlinux.org> 1.4.10-alt1
- > used Ruby Policy 2.0
- ^ 1.1.9 -> 1.4.10
- * renamed package with subpackages
- * define explicit dependencies

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.9-alt1.3
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.9-alt1.2
- Rebuild with Ruby 2.4.1

* Tue Dec 04 2012 Led <led@altlinux.ru> 1.1.9-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Sep 28 2011 Sergey Alembekov <rt@altlinux.ru> 1.1.9-alt1
- Built for Sisyphus
