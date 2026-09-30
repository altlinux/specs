%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname tdiff

Name:          gem-tdiff
Version:       0.4.0
Release:       alt1
Summary:       Calculates the differences between two tree-like structures
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/postmodern/tdiff#readme
Vcs:           https://github.com/postmodern/tdiff.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby
BuildRequires(pre): setup-rb
BuildRequires(pre): rake
%if_enabled check
BuildRequires: gem(bundler) >= 2.0.0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubygems-tasks) >= 0.1
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(yard) >= 0.9
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubygems-tasks) >= 1
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17
Requires:      ruby >= 2.0.0
Provides:      gem(tdiff) = 0.4.0

%description
Calculates the differences between two tree-like structures. Similar to Rubys
built-in TSort module.


%if_enabled    doc
%package       -n gem-tdiff-doc
Version:       0.4.0
Release:       alt1
Summary:       Calculates the differences between two tree-like structures documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tdiff
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tdiff) = 0.4.0

%description   -n gem-tdiff-doc
Calculates the differences between two tree-like structures documentation
files.

Calculates the differences between two tree-like structures. Similar to Rubys
built-in TSort module.

%description   -n gem-tdiff-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tdiff.
%endif


%if_enabled    devel
%package       -n gem-tdiff-devel
Version:       0.4.0
Release:       alt1
Summary:       Calculates the differences between two tree-like structures development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета tdiff
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tdiff) = 0.4.0
Requires:      gem(bundler) >= 2.0.0
Requires:      gem(kramdown) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubygems-tasks) >= 0.1
Requires:      gem(simplecov) >= 0.17
Requires:      gem(yard) >= 0.9
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubygems-tasks) >= 1
Conflicts:     gem(yard) >= 1

%description   -n gem-tdiff-devel
Calculates the differences between two tree-like structures development
package.

Calculates the differences between two tree-like structures. Similar to Rubys
built-in TSort module.

%description   -n gem-tdiff-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета tdiff.
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
%doc ChangeLog.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-tdiff-doc
%doc ChangeLog.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-tdiff-devel
%doc ChangeLog.md LICENSE.txt README.md
%endif


%changelog
* Sun May 31 2026 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
