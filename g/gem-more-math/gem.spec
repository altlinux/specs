%define        gemname more_math

Name:          gem-more-math
Version:       0.4.0
Release:       alt1
Summary:       Library that provides more mathematics
License:       MIT
Group:         Development/Ruby
Url:           http://flori.github.com/more_math
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(gem_hadar) >= 1.9.1 gem(gem_hadar) < 2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(codeclimate-test-reporter) >= 0
BuildRequires: gem(tins) >= 1.0 gem(tins) < 2
BuildRequires: gem(mize) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency gem_hadar >= 1.12.0,gem_hadar < 2
Requires:      gem(tins) >= 1.0 gem(tins) < 2
Requires:      gem(mize) >= 0
Provides:      gem(more_math) = 0.4.0


%description
Library that provides more mathematical functions/algorithms than standard Ruby.


%package       -n gem-more-math-doc
Version:       0.4.0
Release:       alt1
Summary:       Library that provides more mathematics documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета more_math
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(more_math) = 0.4.0

%description   -n gem-more-math-doc
Library that provides more mathematics documentation files.

Library that provides more mathematical functions/algorithms than standard Ruby.

%description   -n gem-more-math-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета more_math.


%package       -n gem-more-math-devel
Version:       0.4.0
Release:       alt1
Summary:       Library that provides more mathematics development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета more_math
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(more_math) = 0.4.0
Requires:      gem(gem_hadar) >= 1.9.1 gem(gem_hadar) < 2
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(codeclimate-test-reporter) >= 0

%description   -n gem-more-math-devel
Library that provides more mathematics development package.

Library that provides more mathematical functions/algorithms than standard Ruby.

%description   -n gem-more-math-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета more_math.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-more-math-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-more-math-devel
%doc README.rdoc


%changelog
* Wed Jul 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with Ruby Policy 2.0
