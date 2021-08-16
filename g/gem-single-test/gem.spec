%define        gemname single_test

Name:          gem-single-test
Version:       0.6.0
Release:       alt1
Summary:       Rake tasks to invoke single tests/specs with rakish syntax
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/grosser/single_test
Vcs:           https://github.com/grosser/single_test.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rake) >= 0
Provides:      gem(single_test) = 0.6.0

%description
Rake tasks to invoke single tests/specs with rakish syntax.


%package       -n gem-single-test-doc
Version:       0.6.0
Release:       alt1
Summary:       Rake tasks to invoke single tests/specs with rakish syntax documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета single_test
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(single_test) = 0.6.0

%description   -n gem-single-test-doc
Rake tasks to invoke single tests/specs with rakish syntax documentation files.

%description   -n gem-single-test-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета single_test.


%package       -n gem-single-test-devel
Version:       0.6.0
Release:       alt1
Summary:       Rake tasks to invoke single tests/specs with rakish syntax development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета single_test
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(single_test) = 0.6.0

%description   -n gem-single-test-devel
Rake tasks to invoke single tests/specs with rakish syntax development package.

%description   -n gem-single-test-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета single_test.


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

%files         -n gem-single-test-doc
%ruby_gemdocdir

%files         -n gem-single-test-devel


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- + packaged gem with Ruby Policy 2.0
