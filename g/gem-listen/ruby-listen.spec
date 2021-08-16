%define        gemname listen

Name:          gem-listen
Version:       3.5.1
Release:       alt1
Summary:       The Listen gem listens to file modifications and notifies you about the changes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/guard/listen
Vcs:           https://github.com/guard/listen.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rb-fsevent) >= 0.10.3 gem(rb-fsevent) < 1
BuildRequires: gem(rb-inotify) >= 0.9.10 gem(rb-inotify) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rb-fsevent) >= 0.10.3 gem(rb-fsevent) < 1
Requires:      gem(rb-inotify) >= 0.9.10 gem(rb-inotify) < 1
Obsoletes:     ruby-listen < %EVR
Provides:      ruby-listen = %EVR
Provides:      gem(listen) = 3.5.1


%description
The Listen gem listens to file modifications and notifies you about the
changes. Works everywhere!


%package       -n listen
Version:       3.5.1
Release:       alt1
Summary:       The Listen gem listens to file modifications and notifies you about the changes executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета listen
Group:         Other
BuildArch:     noarch

Requires:      gem(listen) = 3.5.1

%description   -n listen
The Listen gem listens to file modifications and notifies you about the changes
executable(s).

The Listen gem listens to file modifications and notifies you about the
changes. Works everywhere!

%description   -n listen -l ru_RU.UTF-8
Исполнямка для самоцвета listen.


%package       -n gem-listen-doc
Version:       3.5.1
Release:       alt1
Summary:       The Listen gem listens to file modifications and notifies you about the changes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета listen
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(listen) = 3.5.1

%description   -n gem-listen-doc
The Listen gem listens to file modifications and notifies you about the changes
documentation files.

The Listen gem listens to file modifications and notifies you about the
changes. Works everywhere!

%description   -n gem-listen-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета listen.


%package       -n gem-listen-devel
Version:       3.5.1
Release:       alt1
Summary:       The Listen gem listens to file modifications and notifies you about the changes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета listen
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(listen) = 3.5.1

%description   -n gem-listen-devel
The Listen gem listens to file modifications and notifies you about the changes
development package.

The Listen gem listens to file modifications and notifies you about the
changes. Works everywhere!

%description   -n gem-listen-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета listen.


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

%files         -n listen
%doc README.md
%_bindir/listen

%files         -n gem-listen-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-listen-devel
%doc README.md


%changelog
* Tue Jun 29 2021 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt1
- ^ 3.1.5 -> 3.5.1

* Mon Jul 16 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.5-alt2.git587f4a7
- Upgrade to git 587f4a7.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.5-alt1
- Initial build for Sisyphus
