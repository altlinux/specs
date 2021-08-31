%define        gemname bacon

Name:          gem-bacon
Version:       1.2.0
Release:       alt1
Summary:       Bacon -- small RSpec clone
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/leahneukirchen/bacon
Vcs:           https://github.com/leahneukirchen/bacon.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(bacon) = 1.2.0


%description
Bacon is a small RSpec clone weighing less than 300 LoC but nevertheless
providing all essential features.


%package       -n bacon
Version:       1.2.0
Release:       alt1
Summary:       Bacon -- small RSpec clone executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета bacon
Group:         Other
BuildArch:     noarch

Requires:      gem(bacon) = 1.2.0

%description   -n bacon
Bacon -- small RSpec clone executable(s).

Bacon is a small RSpec clone weighing less than 300 LoC but nevertheless
providing all essential features.

%description   -n bacon -l ru_RU.UTF-8
Исполнямка для самоцвета bacon.


%package       -n gem-bacon-doc
Version:       1.2.0
Release:       alt1
Summary:       Bacon -- small RSpec clone documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bacon
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bacon) = 1.2.0

%description   -n gem-bacon-doc
Bacon -- small RSpec clone documentation files.

Bacon is a small RSpec clone weighing less than 300 LoC but nevertheless
providing all essential features.

%description   -n gem-bacon-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bacon.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n bacon
%doc README.rdoc
%_bindir/bacon

%files         -n gem-bacon-doc
%doc README.rdoc
%ruby_gemdocdir


%changelog
* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- ^ 1.1.0 -> 1.2.0
- * relicensing to pure MIT

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.0-alt1
- [1.1.0]
- License changed to MIT/Ruby

* Wed Jul 09 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.0.0-alt1
- New version

* Wed Apr 09 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt1
- Initial build
