%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname RedCloth

Name:          gem-redcloth
Version:       4.3.4
Release:       alt1
Summary:       Textile parser for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://redcloth.org/
Vcs:           https://github.com/jgarber/redcloth.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         gemfile.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: ragel6 < 7.0
%if_enabled check
BuildRequires: gem(bundler) > 1.3.4
BuildRequires: gem(rake) >= 13
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(diff-lcs) >= 1.5
BuildRequires: gem(rvm) >= 1.11.3.9
BuildRequires: gem(rake-compiler) >= 0.7.1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(diff-lcs) >= 2
BuildConflicts: gem(rvm) >= 1.11.4
BuildConflicts: gem(rake-compiler) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
%ruby_alias_names RedCloth,redcloth
Obsoletes:     ruby-redcloth
Provides:      ruby-redcloth
Provides:      gem(RedCloth) = 4.3.4

%ruby_on_build_rake_tasks compile

%description
RedCloth is a module for using Textile in Ruby. Textile is a text format. A very
simple text format. Another stab at making readable text that can be converted
to HTML.


%package       -n redcloth
Version:       4.3.4
Release:       alt1
Summary:       Textile parser for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета RedCloth
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(RedCloth) = 4.3.4

%description   -n redcloth
Textile parser for Ruby executable(s).

RedCloth is a module for using Textile in Ruby. Textile is a text format. A very
simple text format. Another stab at making readable text that can be converted
to HTML.

%description   -n redcloth -l ru_RU.UTF-8
Исполнямка для самоцвета RedCloth.


%if_enabled    doc
%package       -n gem-redcloth-doc
Version:       4.3.4
Release:       alt1
Summary:       Textile parser for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета RedCloth
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(RedCloth) = 4.3.4

%description   -n gem-redcloth-doc
Textile parser for Ruby documentation files.

RedCloth is a module for using Textile in Ruby. Textile is a text format. A very
simple text format. Another stab at making readable text that can be converted
to HTML.

%description   -n gem-redcloth-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета RedCloth.
%endif


%if_enabled    devel
%package       -n gem-redcloth-devel
Version:       4.3.4
Release:       alt1
Summary:       Textile parser for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета RedCloth
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ragel6 < 7.0
Requires:      gem(RedCloth) = 4.3.4
Requires:      gem(bundler) > 1.3.4
Requires:      gem(rake) >= 13
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(diff-lcs) >= 1.5
Requires:      gem(rvm) >= 1.11.3.9
Requires:      gem(rake-compiler) >= 0.7.1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(diff-lcs) >= 2
Conflicts:     gem(rvm) >= 1.11.4
Conflicts:     gem(rake-compiler) >= 2

%description   -n gem-redcloth-devel
Textile parser for Ruby development package.

RedCloth is a module for using Textile in Ruby. Textile is a text format. A very
simple text format. Another stab at making readable text that can be converted
to HTML.

%description   -n gem-redcloth-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета RedCloth.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n redcloth
%doc README.rdoc
%_bindir/redcloth

%if_enabled    doc
%files         -n gem-redcloth-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-redcloth-devel
%doc README.rdoc
%ruby_includedir/*
%endif


%changelog
* Fri Aug 09 2024 Pavel Skrylev <majioa@altlinux.org> 4.3.4-alt1
- ^ 4.3.2.1 -> 4.3.4 with fixes (closes: #51105)

* Sun May 08 2022 Pavel Skrylev <majioa@altlinux.org> 4.3.2.1-alt1
- ^ 4.3.2 -> 4.3.2.1

* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 4.3.2-alt3
- + devel package
- ! spec

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 4.3.2-alt2.1
- Fix spec

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 4.3.2-alt2
- Use Ruby Policy 2.0
- Fix 4.3.2 gem version

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 4.3.2-alt1
- New version 4.3.2
- Build as noarch

* Wed Mar 19 2014 Led <led@altlinux.ru> 4.2.2-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Tue Dec 04 2012 Led <led@altlinux.ru> 4.2.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Jul 24 2009 Alexey I. Froloff <raorn@altlinux.org> 4.2.2-alt1
- [4.2.2]
- Do not package useless rake tasks

* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 4.2.1-alt1
- [4.2.1]

* Fri Jul 25 2008 Sir Raorn <raorn@altlinux.ru> 4.0.1-alt1
- [4.0.1]

* Tue Mar 28 2006 Kirill A. Shutemov <kas@altlinux.ru> 3.0.4-alt1
- first build
