%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname drake

Name:          gem-drake
Version:       0.9.2.0.3.1
Release:       alt1
Summary:       A branch of Rake supporting automatic parallelizing of tasks
License:       Unlicense
Group:         Development/Ruby
Url:           http://quix.github.com/rake
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(comp_tree) >= 1.1.3
BuildRequires: gem(flexmock) >= 0.8.11
BuildRequires: gem(minitest) >= 2.1
BuildRequires: gem(session) >= 2.4
BuildConflicts: gem(flexmock) >= 3
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(session) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency flexmock >= 2.3.6.1,flexmock < 3
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency session >= 3.2.0,session < 4
Requires:      rubygems >= 1.3.2
Requires:      gem(comp_tree) >= 1.1.3
Provides:      gem(drake) = 0.9.2.0.3.1

%description
Drake is an auto-parallelizing branch of Rake, a Make-like program implemented
in Ruby. Tasks and dependencies are specified in standard Ruby syntax.


%package       -n drake
Version:       0.9.2.0.3.1
Release:       alt1
Summary:       A branch of Rake supporting automatic parallelizing of tasks executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета drake
Group:         Other
BuildArch:     noarch

Requires:      gem(drake) = 0.9.2.0.3.1

%description   -n drake
A branch of Rake supporting automatic parallelizing of tasks
executable(s).

Drake is an auto-parallelizing branch of Rake, a Make-like program implemented
in Ruby. Tasks and dependencies are specified in standard Ruby syntax.

%description   -n drake -l ru_RU.UTF-8
Исполнямка для самоцвета drake.


%if_enabled    doc
%package       -n gem-drake-doc
Version:       0.9.2.0.3.1
Release:       alt1
Summary:       A branch of Rake supporting automatic parallelizing of tasks documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета drake
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(drake) = 0.9.2.0.3.1

%description   -n gem-drake-doc
A branch of Rake supporting automatic parallelizing of tasks documentation
files.

Drake is an auto-parallelizing branch of Rake, a Make-like program implemented
in Ruby. Tasks and dependencies are specified in standard Ruby syntax.

%description   -n gem-drake-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета drake.
%endif


%if_enabled    devel
%package       -n gem-drake-devel
Version:       0.9.2.0.3.1
Release:       alt1
Summary:       A branch of Rake supporting automatic parallelizing of tasks development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета drake
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(drake) = 0.9.2.0.3.1
Requires:      gem(flexmock) >= 0.8.11
Requires:      gem(minitest) >= 2.1
Requires:      gem(session) >= 2.4
Conflicts:     gem(flexmock) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(session) >= 4

%description   -n gem-drake-devel
A branch of Rake supporting automatic parallelizing of tasks development
package.

Drake is an auto-parallelizing branch of Rake, a Make-like program implemented
in Ruby. Tasks and dependencies are specified in standard Ruby syntax.

%description   -n gem-drake-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета drake.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc MIT-LICENSE README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n drake
%doc MIT-LICENSE README.rdoc
%_bindir/drake

%if_enabled    doc
%files         -n gem-drake-doc
%doc MIT-LICENSE README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-drake-devel
%doc MIT-LICENSE README.rdoc
%endif


%changelog
* Thu Oct 02 2025 Pavel Skrylev <majioa@altlinux.org> 0.9.2.0.3.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
