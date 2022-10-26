%define        gemname google-id-token

Name:          gem-google-id-token
Version:       1.4.2
Release:       alt1
Summary:       Google ID Token utilities
License:       APACHE-2.0
Group:         Development/Ruby
Url:           https://github.com/google/google-id-token/
Vcs:           https://github.com/google/google-id-token.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(fakeweb) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(openssl) >= 0
BuildRequires: gem(jwt) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(jwt) >= 1
Provides:      gem(google-id-token) = 1.4.2


%description
Google ID Token utilities; currently just a parser/checker


%package       -n gem-google-id-token-doc
Version:       1.4.2
Release:       alt1
Summary:       Google ID Token utilities documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-id-token
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-id-token) = 1.4.2

%description   -n gem-google-id-token-doc
Google ID Token utilities documentation files.

Google ID Token utilities; currently just a parser/checker

%description   -n gem-google-id-token-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-id-token.


%package       -n gem-google-id-token-devel
Version:       1.4.2
Release:       alt1
Summary:       Google ID Token utilities development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-id-token
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-id-token) = 1.4.2
Requires:      gem(fakeweb) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(openssl) >= 0

%description   -n gem-google-id-token-devel
Google ID Token utilities development package.

Google ID Token utilities; currently just a parser/checker

%description   -n gem-google-id-token-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-id-token.


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

%files         -n gem-google-id-token-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-google-id-token-devel
%doc README.md


%changelog
* Thu Oct 20 2022 Pavel Skrylev <majioa@altlinux.org> 1.4.2-alt1
- + packaged gem with Ruby Policy 2.0
