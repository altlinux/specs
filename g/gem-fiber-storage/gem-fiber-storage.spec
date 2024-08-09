%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fiber-storage

Name:          gem-fiber-storage
Version:       0.1.2
Release:       alt1
Summary:       Provides a compatibility shim for fiber storage
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/fiber-storage
Vcs:           https://github.com/ioquatix/fiber-storage.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names gem-rb-sys
Provides:      gem(fiber-storage) = 0.1.2


%description
Provides a compatibility shim for fiber storage.


%if_enabled    doc
%package       -n gem-fiber-storage-doc
Version:       0.1.2
Release:       alt1
Summary:       Provides a compatibility shim for fiber storage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fiber-storage
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fiber-storage) = 0.1.2

%description   -n gem-fiber-storage-doc
Provides a compatibility shim for fiber storage documentation files.

%description   -n gem-fiber-storage-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fiber-storage.
%endif


%if_enabled    devel
%package       -n gem-fiber-storage-devel
Version:       0.1.2
Release:       alt1
Summary:       Provides a compatibility shim for fiber storage development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fiber-storage
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fiber-storage) = 0.1.2

%description   -n gem-fiber-storage-devel
Provides a compatibility shim for fiber storage development package.

%description   -n gem-fiber-storage-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fiber-storage.
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
%doc readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-fiber-storage-doc
%doc readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fiber-storage-devel
%doc readme.md
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- + packaged gem with Ruby Policy 2.0
