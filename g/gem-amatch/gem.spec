%define        gemname amatch

Name:          gem-amatch
Version:       0.4.0
Release:       alt1
Summary:       Approximate String Matching library
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://github.com/flori/amatch
Vcs:           https://github.com/flori/amatch.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(gem_hadar) >= 1.9.1 gem(gem_hadar) < 2
BuildRequires: gem(test-unit) >= 3.0 gem(test-unit) < 4
BuildRequires: gem(tins) >= 1.0 gem(tins) < 2
BuildRequires: gem(mize) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency gem_hadar >= 1.11.0,gem_hadar < 2
Requires:      gem(tins) >= 1.0 gem(tins) < 2
Requires:      gem(mize) >= 0
Provides:      gem(amatch) = 0.4.0


%description
Amatch is a library for approximate string matching and searching in strings.
Several algorithms can be used to do this, and it's also possible to compute a
similarity metric number between 0.0 and 1.0 for two given strings.


%package       -n amatch
Version:       0.4.0
Release:       alt1
Summary:       Approximate String Matching library executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета amatch
Group:         Other
BuildArch:     noarch

Requires:      gem(amatch) = 0.4.0

%description   -n amatch
Approximate String Matching library executable(s).

Amatch is a library for approximate string matching and searching in strings.
Several algorithms can be used to do this, and it's also possible to compute a
similarity metric number between 0.0 and 1.0 for two given strings.

%description   -n amatch -l ru_RU.UTF-8
Исполнямка для самоцвета amatch.


%package       -n gem-amatch-doc
Version:       0.4.0
Release:       alt1
Summary:       Approximate String Matching library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета amatch
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(amatch) = 0.4.0

%description   -n gem-amatch-doc
Approximate String Matching library documentation files.

Amatch is a library for approximate string matching and searching in strings.
Several algorithms can be used to do this, and it's also possible to compute a
similarity metric number between 0.0 and 1.0 for two given strings.

%description   -n gem-amatch-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета amatch.


%package       -n gem-amatch-devel
Version:       0.4.0
Release:       alt1
Summary:       Approximate String Matching library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета amatch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(amatch) = 0.4.0
Requires:      gem(gem_hadar) >= 1.9.1 gem(gem_hadar) < 2
Requires:      gem(test-unit) >= 3.0 gem(test-unit) < 4

%description   -n gem-amatch-devel
Approximate String Matching library development package.

Amatch is a library for approximate string matching and searching in strings.
Several algorithms can be used to do this, and it's also possible to compute a
similarity metric number between 0.0 and 1.0 for two given strings.

%description   -n gem-amatch-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета amatch.


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

%files         -n amatch
%doc README.md
%_bindir/agrep
%_bindir/dupfind

%files         -n gem-amatch-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-amatch-devel
%doc README.md
%ruby_includedir/*


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with Ruby Policy 2.0
