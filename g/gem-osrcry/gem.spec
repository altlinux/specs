%define        gemname osrcry

Name:          gem-osrcry
Version:       0.3.0
Release:       alt1
Summary:       Tools for open source project management
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/geemus/osrcry
Vcs:           https://github.com/geemus/osrcry.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Provides:      gem(osrcry) = 0.3.0


%description
Open Sourcery - Tools for open source project management.


%package       -n osrcry
Version:       0.3.0
Release:       alt1
Summary:       Tools for open source project management executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета osrcry
Group:         Other
BuildArch:     noarch

Requires:      gem(osrcry) = 0.3.0

%description   -n osrcry
Tools for open source project management executable(s).

Open Sourcery - Tools for open source project management.

%description   -n osrcry -l ru_RU.UTF-8
Исполнямка для самоцвета osrcry.


%package       -n gem-osrcry-doc
Version:       0.3.0
Release:       alt1
Summary:       Tools for open source project management documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета osrcry
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(osrcry) = 0.3.0

%description   -n gem-osrcry-doc
Tools for open source project management documentation files.

Open Sourcery - Tools for open source project management.

%description   -n gem-osrcry-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета osrcry.


%package       -n gem-osrcry-devel
Version:       0.3.0
Release:       alt1
Summary:       Tools for open source project management development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета osrcry
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(osrcry) = 0.3.0
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3
Requires:      gem(rake) >= 0

%description   -n gem-osrcry-devel
Tools for open source project management development package.

Open Sourcery - Tools for open source project management.

%description   -n gem-osrcry-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета osrcry.


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

%files         -n osrcry
%doc README.md
%_bindir/osrcry

%files         -n gem-osrcry-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-osrcry-devel
%doc README.md


%changelog
* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
