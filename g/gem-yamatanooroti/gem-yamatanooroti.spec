%define        gemname yamatanooroti

Name:          gem-yamatanooroti
Version:       0.0.9
Release:       alt1
Summary:       Multi-platform real(?) terminal test framework
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/aycabta/yamatanooroti
Vcs:           https://github.com/aycabta/yamatanooroti.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(vterm) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(reline) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(test-unit) >= 0
Provides:      gem(yamatanooroti) = 0.0.9


%description
Yamatanooroti is a multi-platform real(?) terminal test framework.


%package       -n gem-yamatanooroti-doc
Version:       0.0.9
Release:       alt1
Summary:       Multi-platform real(?) terminal test framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета yamatanooroti
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(yamatanooroti) = 0.0.9

%description   -n gem-yamatanooroti-doc
Multi-platform real(?) terminal test framework documentation
files.

Yamatanooroti is a multi-platform real(?) terminal test framework.

%description   -n gem-yamatanooroti-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета yamatanooroti.


%package       -n gem-yamatanooroti-devel
Version:       0.0.9
Release:       alt1
Summary:       Multi-platform real(?) terminal test framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета yamatanooroti
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(yamatanooroti) = 0.0.9
Requires:      gem(vterm) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(reline) >= 0

%description   -n gem-yamatanooroti-devel
Multi-platform real(?) terminal test framework development
package.

Yamatanooroti is a multi-platform real(?) terminal test framework.

%description   -n gem-yamatanooroti-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета yamatanooroti.


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

%files         -n gem-yamatanooroti-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-yamatanooroti-devel
%doc README.md


%changelog
* Tue Nov 01 2022 Pavel Skrylev <majioa@altlinux.org> 0.0.9-alt1
- + packaged gem with Ruby Policy 2.0
