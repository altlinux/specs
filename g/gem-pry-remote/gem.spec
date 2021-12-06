%define        gemname pry-remote

Name:          gem-pry-remote
Version:       0.1.8
Release:       alt2
Summary:       Connect to Pry remotely
License:       Zlib
Group:         Development/Ruby
Url:           http://github.com/Mon-Ouie/pry-remote
Vcs:           https://github.com/mon-ouie/pry-remote.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         new_slop_4.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(slop) >= 4.0 gem(slop) < 5
BuildRequires: gem(pry) >= 0.9 gem(pry) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(slop) >= 4.0 gem(slop) < 5
Requires:      gem(pry) >= 0.9 gem(pry) < 1
Provides:      gem(pry-remote) = 0.1.8


%description
Connect to Pry remotely using DRb.


%package       -n pry-remote
Version:       0.1.8
Release:       alt2
Summary:       Connect to Pry remotely executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета pry-remote
Group:         Other
BuildArch:     noarch

Requires:      gem(pry-remote) = 0.1.8

%description   -n pry-remote
Connect to Pry remotely executable(s).

Connect to Pry remotely using DRb.

%description   -n pry-remote -l ru_RU.UTF-8
Исполнямка для самоцвета pry-remote.


%package       -n gem-pry-remote-doc
Version:       0.1.8
Release:       alt2
Summary:       Connect to Pry remotely documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pry-remote
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pry-remote) = 0.1.8

%description   -n gem-pry-remote-doc
Connect to Pry remotely documentation files.

Connect to Pry remotely using DRb.

%description   -n gem-pry-remote-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pry-remote.


%package       -n gem-pry-remote-devel
Version:       0.1.8
Release:       alt2
Summary:       Connect to Pry remotely development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pry-remote
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pry-remote) = 0.1.8

%description   -n gem-pry-remote-devel
Connect to Pry remotely development package.

Connect to Pry remotely using DRb.

%description   -n gem-pry-remote-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pry-remote.


%prep
%setup
%patch

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

%files         -n pry-remote
%doc README.md
%_bindir/pry-remote

%files         -n gem-pry-remote-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-pry-remote-devel
%doc README.md


%changelog
* Thu Nov 18 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.8-alt2
- ^ slop 3.x -> 4.x

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.8-alt1
- + packaged gem with Ruby Policy 2.0
