%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname language_server-protocol

Name:          gem-language-server-protocol
Version:       3.17.0.3
Release:       alt1
Summary:       A Language Server Protocol SDK
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mtsmfm/language_server-protocol-ruby
Vcs:           https://github.com/mtsmfm/language_server-protocol-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.0.0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(minitest-power_assert) >= 0
BuildRequires: gem(m) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(activesupport) >= 0
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names language_server-protocol,language-server-protocol
Provides:      gem(language_server-protocol) = 3.17.0.3


%description
A Language Server Protocol SDK.


%if_enabled    doc
%package       -n gem-language-server-protocol-doc
Version:       3.17.0.3
Release:       alt1
Summary:       A Language Server Protocol SDK documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета language_server-protocol
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(language_server-protocol) = 3.17.0.3

%description   -n gem-language-server-protocol-doc
A Language Server Protocol SDK documentation files.
%description   -n gem-language-server-protocol-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета language_server-protocol.
%endif


%if_enabled    devel
%package       -n gem-language-server-protocol-devel
Version:       3.17.0.3
Release:       alt1
Summary:       A Language Server Protocol SDK development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета language_server-protocol
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(language_server-protocol) = 3.17.0.3
Requires:      gem(bundler) >= 2.0.0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(minitest) >= 5.0
Requires:      gem(minitest-power_assert) >= 0
Requires:      gem(m) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(activesupport) >= 0
Conflicts:     gem(minitest) >= 6

%description   -n gem-language-server-protocol-devel
A Language Server Protocol SDK development package.
%description   -n gem-language-server-protocol-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета language_server-protocol.
%endif


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

%if_enabled    doc
%files         -n gem-language-server-protocol-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-language-server-protocol-devel
%doc README.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 3.17.0.3-alt1
- ^ 3.17.0.1 -> 3.17.0.3

* Mon Oct 31 2022 Pavel Skrylev <majioa@altlinux.org> 3.17.0.1-alt1
- + packaged gem with Ruby Policy 2.0
