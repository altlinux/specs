%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname shellany

Name:          gem-shellany
Version:       0.0.1
Release:       alt1
Summary:       Simple, somewhat portable command capturing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/guard/shellany
Vcs:           https://github.com/guard/shellany.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.7
BuildRequires: gem(nenv) >= 0.1
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rspec) >= 3.1
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(nenv) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.5.9,bundler < 3
%ruby_use_gem_dependency rake >= 13.3.1,rake < 14
Provides:      gem(shellany) = 0.0.1

%description
MRI+JRuby compatible command output capturing


%if_enabled    doc
%package       -n gem-shellany-doc
Version:       0.0.1
Release:       alt1
Summary:       Simple, somewhat portable command capturing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета shellany
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(shellany) = 0.0.1

%description   -n gem-shellany-doc
Simple, somewhat portable command capturing documentation files.

MRI+JRuby compatible command output capturing

%description   -n gem-shellany-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета shellany.
%endif


%if_enabled    devel
%package       -n gem-shellany-devel
Version:       0.0.1
Release:       alt1
Summary:       Simple, somewhat portable command capturing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета shellany
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(shellany) = 0.0.1
Requires:      gem(bundler) >= 1.7
Requires:      gem(nenv) >= 0.1
Requires:      gem(rake) >= 10.0
Requires:      gem(rspec) >= 3.1
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(nenv) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-shellany-devel
Simple, somewhat portable command capturing development package.

MRI+JRuby compatible command output capturing

%description   -n gem-shellany-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета shellany.
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-shellany-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-shellany-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Tue Jul 07 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
