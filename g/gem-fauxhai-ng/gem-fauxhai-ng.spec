%define        gemname fauxhai-ng

Name:          gem-fauxhai-ng
Version:       9.3.0
Release:       alt1
Summary:       Easily mock out ohai data
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/chefspec/fauxhai
Vcs:           https://github.com/chefspec/fauxhai.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(chef) >= 13.0
BuildRequires: gem(ohai) >= 13.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.7
BuildRequires: gem(rspec-its) >= 1.2
BuildRequires: gem(net-ssh) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-its) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(net-ssh) >= 0
Provides:      gem(fauxhai-ng) = 9.3.0


%description
Fauxhai provides an easy way to mock out your ohai data for testing with
chefspec.


%package       -n fauxhai
Version:       9.3.0
Release:       alt1
Summary:       Easily mock out ohai data executable(s).
Summary(ru_RU.UTF-8): Исполнямка для самоцвета fauxhai-ng
Group:         Other
BuildArch:     noarch

Requires:      gem(fauxhai-ng) = 9.3.0

%description   -n fauxhai
Easily mock out ohai data executable(s).

Fauxhai provides an easy way to mock out your ohai data for testing with
chefspec.

%description   -n fauxhai -l ru_RU.UTF-8
Исполнямка для самоцвета fauxhai-ng.


%package       -n gem-fauxhai-ng-doc
Version:       9.3.0
Release:       alt1
Summary:       Easily mock out ohai data documentation files.
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fauxhai-ng
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fauxhai-ng) = 9.3.0

%description   -n gem-fauxhai-ng-doc
Easily mock out ohai data documentation files.

Fauxhai provides an easy way to mock out your ohai data for testing with
chefspec.

%description   -n gem-fauxhai-ng-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fauxhai-ng.


%package       -n gem-fauxhai-ng-devel
Version:       9.3.0
Release:       alt1
Summary:       Easily mock out ohai data development package.
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fauxhai-ng
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fauxhai-ng) = 9.3.0
Requires:      gem(chef) >= 13.0
Requires:      gem(ohai) >= 13.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.7
Requires:      gem(rspec-its) >= 1.2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-its) >= 2

%description   -n gem-fauxhai-ng-devel
Easily mock out ohai data development package.

Fauxhai provides an easy way to mock out your ohai data for testing with
chefspec.

%description   -n gem-fauxhai-ng-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fauxhai-ng.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n fauxhai
%_bindir/fauxhai

%files         -n gem-fauxhai-ng-doc
%ruby_gemdocdir

%files         -n gem-fauxhai-ng-devel


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 9.3.0-alt1
- ^ 9.0.0 -> 9.3.0

* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 9.0.0-alt1
- + packaged gem with Ruby Policy 2.0
