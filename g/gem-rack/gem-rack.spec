%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rack

Name:          gem-rack
Epoch:         1
Version:       3.1.7
Release:       alt1
Summary:       Modular Ruby webserver interface
License:       MIT
Group:         Development/Ruby
Url:           https://rack.github.io/
Vcs:           https://github.com/rack/rack.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         fix-digit-when-nil-body.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(minitest-global_expectations) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-packaging) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(bake-test-external) >= 0
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-rack < %EVR
Provides:      ruby-rack = %EVR
Provides:      gem(rack) = 3.1.7


%description
Rack provides a minimal, modular and adaptable interface for developing web
applications in Ruby. By wrapping HTTP requests and responses in the simplest
way possible, it unifies and distills the API for web servers, web frameworks,
and software in between (the so-called middleware) into a single method
call.

You may need to install appropriate gem-rack-handler-XXX.


%if_enabled    doc
%package       -n gem-rack-doc
Version:       3.1.7
Release:       alt1
Summary:       Modular Ruby webserver interface documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack) = 3.1.7

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
%endif


%if_enabled    devel
%package       -n gem-rack-devel
Version:       3.1.7
Release:       alt1
Summary:       Modular Ruby webserver interface development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack) = 3.1.7
Requires:      gem(minitest) >= 5.0
Requires:      gem(minitest-global_expectations) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-packaging) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(webrick) >= 0
Requires:      gem(bake-test-external) >= 0
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
%endif


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

%if_enabled    doc
%files         -n gem-rack-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rack-devel
%doc README.md
%endif


%changelog
* Tue Oct 08 2024 Pavel Skrylev <majioa@altlinux.org> 1:3.1.7-alt1
- ^ 3.0.10 -> 3.1.7

* Tue May 14 2024 Pavel Skrylev <majioa@altlinux.org> 1:3.0.10-alt2
- ! fixed digest calculation when body is null

* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 1:3.0.10-alt1
- ^ 2.2.6.3 -> 3.0.10

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
