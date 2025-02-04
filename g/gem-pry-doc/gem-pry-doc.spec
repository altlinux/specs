%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname pry-doc

Name:          gem-pry-doc
Version:       1.5.0.5
Release:       alt0.1
Summary:       Provides YARD and extended documentation support for Pry
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/pry/pry-doc
Vcs:           https://github.com/pry/pry-doc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: /usr/bin/etags
%if_enabled check
BuildRequires: gem(latest_ruby) >= 3.3.0
BuildRequires: gem(pry) >= 0.11
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.5
BuildRequires: gem(yard) >= 0.9.11
BuildRequires: gem(bigdecimal) >= 0
BuildConflicts: gem(latest_ruby) >= 4
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency latest_ruby >= 3.3.0,latest_ruby < 4
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      /usr/bin/etags
Requires:      ruby >= 2.0
Requires:      gem(bigdecimal) >= 0
Requires:      gem(pry) >= 0.11
Requires:      gem(yard) >= 0.9.11
Conflicts:     gem(pry) >= 1
Conflicts:     gem(yard) >= 1
Provides:      gem(pry-doc) = 1.5.0.5

%ruby_use_gem_version pry-doc:1.5.0.5

%description
Pry Doc is a Pry REPL plugin. It provides extended documentation support for the
REPL by means of improving the `show-doc` and `show-source` commands. With help
of the plugin the commands are be able to display the source code and the docs
of Ruby methods and classes implemented in C. documentation


%if_enabled    doc
%package       -n gem-pry-doc-doc
Version:       1.5.0.5
Release:       alt0.1
Summary:       Provides YARD and extended documentation support for Pry documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pry-doc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pry-doc) = 1.5.0.5

%description   -n gem-pry-doc-doc
Provides YARD and extended documentation support for Pry documentation
files.

Pry Doc is a Pry REPL plugin. It provides extended documentation support for the
REPL by means of improving the `show-doc` and `show-source` commands. With help
of the plugin the commands are be able to display the source code and the docs
of Ruby methods and classes implemented in C. documentation

%description   -n gem-pry-doc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pry-doc.
%endif


%if_enabled    devel
%package       -n gem-pry-doc-devel
Version:       1.5.0.5
Release:       alt0.1
Summary:       Provides YARD and extended documentation support for Pry development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pry-doc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pry-doc) = 1.5.0.5
Requires:      gem(latest_ruby) >= 3.3.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.5
Conflicts:     gem(latest_ruby) >= 4
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-pry-doc-devel
Provides YARD and extended documentation support for Pry development
package.

Pry Doc is a Pry REPL plugin. It provides extended documentation support for the
REPL by means of improving the `show-doc` and `show-source` commands. With help
of the plugin the commands are be able to display the source code and the docs
of Ruby methods and classes implemented in C. documentation

%description   -n gem-pry-doc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pry-doc.
%endif


%prep
%setup
rm -rf libexec/linux/

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-pry-doc-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-pry-doc-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Mon Feb 03 2025 Pavel Skrylev <majioa@altlinux.org> 1.5.0.5-alt0.1
- ^ 1.1.0 -> 1.5.0p5

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
