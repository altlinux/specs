%define        gemname jazz_fingers

Name:          gem-jazz-fingers
Version:       6.2.0
Release:       alt1
Summary:       Exercise those fingers. Pry-based enhancements for the default Ruby console
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/plribeiro3000/jazz_fingers
Vcs:           https://github.com/plribeiro3000/jazz_fingers.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(amazing_print) >= 1.3 gem(amazing_print) < 2
BuildRequires: gem(pry) >= 0.10 gem(pry) < 1
BuildRequires: gem(pry-byebug) >= 3.9 gem(pry-byebug) < 4
BuildRequires: gem(pry-coolline) >= 0.2 gem(pry-coolline) < 1
BuildRequires: gem(rubocop) >= 0 gem(rubocop) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
Requires:      gem(amazing_print) >= 1.3 gem(amazing_print) < 2
Requires:      gem(pry) >= 0.10 gem(pry) < 1
Requires:      gem(pry-byebug) >= 3.9 gem(pry-byebug) < 4
Requires:      gem(pry-coolline) >= 0.2 gem(pry-coolline) < 1
Provides:      gem(jazz_fingers) = 6.2.0


%description
Spending hours in the ruby console? Spruce it up and show off those hard-working
hands! jazz_fingersreplaces IRB with Pry, improves output through amazing_print,
and has some other goodies up its sleeves.


%package       -n gem-jazz-fingers-doc
Version:       6.2.0
Release:       alt1
Summary:       Exercise those fingers. Pry-based enhancements for the default Ruby console documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jazz_fingers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jazz_fingers) = 6.2.0

%description   -n gem-jazz-fingers-doc
Exercise those fingers. Pry-based enhancements for the default Ruby console
documentation files.

Spending hours in the ruby console? Spruce it up and show off those hard-working
hands! jazz_fingersreplaces IRB with Pry, improves output through amazing_print,
and has some other goodies up its sleeves.

%description   -n gem-jazz-fingers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jazz_fingers.


%package       -n gem-jazz-fingers-devel
Version:       6.2.0
Release:       alt1
Summary:       Exercise those fingers. Pry-based enhancements for the default Ruby console development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jazz_fingers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jazz_fingers) = 6.2.0
Requires:      gem(rubocop) >= 0 gem(rubocop) < 2

%description   -n gem-jazz-fingers-devel
Exercise those fingers. Pry-based enhancements for the default Ruby console
development package.

Spending hours in the ruby console? Spruce it up and show off those hard-working
hands! jazz_fingersreplaces IRB with Pry, improves output through amazing_print,
and has some other goodies up its sleeves.

%description   -n gem-jazz-fingers-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jazz_fingers.


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

%files         -n gem-jazz-fingers-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-jazz-fingers-devel
%doc README.md


%changelog
* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 6.2.0-alt1
- + packaged gem with Ruby Policy 2.0
