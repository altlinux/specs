%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel

Name:          gem-mongrel
Version:       1.2.0
Release:       alt2
Summary:       Simple Fast Mostly Ruby Web Server
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/evan/mongrel
Vcs:           https://github.com/evan/mongrel.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: ragel6
%if_enabled check
BuildRequires: gem(gem_plugin) >= 0.2.3
BuildRequires: gem(daemons) >= 1.0.10
BuildRequires: gem(rake-compiler) >= 0.7.0
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(hoe) >= 3.22
BuildRequires: gem(rspec) >= 0
BuildConflicts: gem(gem_plugin) >= 0.3
BuildConflicts: gem(daemons) >= 2
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(hoe) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency hoe >= 4.0.0,hoe < 5
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
%ruby_use_gem_dependency daemons >= 1.0.10,daemons < 2
%ruby_ignore_names cgi_multipart_eof_fix,gem_plugin,/mongrel_,fastthread,/project
Requires:      gem(gem_plugin) >= 0.2.3
Requires:      gem(daemons) >= 1.0.10
Conflicts:     gem(gem_plugin) >= 0.3
Conflicts:     gem(daemons) >= 2
Obsoletes:     ruby-mongrel < %EVR
Provides:      ruby-mongrel = %EVR
Provides:      gem(mongrel) = 1.2.0


%description
Mongrel is a small library that provides a very fast HTTP 1.1 server for Ruby
web applications. It is not particular to any framework, and is intended to be
just enough to get a web application running behind a more complete and robust
web server.


%package       -n mongrel-rails
Version:       1.2.0
Release:       alt2
Summary:       Simple Fast Mostly Ruby Web Server executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета mongrel
Group:         Other
BuildArch:     noarch

Requires:      gem(mongrel) = 1.2.0

%description   -n mongrel-rails
Simple Fast Mostly Ruby Web Server executable(s).

Mongrel is a small library that provides a very fast HTTP 1.1 server for Ruby
web applications. It is not particular to any framework, and is intended to be
just enough to get a web application running behind a more complete and robust
web server.

%description   -n mongrel-rails -l ru_RU.UTF-8
Исполнямка для самоцвета mongrel.


%if_enabled    doc
%package       -n gem-mongrel-doc
Version:       1.2.0
Release:       alt2
Summary:       Simple Fast Mostly Ruby Web Server documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mongrel
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mongrel) = 1.2.0

%description   -n gem-mongrel-doc
Simple Fast Mostly Ruby Web Server documentation files.

Mongrel is a small library that provides a very fast HTTP 1.1 server for Ruby
web applications. It is not particular to any framework, and is intended to be
just enough to get a web application running behind a more complete and robust
web server.

%description   -n gem-mongrel-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mongrel.
%endif


%if_enabled    devel
%package       -n gem-mongrel-devel
Version:       1.2.0
Release:       alt1.1
Summary:       Simple Fast Mostly Ruby Web Server development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mongrel
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mongrel) = 1.2.0
Requires:      gem(rake-compiler) >= 0.7.0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 3.22
Requires:      gem(rspec) >= 0
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(hoe) >= 5

%description   -n gem-mongrel-devel
Simple Fast Mostly Ruby Web Server development package.

Mongrel is a small library that provides a very fast HTTP 1.1 server for Ruby
web applications. It is not particular to any framework, and is intended to be
just enough to get a web application running behind a more complete and robust
web server.

%description   -n gem-mongrel-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mongrel.
%endif


%prep
%setup
%autopatch -p1

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
%ruby_gemextdir

%files         -n mongrel-rails
%doc README.rdoc
%_bindir/mongrel_rails

%if_enabled    doc
%files         -n gem-mongrel-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-mongrel-devel
%doc README.rdoc
%ruby_includedir/*
%endif


%changelog
* Fri Sep 27 2024 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt2
- ! spec and deps

* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1.1
- !fix spec and .gear

* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- ^ 1.1.5 -> 1.2.0

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt8.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt8.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt8.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt8.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt8
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt7
- Rebuild with Ruby 2.3.1

* Wed Mar 19 2014 Led <led@altlinux.ru> 1.1.5-alt6.3
- Rebuilt with ruby-2.0.0-alt1

* Fri Mar 14 2014 Led <led@altlinux.ru> 1.1.5-alt6.2
- fixed Group for doc subpackage
- disabled test_more_web_server and test_deflate for ruby >= 2.0

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.1.5-alt6.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Nov 29 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.5-alt6
- Fix build with Ruby 1.9.2

* Sat Jun 05 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.5-alt5
- Fix cookies processing (once more)

* Sun May 02 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.5-alt4
- Fix cookies processing

* Fri Nov 20 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.5-alt3
- Fixed :prefix setting for new Rails API

* Fri May 15 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.5-alt2
- Rebuilt with Ruby 1.9

* Wed Aug 27 2008 Sir Raorn <raorn@altlinux.ru> 1.1.5-alt1
- Built for Sisyphus
