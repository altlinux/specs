%define        gemname uuid

Name:          gem-uuid
Version:       2.3.9
Release:       alt1
Summary:       UUID generator
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/assaf/uuid
Vcs:           https://github.com/assaf/uuid.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(macaddr) >= 1.0 gem(macaddr) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(macaddr) >= 1.0 gem(macaddr) < 2
Provides:      gem(uuid) = 2.3.9


%description
UUID generator for producing universally unique identifiers based on RFC 4122
(http://www.ietf.org/rfc/rfc4122.txt).


%package       -n uuid
Version:       2.3.9
Release:       alt1
Summary:       UUID generator executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета uuid
Group:         Other
BuildArch:     noarch

Requires:      gem(uuid) = 2.3.9

%description   -n uuid
UUID generator executable(s).

UUID generator for producing universally unique identifiers based on RFC 4122
(http://www.ietf.org/rfc/rfc4122.txt).

%description   -n uuid -l ru_RU.UTF-8
Исполнямка для самоцвета uuid.


%package       -n gem-uuid-doc
Version:       2.3.9
Release:       alt1
Summary:       UUID generator documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета uuid
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(uuid) = 2.3.9

%description   -n gem-uuid-doc
UUID generator documentation files.

UUID generator for producing universally unique identifiers based on RFC 4122
(http://www.ietf.org/rfc/rfc4122.txt).

%description   -n gem-uuid-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета uuid.


%package       -n gem-uuid-devel
Version:       2.3.9
Release:       alt1
Summary:       UUID generator development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета uuid
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(uuid) = 2.3.9

%description   -n gem-uuid-devel
UUID generator development package.

UUID generator for producing universally unique identifiers based on RFC 4122
(http://www.ietf.org/rfc/rfc4122.txt).

%description   -n gem-uuid-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета uuid.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n uuid
%doc README.rdoc
%_bindir/uuid

%files         -n gem-uuid-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-uuid-devel
%doc README.rdoc


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 2.3.9-alt1
- + packaged gem with Ruby Policy 2.0
