%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname unf

Name:          gem-unf
Version:       0.2.0.7
Release:       alt0.1
Summary:       A wrapper library to bring Unicode Normalization Form support to Ruby/JRuby
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/knu/ruby-unf
Vcs:           https://github.com/knu/ruby-unf.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.2.0
BuildRequires: gem(rake) >= 0.9.2.2
BuildRequires: gem(rdoc) > 2.4.2
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(unf_ext) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 1.9.3
Obsoletes:     ruby-unf < %EVR
Provides:      ruby-unf = %EVR
Provides:      unf = %EVR
Provides:      gem(unf) = 0.2.0.7

%ruby_use_gem_version unf:0.2.0.7

%description
A wrapper library to bring Unicode Normalization Form support to Ruby/JRuby.


%if_enabled    doc
%package       -n gem-unf-doc
Version:       0.2.0.7
Release:       alt0.1
Summary:       A wrapper library to bring Unicode Normalization Form support to Ruby/JRuby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета unf
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(unf) = 0.2.0.7

%description   -n gem-unf-doc
A wrapper library to bring Unicode Normalization Form support to Ruby/JRuby
documentation files.

%description   -n gem-unf-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета unf.
%endif


%if_enabled    devel
%package       -n gem-unf-devel
Version:       0.2.0.7
Release:       alt0.1
Summary:       A wrapper library to bring Unicode Normalization Form support to Ruby/JRuby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета unf
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(unf) = 0.2.0.7
Requires:      gem(bundler) >= 1.2.0
Requires:      gem(rake) >= 0.9.2.2
Requires:      gem(rdoc) > 2.4.2
Requires:      gem(test-unit) >= 0
Requires:      gem(unf_ext) >= 0

%description   -n gem-unf-devel
A wrapper library to bring Unicode Normalization Form support to Ruby/JRuby
development package.

%description   -n gem-unf-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета unf.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-unf-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-unf-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Fri Aug 14 2026 Pavel Skrylev <majioa@altlinux.org> 0.2.0.7-alt0.1
- ^ 0.2.0[1] -> 0.2.0p7

* Mon Dec 19 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.0.1-alt1
- ^ 0.2.0 -> 0.2.0[1]

* Fri Apr 03 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt0.1
- > Ruby Policy 2.0
- ^ 0.1.4 -> 0.2.0pre
- ! spec tags

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus.
