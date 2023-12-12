%define        _unpackaged_files_terminate_build 1
%define        gemname libv8

Name:          gem-libv8
Version:       8.4.255.0
Release:       alt1
Summary:       Distribution of the V8 JavaScript engine
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/rubyjs/libv8
Vcs:           https://github.com/rubyjs/libv8.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 12
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rspec) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Provides:      gem(libv8) = 8.4.255.0


%description
Distributes the V8 JavaScript engine in binary and source forms in order to
support fast builds of The Ruby Racer


%package       -n gem-libv8-doc
Version:       8.4.255.0
Release:       alt1
Summary:       Distribution of the V8 JavaScript engine documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета libv8
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(libv8) = 8.4.255.0

%description   -n gem-libv8-doc
Distribution of the V8 JavaScript engine documentation files.

Distributes the V8 JavaScript engine in binary and source forms in order to
support fast builds of The Ruby Racer

%description   -n gem-libv8-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета libv8.


%package       -n gem-libv8-devel
Version:       8.4.255.0
Release:       alt1
Summary:       Distribution of the V8 JavaScript engine development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета libv8
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(libv8) = 8.4.255.0
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


%prep
%setup

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

%files         -n gem-libv8-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-libv8-devel
%doc README.md


%changelog
* Sat Dec 02 2023 Pavel Skrylev <majioa@altlinux.org> 8.4.255.0-alt1
- + packaged gem with Ruby Policy 2.0
