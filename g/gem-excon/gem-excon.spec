%define        _unpackaged_files_terminate_build 1
%define        gemname excon

Name:          gem-excon
Version:       0.105.0
Release:       alt1
Summary:       Usable, fast, simple HTTP 1.1 for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/excon/excon
Vcs:           https://github.com/excon/excon.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         delorean_to_timecop.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 3.5.0
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(eventmachine) >= 1.0.4
BuildRequires: gem(open4) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(shindo) >= 0
BuildRequires: gem(sinatra) >= 0
BuildRequires: gem(sinatra-contrib) >= 0
BuildRequires: gem(json) >= 1.8.5
BuildRequires: gem(puma) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(unicorn) >= 0
BuildRequires: gem(rack) >= 2.2.2
BuildRequires: gem(rubocop) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 2.2.2,rack < 3
Obsoletes:     ruby-excon
Provides:      ruby-excon
Provides:      gem(excon) = 0.105.0


%description
Usable, fast, simple Ruby HTTP 1.1

Excon was designed to be simple, fast and performant. It works great as a
general HTTP(s) client and is particularly well suited to usage in API clients.


%package       -n gem-excon-doc
Version:       0.105.0
Release:       alt1
Summary:       Usable, fast, simple HTTP 1.1 for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета excon
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(excon) = 0.105.0

%description   -n gem-excon-doc
Usable, fast, simple HTTP 1.1 for Ruby documentation files.

Usable, fast, simple Ruby HTTP 1.1

Excon was designed to be simple, fast and performant. It works great as a
general HTTP(s) client and is particularly well suited to usage in API clients.

%description   -n gem-excon-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета excon.


%package       -n gem-excon-devel
Version:       0.105.0
Release:       alt1
Summary:       Usable, fast, simple HTTP 1.1 for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета excon
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(excon) = 0.105.0
Requires:      gem(rspec) >= 3.5.0
Requires:      gem(activesupport) >= 0
Requires:      gem(timecop) >= 0
Requires:      gem(eventmachine) >= 1.0.4
Requires:      gem(open4) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(shindo) >= 0
Requires:      gem(sinatra) >= 0
Requires:      gem(sinatra-contrib) >= 0
Requires:      gem(json) >= 1.8.5
Requires:      gem(puma) >= 0
Requires:      gem(webrick) >= 0
Requires:      gem(unicorn) >= 0
Requires:      gem(rack) >= 2.2.2
Requires:      gem(rubocop) >= 0

%description   -n gem-excon-devel
Usable, fast, simple HTTP 1.1 for Ruby development package.

Usable, fast, simple Ruby HTTP 1.1

Excon was designed to be simple, fast and performant. It works great as a
general HTTP(s) client and is particularly well suited to usage in API clients.

%description   -n gem-excon-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета excon.


%prep
%setup
%autopatch

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

%files         -n gem-excon-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-excon-devel
%doc README.md


%changelog
* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 0.105.0-alt1
- ^ 0.72.0 -> 0.105.0

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.72.0-alt1
- updated (^) 0.66.0 -> 0.72.0
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.66.0-alt1
- updated (^) 0.62.0 -> 0.66.0
- used (>) Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.62.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.62.0-alt1
- Initial build for Sisyphus
