%define        gemname notify

Name:          gem-notify
Version:       0.5.2
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

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(notify) = 0.5.2


%description
The "notify" provides a function to notify on cross platform.


%package       -n notify
Version:       0.5.2
Release:       alt1
Summary:       A function to notify on cross platform executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета notify
Group:         Other
BuildArch:     noarch

Requires:      gem(notify) = 0.5.2

%description   -n notify
A function to notify on cross platform executable(s).

The "notify" provides a function to notify on cross platform.

%description   -n notify -l ru_RU.UTF-8
Исполнямка для самоцвета notify.


%package       -n gem-notify-doc
Version:       0.5.2
Release:       alt1
Summary:       A function to notify on cross platform documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета notify
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(notify) = 0.5.2

%description   -n gem-notify-doc
A function to notify on cross platform documentation files.

The "notify" provides a function to notify on cross platform.

%description   -n gem-notify-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета notify.


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


%changelog
* Sat Sep 11 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.2-alt1
- + packaged gem with Ruby Policy 2.0
