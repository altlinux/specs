%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rugged

Name:          gem-rugged
Version:       1.7.2
Release:       alt1
Summary:       Rugged is a Ruby binding to the libgit2 linkable library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/libgit2/rugged
Vcs:           https://github.com/libgit2/rugged.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         system_git2.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: libgit2-devel
%if_enabled check
BuildRequires: gem(rake-compiler) >= 0.9.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(rugged) = 1.7.2


%description
Rugged is a Ruby bindings to the libgit2 linkable C Git library. This is for
testing and using the libgit2 library in a language that is awesome.


%if_enabled    doc
%package       -n gem-rugged-doc
Version:       1.7.2
Release:       alt1
Summary:       Rugged is a Ruby binding to the libgit2 linkable library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rugged
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rugged) = 1.7.2

%description   -n gem-rugged-doc
Rugged is a Ruby binding to the libgit2 linkable library documentation
files.

Rugged is a Ruby bindings to the libgit2 linkable C Git library. This is for
testing and using the libgit2 library in a language that is awesome.

%description   -n gem-rugged-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rugged.
%endif


%if_enabled    devel
%package       -n gem-rugged-devel
Version:       1.7.2
Release:       alt1
Summary:       Rugged is a Ruby binding to the libgit2 linkable library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rugged
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rugged) = 1.7.2
Requires:      gem(rake-compiler) >= 0.9.0
Requires:      gem(pry) >= 0
Requires:      gem(minitest) >= 5.0
Requires:      libgit2-devel
Conflicts:     gem(minitest) >= 6

%description   -n gem-rugged-devel
Rugged is a Ruby binding to the libgit2 linkable library development
package.

Rugged is a Ruby bindings to the libgit2 linkable C Git library. This is for
testing and using the libgit2 library in a language that is awesome.

%description   -n gem-rugged-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rugged.
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
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-rugged-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rugged-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 1.7.2-alt1
- ^ 1.7.1 -> 1.7.2

* Wed Dec 06 2023 Pavel Skrylev <majioa@altlinux.org> 1.7.1-alt1
- ^ 1.5.1 -> 1.7.1

* Thu Mar 02 2023 Pavel Skrylev <majioa@altlinux.org> 1.5.1-alt1
- ^ 1.4.3 -> 1.5.1

* Mon Apr 18 2022 Pavel Skrylev <majioa@altlinux.org> 1.4.3-alt1
- ^ 1.1.1 -> 1.4.3

* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with Ruby Policy 2.0
