%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fssm

Name:          gem-fssm
Version:       0.2.10
Release:       alt1
Summary:       File System State Monitor
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/ttilley/fssm
Vcs:           https://github.com/ttilley/fssm.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(rspec) >= 2.4.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(fssm) = 0.2.10

%description
The File System State Monitor keeps track of the state of any number of paths
and will fire events when said state changes (create/update/delete). FSSM
supports using FSEvents on MacOS, Inotify on GNU/Linux, and polling anywhere
else.


%if_enabled    doc
%package       -n gem-fssm-doc
Version:       0.2.10
Release:       alt1
Summary:       File System State Monitor documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fssm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fssm) = 0.2.10

%description   -n gem-fssm-doc
File System State Monitor documentation files.

The File System State Monitor keeps track of the state of any number of paths
and will fire events when said state changes (create/update/delete). FSSM
supports using FSEvents on MacOS, Inotify on GNU/Linux, and polling anywhere
else.

%description   -n gem-fssm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fssm.
%endif


%if_enabled    devel
%package       -n gem-fssm-devel
Version:       0.2.10
Release:       alt1
Summary:       File System State Monitor development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fssm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fssm) = 0.2.10
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 2.4.0

%description   -n gem-fssm-devel
File System State Monitor development package.

The File System State Monitor keeps track of the state of any number of paths
and will fire events when said state changes (create/update/delete). FSSM
supports using FSEvents on MacOS, Inotify on GNU/Linux, and polling anywhere
else.

%description   -n gem-fssm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fssm.
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
%doc LICENSE README.markdown
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-fssm-doc
%doc LICENSE README.markdown
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fssm-devel
%doc LICENSE README.markdown
%endif


%changelog
* Mon Jan 13 2025 Pavel Skrylev <majioa@altlinux.org> 0.2.10-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
