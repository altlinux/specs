%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname mmap2

Name:          gem-mmap2
Version:       2.2.9.0.1
Release:       alt0.1
Summary:       The Mmap class
License:       Ruby
Group:         Development/Ruby
Url:           https://gitlab.com/gitlab-org/mmap2
Vcs:           https://gitlab.com/gitlab-org/mmap2.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake libruby-devel
%if_enabled check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 10.4.2
BuildRequires: gem(rake-compiler) >= 0.9.5
BuildRequires: gem(rubocop) >= 0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Provides:      gem(mmap2) = 2.2.9.0.1

%ruby_use_gem_version mmap2:2.2.9.0.1

%description
The Mmap class implement memory-mapped file objects for Ruby 2.x


%if_enabled    doc
%package       -n gem-mmap2-doc
Version:       2.2.9.0.1
Release:       alt0.1
Summary:       The Mmap class documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mmap2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mmap2) = 2.2.9.0.1

%description   -n gem-mmap2-doc
The Mmap class documentation files.

The Mmap class implement memory-mapped file objects for Ruby 2.x

%description   -n gem-mmap2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mmap2.
%endif


%if_enabled    devel
%package       -n gem-mmap2-devel
Version:       2.2.9.0.1
Release:       alt0.1
Summary:       The Mmap class development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mmap2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mmap2) = 2.2.9.0.1
Requires:      libruby-devel
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 10.4.2
Requires:      gem(rake-compiler) >= 0.9.5
Requires:      gem(rubocop) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2

%description   -n gem-mmap2-devel
The Mmap class development package.

The Mmap class implement memory-mapped file objects for Ruby 2.x

%description   -n gem-mmap2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mmap2.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-mmap2-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-mmap2-devel
%doc README.rdoc
%endif


%changelog
* Wed May 13 2026 Pavel Skrylev <majioa@altlinux.org> 2.2.9.0.1-alt0.1
- ^ 2.2.7.32 -> 2.2.9p0.1

* Tue Jul 22 2025 Pavel Skrylev <majioa@altlinux.org> 2.2.7.32-alt0.1
- + packaged v2.2.7p32 gem with Ruby Policy 2.0
- * define explicit dependencies
