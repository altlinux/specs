%define        _unpackaged_files_terminate_build 1
%define        gemname rack

Name:          gem-rack
Epoch:         1
Version:       2.2.6.3
Release:       alt1
Summary:       Modular Ruby webserver interface
License:       MIT
Group:         Development/Ruby
Url:           https://rack.github.io/
Vcs:           https://github.com/rack/rack.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(minitest-sprint) >= 0
BuildRequires: gem(minitest-global_expectations) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(psych) >= 0
BuildRequires: gem(fcgi) >= 0
BuildRequires: gem(dalli) >= 0
BuildRequires: gem(thin) >= 0
BuildRequires: gem(rdoc) >= 0
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-rack < %EVR
Provides:      ruby-rack = %EVR
Provides:      gem(rack) = 2.2.6.3


%description
Rack provides a minimal, modular and adaptable interface for developing web
applications in Ruby. By wrapping HTTP requests and responses in the simplest
way possible, it unifies and distills the API for web servers, web frameworks,
and software in between (the so-called middleware) into a single method
call.

You may need to install appropriate gem-rack-handler-XXX.


%package       -n rackup
Version:       2.2.6.3
Release:       alt1
Summary:       Modular Ruby webserver interface executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rack
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack) = 2.2.6.3

%description   -n rackup
Modular Ruby webserver interface executable(s).

Rack provides a minimal, modular and adaptable interface for developing web
applications in Ruby. By wrapping HTTP requests and responses in the simplest
way possible, it unifies and distills the API for web servers, web frameworks,
and software in between (the so-called middleware) into a single method
call.

You may need to install appropriate gem-rack-handler-XXX.

%description   -n rackup -l ru_RU.UTF-8
Исполнямка для самоцвета rack.


%package       -n gem-rack-doc
Version:       2.2.6.3
Release:       alt1
Summary:       Modular Ruby webserver interface documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack) = 2.2.6.3

%description   -n gem-rack-doc
Modular Ruby webserver interface documentation files.

Rack provides a minimal, modular and adaptable interface for developing web
applications in Ruby. By wrapping HTTP requests and responses in the simplest
way possible, it unifies and distills the API for web servers, web frameworks,
and software in between (the so-called middleware) into a single method
call.

You may need to install appropriate gem-rack-handler-XXX.

%description   -n gem-rack-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rack.


%package       -n gem-rack-devel
Version:       2.2.6.3
Release:       alt1
Summary:       Modular Ruby webserver interface development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack) = 2.2.6.3
Requires:      gem(minitest) >= 5.0
Requires:      gem(minitest-sprint) >= 0
Requires:      gem(minitest-global_expectations) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(webrick) >= 0
Requires:      gem(psych) >= 0
Requires:      gem(fcgi) >= 0
Requires:      gem(dalli) >= 0
Requires:      gem(thin) >= 0
Requires:      gem(rdoc) >= 0
Conflicts:     gem(minitest) >= 6

%description   -n gem-rack-devel
Modular Ruby webserver interface development package.

Rack provides a minimal, modular and adaptable interface for developing web
applications in Ruby. By wrapping HTTP requests and responses in the simplest
way possible, it unifies and distills the API for web servers, web frameworks,
and software in between (the so-called middleware) into a single method
call.

You may need to install appropriate gem-rack-handler-XXX.

%description   -n gem-rack-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rack.


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

%files         -n rackup
%doc README.rdoc
%_bindir/rackup

%files         -n gem-rack-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-rack-devel
%doc README.rdoc


%changelog
* Fri Mar 10 2023 Pavel Skrylev <majioa@altlinux.org> 1:2.2.6.3-alt1
- ^ 2.2.2 -> 2.2.6.3

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 1:2.2.2-alt1
- ^ 2.0.7 -> 2.2.2
- ! spec tags

* Wed Jun 05 2019 Pavel Skrylev <majioa@altlinux.org> 1:2.0.7-alt1
- ^ 2.0.6 -> 2.0.7

* Thu Jan 10 2019 Pavel Skrylev <majioa@altlinux.org> 1:2.0.6-alt1
- > Ruby Policy 2.0
- ^ 2.0.4 -> 2.0.6.

* Fri Aug 24 2018 Andrey Cherepanov <cas@altlinux.org> 1:2.0.4-alt1
- New version.

* Fri Aug 24 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt2.4
- Rebuild for new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt2.3
- Use system way to install gemspec.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt2.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt2.1
- Rebuild with Ruby 2.5.0

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Jun 16 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt1
- Decrease version for pcs-pcsd
- Package gemspec
- Spec cleanup

* Tue May 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.3-alt1
- New version

* Mon May 08 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- New version

* Sat Apr 08 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- new version 2.0.1

* Sat Dec 01 2012 Led <led@altlinux.ru> 1.2.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.2.2-alt1
- [1.2.2]

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.0-alt2
- Fix package broken by erthad

* Wed Mar 31 2010 Timur Batyrshin <erthad@altlinux.org> 1.1.0-alt1
- [1.1.0]

* Mon Oct 19 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.1-alt1
- [1.0.1]

* Sun Oct 18 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.0-alt3
- Updated to 1.0-16-g99c47b8
- Force all form data to be UTF-8 String's

* Sun Aug 16 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.0-alt2
- Backported Ruby 1.9 encoding-related fixes.

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.0-alt1
- [1.0.0]
- Packaged rackup script
- Dropped unused handlers

* Sat Nov 01 2008 Sir Raorn <raorn@altlinux.ru> 0.4.0-alt1
- Built for Sisyphus
