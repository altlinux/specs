%define        gemname patron

Name:          gem-patron
Version:       0.13.3
Release:       alt1
Summary:       Patron HTTP Client
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/toland/patron
Vcs:           https://github.com/toland/patron.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libcurl-devel
BuildRequires: gem(rake) >= 10 gem(rake) < 14
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rspec) >= 2.3.0
BuildRequires: gem(simplecov) >= 0.10 gem(simplecov) < 1
BuildRequires: gem(yard) >= 0.9.11 gem(yard) < 0.10
BuildRequires: gem(rack) >= 1 gem(rack) < 3
BuildRequires: gem(puma) >= 3.11 gem(puma) < 6
BuildRequires: gem(rake-compiler) >= 0 gem(rake-compiler) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency puma >= 5.2.2,puma < 6
%ruby_use_gem_dependency rack >= 2.2.2,rack < 3
Provides:      gem(patron) = 0.13.3


%description
Patron is a Ruby HTTP client library based on libcurl. It does not try to
expose the full "power" (read complexity) of libcurl but instead tries to
provide a sane API while taking advantage of libcurl under the hood.


%package       -n gem-patron-doc
Version:       0.13.3
Release:       alt1
Summary:       Patron HTTP Client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета patron
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(patron) = 0.13.3

%description   -n gem-patron-doc
Patron HTTP Client documentation files.

Patron is a Ruby HTTP client library based on libcurl. It does not try to
expose the full "power" (read complexity) of libcurl but instead tries to
provide a sane API while taking advantage of libcurl under the hood.

%description   -n gem-patron-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета patron.


%package       -n gem-patron-devel
Version:       0.13.3
Release:       alt1
Summary:       Patron HTTP Client development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета patron
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(patron) = 0.13.3
Requires:      gem(rake) >= 10 gem(rake) < 14
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(rspec) >= 2.3.0
Requires:      gem(simplecov) >= 0.10 gem(simplecov) < 1
Requires:      gem(yard) >= 0.9.11 gem(yard) < 0.10
Requires:      gem(rack) >= 1 gem(rack) < 3
Requires:      gem(puma) >= 3.11 gem(puma) < 6
Requires:      gem(rake-compiler) >= 0 gem(rake-compiler) < 2

%description   -n gem-patron-devel
Patron HTTP Client development package.

Patron is a Ruby HTTP client library based on libcurl. It does not try to
expose the full "power" (read complexity) of libcurl but instead tries to
provide a sane API while taking advantage of libcurl under the hood.

%description   -n gem-patron-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета patron.


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
%ruby_gemextdir

%files         -n gem-patron-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-patron-devel
%doc README.md
%ruby_includedir/*


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.13.3-alt1
- + packaged gem with Ruby Policy 2.0
