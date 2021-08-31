%define        gemname temple

Name:          gem-temple
Version:       0.8.2
Release:       alt1
Summary:       Template compilation framework in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/judofyr/temple
Vcs:           https://github.com/judofyr/temple.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(tilt) >= 0
BuildRequires: gem(bacon) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(erubis) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-temple < %EVR
Provides:      ruby-temple = %EVR
Provides:      gem(temple) = 0.8.2


%description
Temple is an abstraction and a framework for compiling templates to pure Ruby.
It's all about making it easier to experiment, implement and optimize template
languages. If you're interested in implementing your own template language, or
anything else related to the internals of a template engine: You've come to the
right place.


%package       -n gem-temple-doc
Version:       0.8.2
Release:       alt1
Summary:       Template compilation framework in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета temple
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(temple) = 0.8.2

%description   -n gem-temple-doc
Template compilation framework in Ruby documentation files.

Temple is an abstraction and a framework for compiling templates to pure Ruby.
It's all about making it easier to experiment, implement and optimize template
languages. If you're interested in implementing your own template language, or
anything else related to the internals of a template engine: You've come to the
right place.

%description   -n gem-temple-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета temple.


%package       -n gem-temple-devel
Version:       0.8.2
Release:       alt1
Summary:       Template compilation framework in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета temple
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(temple) = 0.8.2
Requires:      gem(tilt) >= 0
Requires:      gem(bacon) >= 0
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(erubis) >= 0

%description   -n gem-temple-devel
Template compilation framework in Ruby development package.

Temple is an abstraction and a framework for compiling templates to pure Ruby.
It's all about making it easier to experiment, implement and optimize template
languages. If you're interested in implementing your own template language, or
anything else related to the internals of a template engine: You've come to the
right place.

%description   -n gem-temple-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета temple.


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

%files         -n gem-temple-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-temple-devel
%doc README.md


%changelog
* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 0.8.2-alt1
- ^ 0.8.0 -> 0.8.2

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Thu Sep 28 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus
