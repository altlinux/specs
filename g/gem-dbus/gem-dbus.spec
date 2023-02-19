%define        gemname ruby-dbus

Name:          gem-dbus
Version:       0.19.0
Release:       alt1
Summary:       Ruby D-BUS library
License:       LGPL-2.1
Group:         Development/Ruby
Url:           https://trac.luon.net/ruby-dbus/
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(packaging_rake_tasks) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(rubocop) >= 1.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-lcov) >= 0
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(racc) >= 0
BuildRequires: gem(rexml) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_alias_names ruby-dbus,dbus
Requires:      gem(rexml) >= 0
Obsoletes:     ruby-dbus < %EVR
Provides:      ruby-dbus = %EVR
Provides:      gem(ruby-dbus) = 0.19.0


%description
Ruby D-Bus provides an implementation of the D-Bus protocol such that the D-Bus
system can be used in the Ruby programming language.


%package       -n gem-dbus-doc
Version:       0.19.0
Release:       alt1
Summary:       Ruby D-BUS library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-dbus
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-dbus) = 0.19.0

%description   -n gem-dbus-doc
Ruby D-BUS library documentation files.

Ruby D-Bus provides an implementation of the D-Bus protocol such that the D-Bus
system can be used in the Ruby programming language.

%description   -n gem-dbus-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-dbus.


%package       -n gem-dbus-devel
Version:       0.19.0
Release:       alt1
Summary:       Ruby D-BUS library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-dbus
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-dbus) = 0.19.0
Requires:      gem(packaging_rake_tasks) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3
Requires:      gem(rubocop) >= 1.0
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-lcov) >= 0
Requires:      gem(nokogiri) >= 0
Requires:      gem(racc) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-dbus-devel
Ruby D-BUS library development package.

Ruby D-Bus provides an implementation of the D-Bus protocol such that the D-Bus
system can be used in the Ruby programming language.

%description   -n gem-dbus-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-dbus.


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

%files         -n gem-dbus-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-dbus-devel
%doc README.md


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 0.19.0-alt1
- ^ 0.16.0 -> 0.19.0

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.16.0-alt1
- ^ 0.15.0 -> 0.16.0
- > Ruby Policy 2.0

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.15.0-alt3
- Fix spec due to new rpm-build-ruby.

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 0.15.0-alt2
- Use setup gem's dependency detection

* Mon Feb 18 2019 Pavel Skrylev <majioa@altlinux.org> 0.15.0-alt1
- Bump to 0.15.0;
- Use Ruby Policy 2.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.12-alt1.3
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.2.12-alt1.2
- Rebuild with Ruby 2.4.1

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.2.12-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sun Mar 14 2010 Igor Zubkov <icesik@altlinux.org> 0.2.12-alt1
- 0.2.11 -> 0.2.12

* Sat Dec 19 2009 Igor Zubkov <icesik@altlinux.org> 0.2.11-alt1
- 0.2.10 -> 0.2.11

* Sat Oct 31 2009 Igor Zubkov <icesik@altlinux.org> 0.2.10-alt1
- 0.2.1 -> 0.2.10

* Wed Oct 14 2009 Igor Zubkov <icesik@altlinux.org> 0.2.1-alt2
- update setup.rb

* Sat Aug 08 2009 Igor Zubkov <icesik@altlinux.org> 0.2.1-alt1
- build
