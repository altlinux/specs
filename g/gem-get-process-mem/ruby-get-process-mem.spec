%define        gemname get_process_mem

Name:          gem-get-process-mem
Version:       0.2.7
Release:       alt1
Summary:       Get memory usage of a process in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/schneems/get_process_mem
Vcs:           https://github.com/schneems/get_process_mem.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
# BuildRequires: gem(ffi) >= 1.0 gem(ffi) < 2
BuildRequires: gem(sys-proctable) >= 1.2 gem(sys-proctable) < 2
BuildRequires: gem(rake) >= 12 gem(rake) < 14
BuildRequires: gem(test-unit) >= 3 gem(test-unit) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_alias_names get_process_mem,get-process-mem
Requires:      gem(ffi) >= 1.0 gem(ffi) < 2
Obsoletes:     ruby-get-process-mem < %EVR
Provides:      ruby-get-process-mem = %EVR
Provides:      gem(get_process_mem) = 0.2.7


%description
Do you need to get the memory usage of a process? Great because this library
does that.


%package       -n gem-get-process-mem-doc
Version:       0.2.7
Release:       alt1
Summary:       Get memory usage of a process in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета get_process_mem
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(get_process_mem) = 0.2.7

%description   -n gem-get-process-mem-doc
Get memory usage of a process in Ruby documentation files.

Do you need to get the memory usage of a process? Great because this library
does that.

%description   -n gem-get-process-mem-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета get_process_mem.


%package       -n gem-get-process-mem-devel
Version:       0.2.7
Release:       alt1
Summary:       Get memory usage of a process in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета get_process_mem
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(get_process_mem) = 0.2.7
Requires:      gem(sys-proctable) >= 1.2 gem(sys-proctable) < 2
Requires:      gem(rake) >= 12 gem(rake) < 14
Requires:      gem(test-unit) >= 3 gem(test-unit) < 4

%description   -n gem-get-process-mem-devel
Get memory usage of a process in Ruby development package.

Do you need to get the memory usage of a process? Great because this library
does that.

%description   -n gem-get-process-mem-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета get_process_mem.


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

%files         -n gem-get-process-mem-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-get-process-mem-devel
%doc README.md


%changelog
* Fri Jul 16 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.7-alt1
- ^ 0.2.4 -> 0.2.7

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.4-alt1
- updated to (^) v0.2.4
- updated to (^) Ruby Policy 2.0

* Fri Oct 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.3-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus (without tests)
