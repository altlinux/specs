%define        gemname sassc

Name:          gem-sassc
Version:       2.4.0.1
Release:       alt1.1
Summary:       Use libsass with Ruby!
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sass/sassc-ruby
Vcs:           https://github.com/sass/sassc-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         use-system-libsass.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: libstdc++-devel
BuildRequires: libsass-devel
%if_with check
BuildRequires: gem(minitest) >= 5.5.1 gem(minitest) < 6
BuildRequires: gem(minitest-around) >= 0
BuildRequires: gem(test_construct) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rake-compiler-dock) >= 0
BuildRequires: gem(ffi) >= 1.9 gem(ffi) < 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      gem(ffi) >= 1.9 gem(ffi) < 2
Requires:      libsass
Obsoletes:     ruby-sassc < %EVR
Provides:      ruby-sassc = %EVR
Provides:      gem(sassc) = 2.4.0.1

%ruby_use_gem_version sassc:2.4.0.1

%description
This gem combines the speed of libsass, the Sass C implementation, with the ease
of use of the original Ruby Sass library.


%package       -n gem-sassc-doc
Version:       2.4.0.1
Release:       alt1.1
Summary:       Use libsass with Ruby! documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sassc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sassc) = 2.4.0.1

%description   -n gem-sassc-doc
Use libsass with Ruby! documentation files.

This gem combines the speed of libsass, the Sass C implementation, with the ease
of use of the original Ruby Sass library.

%description   -n gem-sassc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sassc.


%package       -n gem-sassc-devel
Version:       2.4.0.1
Release:       alt1.1
Summary:       Use libsass with Ruby! development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sassc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sassc) = 2.4.0.1
Requires:      libstdc++-devel
Requires:      gem(minitest) >= 5.5.1 gem(minitest) < 6
Requires:      gem(minitest-around) >= 0
Requires:      gem(test_construct) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rake-compiler-dock) >= 0

%description   -n gem-sassc-devel
Use libsass with Ruby! development package.

This gem combines the speed of libsass, the Sass C implementation, with the ease
of use of the original Ruby Sass library.

%description   -n gem-sassc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sassc.


%prep
%setup
%autopatch

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

%files         -n gem-sassc-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sassc-devel
%doc README.md


%changelog
* Wed Dec 21 2022 Pavel Skrylev <majioa@altlinux.org> 2.4.0.1-alt1.1
- - extension for gemspec

* Tue Oct 11 2022 Pavel Skrylev <majioa@altlinux.org> 2.4.0.1-alt1
- ^ 2.4.0 -> 2.4.0.1

* Fri Oct 29 2021 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt3
- ! patch loading the sassc in runtime

* Wed Dec 09 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt2
- ! typo

* Wed Dec 09 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1.1
- ! picking up the libsass from system if any

* Tue Dec 08 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- ^ 2.2.1 -> 2.4.0

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt2.1
- ! spec tags and syntax, build procedure

* Fri Nov 08 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt2
- changed (*) spec to use build requires
- fixed (!) lost link to system's .so lib (closes #37433)
- fixed (!) requires

* Thu Sep 26 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt1
- update (^) 2.0.0 -> 2.2.1
- use (>) Ruby Police 2.0

* Wed Sep 26 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.12.1-alt1
- New version.
- Disable tests.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.12.0-alt1
- New version.
- Package as gem.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.11.4-alt1
- Initial build for Sisyphus
