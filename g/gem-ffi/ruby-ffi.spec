%define        gemname ffi

Name:          gem-ffi
Version:       1.15.0
Release:       alt1
Summary:       Ruby foreign function interface
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           https://github.com/ffi/ffi/wiki
Vcs:           https://github.com/ffi/ffi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libffi-devel
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rake-compiler) >= 1.0 gem(rake-compiler) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-ffi < %EVR
Provides:      ruby-ffi = %EVR
Provides:      gem(ffi) = 1.15.0

%description
Ruby-FFI is a gem for programmatically loading dynamically-linked native
libraries, binding functions within them, and calling those functions from Ruby
code. Moreover, a Ruby-FFI extension works without changes on CRuby (MRI),
JRuby, Rubinius and TruffleRuby. Discover why you should write your next
extension using Ruby-FFI.


%package       -n gem-ffi-doc
Version:       1.15.0
Release:       alt1
Summary:       Ruby FFI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ffi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ffi) = 1.15.0

%description   -n gem-ffi-doc
Ruby FFI documentation files.

Ruby FFI library

%description   -n gem-ffi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ffi.


%package       -n gem-ffi-devel
Version:       1.15.0
Release:       alt1
Summary:       Ruby FFI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ffi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ffi) = 1.15.0
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rake-compiler) >= 1.0 gem(rake-compiler) < 2

%description   -n gem-ffi-devel
Ruby FFI development package.

Ruby FFI library

%description   -n gem-ffi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ffi.


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

%files         -n gem-ffi-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ffi-devel
%doc README.md
%ruby_includedir/*


%changelog
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
