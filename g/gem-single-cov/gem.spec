%define        gemname single_cov

Name:          gem-single-cov
Version:       1.6.0
Release:       alt1
Summary:       Actionable code coverage
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/grosser/single_cov
Vcs:           https://github.com/grosser/single_cov.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(single_cov) = 1.6.0

%description
Actionable code coverage.


%package       -n gem-single-cov-doc
Version:       1.6.0
Release:       alt1
Summary:       Actionable code coverage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета single_cov
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(single_cov) = 1.6.0

%description   -n gem-single-cov-doc
Actionable code coverage documentation files.

Actionable code coverage.

%description   -n gem-single-cov-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета single_cov.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-single-cov-doc
%ruby_gemdocdir


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- + packaged gem with Ruby Policy 2.0
