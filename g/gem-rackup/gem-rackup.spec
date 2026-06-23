%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rackup

Name:          gem-rackup
Epoch:         2
Version:       2.3.1
Release:       alt1
Summary:       A general server command for Rack applications
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rack/rackup
Vcs:           https://github.com/rack/rackup.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(rack) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.5
Requires:      gem(rack) >= 3
Provides:      gem(rackup) = 2.3.1

%description
A general server command for Rack applications.


%package       -n rackup
Version:       2.3.1
Release:       alt1
Summary:       A general server command for Rack applications executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rackup
Group:         Other
BuildArch:     noarch

Requires:      gem(rackup) = 2.3.1

%description   -n rackup
A general server command for Rack applications executable(s).

%description   -n rackup -l ru_RU.UTF-8
Исполнямка для самоцвета rackup.


%if_enabled    doc
%package       -n gem-rackup-doc
Version:       2.3.1
Release:       alt1
Summary:       A general server command for Rack applications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rackup
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rackup) = 2.3.1

%description   -n gem-rackup-doc
A general server command for Rack applications documentation files.

%description   -n gem-rackup-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rackup.
%endif


%if_enabled    devel
%package       -n gem-rackup-devel
Version:       2.3.1
Release:       alt1
Summary:       A general server command for Rack applications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rackup
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rackup) = 2.3.1

%description   -n gem-rackup-devel
A general server command for Rack applications development package.

%description   -n gem-rackup-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rackup.
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
%doc license.md readme.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n rackup
%doc license.md readme.md
%_bindir/rackup

%if_enabled    doc
%files         -n gem-rackup-doc
%doc license.md readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rackup-devel
%doc license.md readme.md
%endif


%changelog
* Sat May 30 2026 Pavel Skrylev <majioa@altlinux.org> 2:2.3.1-alt1
- ^ 2.2.1 -> 2.3.1

* Mon May 19 2025 Pavel Skrylev <majioa@altlinux.org> 2:2.2.1-alt1
- ^ 2.1.0 -> 2.2.1
- > regeared as direct flow as tag
- - droppen thin.rb in favor of specific gem

* Sat Nov 02 2024 Alexander Burmatov <thatman@altlinux.org> 2:2.1.0-alt2
- Add thin rackup handler.

* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 2:2.1.0-alt1
- + packaged gem with Ruby Policy 2.0
