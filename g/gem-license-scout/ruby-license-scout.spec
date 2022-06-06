%define        gemname license_scout

Name:          gem-license-scout
Version:       2.6.2
Release:       alt1
Summary:       Discovers license files of a project's dependencies
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/license_scout
Vcs:           https://github.com/chef/license_scout.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ffi-yajl) >= 2.2 gem(ffi-yajl) < 3
BuildRequires: gem(toml-rb) >= 1.0 gem(toml-rb) < 3
BuildRequires: gem(licensee) >= 9.8 gem(licensee) < 10
BuildRequires: gem(mixlib-config) >= 2.2 gem(mixlib-config) < 4
BuildRequires: gem(mixlib-cli) >= 0
BuildRequires: gem(mixlib-log) >= 0
BuildRequires: gem(mixlib-shellout) >= 2.2 gem(mixlib-shellout) < 4
BuildRequires: gem(terminal-table) >= 0
BuildRequires: gem(fuzzy_match) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency toml-rb >= 2.1.2,toml-rb < 3
%ruby_use_gem_dependency mixlib-config >= 3.0.6,mixlib-config < 4
%ruby_use_gem_dependency mixlib-shellout >= 3.2.5,mixlib-shellout < 4
Requires:      gem(ffi-yajl) >= 2.2 gem(ffi-yajl) < 3
Requires:      gem(mixlib-shellout) >= 2.2 gem(mixlib-shellout) < 4
Requires:      gem(toml-rb) >= 1.0 gem(toml-rb) < 3
Requires:      gem(licensee) >= 9.8 gem(licensee) < 10
Requires:      gem(mixlib-config) >= 2.2 gem(mixlib-config) < 4
Requires:      gem(mixlib-cli) >= 0
Requires:      gem(mixlib-log) >= 0
Requires:      gem(terminal-table) >= 0
Requires:      gem(fuzzy_match) >= 0
Provides:      gem(license_scout) = 2.6.2


%description
Discovers license files of a project's dependencies.


%package       -n license-scout
Version:       2.6.2
Release:       alt1
Summary:       Discovers license files of a project's dependencies executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета license_scout
Group:         Other
BuildArch:     noarch

Requires:      gem(license_scout) = 2.6.2

%description   -n license-scout
Discovers license files of a project's dependencies executable(s).

%description   -n license-scout -l ru_RU.UTF-8
Исполнямка для самоцвета license_scout.


%package       -n gem-license-scout-doc
Version:       2.6.2
Release:       alt1
Summary:       Discovers license files of a project's dependencies documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета license_scout
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(license_scout) = 2.6.2

%description   -n gem-license-scout-doc
Discovers license files of a project's dependencies documentation files.

%description   -n gem-license-scout-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета license_scout.


%package       -n gem-license-scout-devel
Version:       2.6.2
Release:       alt1
Summary:       Discovers license files of a project's dependencies development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета license_scout
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(license_scout) = 2.6.2

%description   -n gem-license-scout-devel
Discovers license files of a project's dependencies development package.

%description   -n gem-license-scout-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета license_scout.


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

%files         -n license-scout
%doc README.md
%_bindir/license_scout

%files         -n gem-license-scout-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-license-scout-devel
%doc README.md


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.6.2-alt1
- + packaged gem with Ruby Policy 2.0
