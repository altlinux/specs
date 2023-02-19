%define        gemname mocha-on-bacon

Name:          gem-mocha-on-bacon
Version:       0.2.3
Release:       alt1
Summary:       A Mocha adapter for Bacon
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/alloy/mocha-on-bacon
Vcs:           https://github.com/alloy/mocha-on-bacon.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(mocha) >= 0.13.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(mocha) >= 0.13.0
Provides:      gem(mocha-on-bacon) = 0.2.3


%description
A Mocha adapter for Bacon, because it's yummy!


%package       -n gem-mocha-on-bacon-doc
Version:       0.2.3
Release:       alt1
Summary:       A Mocha adapter for Bacon documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mocha-on-bacon
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mocha-on-bacon) = 0.2.3

%description   -n gem-mocha-on-bacon-doc
A Mocha adapter for Bacon documentation files.

A Mocha adapter for Bacon, because it's yummy!

%description   -n gem-mocha-on-bacon-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mocha-on-bacon.


%package       -n gem-mocha-on-bacon-devel
Version:       0.2.3
Release:       alt1
Summary:       A Mocha adapter for Bacon development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mocha-on-bacon
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mocha-on-bacon) = 0.2.3

%description   -n gem-mocha-on-bacon-devel
A Mocha adapter for Bacon development package.

A Mocha adapter for Bacon, because it's yummy!

%description   -n gem-mocha-on-bacon-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mocha-on-bacon.


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

%files         -n gem-mocha-on-bacon-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mocha-on-bacon-devel
%doc README.md


%changelog
* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt1
- + packaged gem with Ruby Policy 2.0
