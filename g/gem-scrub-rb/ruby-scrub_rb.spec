%define        gemname scrub_rb

Name:          gem-scrub-rb
Version:       1.0.1
Release:       alt1.1
Summary:       Pure-ruby polyfill of MRI 2.1 String#scrub, for ruby 1.9 and 2.0 any interpreter
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jrochkind/scrub_rb
Vcs:           https://github.com/jrochkind/scrub_rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Obsoletes:     ruby-scrub_rb < %EVR
Provides:      ruby-scrub_rb = %EVR
Provides:      gem(scrub_rb) = 1.0.1


%description
Pure-ruby polyfill of MRI 2.1 String#scrub, for ruby 1.9 and 2.0 any
interpreter.


%package       -n gem-scrub-rb-doc
Version:       1.0.1
Release:       alt1.1
Summary:       Pure-ruby polyfill of MRI 2.1 String#scrub, for ruby 1.9 and 2.0 any interpreter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета scrub_rb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(scrub_rb) = 1.0.1

%description   -n gem-scrub-rb-doc
Pure-ruby polyfill of MRI 2.1 String#scrub, for ruby 1.9 and 2.0 any interpreter
documentation files.

Pure-ruby polyfill of MRI 2.1 String#scrub, for ruby 1.9 and 2.0 any
interpreter.

%description   -n gem-scrub-rb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета scrub_rb.


%package       -n gem-scrub-rb-devel
Version:       1.0.1
Release:       alt1.1
Summary:       Pure-ruby polyfill of MRI 2.1 String#scrub, for ruby 1.9 and 2.0 any interpreter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета scrub_rb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(scrub_rb) = 1.0.1
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3
Requires:      gem(rake) >= 0 gem(rake) < 14

%description   -n gem-scrub-rb-devel
Pure-ruby polyfill of MRI 2.1 String#scrub, for ruby 1.9 and 2.0 any interpreter
development package.

Pure-ruby polyfill of MRI 2.1 String#scrub, for ruby 1.9 and 2.0 any
interpreter.

%description   -n gem-scrub-rb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета scrub_rb.


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

%files         -n gem-scrub-rb-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-scrub-rb-devel
%doc README.md


%changelog
* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1.1
- ! spec

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
