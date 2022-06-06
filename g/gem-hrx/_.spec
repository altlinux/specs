%define        gemname hrx

Name:          gem-hrx
Version:       1.0.0.2
Release:       alt1
Summary:       A Ruby implementation of the HRX format
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/google/hrx-ruby
Vcs:           https://github.com/google/hrx-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(linked-list) >= 0.0.13 gem(linked-list) < 0.1
BuildRequires: gem(thor) >= 0.20 gem(thor) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency thor >= 1.0.1,thor < 2
Requires:      gem(linked-list) >= 0.0.13 gem(linked-list) < 0.1
Requires:      gem(thor) >= 0.20 gem(thor) < 2
Provides:      gem(hrx) = 1.0.0.2

%ruby_use_gem_version hrx:1.0.0.2

%description
A Ruby implementation of the HRX format.


%package       -n hrx
Version:       1.0.0.2
Release:       alt1
Summary:       A Ruby implementation of the HRX format executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета hrx
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hrx) = 1.0.0.2

%description   -n hrx
A Ruby implementation of the HRX format executable(s).

%description   -n hrx -l ru_RU.UTF-8
Исполнямка для самоцвета hrx.


%package       -n gem-hrx-devel
Version:       1.0.0.2
Release:       alt1
Summary:       A Ruby implementation of the HRX format development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hrx
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hrx) = 1.0.0.2
Requires:      gem(thor) >= 1.0 gem(thor) < 2

%description   -n gem-hrx-devel
A Ruby implementation of the HRX format development package.

%description   -n gem-hrx-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hrx.


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

%files         -n hrx
%doc README.md
%_bindir/hrx

%files         -n gem-hrx-devel
%doc README.md


%changelog
* Thu Jun 02 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.0.2-alt1
- ^ 1.0.0.1 -> 1.0.0.2

* Wed Sep 16 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0.1-alt0.1
- ^ 1.0.0 -> 1.0.0.1pre
- * relicensing
- ! deps

* Tue Feb 18 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
