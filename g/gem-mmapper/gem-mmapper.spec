%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%define        gemname mmapper

Name:          gem-mmapper
Version:       2.0.0
Release:       alt1
Summary:       Mmap-ed files in Ruby using a C native extension
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/carldaws/mmapper
Vcs:           https://github.com/carldaws/mmapper.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(mmapper) = 2.0.0

%description
Wraps a C extension for mmap-ing files.


%if_enabled    doc
%package       -n gem-mmapper-doc
Version:       2.0.0
Release:       alt1
Summary:       Mmap-ed files in Ruby using a C native extension documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mmapper
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mmapper) = 2.0.0

%description   -n gem-mmapper-doc
Mmap-ed files in Ruby using a C native extension documentation files.

Wraps a C extension for mmap-ing files.

%description   -n gem-mmapper-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mmapper.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-mmapper-doc
%doc README.md
%ruby_gemdocdir
%endif


%changelog
* Tue Jul 22 2025 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
