%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname getoptlong

Name:          gem-getoptlong
Version:       0.2.1
Release:       alt1
Summary:       GetoptLong for Ruby
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/getoptlong
Vcs:           https://github.com/ruby/getoptlong.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Provides:      gem(getoptlong) = 0.2.1

%description
The GetoptLong class allows you to parse command line options similarly to the
GNU getopt_long() C library call. Note, however, that GetoptLong is a pure Ruby
implementation.

GetoptLong allows for POSIX-style options like --file as well as single letter
options like -f

The empty option -- (two minus symbols) is used to end option processing. This
can be particularly important if options have optional arguments.


%if_enabled    doc
%package       -n gem-getoptlong-doc
Version:       0.2.1
Release:       alt1
Summary:       GetoptLong for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета getoptlong
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(getoptlong) = 0.2.1

%description   -n gem-getoptlong-doc
GetoptLong for Ruby documentation files.

The GetoptLong class allows you to parse command line options similarly to the
GNU getopt_long() C library call. Note, however, that GetoptLong is a pure Ruby
implementation.

GetoptLong allows for POSIX-style options like --file as well as single letter
options like -f

The empty option -- (two minus symbols) is used to end option processing. This
can be particularly important if options have optional arguments.

%description   -n gem-getoptlong-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета getoptlong.
%endif


%if_enabled    devel
%package       -n gem-getoptlong-devel
Version:       0.2.1
Release:       alt1
Summary:       GetoptLong for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета getoptlong
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(getoptlong) = 0.2.1

%description   -n gem-getoptlong-devel
GetoptLong for Ruby development package.

The GetoptLong class allows you to parse command line options similarly to the
GNU getopt_long() C library call. Note, however, that GetoptLong is a pure Ruby
implementation.

GetoptLong allows for POSIX-style options like --file as well as single letter
options like -f

The empty option -- (two minus symbols) is used to end option processing. This
can be particularly important if options have optional arguments.

%description   -n gem-getoptlong-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета getoptlong.
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
%files         -n gem-getoptlong-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-getoptlong-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Thu Sep 18 2025 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
