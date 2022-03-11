%define        gemname kgio

Name:          gem-kgio
Version:       2.11.4
Release:       alt1
Summary:       kinder, gentler I/O for Ruby
License:       LGPL-2.1+
Group:         Development/Ruby
Url:           https://bogomips.org/kgio
Vcs:           https://bogomips.org/kgio.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(test-unit) >= 3.0 gem(test-unit) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-kgio < %EVR
Provides:      ruby-kgio = %EVR
Provides:      gem(kgio) = 2.11.4


%description
kgio provides non-blocking I/O methods for Ruby without raising exceptions on
EAGAIN and EINPROGRESS. It is intended for use with the Unicorn and Rainbows!
Rack servers, but may be used by other applications (that run on Unix-like
platforms).


%package       -n gem-kgio-doc
Version:       2.11.4
Release:       alt1
Summary:       kinder, gentler I/O for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета kgio
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(kgio) = 2.11.4

%description   -n gem-kgio-doc
kinder, gentler I/O for Ruby documentation files.

kgio provides non-blocking I/O methods for Ruby without raising exceptions on
EAGAIN and EINPROGRESS. It is intended for use with the Unicorn and Rainbows!
Rack servers, but may be used by other applications (that run on Unix-like
platforms).

%description   -n gem-kgio-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета kgio.


%package       -n gem-kgio-devel
Version:       2.11.4
Release:       alt1
Summary:       kinder, gentler I/O for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета kgio
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(kgio) = 2.11.4
Requires:      gem(test-unit) >= 3.0 gem(test-unit) < 4

%description   -n gem-kgio-devel
kinder, gentler I/O for Ruby development package.

kgio provides non-blocking I/O methods for Ruby without raising exceptions on
EAGAIN and EINPROGRESS. It is intended for use with the Unicorn and Rainbows!
Rack servers, but may be used by other applications (that run on Unix-like
platforms).

%description   -n gem-kgio-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета kgio.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-kgio-doc
%doc README
%ruby_gemdocdir

%files         -n gem-kgio-devel
%doc README
%ruby_includedir/*


%changelog
* Fri Mar 11 2022 Pavel Skrylev <majioa@altlinux.org> 2.11.4-alt1
- ^ 2.11.3 -> 2.11.4

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 2.11.3-alt1
- ^ 2.11.2 -> 2.11.3
- ! spec tags and syntax

* Fri Feb 01 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.2-alt4
- > Ruby Policy 2.0

* Wed Jan 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.2-alt3
- * placement library into proper ruby gem folder

* Thu Nov 15 2018 Pavel Skrylev <majioa@altlinux.org> 2.11.2-alt2
- ! binding with compiled binary so-libs

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.2-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.2-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.2-alt1.1
- Rebuild with Ruby 2.5.0

* Wed Jan 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.2-alt1
- New version.

* Tue Dec 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.1-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt1
- new version 2.11.0

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 2.10.0-alt1
- new version 2.10.0

* Fri Nov 07 2014 Anton Gorlov <stalker@altlinux.ru> 2.9.2-alt1
- new version

* Wed Mar 19 2014 Led <led@altlinux.ru> 2.7.2-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Fri Dec 07 2012 Led <led@altlinux.ru> 2.7.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Jan 10 2012 Anton Gorlov <stalker@altlinux.ru> 2.7.2-alt1
- new version

* Wed Aug 10 2011 Anton Gorlov <stalker@altlinux.ru> 2.6.0-alt1
- initial build for altlinux
