%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname libv8

Name:          gem-libv8
Version:       8.4.255.5
Release:       alt1
Summary:       Distribution of the V8 JavaScript engine
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/rubyjs/libv8
Vcs:           https://github.com/rubyjs/libv8.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%ifarch i586 x86_64
BuildRequires: libv8-3.14-devel
%endif
BuildRequires: gem(rake) >= 12
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rspec) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rspec) >= 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Provides:      libv8 = %EVR
Provides:      gem(libv8) = 8.4.255.5

%description
Distributes the V8 JavaScript engine in binary and source forms in order to
support fast builds of The Ruby Racer


%if_enabled    doc
%package       -n gem-libv8-doc
Version:       8.4.255.5
Release:       alt1
Summary:       Distribution of the V8 JavaScript engine documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета libv8
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(libv8) = 8.4.255.5

%description   -n gem-libv8-doc
Distribution of the V8 JavaScript engine documentation files.

Distributes the V8 JavaScript engine in binary and source forms in order to
support fast builds of The Ruby Racer

%description   -n gem-libv8-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета libv8.
%endif


%if_enabled    devel
%package       -n gem-libv8-devel
Version:       8.4.255.5
Release:       alt1
Summary:       Distribution of the V8 JavaScript engine development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета libv8
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(libv8) = 8.4.255.5
Requires:      gem(rake) >= 12
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rspec) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rspec) >= 4

%description   -n gem-libv8-devel
Distribution of the V8 JavaScript engine development package.

Distributes the V8 JavaScript engine in binary and source forms in order to
support fast builds of The Ruby Racer

%description   -n gem-libv8-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета libv8.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install
%ifarch i586 x86_64
install ext/libv8/.location.yml %buildroot%ruby_gemlibdir/ext/libv8/.location.yml
%endif

%check
%ruby_test

%files
%doc CHANGELOG.md README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-libv8-doc
%doc CHANGELOG.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-libv8-devel
%doc CHANGELOG.md README.md
%endif


%changelog
* Fri Dec 13 2024 Pavel Skrylev <majioa@altlinux.org> 8.4.255.5-alt1
- ^ 8.4.255.0 -> 8.4.255.5

* Sat Dec 02 2023 Pavel Skrylev <majioa@altlinux.org> 8.4.255.0-alt1
- + packaged gem with Ruby Policy 2.0
