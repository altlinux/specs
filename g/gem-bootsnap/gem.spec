%define        gemname bootsnap

Name:          gem-bootsnap
Version:       1.7.5
Release:       alt1
Summary:       Boot large ruby/rails apps faster
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Shopify/bootsnap
Vcs:           https://github.com/shopify/bootsnap.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(mocha) >= 1.2 gem(mocha) < 2
BuildRequires: gem(msgpack) >= 1.0 gem(msgpack) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(msgpack) >= 1.0 gem(msgpack) < 2
Provides:      gem(bootsnap) = 1.7.5


%description
Boot large ruby/rails apps faster.


%package       -n bootsnap
Version:       1.7.5
Release:       alt1
Summary:       Boot large ruby/rails apps faster executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета bootsnap
Group:         Other
BuildArch:     noarch

Requires:      gem(bootsnap) = 1.7.5

%description   -n bootsnap
Boot large ruby/rails apps faster executable(s).

Boot large ruby/rails apps faster

%description   -n bootsnap -l ru_RU.UTF-8
Исполнямка для самоцвета bootsnap.


%package       -n gem-bootsnap-doc
Version:       1.7.5
Release:       alt1
Summary:       Boot large ruby/rails apps faster documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bootsnap
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bootsnap) = 1.7.5

%description   -n gem-bootsnap-doc
Boot large ruby/rails apps faster documentation files.

Boot large ruby/rails apps faster

%description   -n gem-bootsnap-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bootsnap.


%package       -n gem-bootsnap-devel
Version:       1.7.5
Release:       alt1
Summary:       Boot large ruby/rails apps faster development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bootsnap
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bootsnap) = 1.7.5
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rake-compiler) >= 0
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(mocha) >= 1.2 gem(mocha) < 2

%description   -n gem-bootsnap-devel
Boot large ruby/rails apps faster development package.

Boot large ruby/rails apps faster

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
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 1.7.5-alt1
- + packaged gem with Ruby Policy 2.0
