%define        _unpackaged_files_terminate_build 1
%define        gemname ffi-libarchive

Name:          gem-ffi-libarchive
Version:       1.1.13
Release:       alt1
Summary:       A Ruby FFI binding to libarchive
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/ffi-libarchive
Vcs:           https://github.com/chef/ffi-libarchive.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(chefstyle) >= 2.2.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(ffi) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rb-readline) >= 0
BuildConflicts: gem(chefstyle) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(ffi) > 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency chefstyle >= 2.2.2,chefstyle < 3
%ruby_use_gem_dependency ffi >= 1.15.5,ffi < 2
Requires:      gem(ffi) >= 0
Conflicts:     gem(ffi) > 2
Obsoletes:     ruby-ffi-libarchive < %EVR
Provides:      ruby-ffi-libarchive = %EVR
Provides:      gem(ffi-libarchive) = 1.1.13


%description
A Ruby FFI binding to libarchive..

This library provides Ruby FFI bindings to the well-known libarchive library.


%package       -n gem-ffi-libarchive-doc
Version:       1.1.13
Release:       alt1
Summary:       A Ruby FFI binding to libarchive documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ffi-libarchive
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ffi-libarchive) = 1.1.13

%description   -n gem-ffi-libarchive-doc
A Ruby FFI binding to libarchive documentation files.

A Ruby FFI binding to libarchive..

This library provides Ruby FFI bindings to the well-known libarchive library.

%description   -n gem-ffi-libarchive-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ffi-libarchive.


%package       -n gem-ffi-libarchive-devel
Version:       1.1.13
Release:       alt1
Summary:       A Ruby FFI binding to libarchive development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ffi-libarchive
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ffi-libarchive) = 1.1.13
Requires:      gem(chefstyle) >= 2.2.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rb-readline) >= 0
Conflicts:     gem(chefstyle) >= 3
Conflicts:     gem(rspec) >= 4

%description   -n gem-ffi-libarchive-devel
A Ruby FFI binding to libarchive development package.

A Ruby FFI binding to libarchive..

This library provides Ruby FFI bindings to the well-known libarchive library.

%description   -n gem-ffi-libarchive-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ffi-libarchive.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-ffi-libarchive-doc
%ruby_gemdocdir

%files         -n gem-ffi-libarchive-devel


%changelog
* Mon Dec 04 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.13-alt1
- ^ 1.0.3 -> 1.1.13

* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1
- > Ruby Policy 2.0
- ^ 0.4.2 -> 1.0.3

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.2-alt1
- New version.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt1
- New version.
- Disable tests.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
