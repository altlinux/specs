%define        gemname powerpack

Name:          gem-powerpack
Version:       0.1.3
Release:       alt1
Summary:       Some useful extensions to the core Ruby classes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bbatsov/powerpack
Vcs:           https://github.com/bbatsov/powerpack.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(yard) >= 0.9 gem(yard) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Provides:      gem(powerpack) = 0.1.3


%description
Powerpack offers some useful extensions to the standard Ruby classes (kind of
like ActiveSupport, but less ambitious and more modular).

The project has several design goals:

* minimalistic - we don't add every possible extensions, we focus only on the
  stuff that are commonly requested and would be often useful in practice
* modular - all extensions can be loaded individually (often they are just
  individual methods)
* safe - you can't end up accidentally overriding some existing method
  definition with Powerpack's extensions


%package       -n gem-powerpack-doc
Version:       0.1.3
Release:       alt1
Summary:       Some useful extensions to the core Ruby classes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета powerpack
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(powerpack) = 0.1.3

%description   -n gem-powerpack-doc
Some useful extensions to the core Ruby classes documentation files.

Powerpack offers some useful extensions to the standard Ruby classes (kind of
like ActiveSupport, but less ambitious and more modular).

The project has several design goals:

* minimalistic - we don't add every possible extensions, we focus only on the
  stuff that are commonly requested and would be often useful in practice
* modular - all extensions can be loaded individually (often they are just
  individual methods)
* safe - you can't end up accidentally overriding some existing method
  definition with Powerpack's extensions

%description   -n gem-powerpack-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета powerpack.


%package       -n gem-powerpack-devel
Version:       0.1.3
Release:       alt1
Summary:       Some useful extensions to the core Ruby classes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета powerpack
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(powerpack) = 0.1.3
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(yard) >= 0.9 gem(yard) < 1

%description   -n gem-powerpack-devel
Some useful extensions to the core Ruby classes development package.

Powerpack offers some useful extensions to the standard Ruby classes (kind of
like ActiveSupport, but less ambitious and more modular).

The project has several design goals:

* minimalistic - we don't add every possible extensions, we focus only on the
  stuff that are commonly requested and would be often useful in practice
* modular - all extensions can be loaded individually (often they are just
  individual methods)
* safe - you can't end up accidentally overriding some existing method
  definition with Powerpack's extensions

%description   -n gem-powerpack-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета powerpack.


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

%files         -n gem-powerpack-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-powerpack-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.3-alt1
- ^ 0.1.2 -> 0.1.3

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
