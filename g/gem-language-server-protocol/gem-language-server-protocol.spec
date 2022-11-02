%define        gemname language_server-protocol

Name:          gem-language-server-protocol
Version:       3.17.0.1
Release:       alt1
Summary:       A Language Server Protocol SDK
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mtsmfm/language_server-protocol-ruby
Vcs:           https://github.com/mtsmfm/language_server-protocol-ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 2.0.0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(minitest-power_assert) >= 0
BuildRequires: gem(m) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(activesupport) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(language_server-protocol) = 3.17.0.1


%description
A Language Server Protocol SDK


%package       -n gem-language-server-protocol-doc
Version:       3.17.0.1
Release:       alt1
Summary:       A Language Server Protocol SDK documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета language_server-protocol
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(language_server-protocol) = 3.17.0.1

%description   -n gem-language-server-protocol-doc
A Language Server Protocol SDK documentation files.

%description   -n gem-language-server-protocol-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета language_server-protocol.


%package       -n gem-language-server-protocol-devel
Version:       3.17.0.1
Release:       alt1
Summary:       A Language Server Protocol SDK development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета language_server-protocol
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(language_server-protocol) = 3.17.0.1
Requires:      gem(bundler) >= 2.0.0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(minitest-power_assert) >= 0
Requires:      gem(m) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(activesupport) >= 0

%description   -n gem-language-server-protocol-devel
A Language Server Protocol SDK development package.

%description   -n gem-language-server-protocol-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета language_server-protocol.


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

%files         -n gem-language-server-protocol-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-language-server-protocol-devel
%doc README.md


%changelog
* Mon Oct 31 2022 Pavel Skrylev <majioa@altlinux.org> 3.17.0.1-alt1
- + packaged gem with Ruby Policy 2.0
