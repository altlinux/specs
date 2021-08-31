%define        gemname tilt

Name:          gem-tilt
Version:       2.0.10.1
Release:       alt1
Summary:       Generic interface to multiple Ruby template engines
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rtomayko/tilt
Vcs:           https://github.com/rtomayko/tilt.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version tilt:2.0.10.1
Obsoletes:     ruby-tilt < %EVR
Provides:      ruby-tilt = %EVR
Provides:      gem(tilt) = 2.0.10.1


%description
Tilt is a thin interface over a bunch of different Ruby template engines in an
attempt to make their usage as generic as possible. This is useful for web
frameworks, static site generators, and other systems that support multiple
template engines but don't want to code for each of them individually.

The following features are supported for all template engines (assuming the
feature is relevant to the engine):
* Custom template evaluation scopes / bindings
* Ability to pass locals to template evaluation
* Support for passing a block to template evaluation for "yield"
* Backtraces with correct filenames and line numbers
* Template file caching and reloading
* Fast, method-based template source compilation


%package       -n tilt
Version:       2.0.10.1
Release:       alt1
Summary:       Generic interface to multiple Ruby template engines executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета tilt
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tilt) = 2.0.10.1

%description   -n tilt
Generic interface to multiple Ruby template engines executable(s).

Tilt is a thin interface over a bunch of different Ruby template engines in an
attempt to make their usage as generic as possible. This is useful for web
frameworks, static site generators, and other systems that support multiple
template engines but don't want to code for each of them individually.

The following features are supported for all template engines (assuming the
feature is relevant to the engine):
* Custom template evaluation scopes / bindings
* Ability to pass locals to template evaluation
* Support for passing a block to template evaluation for "yield"
* Backtraces with correct filenames and line numbers
* Template file caching and reloading
* Fast, method-based template source compilation

%description   -n tilt -l ru_RU.UTF-8
Исполнямка для самоцвета tilt.


%package       -n gem-tilt-doc
Version:       2.0.10.1
Release:       alt1
Summary:       Generic interface to multiple Ruby template engines documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tilt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tilt) = 2.0.10.1

%description   -n gem-tilt-doc
Generic interface to multiple Ruby template engines documentation files.

Tilt is a thin interface over a bunch of different Ruby template engines in an
attempt to make their usage as generic as possible. This is useful for web
frameworks, static site generators, and other systems that support multiple
template engines but don't want to code for each of them individually.

The following features are supported for all template engines (assuming the
feature is relevant to the engine):
* Custom template evaluation scopes / bindings
* Ability to pass locals to template evaluation
* Support for passing a block to template evaluation for "yield"
* Backtraces with correct filenames and line numbers
* Template file caching and reloading
* Fast, method-based template source compilation

%description   -n gem-tilt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tilt.


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

%files         -n tilt
%_bindir/tilt

%files         -n gem-tilt-doc
%ruby_gemdocdir


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.10.1-alt1
- ^ 2.0.10 -> 2.0.10[1]

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.10-alt1
- updated to (^) v2.0.10
- fixed (!) spec

* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.9-alt2
- updated to (^) Ruby Policy 2.0

* Wed Dec 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.9-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.8-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Sat Oct 14 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.8-alt1
- New version

* Sun Sep 10 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.7-alt1.2
- Rebuild with Ruby 2.4.1

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.7-alt1.1
- Rebuild with Ruby 2.4.1

* Wed Jun 14 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.7-alt1
- Initial build for Sisyphus
