%define        gemname bootsnap

Name:          gem-bootsnap
Version:       1.13.0
Release:       alt1
Summary:       Boot large ruby/rails apps faster
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Shopify/bootsnap
Vcs:           https://github.com/shopify/bootsnap.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(msgpack) >= 1.2 gem(msgpack) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.27.0,rubocop < 2
Requires:      gem(msgpack) >= 1.2 gem(msgpack) < 2
Provides:      gem(bootsnap) = 1.13.0


%description
Boot large ruby/rails apps faster.


%package       -n bootsnap
Version:       1.13.0
Release:       alt1
Summary:       Boot large ruby/rails apps faster executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета bootsnap
Group:         Other
BuildArch:     noarch

Requires:      gem(bootsnap) = 1.13.0

%description   -n bootsnap
Boot large ruby/rails apps faster executable(s).

%description   -n bootsnap -l ru_RU.UTF-8
Исполнямка для самоцвета bootsnap.


%package       -n gem-bootsnap-doc
Version:       1.13.0
Release:       alt1
Summary:       Boot large ruby/rails apps faster documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bootsnap
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bootsnap) = 1.13.0

%description   -n gem-bootsnap-doc
Boot large ruby/rails apps faster documentation files.

%description   -n gem-bootsnap-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bootsnap.


%package       -n gem-bootsnap-devel
Version:       1.13.0
Release:       alt1
Summary:       Boot large ruby/rails apps faster development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bootsnap
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bootsnap) = 1.13.0

%description   -n gem-bootsnap-devel
Boot large ruby/rails apps faster development package.

%description   -n gem-bootsnap-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bootsnap.


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

%files         -n bootsnap
%doc README.md
%_bindir/bootsnap

%files         -n gem-bootsnap-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-bootsnap-devel
%doc README.md
%ruby_includedir/*


%changelog
* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt1
- ^ 1.11.1 -> 1.13.0

* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.11.1-alt1
- ^ 1.7.5 -> 1.11.1

* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 1.7.5-alt1
- + packaged gem with Ruby Policy 2.0
