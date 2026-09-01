%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fakefs

Name:          gem-fakefs
Version:       3.2.1
Release:       alt1
Summary:       A fake filesystem. Use it in your tests
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fakefs/fakefs
Vcs:           https://github.com/fakefs/fakefs.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bump) >= 0
BuildRequires: gem(csv) >= 0
BuildRequires: gem(irb) >= 0
BuildRequires: gem(maxitest) >= 0
BuildRequires: gem(mutex_m) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0
Requires:      ruby >= 3.2.0
Provides:      gem(fakefs) = 3.2.1

%description
A fake filesystem. Use it in your tests.


%if_enabled    doc
%package       -n gem-fakefs-doc
Version:       3.2.1
Release:       alt1
Summary:       A fake filesystem. Use it in your tests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fakefs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fakefs) = 3.2.1

%description   -n gem-fakefs-doc
A fake filesystem. Use it in your tests documentation files.

%description   -n gem-fakefs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fakefs.
%endif


%if_enabled    devel
%package       -n gem-fakefs-devel
Version:       3.2.1
Release:       alt1
Summary:       A fake filesystem. Use it in your tests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fakefs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fakefs) = 3.2.1
Requires:      gem(bump) >= 0
Requires:      gem(csv) >= 0
Requires:      gem(irb) >= 0
Requires:      gem(maxitest) >= 0
Requires:      gem(mutex_m) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 1.15.0

%description   -n gem-fakefs-devel
A fake filesystem. Use it in your tests development package.

%description   -n gem-fakefs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fakefs.
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
%doc LICENSE README.md CHANGELOG.md CONTRIBUTORS
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-fakefs-doc
%doc LICENSE README.md CHANGELOG.md CONTRIBUTORS
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fakefs-devel
%doc LICENSE README.md CHANGELOG.md CONTRIBUTORS
%endif


%changelog
* Tue Sep 01 2026 Pavel Skrylev <majioa@altlinux.org> 3.2.1-alt1
- ^ 1.9.0 -> 3.2.1

* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.9.0-alt1
- ^ 1.3.2 -> 1.9.0

* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.2-alt1
- + packaged gem with Ruby Policy 2.0
