%define        _unpackaged_files_terminate_build 1
%define        gemname async-http-faraday

Name:          gem-async-http-faraday
Version:       0.12.0
Release:       alt1
Summary:       Provides an adaptor between async-http and faraday
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async-http
Vcs:           https://github.com/socketry/async-http.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(async-http) >= 0.42
BuildRequires: gem(faraday) >= 0
BuildRequires: gem(async-rspec) >= 1.2
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 3.6
BuildConflicts: gem(async-http) >= 1
BuildConflicts: gem(async-rspec) >= 2
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(async-http) >= 0.42
Requires:      gem(faraday) >= 0
Conflicts:     gem(async-http) >= 1
Provides:      gem(async-http-faraday) = 0.12.0


%description
Provides an adaptor between async-http and faraday.


%package       -n gem-async-http-faraday-doc
Version:       0.12.0
Release:       alt1
Summary:       Provides an adaptor between async-http and faraday documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async-http-faraday
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(async-http-faraday) = 0.12.0

%description   -n gem-async-http-faraday-doc
Provides an adaptor between async-http and faraday documentation files.

%description   -n gem-async-http-faraday-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета async-http-faraday.


%package       -n gem-async-http-faraday-devel
Version:       0.12.0
Release:       alt1
Summary:       Provides an adaptor between async-http and faraday development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async-http-faraday
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(async-http-faraday) = 0.12.0
Requires:      gem(async-rspec) >= 1.2
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 3.6
Conflicts:     gem(async-rspec) >= 2
Conflicts:     gem(rspec) >= 4

%description   -n gem-async-http-faraday-devel
Provides an adaptor between async-http and faraday development package.

%description   -n gem-async-http-faraday-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета async-http-faraday.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc readme.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-async-http-faraday-doc
%doc readme.md
%ruby_gemdocdir

%files         -n gem-async-http-faraday-devel
%doc readme.md


%changelog
* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 0.12.0-alt1
- + packaged gem with Ruby Policy 2.0
