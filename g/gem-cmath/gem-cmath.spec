%define        gemname cmath

Name:          gem-cmath
Version:       1.0.0
Release:       alt1
Summary:       Provides Trigonometric and Transcendental functions for complex numbers
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/cmath
Vcs:           https://github.com/ruby/cmath.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(cmath) = 1.0.0


%description
CMath is a library that provides trigonometric and transcendental functions for
complex numbers. The functions in this module accept integers, floating-point
numbers or complex numbers as arguments.


%package       -n gem-cmath-doc
Version:       1.0.0
Release:       alt1
Summary:       Provides Trigonometric and Transcendental functions for complex numbers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cmath
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(cmath) = 1.0.0

%description   -n gem-cmath-doc
Provides Trigonometric and Transcendental functions for complex numbers
documentation files.

CMath is a library that provides trigonometric and transcendental functions for
complex numbers. The functions in this module accept integers, floating-point
numbers or complex numbers as arguments.

%description   -n gem-cmath-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cmath.


%package       -n gem-cmath-devel
Version:       1.0.0
Release:       alt1
Summary:       Provides Trigonometric and Transcendental functions for complex numbers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cmath
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cmath) = 1.0.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-cmath-devel
Provides Trigonometric and Transcendental functions for complex numbers
development package.

CMath is a library that provides trigonometric and transcendental functions for
complex numbers. The functions in this module accept integers, floating-point
numbers or complex numbers as arguments.

%description   -n gem-cmath-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cmath.


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

%files         -n gem-cmath-doc
%ruby_gemdocdir

%files         -n gem-cmath-devel


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
