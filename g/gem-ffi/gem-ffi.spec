%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ffi

Name:          gem-ffi
Version:       1.17.0
Release:       alt2
Summary:       Ruby foreign function interface
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           https://github.com/ffi/ffi/wiki
Vcs:           https://github.com/ffi/ffi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Source1:       e2k-types.conf
BuildRequires(pre): rpm-build-ruby
BuildRequires: libffi-devel
%if_enabled check
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(bundler) >= 1.16
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 1.1
BuildRequires: gem(rake-compiler-dock) >= 1.2.1
BuildRequires: gem(rspec) >= 2.15
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(rbs) >= 3.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(rbs) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rake-compiler-dock >= 1.2.1,rake-compiler-dock < 2
Obsoletes:     ruby-ffi < %EVR
Provides:      ruby-ffi = %EVR
Provides:      gem(ffi) = 1.17.0


%description
Ruby-FFI is a gem for programmatically loading dynamically-linked native
libraries, binding functions within them, and calling those functions from Ruby
code. Moreover, a Ruby-FFI extension works without changes on CRuby (MRI),
JRuby, Rubinius and TruffleRuby. Discover why you should write your next
extension using Ruby-FFI.


%if_enabled    doc
%package       -n gem-ffi-doc
Version:       1.17.0
Release:       alt1
Summary:       Ruby foreign function interface documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ffi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ffi) = 1.17.0

%description   -n gem-ffi-doc
Ruby foreign function interface documentation files.

Ruby-FFI is a gem for programmatically loading dynamically-linked native
libraries, binding functions within them, and calling those functions from Ruby
code. Moreover, a Ruby-FFI extension works without changes on CRuby (MRI),
JRuby, Rubinius and TruffleRuby. Discover why you should write your next
extension using Ruby-FFI.

%description   -n gem-ffi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ffi.
%endif


%if_enabled    devel
%package       -n gem-ffi-devel
Version:       1.17.0
Release:       alt1
Summary:       Ruby foreign function interface development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ffi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ffi) = 1.17.0
Requires:      gem(bigdecimal) >= 0
Requires:      gem(bundler) >= 1.16
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 1.1
Requires:      gem(rake-compiler-dock) >= 1.2.1
Requires:      gem(rspec) >= 2.15
Requires:      gem(kramdown) >= 0
Requires:      gem(yard) >= 0.9
Requires:      gem(rbs) >= 3.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(yard) >= 1
Conflicts:     gem(rbs) >= 4

%description   -n gem-ffi-devel
Ruby foreign function interface development package.

Ruby-FFI is a gem for programmatically loading dynamically-linked native
libraries, binding functions within them, and calling those functions from Ruby
code. Moreover, a Ruby-FFI extension works without changes on CRuby (MRI),
JRuby, Rubinius and TruffleRuby. Discover why you should write your next
extension using Ruby-FFI.

%description   -n gem-ffi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ffi.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install
install -pDm644 %SOURCE1 \
	%buildroot%ruby_gemlibdir/lib/ffi/platform/e2k-linux/types.conf

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-ffi-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ffi-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Mon Sep 02 2024 Michael Shigorin <mike@altlinux.org> 1.17.0-alt2
- added types.conf for e2k from MCST PDK 8.1rc2 (distributable)

* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.17.0-alt1
- ^ 1.16.3p25 -> 1.17.0

* Sun Feb 04 2024 Pavel Skrylev <majioa@altlinux.org> 1.16.3.25-alt0.1
- ^ 1.16.3 -> 1.16.3p25
- ! FTBFS for lost ffi.h

* Mon Dec 04 2023 Pavel Skrylev <majioa@altlinux.org> 1.16.3-alt1
- ^ 1.15.5 -> 1.16.3

* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.15.5-alt1
- ^ 1.15.4 -> 1.15.5

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.15.4-alt1
- ^ 1.15.0 -> 1.15.4

* Wed May 12 2021 Pavel Skrylev <majioa@altlinux.org> 1.15.0-alt1
- ^ 1.13.1 -> 1.15.0

* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.13.1-alt1
- ^ 1.12.2 -> 1.13.1

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 1.12.2-alt1
- ^ 1.11.3 -> 1.12.2
- ! spec tags

* Sun Dec 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.11.3-alt1
- updated (^) 1.11.1 -> 1.11.3
- fixed (!) spec's changelog, Vcs tag, minor others

* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 1.11.1-alt1
- updated (^) 1.10.0 -> 1.11.1
- fixed (!) spec

* Tue Feb 05 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.0-alt1
- updated (^) 1.9.25 -> 1.10.0
- updated (^) -> Ruby Policy 2.0

* Wed Aug 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.25-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.25-alt1
- New version.
- Package as gem in form libraries+gemspec.

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 1.9.23-alt2
- Rebuild as ruby gem for openqa

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.23-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.23-alt1.1
- Rebuild with Ruby 2.5.0

* Mon Feb 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.23-alt1
- New version.

* Fri Feb 23 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.22-alt1
- New version.

* Tue Feb 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.21-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt2
- Rebuild with new %%ruby_sitearchdir location

* Sat Mar 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt1
- New version

* Sun Jan 29 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.17-alt1
- new version 1.9.17
- fix module requires pathes

* Sat Sep 10 2016 Andrey Cherepanov <cas@altlinux.org> 1.9.14-alt1
- new version 1.9.14

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.9.6-alt1
- New version
- Fix project URL

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.6.3-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Fri Dec 07 2012 Led <led@altlinux.ru> 0.6.3-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- fixed build

* Fri Aug 13 2010 Kirill A. Shutemov <kas@altlinux.org> 0.6.3-alt1
- 0.6.3
- Rebuild with new libffi

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.3.5-alt1
- Built for Sisyphus
