%define        gemname notify

Name:          gem-notify
Version:       0.5.2.1
Release:       alt1
Summary:       A function to notify on cross platform
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/jugyo/notify
Vcs:           https://github.com/jugyo/notify.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Provides:      gem(notify) = 0.5.2.1

%ruby_use_gem_version notify:0.5.2.1

%description
The "notify" provides a function to notify on cross platform.


%package       -n notify
Version:       0.5.2.1
Release:       alt1
Summary:       A function to notify on cross platform executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета notify
Group:         Other
BuildArch:     noarch

Requires:      gem(notify) = 0.5.2.1

%description   -n notify
A function to notify on cross platform executable(s).

The "notify" provides a function to notify on cross platform.

%description   -n notify -l ru_RU.UTF-8
Исполнямка для самоцвета notify.


%package       -n gem-notify-doc
Version:       0.5.2.1
Release:       alt1
Summary:       A function to notify on cross platform documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета notify
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(notify) = 0.5.2.1

%description   -n gem-notify-doc
A function to notify on cross platform documentation files.

The "notify" provides a function to notify on cross platform.

%description   -n gem-notify-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета notify.


%package       -n gem-notify-devel
Version:       0.5.2.1
Release:       alt1
Summary:       A function to notify on cross platform development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета notify
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(notify) = 0.5.2.1
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3
Requires:      gem(rake) >= 0

%description   -n gem-notify-devel
A function to notify on cross platform development package.

The "notify" provides a function to notify on cross platform.

%description   -n gem-notify-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета notify.


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

%files         -n notify
%doc README.md
%_bindir/notify

%files         -n gem-notify-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-notify-devel
%doc README.md


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 0.5.2.1-alt1
- ^ 0.5.2 -> 0.5.2.1

* Sat Sep 11 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.2-alt1
- + packaged gem with Ruby Policy 2.0
