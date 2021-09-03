%define        gemname ffi-yajl

Name:          gem-ffi-yajl
Version:       2.4.0.1
Release:       alt1
Summary:       ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/chef/ffi-yajl
Vcs:           https://github.com/chef/ffi-yajl.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         use-system-yajl-without-wrapper.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(libyajl2) >= 1.2
BuildRequires: libyajl-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version ffi-yajl:2.4.0.1
Requires:      gem(libyajl2) >= 1.2
Obsoletes:     ruby-ffi-yajl < %EVR
Provides:      ruby-ffi-yajl = %EVR
Provides:      gem(ffi-yajl) = 2.4.0.1


%description
ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library. ffi-yajl
supports multiple Ruby C extension mechanisms, including both MRI native
extensions and FFI in order to be compatible with as many Ruby implementations
as possible while providing good performance where possible.


%package       -n ffi-yajl-bench
Version:       2.4.0.1
Release:       alt1
Summary:       ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ffi-yajl
Group:         Development/Other
BuildArch:     noarch

Requires:      gem(ffi-yajl) = 2.4.0.1

%description   -n ffi-yajl-bench
ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library
executable(s).

ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library. ffi-yajl
supports multiple Ruby C extension mechanisms, including both MRI native
extensions and FFI in order to be compatible with as many Ruby implementations
as possible while providing good performance where possible.

%description   -n ffi-yajl-bench -l ru_RU.UTF-8
Исполнямка для самоцвета ffi-yajl.


%package       -n gem-ffi-yajl-doc
Version:       2.4.0.1
Release:       alt1
Summary:       ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ffi-yajl
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ffi-yajl) = 2.4.0.1

%description   -n gem-ffi-yajl-doc
ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library
documentation files.

ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library. ffi-yajl
supports multiple Ruby C extension mechanisms, including both MRI native
extensions and FFI in order to be compatible with as many Ruby implementations
as possible while providing good performance where possible.

%description   -n gem-ffi-yajl-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ffi-yajl.


%package       -n gem-ffi-yajl-devel
Version:       2.4.0.1
Release:       alt1
Summary:       ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ffi-yajl
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ffi-yajl) = 2.4.0.1
Requires:      libyajl-devel

%description   -n gem-ffi-yajl-devel
ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library
development package.

ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library. ffi-yajl
supports multiple Ruby C extension mechanisms, including both MRI native
extensions and FFI in order to be compatible with as many Ruby implementations
as possible while providing good performance where possible.

%description   -n gem-ffi-yajl-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ffi-yajl.


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
%ruby_gemextdir

%files         -n ffi-yajl-bench
%doc README.md
%_bindir/ffi-yajl-bench

%files         -n gem-ffi-yajl-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ffi-yajl-devel
%doc README.md


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 2.4.0.1-alt1
- ^ 2.4.0 -> 2.4.0.1

* Sat Apr 24 2021 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- ^ 2.3.3 -> 2.4.0

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 2.3.3-alt1
- ^ 2.3.1 -> 2.3.3
- ! spec stags and syntax

* Tue Mar 12 2019 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt4
- ! built extensions by the patch

* Tue Feb 05 2019 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt3
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt2.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt2
- Fix yajl-ruby library name.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Jun 22 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt2
- Rebuild with new %%ruby_sitearchdir location
- Optionally build benchmark tool, disabled by default

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- new version 2.3.0

* Tue Sep 22 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- New version

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux
