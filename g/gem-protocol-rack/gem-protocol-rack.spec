%define        gemname protocol-rack

Name:          gem-protocol-rack
Version:       0.2.4
Release:       alt1
Summary:       An implementation of the Rack protocol/specification
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/protocol-rack
Vcs:           https://github.com/socketry/protocol-rack.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(protocol-http) >= 0.23 gem(protocol-http) < 1
BuildRequires: gem(rack) >= 1.0
BuildRequires: gem(async-http) >= 0.59 gem(async-http) < 1
BuildRequires: gem(bake-test) >= 0.1 gem(bake-test) < 1
BuildRequires: gem(bake-test-external) >= 0.1 gem(bake-test-external) < 1
BuildRequires: gem(covered) >= 0.16 gem(covered) < 1
BuildRequires: gem(sus) >= 0.12 gem(sus) < 1
BuildRequires: gem(sus-fixtures-async-http) >= 0.1 gem(sus-fixtures-async-http) < 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(protocol-http) >= 0.23 gem(protocol-http) < 1
Requires:      gem(rack) >= 1.0
Provides:      gem(protocol-rack) = 0.2.4

%description
An implementation of the Rack protocol/specification.


%package       -n gem-protocol-rack-doc
Version:       0.2.4
Release:       alt1
Summary:       An implementation of the Rack protocol/specification documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета protocol-rack
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(protocol-rack) = 0.2.4

%description   -n gem-protocol-rack-doc
An implementation of the Rack protocol/specification documentation files.

%description   -n gem-protocol-rack-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета protocol-rack.


%package       -n gem-protocol-rack-devel
Version:       0.2.4
Release:       alt1
Summary:       An implementation of the Rack protocol/specification development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета protocol-rack
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(protocol-rack) = 0.2.4
Requires:      gem(async-http) >= 0.59 gem(async-http) < 1
Requires:      gem(bake-test) >= 0.1 gem(bake-test) < 1
Requires:      gem(bake-test-external) >= 0.1 gem(bake-test-external) < 1
Requires:      gem(covered) >= 0.16 gem(covered) < 1
Requires:      gem(sus) >= 0.12 gem(sus) < 1
Requires:      gem(sus-fixtures-async-http) >= 0.1 gem(sus-fixtures-async-http) < 1

%description   -n gem-protocol-rack-devel
An implementation of the Rack protocol/specification development package.

%description   -n gem-protocol-rack-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета protocol-rack.


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

%files         -n gem-protocol-rack-doc
%doc readme.md
%ruby_gemdocdir

%files         -n gem-protocol-rack-devel
%doc readme.md


%changelog
* Mon Oct 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.4-alt1
- + packaged gem with Ruby Policy 2.0
