%define        gemname http-2

Name:          gem-http-2
Version:       0.11.0
Release:       alt1
Summary:       Pure-ruby HTTP 2.0 protocol implementation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/igrigorik/http-2
Vcs:           https://github.com/igrigorik/http-2.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names example
Provides:      gem(http-2) = 0.11.0


%description
Pure-ruby HTTP 2.0 protocol implementation.


%package       -n gem-http-2-doc
Version:       0.11.0
Release:       alt1
Summary:       Pure-ruby HTTP 2.0 protocol implementation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета http-2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(http-2) = 0.11.0

%description   -n gem-http-2-doc
Pure-ruby HTTP 2.0 protocol implementation documentation files.

%description   -n gem-http-2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета http-2.


%package       -n gem-http-2-devel
Version:       0.11.0
Release:       alt1
Summary:       Pure-ruby HTTP 2.0 protocol implementation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета http-2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(http-2) = 0.11.0
Requires:      gem(bundler) >= 0 gem(bundler) < 3

%description   -n gem-http-2-devel
Pure-ruby HTTP 2.0 protocol implementation development package.

%description   -n gem-http-2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета http-2.


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

%files         -n gem-http-2-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-http-2-devel
%doc README.md


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.11.0-alt1
- + packaged gem with Ruby Policy 2.0
