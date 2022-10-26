%define        gemname faraday-excon

Name:          gem-faraday-excon
Version:       2.1.0
Release:       alt1
Summary:       Faraday adapter for Excon
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday-excon
Vcs:           https://github.com/lostisland/faraday-excon.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(excon) >= 0.27.4
BuildRequires: gem(faraday) >= 2.0 gem(faraday) < 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(excon) >= 0.27.4
Requires:      gem(faraday) >= 2.0 gem(faraday) < 3
Provides:      gem(faraday-excon) = 2.1.0


%description
Faraday adapter for Excon


%package       -n gem-faraday-excon-doc
Version:       2.1.0
Release:       alt1
Summary:       Faraday adapter for Excon documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-excon
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-excon) = 2.1.0

%description   -n gem-faraday-excon-doc
Faraday adapter for Excon documentation files.

%description   -n gem-faraday-excon-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-excon.


%package       -n gem-faraday-excon-devel
Version:       2.1.0
Release:       alt1
Summary:       Faraday adapter for Excon development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday-excon
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday-excon) = 2.1.0

%description   -n gem-faraday-excon-devel
Faraday adapter for Excon development package.

%description   -n gem-faraday-excon-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday-excon.


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

%files         -n gem-faraday-excon-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-faraday-excon-devel
%doc README.md


%changelog
* Tue Oct 11 2022 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 1.1.0 -> 2.1.0

* Sat Jun 05 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
