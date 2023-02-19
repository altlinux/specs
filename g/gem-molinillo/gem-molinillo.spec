%define        gemname molinillo

Name:          gem-molinillo
Version:       0.8.0
Release:       alt1
Summary:       A generic dependency resolution algorithm
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/CocoaPods/Molinillo
Vcs:           https://github.com/cocoapods/molinillo.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(kicker) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(codeclimate-test-reporter) >= 0
BuildRequires: gem(inch_by_inch) >= 0
BuildRequires: gem(rubocop) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-molinillo < %EVR
Provides:      ruby-molinillo = %EVR
Provides:      gem(molinillo) = 0.8.0


%description
A generic dependency resolution algorithm.


%package       -n gem-molinillo-doc
Version:       0.8.0
Release:       alt1
Summary:       A generic dependency resolution algorithm documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета molinillo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(molinillo) = 0.8.0

%description   -n gem-molinillo-doc
A generic dependency resolution algorithm documentation files.

%description   -n gem-molinillo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета molinillo.


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

%files         -n gem-molinillo-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- ^ 0.6.6 -> 0.8.0 (no devel)

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.6-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.5-alt1
- Initial build for Sisyphus
