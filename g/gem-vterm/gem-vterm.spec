%define        gemname vterm

Name:          gem-vterm
Version:       0.0.5
Release:       alt1
Summary:       A wrapper library of libvterm
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/aycabta/vterm-gem
Vcs:           https://github.com/aycabta/vterm-gem.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: pkgconfig(vterm)
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(vterm) = 0.0.5


%description
A wrapper library of libvterm


%package       -n gem-vterm-doc
Version:       0.0.5
Release:       alt1
Summary:       A wrapper library of libvterm documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vterm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vterm) = 0.0.5

%description   -n gem-vterm-doc
A wrapper library of libvterm documentation files.

%description   -n gem-vterm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vterm.


%package       -n gem-vterm-devel
Version:       0.0.5
Release:       alt1
Summary:       A wrapper library of libvterm development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vterm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vterm) = 0.0.5
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-vterm-devel
A wrapper library of libvterm development package.

%description   -n gem-vterm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vterm.


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

%files         -n gem-vterm-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-vterm-devel
%doc README.md


%changelog
* Tue Nov 01 2022 Pavel Skrylev <majioa@altlinux.org> 0.0.5-alt1
- + packaged gem with Ruby Policy 2.0
